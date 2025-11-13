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

    playbook_device_info = test_data.get("playbook_device_info")
    playbook_linecard_info = test_data.get("playbook_linecard_info")
    playbook_supervisor_card_info = test_data.get("playbook_supervisor_card_info")
    playbook_poe_details = test_data.get("playbook_poe_details")
    playbook_module_count_info = test_data.get("playbook_module_count_info")
    playbook_device_interfaces_by_range_info = test_data.get("playbook_device_interfaces_by_range_info")
    playbook_device_summary_info = test_data.get("playbook_device_summary_info")
    playbook_get_polling_interval = test_data.get("playbook_get_polling_interval")
    playbook_get_stack_info = test_data.get("playbook_get_stack_info")
    playbook_devicelink_mismatch = test_data.get("playbook_devicelink_mismatch")
    playbook_interface_info = test_data.get("playbook_interface_info")
    playbook_config_info = test_data.get("playbook_config_info")
    playbook_connected_device_info = test_data.get("playbook_connected_device_info")
    playbook_interface_vlan_info = test_data.get("playbook_interface_vlan_info")
    playbook_negative_scenario1 = test_data.get("playbook_negative_scenario1")
    playbook_negative_scenario2 = test_data.get("playbook_negative_scenario2")
    playbook_negative_scenario3 = test_data.get("playbook_negative_scenario3")
    playbook_negative_scenario4 = test_data.get("playbook_negative_scenario4")
    playbook_negative_scenario5 = test_data.get("playbook_negative_scenario5")
    playbook_negative_scenario6 = test_data.get("playbook_negative_scenario6")
    playbook_negative_scenario7 = test_data.get("playbook_negative_scenario7")
    playbook_negative_scenario8 = test_data.get("playbook_negative_scenario8")
    playbook_negative_scenario9 = test_data.get("playbook_negative_scenario9")
    playbook_no_network_device = test_data.get("playbook_no_network_device")
    playbook_no_device = test_data.get("playbook_no_device")
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

        if "playbook_device_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ip_address"),
                self.test_data.get("serial_number"),
                self.test_data.get("hostname"),
                self.test_data.get("mac_address"),
                self.test_data.get("get_network_devices"),
                self.test_data.get("get_network_devices1"),
                self.test_data.get("get_network_devices2"),
                self.test_data.get("get_network_devices3"),
                self.test_data.get("get_device_info"),
            ]
        elif "playbook_linecard_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ip_address_1"),
                self.test_data.get("get_network_devices4"),
                self.test_data.get("get_linecard_details"),
            ]

        elif "playbook_supervisor_card_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ip_address_2"),
                self.test_data.get("get_network_devices_5"),
                self.test_data.get("get_supervisor_card_details"),
            ]

        elif "playbook_poe_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ip_address_3"),
                self.test_data.get("get_network_devices_6"),
                self.test_data.get("poe_details"),
            ]

        elif "playbook_module_count_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ip_address_4"),
                self.test_data.get("get_network_devices_7"),
                self.test_data.get("get_module_count"),
            ]

        elif "playbook_device_interfaces_by_range_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ip_address_5"),
                self.test_data.get("get_network_devices_8"),
                self.test_data.get("get_device_interfaces_by_specified_range"),
            ]

        elif "playbook_device_summary_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ip_address_6"),
                self.test_data.get("get_network_devices_9"),
                self.test_data.get("get_device_summary"),
            ]

        elif "playbook_get_polling_interval" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ip_address_7"),
                self.test_data.get("get_network_devices_10"),
                self.test_data.get("get_polling_interval"),
            ]

        elif "playbook_get_stack_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ip_address_8"),
                self.test_data.get("get_network_devices_11"),
                self.test_data.get("get_stack_details"),
            ]

        elif "playbook_devicelink_mismatch" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites"),
                self.test_data.get("get_sites1"),
                self.test_data.get("get_sites2"),
                self.test_data.get("get_sites3"),
                self.test_data.get("get_sites4"),
                self.test_data.get("get_sites5"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD21"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD22"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD23"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD23_1"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD20"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD20/FLOOR1"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD20/FLOOR3"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD20/FLOOR2"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD21/FLOOR1"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD21/FLOOR3"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD21/FLOOR4"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD22/FLOOR1"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD22/FLOOR2"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD22/FLOOR3"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD23/FLOOR1"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD22/FLOOR4"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD23/FLOOR4"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD23/FLOOR4_1"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD23/FLOOR2"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD23/FLOOR2_1"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD23/FLOOR3"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD23/FLOOR3_1"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD20/FLOOR4"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD21/FLOOR2"),
                self.test_data.get("ip_address_9"),
                self.test_data.get("get_network_devices12"),
                self.test_data.get("get_sites10"),
                self.test_data.get("Global/USA/SAN JOSE"),
                self.test_data.get("inventory_insight_device_link_mismatch"),
                self.test_data.get("VLAN"),
                self.test_data.get("inventory_insight_device_link_mismatch1"),
                self.test_data.get("Speed-Duplex"),
            ]

        elif "playbook_interface_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ip_address_10"),
                self.test_data.get("get_network_devices13"),
                self.test_data.get("get_interface_info"),
            ]

        elif "playbook_config_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ip_address_11"),
                self.test_data.get("get_network_devices14"),
                self.test_data.get("get_device_config"),
            ]

        elif "playbook_connected_device_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ip_address_12"),
                self.test_data.get("get_network_devices15"),
                self.test_data.get("get_interface_info_by_id"),
                self.test_data.get("204.192.4.200"),
                self.test_data.get("interface"),
                self.test_data.get("interface_1"),
                self.test_data.get("interface_2"),
                self.test_data.get("interface_3"),
                self.test_data.get("interface_4"),
                self.test_data.get("interface_5"),
                self.test_data.get("interface_6"),
                self.test_data.get("interface_7"),
                self.test_data.get("interface_8"),
            ]

        elif "playbook_interface_vlan_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ip_address_13"),
                self.test_data.get("get_network_devices16"),
                self.test_data.get("get_device_interface_vlans"),
            ]

        elif "playbook_no_network_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("ip_address_14"),
                self.test_data.get("ip_address_15"),
            ]

        elif "playbook_no_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites14"),
                self.test_data.get("get_sites15"),
                self.test_data.get("get_sites17"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD23/FLOOR2_2"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD23/FLOOR2_3"),
                self.test_data.get("get_network_devices20"),
                self.test_data.get("get_sites18"),
                self.test_data.get("Global/USA/SAN JOSE/SJ_BLD23/FLOOR2_4"),
                self.test_data.get("inventory_insight_device_link_mismatch3"),
                self.test_data.get("VLAN1"),
                self.test_data.get("inventory_insight_device_link_mismatch4"),
                self.test_data.get("Speed-Duplex1"),
            ]

    def test_network_devices_info_workflow_manager_playbook_device_info(self):
        """
        Test retrieving device information for network devices.
        Validates device details including type, uptime, MAC address, and management state.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_device_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices filtered from the provided filters are: ['204.1.2.1']",
                [
                    {
                        'device_info': [
                            {
                                'device_ip': '204.1.2.1',
                                'device_details': [
                                    {
                                        'type': 'Cisco Catalyst 9300 Switch',
                                        'upTime': '13 days, 16:41:01.85',
                                        'macAddress': '24:6c:84:d3:7f:80',
                                        'deviceSupportLevel': 'Supported',
                                        'softwareType': 'IOS-XE',
                                        'softwareVersion': '17.12.1',
                                        'serialNumber': 'FJC271924D9',
                                        'lastManagedResyncReasons': 'Config Change Event',
                                        'managementState': 'Managed',
                                        'pendingSyncRequestsCount': '0',
                                        'reasonsForDeviceResync': 'Config Change Event',
                                        'reasonsForPendingSyncRequests': '',
                                        'inventoryStatusDetail': '<status><general code=SNMP_FAILED_POLL/></status>',
                                        'syncRequestedByApp': '',
                                        'collectionInterval': 'Global Default',
                                        'dnsResolvedManagementAddress': '204.1.2.1',
                                        'lastUpdated': '2025-10-31 03:27:20',
                                        'bootDateTime': '2025-10-17 10:46:20',
                                        'apManagerInterfaceIp': '',
                                        'collectionStatus': 'Managed',
                                        'family': 'Switches and Hubs',
                                        'hostname': 'SJ-EN-9300.cisco.local',
                                        'lastUpdateTime': 1761881240428,
                                        'locationName': None,
                                        'managementIpAddress': '204.1.2.1',
                                        'platformId': 'C9300-48UXM',
                                        'reachabilityFailureReason': 'Completed',
                                        'reachabilityStatus': 'Ping Reachable',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'snmpContact': '',
                                        'snmpLocation': '',
                                        'roleSource': 'AUTO',
                                        'interfaceCount': '0',
                                        'apEthernetMacAddress': None,
                                        'errorCode': None,
                                        'errorDescription': None,
                                        'lastDeviceResyncStartTime': '2025-10-31 03:27:16',
                                        'lineCardCount': '0',
                                        'lineCardId': '',
                                        'managedAtleastOnce': False,
                                        'memorySize': 'NA',
                                        'tagCount': '0',
                                        'tunnelUdpPort': None,
                                        'uptimeSeconds': 1209025,
                                        'vendor': 'Cisco',
                                        'waasDeviceMode': None,
                                        'associatedWlcIp': '',
                                        'description': (
                                            'Cisco IOS Software [Dublin], Catalyst L3 Switch Software (CAT9K_IOSXE), '
                                            'Version 17.12.1, RELEASE SOFTWARE (fc5) Technical Support: '
                                            'http://www.cisco.com/techsupport Copyright (c) 1986-2023 by Cisco Systems, '
                                            'Inc. Compiled Thu 27-Jul-23 22:38 by mcpre netconf enabled'
                                        ),
                                        'location': None,
                                        'role': 'ACCESS',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'instanceUuid': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'id': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3'
                                    }
                                ]
                            }
                        ]
                    }
                ]
            ],
        )

    def test_network_devices_info_workflow_manager_playbook_linecard_info(self):
        """
        Test retrieving line card information for network devices.
        Validates line card details and configuration data.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_linecard_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices filtered from the provided filters are: ['204.1.2.1']",
                [
                    {
                        "line_card_info": [
                            {
                                "device_ip": "204.1.2.1",
                                "linecard_details": []
                            }
                        ]
                    }
                ]
            ],
        )

    def test_network_devices_info_workflow_manager_playbook_supervisor_card_info(self):
        """
        Test retrieving supervisor card information for network devices.
        Validates supervisor card details and configuration data.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_supervisor_card_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices filtered from the provided filters are: ['204.1.2.1']",
                [
                    {
                        "supervisor_card_info": [
                            {
                                "device_ip": "204.1.2.1",
                                "supervisor_card_details": []
                            }
                        ]
                    }
                ]
            ],
        )

    def test_network_devices_info_workflow_manager_playbook_poe_details(self):
        """
        Test retrieving Power over Ethernet (PoE) details for network devices.
        Validates PoE power allocation, consumption, and remaining capacity information.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_poe_details
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices filtered from the provided filters are: ['204.1.2.1']",
                [
                    {
                        "poe_info": [
                            {
                                "device_ip": "204.1.2.1",
                                "poe_details": {
                                    "powerAllocated": "525",
                                    "powerConsumed": "196",
                                    "powerRemaining": "329"
                                }
                            }
                        ]
                    }
                ]
            ],
        )

    def test_network_devices_info_workflow_manager_playbook_module_count_info(self):
        """
        Test the Network Devices Info Workflow Manager's module count retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device module count information,
        ensuring proper validation and expected behavior.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_module_count_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices filtered from the provided filters are: ['204.1.2.1']",
                [
                    {
                        "module_count_info": [
                            {
                                "device_ip": "204.1.2.1",
                                "module_count_details": 2
                            }
                        ]
                    }
                ]
            ],
        )

    def test_network_devices_info_workflow_manager_playbook_device_interfaces_by_range_info(self):
        """
        Test the Network Devices Info Workflow Manager's range interface details retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device range interface information,
        ensuring proper validation and expected behavior.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_device_interfaces_by_range_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices filtered from the provided filters are: ['204.1.2.1']",
                [
                    {
                        "device_interfaces_by_range_info": [
                            {
                                "device_ip": "204.1.2.1",
                                "interface_info": [
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "74",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1761917050000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:c1",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "access",
                                        "portName": "AppGigabitEthernet1/0/1",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "up",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "5868e7b8-084d-47a7-b31e-567dfeb83727",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "5868e7b8-084d-47a7-b31e-567dfeb83727"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "DOWN",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "2",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:80",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "1500",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "Bluetooth0/4",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "780bc716-c7e8-4ef0-8d20-4dd505f9e70e",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "780bc716-c7e8-4ef0-8d20-4dd505f9e70e"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "70",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:bd",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "FortyGigabitEthernet1/1/1",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "40000000",
                                        "status": "down",
                                        "vlanId": "",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "cee71b71-991c-4db6-877f-252bd1b85f86",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "cee71b71-991c-4db6-877f-252bd1b85f86"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "71",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:be",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "FortyGigabitEthernet1/1/2",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "40000000",
                                        "status": "down",
                                        "vlanId": "",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "d992720a-4ab3-4fb7-ae05-fe94a7b26ca1",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "d992720a-4ab3-4fb7-ae05-fe94a7b26ca1"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "DOWN",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "1",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697778000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:80",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "1500",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "GigabitEthernet0/0",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "8c805053-da8f-4d5e-8dff-3eca353dd8d5",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "8c805053-da8f-4d5e-8dff-3eca353dd8d5"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "58",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:b1",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "GigabitEthernet1/1/1",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "a36f7783-40d2-4875-960b-c2e2bf7b8831",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "a36f7783-40d2-4875-960b-c2e2bf7b8831"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "59",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:b2",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "GigabitEthernet1/1/2",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "87db801e-4843-4444-812e-ea898129438c",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "87db801e-4843-4444-812e-ea898129438c"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "60",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:b3",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "GigabitEthernet1/1/3",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "5597218a-9e86-4767-8c3a-f0ca0fa8cc44",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "5597218a-9e86-4767-8c3a-f0ca0fa8cc44"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "61",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:b4",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "GigabitEthernet1/1/4",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "e4fb8235-50c6-4bb9-9b53-e96703219dca",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "e4fb8235-50c6-4bb9-9b53-e96703219dca"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "137",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1761917049000,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "L2LISP0",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "ef9005e9-a4ef-418d-9045-f93603932b12",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "ef9005e9-a4ef-418d-9045-f93603932b12"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "145",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "L2LISP0.8188",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "a49eccb4-03c1-4aa9-959a-aea7a6bb8012",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "a49eccb4-03c1-4aa9-959a-aea7a6bb8012"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "146",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "L2LISP0.8189",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "a85111b4-9d25-4330-b362-325c926593e9",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "a85111b4-9d25-4330-b362-325c926593e9"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "147",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "L2LISP0.8190",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "1e719945-01c6-454b-8fb0-ff938c962437",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "1e719945-01c6-454b-8fb0-ff938c962437"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "148",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "L2LISP0.8191",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "d38838dc-1f8e-4d98-a709-f7688b705451",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "d38838dc-1f8e-4d98-a709-f7688b705451"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "149",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "L2LISP0.8192",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "e89a4afc-b6a3-4219-85ba-1630c7ba0ea3",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "e89a4afc-b6a3-4219-85ba-1630c7ba0ea3"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "138",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "L2LISP0.8194",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "4c670034-0754-46ce-96ff-d769ccdecb27",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "4c670034-0754-46ce-96ff-d769ccdecb27"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "139",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "L2LISP0.8195",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "d2888700-a000-4413-a17c-5f5392917b49",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "d2888700-a000-4413-a17c-5f5392917b49"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "140",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "L2LISP0.8196",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "ac7ccd01-358a-4926-b855-cdb05514b405",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "ac7ccd01-358a-4926-b855-cdb05514b405"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "141",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "L2LISP0.8197",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "9cda427f-8768-4a04-937e-7f778d7e2e89",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "9cda427f-8768-4a04-937e-7f778d7e2e89"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "142",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "L2LISP0.8198",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "dc459f5f-d0c8-46a3-9f32-700d7356c3c1",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "dc459f5f-d0c8-46a3-9f32-700d7356c3c1"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "143",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "L2LISP0.8199",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "09af4a67-ffbc-4e57-bd7a-225d0869948c",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "09af4a67-ffbc-4e57-bd7a-225d0869948c"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "144",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "L2LISP0.8200",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "2fd07544-f45b-46cf-8568-ae0fd0f078b1",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "2fd07544-f45b-46cf-8568-ae0fd0f078b1"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "85",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "01fba793-04f9-4a94-aaa9-e6b319d2f84e",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "01fba793-04f9-4a94-aaa9-e6b319d2f84e"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "86",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4097",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "007ed332-9beb-4c69-b7f0-ebcf398035c4",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "007ed332-9beb-4c69-b7f0-ebcf398035c4"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "87",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4098",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "11d56cf2-0119-46d7-91f9-7d9f3ede3122",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "11d56cf2-0119-46d7-91f9-7d9f3ede3122"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "95",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4099",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "c4e10eff-515e-4568-b71f-b0118f601c76",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "c4e10eff-515e-4568-b71f-b0118f601c76"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "97",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4100",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "63e6f2eb-0275-48c0-be3d-18be9cbd946b",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "63e6f2eb-0275-48c0-be3d-18be9cbd946b"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "91",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4101",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "656d97dc-7091-4950-8e88-32431ac04e20",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "656d97dc-7091-4950-8e88-32431ac04e20"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "103",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4102",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "05901c1e-bf6c-48ef-91a5-33308efa8203",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "05901c1e-bf6c-48ef-91a5-33308efa8203"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "101",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4103",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "5ac7d786-86e3-4cb6-95e1-7b4607febace",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "5ac7d786-86e3-4cb6-95e1-7b4607febace"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "99",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4104",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "a3890bb6-1c5e-45dc-ba00-c22920b3a43e",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "a3890bb6-1c5e-45dc-ba00-c22920b3a43e"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "93",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4105",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "4e98a7e5-eb9f-47c8-8e54-e37f92bf3f7c",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "4e98a7e5-eb9f-47c8-8e54-e37f92bf3f7c"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "98",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4106",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "111bf56c-0419-41d9-9342-d277001e1304",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "111bf56c-0419-41d9-9342-d277001e1304"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "96",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4107",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "fb220113-e236-4d21-be64-aba8d4055d36",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "fb220113-e236-4d21-be64-aba8d4055d36"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "94",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4108",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "341abd7b-a757-4435-a03f-2a0db059c4da",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "341abd7b-a757-4435-a03f-2a0db059c4da"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "89",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4109",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "be7764b1-7995-4c9c-8b0d-3ecf30a8e1e1",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "be7764b1-7995-4c9c-8b0d-3ecf30a8e1e1"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "92",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4110",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "0be3374e-d92c-46b0-b807-1a18b1a80aa1",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "0be3374e-d92c-46b0-b807-1a18b1a80aa1"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "102",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4111",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "24a23056-0579-4d59-b83b-fbf9cd8ae892",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "24a23056-0579-4d59-b83b-fbf9cd8ae892"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "100",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4112",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "bdf0e61f-132b-455a-8153-0e177bd9a123",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "bdf0e61f-132b-455a-8153-0e177bd9a123"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "90",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4113",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "5ddb5540-6880-4194-b6fb-c5964413cc63",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "5ddb5540-6880-4194-b6fb-c5964413cc63"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "88",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": None,
                                        "lastOutgoingPacketTime": None,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "LISP0.4114",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "56",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "5e88be25-2135-45ed-9cf2-b8a77cc1b889",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "5e88be25-2135-45ed-9cf2-b8a77cc1b889"
                                    },
                                    {
                                        "addresses": [
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "204.1.2.1"
                                                    },
                                                    "ipMask": {
                                                        "address": "255.255.255.255"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV4_PRIMARY"
                                            }
                                        ],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "79",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": "204.1.2.1",
                                        "ipv4Mask": "255.255.255.255",
                                        "isisSupport": "true",
                                        "lastIncomingPacketTime": 1761917047000,
                                        "lastOutgoingPacketTime": 1761915675000,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "1514",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "Loopback0",
                                        "portType": "Service Module Interface",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "8000000",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "b58e40fa-fa88-41ef-b2e9-40c6d7d4e819",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "b58e40fa-fa88-41ef-b2e9-40c6d7d4e819"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "",
                                        "ifIndex": "3",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "17892",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "SR0",
                                        "portType": "OTHER",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "7cf784d0-2da3-4a3b-8872-4cde78cdcc1d",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "7cf784d0-2da3-4a3b-8872-4cde78cdcc1d"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "46",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:a5",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/0/37",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "9f361b52-d2d3-488a-a4ee-edc3d93226e2",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "9f361b52-d2d3-488a-a4ee-edc3d93226e2"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "47",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:a6",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/0/38",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "140895fe-3844-4e24-9b42-521a5c8291e7",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "140895fe-3844-4e24-9b42-521a5c8291e7"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "48",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:a7",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/0/39",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "33f9e720-a108-4ca8-9cff-5b45cca6c7a1",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "33f9e720-a108-4ca8-9cff-5b45cca6c7a1"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "49",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:a8",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/0/40",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "3ca14ef6-989f-48a6-b31f-1a94037bc540",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "3ca14ef6-989f-48a6-b31f-1a94037bc540"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "50",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:a9",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/0/41",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "c9c81b9e-64ab-49a9-a867-f16cafeee1eb",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "c9c81b9e-64ab-49a9-a867-f16cafeee1eb"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "51",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:aa",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/0/42",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "75b2ce71-f232-431b-9f1f-7b44e804631c",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "75b2ce71-f232-431b-9f1f-7b44e804631c"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "52",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:ab",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/0/43",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "2ab5b603-0d02-4ada-be8d-6518b7e2736f",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "2ab5b603-0d02-4ada-be8d-6518b7e2736f"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "53",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:ac",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/0/44",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "26bdc34c-0c9d-46d4-8ac5-e4d64051d5d7",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "26bdc34c-0c9d-46d4-8ac5-e4d64051d5d7"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "54",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:ad",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/0/45",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "b817e71c-e329-41eb-8277-8aa9a02a2195",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "b817e71c-e329-41eb-8277-8aa9a02a2195"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "55",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:ae",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/0/46",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "aa7b43e4-d5b8-4603-b8e4-70e8dd680f80",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "aa7b43e4-d5b8-4603-b8e4-70e8dd680f80"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "56",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:af",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/0/47",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "08bdabe1-bfde-4cc1-8a42-052af3e23f4c",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "08bdabe1-bfde-4cc1-8a42-052af3e23f4c"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "57",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:b0",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/0/48",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "c5b927ad-2738-455c-9d64-b437f27ac5eb",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "c5b927ad-2738-455c-9d64-b437f27ac5eb"
                                    },
                                    {
                                        "addresses": [
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "204.1.1.2"
                                                    },
                                                    "ipMask": {
                                                        "address": "255.255.255.252"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV4_PRIMARY"
                                            }
                                        ],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "FullDuplex",
                                        "ifIndex": "62",
                                        "interfaceType": "Physical",
                                        "ipv4Address": "204.1.1.2",
                                        "ipv4Mask": "255.255.255.252",
                                        "isisSupport": "true",
                                        "lastIncomingPacketTime": 1761917050000,
                                        "lastOutgoingPacketTime": 1761917050000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:c6",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "TenGigabitEthernet1/1/1",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "up",
                                        "vlanId": "0",
                                        "voiceVlan": "",
                                        "description": "SJ-BN-9300",
                                        "name": None,
                                        "instanceUuid": "d5f05ae4-df3a-4988-b399-7275479a147f",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "d5f05ae4-df3a-4988-b399-7275479a147f"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "63",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:b6",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/1/2",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "c84a1551-556e-477d-8549-9333a79f9684",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "c84a1551-556e-477d-8549-9333a79f9684"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "64",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:b7",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/1/3",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "b5fbeb99-18ce-4596-bf93-69562bfcea7b",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "b5fbeb99-18ce-4596-bf93-69562bfcea7b"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "65",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:b8",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/1/4",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "2edc93c9-2670-41a9-927b-4731e6cebee9",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "2edc93c9-2670-41a9-927b-4731e6cebee9"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "66",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:b9",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/1/5",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "99fde79f-e5bf-4c28-ae72-d483cf4bf887",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "99fde79f-e5bf-4c28-ae72-d483cf4bf887"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "67",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:ba",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/1/6",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "170fc1ea-e044-44a1-af11-d897b630e757",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "170fc1ea-e044-44a1-af11-d897b630e757"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "68",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:bb",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/1/7",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "e523cb83-5460-4c49-81be-92b24602b7d9",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "e523cb83-5460-4c49-81be-92b24602b7d9"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "69",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:bc",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TenGigabitEthernet1/1/8",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "10000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "c7af617f-740d-46ac-b1f2-8fafd8193e29",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "c7af617f-740d-46ac-b1f2-8fafd8193e29"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "72",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:bf",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwentyFiveGigE1/1/1",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "25000000",
                                        "status": "down",
                                        "vlanId": "",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "fa12e173-8cbd-4494-b62f-65094406398f",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "fa12e173-8cbd-4494-b62f-65094406398f"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "73",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:c0",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwentyFiveGigE1/1/2",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "25000000",
                                        "status": "down",
                                        "vlanId": "",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "c2a21bcd-a4fe-4fa6-836f-c0d51e740501",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "c2a21bcd-a4fe-4fa6-836f-c0d51e740501"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "10",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:81",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/1",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "2f59bc78-2671-45b6-84f3-c6e4101e5997",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "2f59bc78-2671-45b6-84f3-c6e4101e5997"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "11",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:82",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/2",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "6de76f04-21aa-4bdc-86e5-a5c0a57f5dd3",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "6de76f04-21aa-4bdc-86e5-a5c0a57f5dd3"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "12",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:83",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/3",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "133963b5-4601-4725-93b2-30c084f7ecb7",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "133963b5-4601-4725-93b2-30c084f7ecb7"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "13",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:84",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/4",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "89668e55-88ab-49b0-a33d-46e439e38f73",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "89668e55-88ab-49b0-a33d-46e439e38f73"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "14",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:85",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/5",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "85c9c006-50b5-4ef7-899e-4bf777a8b503",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "85c9c006-50b5-4ef7-899e-4bf777a8b503"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "15",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:86",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/6",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "2a43a8f0-39ee-46d0-af3e-c588317198c4",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "2a43a8f0-39ee-46d0-af3e-c588317198c4"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "16",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:87",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/7",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "ecb07ded-06d9-4bca-bb99-89ae9dba6a93",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "ecb07ded-06d9-4bca-bb99-89ae9dba6a93"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "17",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:88",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/8",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "846c9c4a-fbed-4a50-9a17-3a5aad76a32f",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "846c9c4a-fbed-4a50-9a17-3a5aad76a32f"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "18",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:89",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/9",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "61d0b4f4-0c59-4b8f-83d4-d851f6a2564b",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "61d0b4f4-0c59-4b8f-83d4-d851f6a2564b"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "19",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:8a",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/10",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "8bbb085a-e75a-43cf-a5c6-fedabce73850",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "8bbb085a-e75a-43cf-a5c6-fedabce73850"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "FullDuplex",
                                        "ifIndex": "20",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1761917031000,
                                        "lastOutgoingPacketTime": 1761917050000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:8b",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "access",
                                        "portName": "TwoGigabitEthernet1/0/11",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "up",
                                        "vlanId": "2160",
                                        "voiceVlan": "",
                                        "description": "AP PnP devices",
                                        "name": None,
                                        "instanceUuid": "0bb58f3b-f7d8-4b06-8985-57ca79b6fe44",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "0bb58f3b-f7d8-4b06-8985-57ca79b6fe44"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "FullDuplex",
                                        "ifIndex": "21",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1761917038000,
                                        "lastOutgoingPacketTime": 1761917050000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:8c",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "access",
                                        "portName": "TwoGigabitEthernet1/0/12",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "up",
                                        "vlanId": "2160",
                                        "voiceVlan": "",
                                        "description": "AP PnP devices",
                                        "name": None,
                                        "instanceUuid": "a94a993f-ec50-4378-a8c8-ce1723b420ad",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "a94a993f-ec50-4378-a8c8-ce1723b420ad"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "FullDuplex",
                                        "ifIndex": "22",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1761917037000,
                                        "lastOutgoingPacketTime": 1761917050000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:8d",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "access",
                                        "portName": "TwoGigabitEthernet1/0/13",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "up",
                                        "vlanId": "2160",
                                        "voiceVlan": "",
                                        "description": "AP PnP devices",
                                        "name": None,
                                        "instanceUuid": "9af75e79-5a19-46b8-82ac-fc82acd0d978",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "9af75e79-5a19-46b8-82ac-fc82acd0d978"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "FullDuplex",
                                        "ifIndex": "23",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1761917027000,
                                        "lastOutgoingPacketTime": 1761917050000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:8e",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "access",
                                        "portName": "TwoGigabitEthernet1/0/14",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "up",
                                        "vlanId": "2160",
                                        "voiceVlan": "",
                                        "description": "AP PnP devices",
                                        "name": None,
                                        "instanceUuid": "12b96080-58ec-4dee-9d12-7c0a66963407",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "12b96080-58ec-4dee-9d12-7c0a66963407"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "FullDuplex",
                                        "ifIndex": "24",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1761917030000,
                                        "lastOutgoingPacketTime": 1761917050000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:8f",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "access",
                                        "portName": "TwoGigabitEthernet1/0/15",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "up",
                                        "vlanId": "2160",
                                        "voiceVlan": "",
                                        "description": "AP PnP devices",
                                        "name": None,
                                        "instanceUuid": "5fb9c362-7c12-4193-befb-eb280a083f91",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "5fb9c362-7c12-4193-befb-eb280a083f91"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "25",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:90",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/16",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "7e650965-dcdc-4991-8db5-4c148d529f58",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "7e650965-dcdc-4991-8db5-4c148d529f58"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "26",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:91",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/17",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "2eac0b5a-a8a7-4d0a-bdbe-6f9e6f899148",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "2eac0b5a-a8a7-4d0a-bdbe-6f9e6f899148"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "27",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:92",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/18",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "3b4990ec-56e7-4e93-a403-8b8cdd5a42e4",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "3b4990ec-56e7-4e93-a403-8b8cdd5a42e4"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "28",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:93",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/19",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "6903915d-cdb5-405b-ab68-e0cd615833df",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "6903915d-cdb5-405b-ab68-e0cd615833df"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "29",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:94",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/20",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "72031587-d2b6-4f0c-b28f-7425165601ad",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "72031587-d2b6-4f0c-b28f-7425165601ad"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "30",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:95",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/21",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "5f2632ed-a125-4aec-a1b6-ea33c3009898",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "5f2632ed-a125-4aec-a1b6-ea33c3009898"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "31",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:96",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/22",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "81e204f8-e68c-426a-a6fd-21dfccb59b88",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "81e204f8-e68c-426a-a6fd-21dfccb59b88"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "32",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:97",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/23",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "89184a98-9ee6-4cd7-bd89-30e092d4ec13",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "89184a98-9ee6-4cd7-bd89-30e092d4ec13"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "33",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:98",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/24",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "521fa694-d1ac-4691-872d-04dbe1cbdad0",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "521fa694-d1ac-4691-872d-04dbe1cbdad0"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "FullDuplex",
                                        "ifIndex": "34",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1761917024000,
                                        "lastOutgoingPacketTime": 1761917050000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:99",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "access",
                                        "portName": "TwoGigabitEthernet1/0/25",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "up",
                                        "vlanId": "2160",
                                        "voiceVlan": "",
                                        "description": "AP PnP devices",
                                        "name": None,
                                        "instanceUuid": "53196ac5-c9c2-43bc-8eeb-f6ea9727acb8",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "53196ac5-c9c2-43bc-8eeb-f6ea9727acb8"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "FullDuplex",
                                        "ifIndex": "35",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1761917043000,
                                        "lastOutgoingPacketTime": 1761917050000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:9a",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "access",
                                        "portName": "TwoGigabitEthernet1/0/26",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "up",
                                        "vlanId": "2160",
                                        "voiceVlan": "",
                                        "description": "AP PnP devices",
                                        "name": None,
                                        "instanceUuid": "8e68beb8-a816-47e5-b9f2-6849dd10db06",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "8e68beb8-a816-47e5-b9f2-6849dd10db06"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "36",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:9b",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/27",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "6bdd29e4-6f05-4690-a1b3-c6f2bd1758b4",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "6bdd29e4-6f05-4690-a1b3-c6f2bd1758b4"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "37",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:9c",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/28",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "4cb8252a-6bd7-4656-8a2c-00a89d9a0351",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "4cb8252a-6bd7-4656-8a2c-00a89d9a0351"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "38",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:9d",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/29",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "d1fa114a-312f-42fc-8219-917e21f76e61",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "d1fa114a-312f-42fc-8219-917e21f76e61"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "39",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:9e",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/30",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "9c425194-900f-444f-acd5-d84c726fe16d",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "9c425194-900f-444f-acd5-d84c726fe16d"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "40",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:9f",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/31",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "0d079e7f-5d1e-4474-8dcb-84641174b87f",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "0d079e7f-5d1e-4474-8dcb-84641174b87f"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "41",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:a0",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/32",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "e1cd5659-91a7-4b78-97e4-da2413326e70",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "e1cd5659-91a7-4b78-97e4-da2413326e70"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "42",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:a1",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/33",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "ad557a8b-5d53-4e2c-a8de-20e31621845e",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "ad557a8b-5d53-4e2c-a8de-20e31621845e"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "43",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:a2",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/34",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "a1f45e63-eb60-4ffc-9519-d1a241b31933",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "a1f45e63-eb60-4ffc-9519-d1a241b31933"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "44",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:a3",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/35",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "f78c9337-16a1-4ed0-8316-76cea92b96b3",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "f78c9337-16a1-4ed0-8316-76cea92b96b3"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "45",
                                        "interfaceType": "Physical",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:a4",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "1",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "dynamic_auto",
                                        "portName": "TwoGigabitEthernet1/0/36",
                                        "portType": "Ethernet Port",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "2500000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "e32eaf9d-e60d-42ed-9f84-2faf97519fa9",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "e32eaf9d-e60d-42ed-9f84-2faf97519fa9"
                                    },
                                    {
                                        "addresses": [],
                                        "adminStatus": "DOWN",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "78",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": None,
                                        "ipv4Mask": None,
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:c7",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "Vlan1",
                                        "portType": "Ethernet SVI",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "1",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "dcfcff24-147f-4892-a718-f3f29df7effb",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "dcfcff24-147f-4892-a718-f3f29df7effb"
                                    },
                                    {
                                        "addresses": [
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "2004:1:80::1:1"
                                                    },
                                                    "ipMask": {
                                                        "address": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV6_UNICAST"
                                            },
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "204.1.80.1"
                                                    },
                                                    "ipMask": {
                                                        "address": "255.255.255.0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV4_PRIMARY"
                                            }
                                        ],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "131",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": "204.1.80.1",
                                        "ipv4Mask": "255.255.255.0",
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "00:00:0c:9f:f7:18",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "Vlan1021",
                                        "portType": "Ethernet SVI",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "1021",
                                        "voiceVlan": "",
                                        "description": "Configured from Catalyst Center",
                                        "name": None,
                                        "instanceUuid": "0ad7f76a-3f08-42d3-98fe-bebf6e6cad77",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "0ad7f76a-3f08-42d3-98fe-bebf6e6cad77"
                                    },
                                    {
                                        "addresses": [
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "2004:1:64::1:1"
                                                    },
                                                    "ipMask": {
                                                        "address": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV6_UNICAST"
                                            },
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "204.1.64.1"
                                                    },
                                                    "ipMask": {
                                                        "address": "255.255.255.0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV4_PRIMARY"
                                            }
                                        ],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "132",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": "204.1.64.1",
                                        "ipv4Mask": "255.255.255.0",
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "00:00:0c:9f:fd:a7",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "Vlan1022",
                                        "portType": "Ethernet SVI",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "1022",
                                        "voiceVlan": "",
                                        "description": "Configured from Catalyst Center",
                                        "name": None,
                                        "instanceUuid": "11df1a03-6bdb-4c68-bddd-8e8358ec2899",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "11df1a03-6bdb-4c68-bddd-8e8358ec2899"
                                    },
                                    {
                                        "addresses": [
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "204.1.240.1"
                                                    },
                                                    "ipMask": {
                                                        "address": "255.255.252.0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV4_PRIMARY"
                                            },
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "2004:1:240::1:1"
                                                    },
                                                    "ipMask": {
                                                        "address": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV6_UNICAST"
                                            }
                                        ],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "133",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": "204.1.240.1",
                                        "ipv4Mask": "255.255.252.0",
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "00:00:0c:9f:f3:7e",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "Vlan1023",
                                        "portType": "Ethernet SVI",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "1023",
                                        "voiceVlan": "",
                                        "description": "Configured from Catalyst Center",
                                        "name": None,
                                        "instanceUuid": "9123c534-1b8b-4785-b4c4-2332ddb652c1",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "9123c534-1b8b-4785-b4c4-2332ddb652c1"
                                    },
                                    {
                                        "addresses": [
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "204.1.224.1"
                                                    },
                                                    "ipMask": {
                                                        "address": "255.255.252.0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV4_PRIMARY"
                                            },
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "2004:1:224::1:1"
                                                    },
                                                    "ipMask": {
                                                        "address": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV6_UNICAST"
                                            }
                                        ],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "134",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": "204.1.224.1",
                                        "ipv4Mask": "255.255.252.0",
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "00:00:0c:9f:fe:ca",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "Vlan1024",
                                        "portType": "Ethernet SVI",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "1024",
                                        "voiceVlan": "",
                                        "description": "Configured from Catalyst Center",
                                        "name": None,
                                        "instanceUuid": "2466b60e-99fe-4b11-aa1d-8533e2aeb1af",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "2466b60e-99fe-4b11-aa1d-8533e2aeb1af"
                                    },
                                    {
                                        "addresses": [
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "204.1.32.1"
                                                    },
                                                    "ipMask": {
                                                        "address": "255.255.255.0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV4_PRIMARY"
                                            }
                                        ],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "136",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": "204.1.32.1",
                                        "ipv4Mask": "255.255.255.0",
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "00:00:0c:9f:f3:83",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "Vlan1025",
                                        "portType": "Ethernet SVI",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "1025",
                                        "voiceVlan": "",
                                        "description": "Configured from Catalyst Center",
                                        "name": None,
                                        "instanceUuid": "36e735b2-690d-4375-b83f-eb1a85273654",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "36e735b2-690d-4375-b83f-eb1a85273654"
                                    },
                                    {
                                        "addresses": [
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "204.1.48.1"
                                                    },
                                                    "ipMask": {
                                                        "address": "255.255.255.0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV4_PRIMARY"
                                            },
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "2004:1:48::1:1"
                                                    },
                                                    "ipMask": {
                                                        "address": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV6_UNICAST"
                                            }
                                        ],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "130",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": "204.1.48.1",
                                        "ipv4Mask": "255.255.255.0",
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "00:00:0c:9f:f9:66",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "Vlan1027",
                                        "portType": "Ethernet SVI",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "1027",
                                        "voiceVlan": "",
                                        "description": "Configured from Catalyst Center",
                                        "name": None,
                                        "instanceUuid": "6130acde-e553-49c4-a8fe-23a58c62c693",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "6130acde-e553-49c4-a8fe-23a58c62c693"
                                    },
                                    {
                                        "addresses": [
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "2004:1:112::1:1"
                                                    },
                                                    "ipMask": {
                                                        "address": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV6_UNICAST"
                                            },
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "204.1.112.1"
                                                    },
                                                    "ipMask": {
                                                        "address": "255.255.252.0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV4_PRIMARY"
                                            }
                                        ],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "128",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": "204.1.112.1",
                                        "ipv4Mask": "255.255.252.0",
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "00:00:0c:9f:f2:76",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "Vlan1028",
                                        "portType": "Ethernet SVI",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "1028",
                                        "voiceVlan": "",
                                        "description": "Configured from Catalyst Center",
                                        "name": None,
                                        "instanceUuid": "1ca482fa-b94f-49d9-9b56-988df07b5234",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "1ca482fa-b94f-49d9-9b56-988df07b5234"
                                    },
                                    {
                                        "addresses": [
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "40.50.0.1"
                                                    },
                                                    "ipMask": {
                                                        "address": "255.255.255.0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV4_PRIMARY"
                                            },
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "2040:50::1:0:1"
                                                    },
                                                    "ipMask": {
                                                        "address": "ffff:ffff:ffff:ffff:ffff:ffff::"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV6_UNICAST"
                                            }
                                        ],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "127",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": "40.50.0.1",
                                        "ipv4Mask": "255.255.255.0",
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "00:00:0c:9f:f7:8a",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "Vlan1029",
                                        "portType": "Ethernet SVI",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "1029",
                                        "voiceVlan": "",
                                        "description": "Configured from Catalyst Center",
                                        "name": None,
                                        "instanceUuid": "eeeb8838-cc9e-4317-8704-6dd63d83d65c",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "eeeb8838-cc9e-4317-8704-6dd63d83d65c"
                                    },
                                    {
                                        "addresses": [
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "2004:1:96::1:1"
                                                    },
                                                    "ipMask": {
                                                        "address": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV6_UNICAST"
                                            },
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "204.1.96.1"
                                                    },
                                                    "ipMask": {
                                                        "address": "255.255.252.0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV4_PRIMARY"
                                            }
                                        ],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "129",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": "204.1.96.1",
                                        "ipv4Mask": "255.255.252.0",
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "00:00:0c:9f:f5:63",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "Vlan1030",
                                        "portType": "Ethernet SVI",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "1030",
                                        "voiceVlan": "",
                                        "description": "Configured from Catalyst Center",
                                        "name": None,
                                        "instanceUuid": "fa85767f-0e7f-46ec-ae39-68025e5d45b8",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "fa85767f-0e7f-46ec-ae39-68025e5d45b8"
                                    },
                                    {
                                        "addresses": [
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "204.1.128.1"
                                                    },
                                                    "ipMask": {
                                                        "address": "255.255.252.0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV4_PRIMARY"
                                            }
                                        ],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "124",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": "204.1.128.1",
                                        "ipv4Mask": "255.255.252.0",
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "00:00:0c:9f:f5:28",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "Vlan1031",
                                        "portType": "Ethernet SVI",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "1031",
                                        "voiceVlan": "",
                                        "description": "Configured from Catalyst Center",
                                        "name": None,
                                        "instanceUuid": "090f3874-153b-4712-a81f-8c1e848754b2",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "090f3874-153b-4712-a81f-8c1e848754b2"
                                    },
                                    {
                                        "addresses": [
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "123.123.0.1"
                                                    },
                                                    "ipMask": {
                                                        "address": "255.255.240.0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV4_PRIMARY"
                                            }
                                        ],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "125",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": "123.123.0.1",
                                        "ipv4Mask": "255.255.240.0",
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "00:00:0c:9f:fd:46",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "Vlan1032",
                                        "portType": "Ethernet SVI",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "1032",
                                        "voiceVlan": "",
                                        "description": "Configured from Catalyst Center",
                                        "name": None,
                                        "instanceUuid": "af72048c-9d88-4166-a9ba-7765b920625d",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "af72048c-9d88-4166-a9ba-7765b920625d"
                                    },
                                    {
                                        "addresses": [
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "40.50.10.1"
                                                    },
                                                    "ipMask": {
                                                        "address": "255.255.255.0"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV4_PRIMARY"
                                            },
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "2040:50::10:0:1"
                                                    },
                                                    "ipMask": {
                                                        "address": "ffff:ffff:ffff:ffff:ffff:ffff::"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV6_UNICAST"
                                            }
                                        ],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "126",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": "40.50.10.1",
                                        "ipv4Mask": "255.255.255.0",
                                        "isisSupport": "false",
                                        "lastIncomingPacketTime": 1760697608000,
                                        "lastOutgoingPacketTime": 1760697608000,
                                        "lastUpdated": None,
                                        "macAddress": "00:00:0c:9f:f2:f2",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "Vlan2046",
                                        "portType": "Ethernet SVI",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "down",
                                        "vlanId": "2046",
                                        "voiceVlan": "",
                                        "description": "Configured from Catalyst Center",
                                        "name": None,
                                        "instanceUuid": "3f152a0b-32eb-4753-8070-538491a1d6e7",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "3f152a0b-32eb-4753-8070-538491a1d6e7"
                                    },
                                    {
                                        "addresses": [
                                            {
                                                "address": {
                                                    "ipAddress": {
                                                        "address": "204.1.216.1"
                                                    },
                                                    "ipMask": {
                                                        "address": "255.255.255.192"
                                                    },
                                                    "isInverseMask": False
                                                },
                                                "type": "IPV4_PRIMARY"
                                            }
                                        ],
                                        "adminStatus": "UP",
                                        "className": None,
                                        "deviceId": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                        "duplex": "AutoNegotiate",
                                        "ifIndex": "80",
                                        "interfaceType": "Virtual",
                                        "ipv4Address": "204.1.216.1",
                                        "ipv4Mask": "255.255.255.192",
                                        "isisSupport": "true",
                                        "lastIncomingPacketTime": 1761917050000,
                                        "lastOutgoingPacketTime": 1761917050000,
                                        "lastUpdated": None,
                                        "macAddress": "24:6c:84:d3:7f:de",
                                        "mappedPhysicalInterfaceId": None,
                                        "mappedPhysicalInterfaceName": None,
                                        "mediaType": None,
                                        "mtu": "9100",
                                        "nativeVlanId": "",
                                        "ospfSupport": "false",
                                        "pid": "C9300-48UXM",
                                        "portMode": "routed",
                                        "portName": "Vlan2160",
                                        "portType": "Ethernet SVI",
                                        "serialNo": "FJC271924D9",
                                        "series": "Cisco Catalyst 9300 Series Switches",
                                        "speed": "1000000",
                                        "status": "up",
                                        "vlanId": "2160",
                                        "voiceVlan": "",
                                        "description": "",
                                        "name": None,
                                        "instanceUuid": "3255a4b3-4c38-4fd9-b38e-417d50af55c8",
                                        "instanceTenantId": "68593aeecd0f400013b8604e",
                                        "id": "3255a4b3-4c38-4fd9-b38e-417d50af55c8"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            ]
        )

    def test_network_devices_info_workflow_manager_playbook_device_summary_info(self):
        """
        Test retrieving device summary information for network devices.
        Validates device summary details including ID, role, and role source.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_device_summary_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices filtered from the provided filters are: ['204.1.2.1']",
                [
                    {
                        "device_summary_info": [
                            {
                                "device_ip": "204.1.2.1",
                                "device_summary_details": {
                                    "id": "8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3",
                                    "role": "ACCESS",
                                    "roleSource": "AUTO"
                                }
                            }
                        ]
                    }
                ]
            ],
        )

    def test_network_devices_info_workflow_manager_playbook_get_polling_interval(self):
        """
        Test retrieving device polling interval information.
        Validates polling interval configuration and timing settings.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_get_polling_interval
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices filtered from the provided filters are: ['204.1.2.1']",
                [
                    {
                        "device_polling_interval_info": [
                            {
                                "device_ip": "204.1.2.1",
                                "polling_interval_details": 86400
                            }
                        ]
                    }
                ]
            ],
        )

    def test_network_devices_info_workflow_manager_playbook_get_stack_info(self):
        """
        Test retrieving device stack information for network devices.
        Validates stack member details, ports, and switch configuration.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_get_stack_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices filtered from the provided filters are: ['204.1.2.1']",
                [
                    {
                        'device_stack_info': [
                            {
                                'device_ip': '204.1.2.1',
                                'stack_details': {
                                    'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                    'stackSwitchInfo': [
                                        {
                                            'hwPriority': 0,
                                            'macAddress': '24:6c:84:d3:7f:80',
                                            'numNextReload': 1,
                                            'role': 'ACTIVE',
                                            'softwareImage': '17.12.01',
                                            'stackMemberNumber': 1,
                                            'state': 'READY',
                                            'switchPriority': 1,
                                            'entPhysicalIndex': '1000',
                                            'serialNumber': 'FJC271924D9',
                                            'platformId': 'C9300-48UXM'
                                        }
                                    ],
                                    'stackPortInfo': [
                                        {
                                            'isSynchOk': 'Yes',
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
                                            'isSynchOk': 'Yes',
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
                            }
                        ]
                    }
                ]
            ],
        )

    def test_network_devices_info_workflow_manager_playbook_devicelink_mismatch(self):
        """
        Test the Network Devices Info Workflow Manager's link mismatch details retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device link mismatch information,
        ensuring proper validation and expected behavior.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_devicelink_mismatch
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices filtered from the provided filters are: ['204.1.2.1']",
                [
                    {
                        'device_link_mismatch_info': [
                            {
                                'device_ip': '204.1.2.1',
                                'vlan': [
                                    {
                                        'device_ip': '204.1.2.1',
                                        'link_mismatch_details': [
                                            {
                                                'id': '18d688cb-e9ca-4a16-abdc-5923edadfb00',
                                                'siteHierarchyId': (
                                                    '73273999-4fde-4376-b071-25ebee51d155/'
                                                    '0cc72385-0e00-4a5a-b11b-a9b79fe2abd1/'
                                                    '18d688cb-e9ca-4a16-abdc-5923edadfb00'
                                                ),
                                                'parentId': '0cc72385-0e00-4a5a-b11b-a9b79fe2abd1',
                                                'name': 'SAN JOSE',
                                                'nameHierarchy': 'Global/USA/SAN JOSE',
                                                'type': 'area'
                                            }
                                        ]
                                    }
                                ],
                                'speed-duplex': [
                                    {
                                        'device_ip': '204.1.2.1',
                                        'link_mismatch_details': [
                                            {
                                                'endPortAllowedVlanIds': 'ALL',
                                                'endPortNativeVlanId': '1',
                                                'startPortAllowedVlanIds': '2-4094',
                                                'startPortNativeVlanId': '1',
                                                'type': 'physical',
                                                'linkStatus': 'up',
                                                'lastUpdated': '',
                                                'numUpdates': 0,
                                                'avgUpdateFrequency': 0,
                                                'endDeviceId': 'd9116ff2-2b64-47bf-9f3a-8552e11b0c59',
                                                'endDeviceHostName': 'SJ-BN-9300.cisco.local',
                                                'endDeviceIpAddress': '204.1.2.3',
                                                'endPortAddress': None,
                                                'endPortDuplex': 'FullDuplex',
                                                'endPortId': 'df9d62ce-6519-413a-9b97-2439aaee7286',
                                                'endPortMask': None,
                                                'endPortName': 'TenGigabitEthernet1/1/1',
                                                'endPortOwningEntityId': '580581_580581',
                                                'endPortSpeed': '10000000',
                                                'startDeviceHostName': 'DC-FR-9300.cisco.local',
                                                'startDeviceId': '2d940748-45a9-465a-bd2e-578bbb98089c',
                                                'startDeviceIpAddress': '204.192.3.40',
                                                'startPortAddress': None,
                                                'startPortDuplex': 'FullDuplex',
                                                'startPortId': 'f41059bf-a6d3-4931-8e88-5d56d1083f25',
                                                'startPortMask': None,
                                                'startPortName': 'TenGigabitEthernet1/1/2',
                                                'startPortOwningEntityId': '580584_580584',
                                                'startPortSpeed': '10000000',
                                                'id': 'b82fe0b1-e614-429e-9a94-c6062fa575b6',
                                                'instanceTenantId': '68593aeecd0f400013b8604e',
                                                'instanceUuid': 'b82fe0b1-e614-429e-9a94-c6062fa575b6'
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            ],
        )

    def test_network_devices_info_workflow_manager_playbook_interface_info(self):
        """
        Test the Network Devices Info Workflow Manager's interface details retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device interface information,
        ensuring proper validation and expected behavior.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_interface_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices filtered from the provided filters are: ['204.1.2.1']",
                [
                    {
                        'interface_info': [
                            {
                                'device_ip': '204.1.2.1',
                                'interface_details': [
                                    {
                                        'addresses': [
                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '74',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1762097046000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:c1',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'access',
                                        'portName': 'AppGigabitEthernet1/0/1',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'up',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '5868e7b8-084d-47a7-b31e-567dfeb83727',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '5868e7b8-084d-47a7-b31e-567dfeb83727'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'DOWN',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '2',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:80',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '1500',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'Bluetooth0/4',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '780bc716-c7e8-4ef0-8d20-4dd505f9e70e',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '780bc716-c7e8-4ef0-8d20-4dd505f9e70e'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '70',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:bd',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'FortyGigabitEthernet1/1/1',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '40000000',
                                        'status': 'down',
                                        'vlanId': '',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'cee71b71-991c-4db6-877f-252bd1b85f86',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'cee71b71-991c-4db6-877f-252bd1b85f86'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '71',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:be',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'FortyGigabitEthernet1/1/2',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '40000000',
                                        'status': 'down',
                                        'vlanId': '',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'd992720a-4ab3-4fb7-ae05-fe94a7b26ca1',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'd992720a-4ab3-4fb7-ae05-fe94a7b26ca1'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'DOWN',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '1',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697778000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:80',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '1500',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'GigabitEthernet0/0',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '8c805053-da8f-4d5e-8dff-3eca353dd8d5',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '8c805053-da8f-4d5e-8dff-3eca353dd8d5'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '58',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:b1',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'GigabitEthernet1/1/1',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'a36f7783-40d2-4875-960b-c2e2bf7b8831',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'a36f7783-40d2-4875-960b-c2e2bf7b8831'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '59',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:b2',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'GigabitEthernet1/1/2',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '87db801e-4843-4444-812e-ea898129438c',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '87db801e-4843-4444-812e-ea898129438c'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '60',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:b3',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'GigabitEthernet1/1/3',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '5597218a-9e86-4767-8c3a-f0ca0fa8cc44',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '5597218a-9e86-4767-8c3a-f0ca0fa8cc44'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '61',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:b4',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'GigabitEthernet1/1/4',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'e4fb8235-50c6-4bb9-9b53-e96703219dca',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'e4fb8235-50c6-4bb9-9b53-e96703219dca'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '137',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1762097037000,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'L2LISP0',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'ef9005e9-a4ef-418d-9045-f93603932b12',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'ef9005e9-a4ef-418d-9045-f93603932b12'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '145',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'L2LISP0.8188',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'a49eccb4-03c1-4aa9-959a-aea7a6bb8012',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'a49eccb4-03c1-4aa9-959a-aea7a6bb8012'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '146',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'L2LISP0.8189',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'a85111b4-9d25-4330-b362-325c926593e9',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'a85111b4-9d25-4330-b362-325c926593e9'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '147',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'L2LISP0.8190',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '1e719945-01c6-454b-8fb0-ff938c962437',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '1e719945-01c6-454b-8fb0-ff938c962437'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '148',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'L2LISP0.8191',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'd38838dc-1f8e-4d98-a709-f7688b705451',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'd38838dc-1f8e-4d98-a709-f7688b705451'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '149',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'L2LISP0.8192',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'e89a4afc-b6a3-4219-85ba-1630c7ba0ea3',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'e89a4afc-b6a3-4219-85ba-1630c7ba0ea3'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '138',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'L2LISP0.8194',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '4c670034-0754-46ce-96ff-d769ccdecb27',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '4c670034-0754-46ce-96ff-d769ccdecb27'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '139',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'L2LISP0.8195',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'd2888700-a000-4413-a17c-5f5392917b49',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'd2888700-a000-4413-a17c-5f5392917b49'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '140',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'L2LISP0.8196',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'ac7ccd01-358a-4926-b855-cdb05514b405',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'ac7ccd01-358a-4926-b855-cdb05514b405'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '141',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'L2LISP0.8197',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '9cda427f-8768-4a04-937e-7f778d7e2e89',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '9cda427f-8768-4a04-937e-7f778d7e2e89'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '142',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'L2LISP0.8198',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'dc459f5f-d0c8-46a3-9f32-700d7356c3c1',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'dc459f5f-d0c8-46a3-9f32-700d7356c3c1'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '143',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'L2LISP0.8199',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '09af4a67-ffbc-4e57-bd7a-225d0869948c',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '09af4a67-ffbc-4e57-bd7a-225d0869948c'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '144',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'L2LISP0.8200',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '2fd07544-f45b-46cf-8568-ae0fd0f078b1',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '2fd07544-f45b-46cf-8568-ae0fd0f078b1'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '85',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '01fba793-04f9-4a94-aaa9-e6b319d2f84e',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '01fba793-04f9-4a94-aaa9-e6b319d2f84e'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '86',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4097',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '007ed332-9beb-4c69-b7f0-ebcf398035c4',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '007ed332-9beb-4c69-b7f0-ebcf398035c4'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '87',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4098',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '11d56cf2-0119-46d7-91f9-7d9f3ede3122',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '11d56cf2-0119-46d7-91f9-7d9f3ede3122'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '95',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4099',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'c4e10eff-515e-4568-b71f-b0118f601c76',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'c4e10eff-515e-4568-b71f-b0118f601c76'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '97',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4100',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '63e6f2eb-0275-48c0-be3d-18be9cbd946b',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '63e6f2eb-0275-48c0-be3d-18be9cbd946b'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '91',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4101',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '656d97dc-7091-4950-8e88-32431ac04e20',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '656d97dc-7091-4950-8e88-32431ac04e20'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '103',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4102',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '05901c1e-bf6c-48ef-91a5-33308efa8203',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '05901c1e-bf6c-48ef-91a5-33308efa8203'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '101',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4103',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '5ac7d786-86e3-4cb6-95e1-7b4607febace',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '5ac7d786-86e3-4cb6-95e1-7b4607febace'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '99',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4104',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'a3890bb6-1c5e-45dc-ba00-c22920b3a43e',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'a3890bb6-1c5e-45dc-ba00-c22920b3a43e'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '93',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4105',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '4e98a7e5-eb9f-47c8-8e54-e37f92bf3f7c',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '4e98a7e5-eb9f-47c8-8e54-e37f92bf3f7c'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '98',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4106',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '111bf56c-0419-41d9-9342-d277001e1304',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '111bf56c-0419-41d9-9342-d277001e1304'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '96',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4107',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'fb220113-e236-4d21-be64-aba8d4055d36',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'fb220113-e236-4d21-be64-aba8d4055d36'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '94',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4108',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '341abd7b-a757-4435-a03f-2a0db059c4da',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '341abd7b-a757-4435-a03f-2a0db059c4da'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '89',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4109',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'be7764b1-7995-4c9c-8b0d-3ecf30a8e1e1',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'be7764b1-7995-4c9c-8b0d-3ecf30a8e1e1'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '92',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4110',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '0be3374e-d92c-46b0-b807-1a18b1a80aa1',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '0be3374e-d92c-46b0-b807-1a18b1a80aa1'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '102',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4111',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '24a23056-0579-4d59-b83b-fbf9cd8ae892',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '24a23056-0579-4d59-b83b-fbf9cd8ae892'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '100',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4112',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'bdf0e61f-132b-455a-8153-0e177bd9a123',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'bdf0e61f-132b-455a-8153-0e177bd9a123'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '90',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4113',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '5ddb5540-6880-4194-b6fb-c5964413cc63',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '5ddb5540-6880-4194-b6fb-c5964413cc63'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '88',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': None,
                                        'lastOutgoingPacketTime': None,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'LISP0.4114',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '56',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '5e88be25-2135-45ed-9cf2-b8a77cc1b889',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '5e88be25-2135-45ed-9cf2-b8a77cc1b889'
                                    },
                                    {
                                        'addresses': [
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '204.1.2.1'
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
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '79',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': '204.1.2.1',
                                        'ipv4Mask': '255.255.255.255',
                                        'isisSupport': 'true',
                                        'lastIncomingPacketTime': 1762097036000,
                                        'lastOutgoingPacketTime': 1762096340000,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '1514',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'Loopback0',
                                        'portType': 'Service Module Interface',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '8000000',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'b58e40fa-fa88-41ef-b2e9-40c6d7d4e819',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'b58e40fa-fa88-41ef-b2e9-40c6d7d4e819'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': '',
                                        'ifIndex': '3',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '17892',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'SR0',
                                        'portType': 'OTHER',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '7cf784d0-2da3-4a3b-8872-4cde78cdcc1d',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '7cf784d0-2da3-4a3b-8872-4cde78cdcc1d'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '46',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:a5',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/0/37',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '9f361b52-d2d3-488a-a4ee-edc3d93226e2',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '9f361b52-d2d3-488a-a4ee-edc3d93226e2'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '47',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:a6',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/0/38',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '140895fe-3844-4e24-9b42-521a5c8291e7',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '140895fe-3844-4e24-9b42-521a5c8291e7'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '48',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:a7',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/0/39',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '33f9e720-a108-4ca8-9cff-5b45cca6c7a1',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '33f9e720-a108-4ca8-9cff-5b45cca6c7a1'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '49',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:a8',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/0/40',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '3ca14ef6-989f-48a6-b31f-1a94037bc540',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '3ca14ef6-989f-48a6-b31f-1a94037bc540'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '50',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:a9',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/0/41',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'c9c81b9e-64ab-49a9-a867-f16cafeee1eb',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'c9c81b9e-64ab-49a9-a867-f16cafeee1eb'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '51',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:aa',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/0/42',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '75b2ce71-f232-431b-9f1f-7b44e804631c',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '75b2ce71-f232-431b-9f1f-7b44e804631c'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '52',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:ab',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/0/43',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '2ab5b603-0d02-4ada-be8d-6518b7e2736f',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '2ab5b603-0d02-4ada-be8d-6518b7e2736f'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '53',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:ac',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/0/44',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '26bdc34c-0c9d-46d4-8ac5-e4d64051d5d7',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '26bdc34c-0c9d-46d4-8ac5-e4d64051d5d7'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '54',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:ad',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/0/45',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'b817e71c-e329-41eb-8277-8aa9a02a2195',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'b817e71c-e329-41eb-8277-8aa9a02a2195'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '55',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:ae',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/0/46',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'aa7b43e4-d5b8-4603-b8e4-70e8dd680f80',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'aa7b43e4-d5b8-4603-b8e4-70e8dd680f80'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '56',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:af',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/0/47',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '08bdabe1-bfde-4cc1-8a42-052af3e23f4c',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '08bdabe1-bfde-4cc1-8a42-052af3e23f4c'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '57',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:b0',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/0/48',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'c5b927ad-2738-455c-9d64-b437f27ac5eb',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'c5b927ad-2738-455c-9d64-b437f27ac5eb'
                                    },
                                    {
                                        'addresses': [
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '204.1.1.2'
                                                    },
                                                    'ipMask': {
                                                        'address': '255.255.255.252'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV4_PRIMARY'
                                            }
                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'FullDuplex',
                                        'ifIndex': '62',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': '204.1.1.2',
                                        'ipv4Mask': '255.255.255.252',
                                        'isisSupport': 'true',
                                        'lastIncomingPacketTime': 1762097046000,
                                        'lastOutgoingPacketTime': 1762097046000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:c6',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'TenGigabitEthernet1/1/1',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'up',
                                        'vlanId': '0',
                                        'voiceVlan': '',
                                        'description': 'SJ-BN-9300',
                                        'name': None,
                                        'instanceUuid': 'd5f05ae4-df3a-4988-b399-7275479a147f',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'd5f05ae4-df3a-4988-b399-7275479a147f'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '63',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:b6',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/1/2',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'c84a1551-556e-477d-8549-9333a79f9684',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'c84a1551-556e-477d-8549-9333a79f9684'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '64',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:b7',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/1/3',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'b5fbeb99-18ce-4596-bf93-69562bfcea7b',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'b5fbeb99-18ce-4596-bf93-69562bfcea7b'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '65',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:b8',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/1/4',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '2edc93c9-2670-41a9-927b-4731e6cebee9',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '2edc93c9-2670-41a9-927b-4731e6cebee9'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '66',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:b9',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/1/5',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '99fde79f-e5bf-4c28-ae72-d483cf4bf887',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '99fde79f-e5bf-4c28-ae72-d483cf4bf887'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '67',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:ba',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/1/6',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '170fc1ea-e044-44a1-af11-d897b630e757',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '170fc1ea-e044-44a1-af11-d897b630e757'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '68',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:bb',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/1/7',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'e523cb83-5460-4c49-81be-92b24602b7d9',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'e523cb83-5460-4c49-81be-92b24602b7d9'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '69',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:bc',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TenGigabitEthernet1/1/8',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '10000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'c7af617f-740d-46ac-b1f2-8fafd8193e29',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'c7af617f-740d-46ac-b1f2-8fafd8193e29'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '72',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:bf',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwentyFiveGigE1/1/1',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '25000000',
                                        'status': 'down',
                                        'vlanId': '',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'fa12e173-8cbd-4494-b62f-65094406398f',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'fa12e173-8cbd-4494-b62f-65094406398f'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '73',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:c0',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwentyFiveGigE1/1/2',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '25000000',
                                        'status': 'down',
                                        'vlanId': '',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'c2a21bcd-a4fe-4fa6-836f-c0d51e740501',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'c2a21bcd-a4fe-4fa6-836f-c0d51e740501'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '10',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:81',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/1',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '2f59bc78-2671-45b6-84f3-c6e4101e5997',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '2f59bc78-2671-45b6-84f3-c6e4101e5997'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '11',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:82',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/2',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '6de76f04-21aa-4bdc-86e5-a5c0a57f5dd3',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '6de76f04-21aa-4bdc-86e5-a5c0a57f5dd3'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '12',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:83',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/3',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '133963b5-4601-4725-93b2-30c084f7ecb7',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '133963b5-4601-4725-93b2-30c084f7ecb7'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '13',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:84',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/4',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '89668e55-88ab-49b0-a33d-46e439e38f73',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '89668e55-88ab-49b0-a33d-46e439e38f73'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '14',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:85',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/5',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '85c9c006-50b5-4ef7-899e-4bf777a8b503',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '85c9c006-50b5-4ef7-899e-4bf777a8b503'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '15',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:86',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/6',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '2a43a8f0-39ee-46d0-af3e-c588317198c4',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '2a43a8f0-39ee-46d0-af3e-c588317198c4'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '16',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:87',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/7',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'ecb07ded-06d9-4bca-bb99-89ae9dba6a93',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'ecb07ded-06d9-4bca-bb99-89ae9dba6a93'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '17',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:88',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/8',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '846c9c4a-fbed-4a50-9a17-3a5aad76a32f',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '846c9c4a-fbed-4a50-9a17-3a5aad76a32f'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '18',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:89',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/9',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '61d0b4f4-0c59-4b8f-83d4-d851f6a2564b',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '61d0b4f4-0c59-4b8f-83d4-d851f6a2564b'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '19',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:8a',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/10',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '8bbb085a-e75a-43cf-a5c6-fedabce73850',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '8bbb085a-e75a-43cf-a5c6-fedabce73850'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'FullDuplex',
                                        'ifIndex': '20',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1762097024000,
                                        'lastOutgoingPacketTime': 1762097046000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:8b',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'access',
                                        'portName': 'TwoGigabitEthernet1/0/11',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'up',
                                        'vlanId': '2160',
                                        'voiceVlan': '',
                                        'description': 'AP PnP devices',
                                        'name': None,
                                        'instanceUuid': '0bb58f3b-f7d8-4b06-8985-57ca79b6fe44',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '0bb58f3b-f7d8-4b06-8985-57ca79b6fe44'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'FullDuplex',
                                        'ifIndex': '21',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1762097040000,
                                        'lastOutgoingPacketTime': 1762097046000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:8c',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'access',
                                        'portName': 'TwoGigabitEthernet1/0/12',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'up',
                                        'vlanId': '2160',
                                        'voiceVlan': '',
                                        'description': 'AP PnP devices',
                                        'name': None,
                                        'instanceUuid': 'a94a993f-ec50-4378-a8c8-ce1723b420ad',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'a94a993f-ec50-4378-a8c8-ce1723b420ad'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'FullDuplex',
                                        'ifIndex': '22',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1762097043000,
                                        'lastOutgoingPacketTime': 1762097046000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:8d',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'access',
                                        'portName': 'TwoGigabitEthernet1/0/13',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'up',
                                        'vlanId': '2160',
                                        'voiceVlan': '',
                                        'description': 'AP PnP devices',
                                        'name': None,
                                        'instanceUuid': '9af75e79-5a19-46b8-82ac-fc82acd0d978',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '9af75e79-5a19-46b8-82ac-fc82acd0d978'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'FullDuplex',
                                        'ifIndex': '23',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1762097038000,
                                        'lastOutgoingPacketTime': 1762097046000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:8e',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'access',
                                        'portName': 'TwoGigabitEthernet1/0/14',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'up',
                                        'vlanId': '2160',
                                        'voiceVlan': '',
                                        'description': 'AP PnP devices',
                                        'name': None,
                                        'instanceUuid': '12b96080-58ec-4dee-9d12-7c0a66963407',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '12b96080-58ec-4dee-9d12-7c0a66963407'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'FullDuplex',
                                        'ifIndex': '24',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1762097037000,
                                        'lastOutgoingPacketTime': 1762097046000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:8f',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'access',
                                        'portName': 'TwoGigabitEthernet1/0/15',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'up',
                                        'vlanId': '2160',
                                        'voiceVlan': '',
                                        'description': 'AP PnP devices',
                                        'name': None,
                                        'instanceUuid': '5fb9c362-7c12-4193-befb-eb280a083f91',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '5fb9c362-7c12-4193-befb-eb280a083f91'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '25',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:90',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/16',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '7e650965-dcdc-4991-8db5-4c148d529f58',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '7e650965-dcdc-4991-8db5-4c148d529f58'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '26',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:91',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/17',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '2eac0b5a-a8a7-4d0a-bdbe-6f9e6f899148',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '2eac0b5a-a8a7-4d0a-bdbe-6f9e6f899148'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '27',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:92',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/18',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '3b4990ec-56e7-4e93-a403-8b8cdd5a42e4',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '3b4990ec-56e7-4e93-a403-8b8cdd5a42e4'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '28',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:93',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/19',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '6903915d-cdb5-405b-ab68-e0cd615833df',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '6903915d-cdb5-405b-ab68-e0cd615833df'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '29',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:94',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/20',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '72031587-d2b6-4f0c-b28f-7425165601ad',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '72031587-d2b6-4f0c-b28f-7425165601ad'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '30',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:95',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/21',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '5f2632ed-a125-4aec-a1b6-ea33c3009898',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '5f2632ed-a125-4aec-a1b6-ea33c3009898'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '31',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:96',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/22',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '81e204f8-e68c-426a-a6fd-21dfccb59b88',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '81e204f8-e68c-426a-a6fd-21dfccb59b88'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '32',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:97',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/23',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '89184a98-9ee6-4cd7-bd89-30e092d4ec13',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '89184a98-9ee6-4cd7-bd89-30e092d4ec13'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '33',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:98',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/24',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '521fa694-d1ac-4691-872d-04dbe1cbdad0',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '521fa694-d1ac-4691-872d-04dbe1cbdad0'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'FullDuplex',
                                        'ifIndex': '34',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1762097039000,
                                        'lastOutgoingPacketTime': 1762097046000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:99',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'access',
                                        'portName': 'TwoGigabitEthernet1/0/25',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'up',
                                        'vlanId': '2160',
                                        'voiceVlan': '',
                                        'description': 'AP PnP devices',
                                        'name': None,
                                        'instanceUuid': '53196ac5-c9c2-43bc-8eeb-f6ea9727acb8',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '53196ac5-c9c2-43bc-8eeb-f6ea9727acb8'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'FullDuplex',
                                        'ifIndex': '35',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1762097037000,
                                        'lastOutgoingPacketTime': 1762097046000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:9a',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'access',
                                        'portName': 'TwoGigabitEthernet1/0/26',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'up',
                                        'vlanId': '2160',
                                        'voiceVlan': '',
                                        'description': 'AP PnP devices',
                                        'name': None,
                                        'instanceUuid': '8e68beb8-a816-47e5-b9f2-6849dd10db06',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '8e68beb8-a816-47e5-b9f2-6849dd10db06'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '36',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:9b',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/27',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '6bdd29e4-6f05-4690-a1b3-c6f2bd1758b4',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '6bdd29e4-6f05-4690-a1b3-c6f2bd1758b4'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '37',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:9c',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/28',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '4cb8252a-6bd7-4656-8a2c-00a89d9a0351',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '4cb8252a-6bd7-4656-8a2c-00a89d9a0351'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '38',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:9d',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/29',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'd1fa114a-312f-42fc-8219-917e21f76e61',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'd1fa114a-312f-42fc-8219-917e21f76e61'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '39',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:9e',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/30',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '9c425194-900f-444f-acd5-d84c726fe16d',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '9c425194-900f-444f-acd5-d84c726fe16d'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '40',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:9f',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/31',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '0d079e7f-5d1e-4474-8dcb-84641174b87f',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '0d079e7f-5d1e-4474-8dcb-84641174b87f'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '41',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:a0',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/32',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'e1cd5659-91a7-4b78-97e4-da2413326e70',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'e1cd5659-91a7-4b78-97e4-da2413326e70'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '42',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:a1',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/33',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'ad557a8b-5d53-4e2c-a8de-20e31621845e',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'ad557a8b-5d53-4e2c-a8de-20e31621845e'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '43',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:a2',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/34',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'a1f45e63-eb60-4ffc-9519-d1a241b31933',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'a1f45e63-eb60-4ffc-9519-d1a241b31933'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '44',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:a3',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/35',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'f78c9337-16a1-4ed0-8316-76cea92b96b3',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'f78c9337-16a1-4ed0-8316-76cea92b96b3'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '45',
                                        'interfaceType': 'Physical',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:a4',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '1',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'dynamic_auto',
                                        'portName': 'TwoGigabitEthernet1/0/36',
                                        'portType': 'Ethernet Port',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '2500000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'e32eaf9d-e60d-42ed-9f84-2faf97519fa9',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'e32eaf9d-e60d-42ed-9f84-2faf97519fa9'
                                    },
                                    {
                                        'addresses': [

                                        ],
                                        'adminStatus': 'DOWN',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '78',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': None,
                                        'ipv4Mask': None,
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:c7',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'Vlan1',
                                        'portType': 'Ethernet SVI',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '1',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': 'dcfcff24-147f-4892-a718-f3f29df7effb',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'dcfcff24-147f-4892-a718-f3f29df7effb'
                                    },
                                    {
                                        'addresses': [
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '2004:1:80::1:1'
                                                    },
                                                    'ipMask': {
                                                        'address': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV6_UNICAST'
                                            },
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '204.1.80.1'
                                                    },
                                                    'ipMask': {
                                                        'address': '255.255.255.0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV4_PRIMARY'
                                            }
                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '131',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': '204.1.80.1',
                                        'ipv4Mask': '255.255.255.0',
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '00:00:0c:9f:f7:18',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'Vlan1021',
                                        'portType': 'Ethernet SVI',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '1021',
                                        'voiceVlan': '',
                                        'description': 'Configured from Catalyst Center',
                                        'name': None,
                                        'instanceUuid': '0ad7f76a-3f08-42d3-98fe-bebf6e6cad77',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '0ad7f76a-3f08-42d3-98fe-bebf6e6cad77'
                                    },
                                    {
                                        'addresses': [
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '2004:1:64::1:1'
                                                    },
                                                    'ipMask': {
                                                        'address': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV6_UNICAST'
                                            },
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '204.1.64.1'
                                                    },
                                                    'ipMask': {
                                                        'address': '255.255.255.0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV4_PRIMARY'
                                            }
                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '132',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': '204.1.64.1',
                                        'ipv4Mask': '255.255.255.0',
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '00:00:0c:9f:fd:a7',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'Vlan1022',
                                        'portType': 'Ethernet SVI',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '1022',
                                        'voiceVlan': '',
                                        'description': 'Configured from Catalyst Center',
                                        'name': None,
                                        'instanceUuid': '11df1a03-6bdb-4c68-bddd-8e8358ec2899',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '11df1a03-6bdb-4c68-bddd-8e8358ec2899'
                                    },
                                    {
                                        'addresses': [
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '2004:1:240::1:1'
                                                    },
                                                    'ipMask': {
                                                        'address': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV6_UNICAST'
                                            },
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '204.1.240.1'
                                                    },
                                                    'ipMask': {
                                                        'address': '255.255.252.0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV4_PRIMARY'
                                            }
                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '133',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': '204.1.240.1',
                                        'ipv4Mask': '255.255.252.0',
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '00:00:0c:9f:f3:7e',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'Vlan1023',
                                        'portType': 'Ethernet SVI',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '1023',
                                        'voiceVlan': '',
                                        'description': 'Configured from Catalyst Center',
                                        'name': None,
                                        'instanceUuid': '9123c534-1b8b-4785-b4c4-2332ddb652c1',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '9123c534-1b8b-4785-b4c4-2332ddb652c1'
                                    },
                                    {
                                        'addresses': [
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '2004:1:224::1:1'
                                                    },
                                                    'ipMask': {
                                                        'address': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV6_UNICAST'
                                            },
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '204.1.224.1'
                                                    },
                                                    'ipMask': {
                                                        'address': '255.255.252.0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV4_PRIMARY'
                                            }
                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '134',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': '204.1.224.1',
                                        'ipv4Mask': '255.255.252.0',
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '00:00:0c:9f:fe:ca',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'Vlan1024',
                                        'portType': 'Ethernet SVI',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '1024',
                                        'voiceVlan': '',
                                        'description': 'Configured from Catalyst Center',
                                        'name': None,
                                        'instanceUuid': '2466b60e-99fe-4b11-aa1d-8533e2aeb1af',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '2466b60e-99fe-4b11-aa1d-8533e2aeb1af'
                                    },
                                    {
                                        'addresses': [
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '204.1.32.1'
                                                    },
                                                    'ipMask': {
                                                        'address': '255.255.255.0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV4_PRIMARY'
                                            }
                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '136',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': '204.1.32.1',
                                        'ipv4Mask': '255.255.255.0',
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '00:00:0c:9f:f3:83',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'Vlan1025',
                                        'portType': 'Ethernet SVI',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '1025',
                                        'voiceVlan': '',
                                        'description': 'Configured from Catalyst Center',
                                        'name': None,
                                        'instanceUuid': '36e735b2-690d-4375-b83f-eb1a85273654',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '36e735b2-690d-4375-b83f-eb1a85273654'
                                    },
                                    {
                                        'addresses': [
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '204.1.48.1'
                                                    },
                                                    'ipMask': {
                                                        'address': '255.255.255.0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV4_PRIMARY'
                                            },
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '2004:1:48::1:1'
                                                    },
                                                    'ipMask': {
                                                        'address': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV6_UNICAST'
                                            }
                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '130',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': '204.1.48.1',
                                        'ipv4Mask': '255.255.255.0',
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '00:00:0c:9f:f9:66',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'Vlan1027',
                                        'portType': 'Ethernet SVI',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '1027',
                                        'voiceVlan': '',
                                        'description': 'Configured from Catalyst Center',
                                        'name': None,
                                        'instanceUuid': '6130acde-e553-49c4-a8fe-23a58c62c693',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '6130acde-e553-49c4-a8fe-23a58c62c693'
                                    },
                                    {
                                        'addresses': [
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '204.1.112.1'
                                                    },
                                                    'ipMask': {
                                                        'address': '255.255.252.0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV4_PRIMARY'
                                            },
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '2004:1:112::1:1'
                                                    },
                                                    'ipMask': {
                                                        'address': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV6_UNICAST'
                                            }
                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '128',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': '204.1.112.1',
                                        'ipv4Mask': '255.255.252.0',
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '00:00:0c:9f:f2:76',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'Vlan1028',
                                        'portType': 'Ethernet SVI',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '1028',
                                        'voiceVlan': '',
                                        'description': 'Configured from Catalyst Center',
                                        'name': None,
                                        'instanceUuid': '1ca482fa-b94f-49d9-9b56-988df07b5234',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '1ca482fa-b94f-49d9-9b56-988df07b5234'
                                    },
                                    {
                                        'addresses': [
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '2040:50::1:0:1'
                                                    },
                                                    'ipMask': {
                                                        'address': 'ffff:ffff:ffff:ffff:ffff:ffff::'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV6_UNICAST'
                                            },
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '40.50.0.1'
                                                    },
                                                    'ipMask': {
                                                        'address': '255.255.255.0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV4_PRIMARY'
                                            }
                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '127',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': '40.50.0.1',
                                        'ipv4Mask': '255.255.255.0',
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '00:00:0c:9f:f7:8a',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'Vlan1029',
                                        'portType': 'Ethernet SVI',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '1029',
                                        'voiceVlan': '',
                                        'description': 'Configured from Catalyst Center',
                                        'name': None,
                                        'instanceUuid': 'eeeb8838-cc9e-4317-8704-6dd63d83d65c',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'eeeb8838-cc9e-4317-8704-6dd63d83d65c'
                                    },
                                    {
                                        'addresses': [
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '2004:1:96::1:1'
                                                    },
                                                    'ipMask': {
                                                        'address': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV6_UNICAST'
                                            },
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '204.1.96.1'
                                                    },
                                                    'ipMask': {
                                                        'address': '255.255.252.0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV4_PRIMARY'
                                            }
                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '129',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': '204.1.96.1',
                                        'ipv4Mask': '255.255.252.0',
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '00:00:0c:9f:f5:63',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'Vlan1030',
                                        'portType': 'Ethernet SVI',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '1030',
                                        'voiceVlan': '',
                                        'description': 'Configured from Catalyst Center',
                                        'name': None,
                                        'instanceUuid': 'fa85767f-0e7f-46ec-ae39-68025e5d45b8',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'fa85767f-0e7f-46ec-ae39-68025e5d45b8'
                                    },
                                    {
                                        'addresses': [
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '204.1.128.1'
                                                    },
                                                    'ipMask': {
                                                        'address': '255.255.252.0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV4_PRIMARY'
                                            }
                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '124',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': '204.1.128.1',
                                        'ipv4Mask': '255.255.252.0',
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '00:00:0c:9f:f5:28',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'Vlan1031',
                                        'portType': 'Ethernet SVI',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '1031',
                                        'voiceVlan': '',
                                        'description': 'Configured from Catalyst Center',
                                        'name': None,
                                        'instanceUuid': '090f3874-153b-4712-a81f-8c1e848754b2',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '090f3874-153b-4712-a81f-8c1e848754b2'
                                    },
                                    {
                                        'addresses': [
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '123.123.0.1'
                                                    },
                                                    'ipMask': {
                                                        'address': '255.255.240.0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV4_PRIMARY'
                                            }
                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '125',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': '123.123.0.1',
                                        'ipv4Mask': '255.255.240.0',
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '00:00:0c:9f:fd:46',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'Vlan1032',
                                        'portType': 'Ethernet SVI',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '1032',
                                        'voiceVlan': '',
                                        'description': 'Configured from Catalyst Center',
                                        'name': None,
                                        'instanceUuid': 'af72048c-9d88-4166-a9ba-7765b920625d',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': 'af72048c-9d88-4166-a9ba-7765b920625d'
                                    },
                                    {
                                        'addresses': [
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '2040:50::10:0:1'
                                                    },
                                                    'ipMask': {
                                                        'address': 'ffff:ffff:ffff:ffff:ffff:ffff::'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV6_UNICAST'
                                            },
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '40.50.10.1'
                                                    },
                                                    'ipMask': {
                                                        'address': '255.255.255.0'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV4_PRIMARY'
                                            }
                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '126',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': '40.50.10.1',
                                        'ipv4Mask': '255.255.255.0',
                                        'isisSupport': 'false',
                                        'lastIncomingPacketTime': 1760697608000,
                                        'lastOutgoingPacketTime': 1760697608000,
                                        'lastUpdated': None,
                                        'macAddress': '00:00:0c:9f:f2:f2',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'Vlan2046',
                                        'portType': 'Ethernet SVI',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'down',
                                        'vlanId': '2046',
                                        'voiceVlan': '',
                                        'description': 'Configured from Catalyst Center',
                                        'name': None,
                                        'instanceUuid': '3f152a0b-32eb-4753-8070-538491a1d6e7',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '3f152a0b-32eb-4753-8070-538491a1d6e7'
                                    },
                                    {
                                        'addresses': [
                                            {
                                                'address': {
                                                    'ipAddress': {
                                                        'address': '204.1.216.1'
                                                    },
                                                    'ipMask': {
                                                        'address': '255.255.255.192'
                                                    },
                                                    'isInverseMask': False
                                                },
                                                'type': 'IPV4_PRIMARY'
                                            }
                                        ],
                                        'adminStatus': 'UP',
                                        'className': None,
                                        'deviceId': '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3',
                                        'duplex': 'AutoNegotiate',
                                        'ifIndex': '80',
                                        'interfaceType': 'Virtual',
                                        'ipv4Address': '204.1.216.1',
                                        'ipv4Mask': '255.255.255.192',
                                        'isisSupport': 'true',
                                        'lastIncomingPacketTime': 1762097046000,
                                        'lastOutgoingPacketTime': 1762097046000,
                                        'lastUpdated': None,
                                        'macAddress': '24:6c:84:d3:7f:de',
                                        'mappedPhysicalInterfaceId': None,
                                        'mappedPhysicalInterfaceName': None,
                                        'mediaType': None,
                                        'mtu': '9100',
                                        'nativeVlanId': '',
                                        'ospfSupport': 'false',
                                        'pid': 'C9300-48UXM',
                                        'portMode': 'routed',
                                        'portName': 'Vlan2160',
                                        'portType': 'Ethernet SVI',
                                        'serialNo': 'FJC271924D9',
                                        'series': 'Cisco Catalyst 9300 Series Switches',
                                        'speed': '1000000',
                                        'status': 'up',
                                        'vlanId': '2160',
                                        'voiceVlan': '',
                                        'description': '',
                                        'name': None,
                                        'instanceUuid': '3255a4b3-4c38-4fd9-b38e-417d50af55c8',
                                        'instanceTenantId': '68593aeecd0f400013b8604e',
                                        'id': '3255a4b3-4c38-4fd9-b38e-417d50af55c8'
                                    }
                                ]
                            }
                        ]
                    }
                ]
            ],
        )

    def test_network_devices_info_workflow_manager_playbook_config_info(self):
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
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_config_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices filtered from the provided filters are: ['204.1.2.1']",
                [
                    {
                        'device_config_info': [
                            {
                                'device_ip': '204.1.2.1',
                                'device_config_details': '\nBuilding configuration...\n\nCurrent configuration : 88800 bytes\n!\n! Last configuration change a'
                                't 09:18:03 UTC Wed Oct 29 2025 by cisco\n!\nversion 17.12\nservice timestamps debug datetime msec\ns'
                                'ervice timestamps log datetime msec\nservice password-encryption\nservice call-home\nplatform punt-k'
                                'eepalive disable-kernel-core\n!\nhostname SJ-EN-9300\n!\n!\nvrf definition DEFAULT_VN\n !\n address-'
                                'family ipv4\n exit-address-family\n !\n address-family ipv6\n exit-address-family\n!\nvrf definition'
                                ' Fabric_VN\n !\n address-family ipv4\n exit-address-family\n !\n address-family ipv6\n exit-address-'
                                'family\n!\nvrf definition IntraSubnet_VN\n !\n address-family ipv4\n exit-address-family\n !\n addre'
                                'ss-family ipv6\n exit-address-family\n!\nvrf definition Mgmt-vrf\n !\n address-family ipv4\n exit-ad'
                                'dress-family\n !\n address-family ipv6\n exit-address-family\n!\nvrf definition SGT_Port_test\n !\n '
                                'address-family ipv4\n exit-address-family\n !\n address-family ipv6\n exit-address-family\n!\nvrf de'
                                'finition VN1\n !\n address-family ipv4\n exit-address-family\n !\n address-family ipv6\n exit-addres'
                                's-family\n!\nvrf definition VN2\n !\n address-family ipv4\n exit-address-family\n !\n address-family'
                                ' ipv6\n exit-address-family\n!\nvrf definition VN3\n !\n address-family ipv4\n exit-address-family\n'
                                ' !\n address-family ipv6\n exit-address-family\n!\nvrf definition VN4\n !\n address-family ipv4\n ex'
                                'it-address-family\n !\n address-family ipv6\n exit-address-family\n!\nvrf definition VN5\n !\n addre'
                                'ss-family ipv4\n exit-address-family\n !\n address-family ipv6\n exit-address-family\n!\nvrf definit'
                                'ion VN6\n !\n address-family ipv4\n exit-address-family\n !\n address-family ipv6\n exit-address-fam'
                                'ily\n!\nvrf definition VN7\n !\n address-family ipv4\n exit-address-family\n !\n address-family ipv6'
                                '\n exit-address-family\n!\nvrf definition VN_SanJose_1\n !\n address-family ipv4\n exit-address-fami'
                                'ly\n !\n address-family ipv6\n exit-address-family\n!\nvrf definition WiredVNFB1\n !\n address-famil'
                                'y ipv4\n exit-address-family\n !\n address-family ipv6\n exit-address-family\n!\nvrf definition Wire'
                                'dVNFBLayer2\n !\n address-family ipv4\n exit-address-family\n !\n address-family ipv6\n exit-address'
                                '-family\n!\nvrf definition WiredVNStatic\n !\n address-family ipv4\n exit-address-family\n !\n addre'
                                'ss-family ipv6\n exit-address-family\n!\nvrf definition WirelessVNFB\n !\n address-family ipv4\n exi'
                                't-address-family\n !\n address-family ipv6\n exit-address-family\n!\nvrf definition WirelessVNFGuest'
                                '\n !\n address-family ipv4\n exit-address-family\n !\n address-family ipv6\n exit-address-family\n!\n'
                                'no logging console\nno logging monitor\naaa new-model\n!\n!\naaa group server radius dnac-client-ra'
                                'dius-group\n server name dnac-radius_172.23.241.229\n ip radius source-interface Loopback0\n!\naaa g'
                                'roup server radius dnac-network-radius-group\n server name dnac-radius_172.23.241.229\n ip radius so'
                                'urce-interface Loopback0\n!\naaa authentication login default local\naaa authentication login dnac-c'
                                'ts-list group dnac-client-radius-group local\naaa authentication login VTY_authen group dnac-network'
                                '-radius-group local\naaa authentication dot1x default group dnac-client-radius-group\naaa authorizat'
                                'ion exec default local \naaa authorization exec VTY_author group dnac-network-radius-group local if-'
                                'authenticated \naaa authorization network default group dnac-client-radius-group \naaa authorization'
                                ' network dnac-cts-list group dnac-client-radius-group \naaa accounting update newinfo periodic 2880\n'
                                'aaa accounting identity default start-stop group dnac-client-radius-group\naaa accounting exec defa'
                                'ult start-stop group dnac-network-radius-group\n!\n!\naaa server radius dynamic-author\n client 172.'
                                '23.241.229 server-key 7 xxxxxxxx\n client 172.23.241.230 server-key 7 xxxxxxxx\n client 172.23.241.2'
                                '31 server-key 7 xxxxxxxx\n client 204.192.1.245 server-key 7 xxxxxxxx\n!\naaa session-id common\nswi'
                                'tch 1 provision c9300-48uxm\n!\n!\n!\n!\nip routing\n!\n!\n!\n!\n!\nip multicast-routing \nip name-s'
                                'erver 204.192.3.40 2006:1:1::1\nip domain lookup source-interface Loopback0\nip domain name cisco.lo'
                                'cal\nip dhcp relay information option\nno ip dhcp conflict logging\n!\nip dhcp pool pnp_vlan_2160\n '
                                'network 204.1.216.0 255.255.255.192\n default-router 204.1.216.1 \n option 43 ascii 5A1N;B2;K4;I204.'
                                '192.1.214;J80\n!\n!\n!\nip dhcp snooping vlan 1021-1025,1027-1032,2046\nip dhcp snooping\nno login o'
                                'n-success log\nipv6 nd raguard policy dnac-sda-permit-nd-raguardv6\n device-role router\n!\nipv6 uni'
                                'cast-routing\nipv6 mld snooping\nipv6 dhcp guard policy dnac-sda-permit-dhcpv6\n device-role server\n'
                                '!\nipv6 multicast-routing\nvtp mode transparent\nvtp version 1\n!\n!\n!\n!\n!\n!\n!\nmpls label mod'
                                'e all-vrfs protocol all-afs per-vrf\n!\nparameter-map type subscriber attribute-to-service BUILTIN_D'
                                'EVICE_TO_TEMPLATE\n 1 map device-type regex Video-Conference\n 10 interface-template MSP_VC_INTERFAC'
                                'E_TEMPLATE\n 2 map device-type regex Cisco-DMP\n 10 interface-template DMP_INTERFACE_TEMPLATE\n 3 ma'
                                'p device-type regex Cisco-TelePresence\n 10 interface-template TP_INTERFACE_TEMPLATE\n 4 map device-'
                                'type regex Cisco-IP-Camera\n 10 interface-template IP_CAMERA_INTERFACE_TEMPLATE\n 5 map device-type '
                                'regex Cisco-IP-Phone\n 10 interface-template IP_PHONE_INTERFACE_TEMPLATE\n 6 map device-type regex S'
                                'urveillance-Camera\n 10 interface-template MSP_CAMERA_INTERFACE_TEMPLATE\n 7 map oui eq 00.23.ac\n 1'
                                '0 interface-template DMP_INTERFACE_TEMPLATE\n 8 map oui eq 00.0f.44\n 10 interface-template DMP_INTE'
                                'RFACE_TEMPLATE\n 9 map device-type regex IE-400*\n 10 interface-template SWITCH_INTERFACE_TEMPLATE\n'
                                ' 11 map device-type regex Cisco-DMP\n 10 interface-template SWITCH_INTERFACE_TEMPLATE\n 12 map devic'
                                'e-type regex IE-401*\n 10 interface-template SWITCH_INTERFACE_TEMPLATE\n 13 map device-type regex Ci'
                                'sco-Switch\n 10 interface-template SWITCH_INTERFACE_TEMPLATE\n 14 map device-type regex CDB*\n 10 in'
                                'terface-template SWITCH_INTERFACE_TEMPLATE\n 15 map device-type regex WS-C3560CX*\n 10 interface-tem'
                                'plate SWITCH_INTERFACE_TEMPLATE\n 16 map device-type regex IE-350*\n 10 interface-template SWITCH_IN'
                                'TERFACE_TEMPLATE\n 17 map device-type regex IE-330*\n 10 interface-template SWITCH_INTERFACE_TEMPLAT'
                                'E\n 18 map device-type regex IE-3400*\n 10 interface-template SWITCH_INTERFACE_TEMPLATE\n 19 map dev'
                                'ice-type regex IE-320*\n 10 interface-template SWITCH_INTERFACE_TEMPLATE\n 21 map device-type regex '
                                'IE-500*\n 10 interface-template SWITCH_INTERFACE_TEMPLATE\n 22 map device-type regex CMICR*\n 10 int'
                                'erface-template SWITCH_INTERFACE_TEMPLATE\n 23 map device-type regex Cisco-CAT-LAP\n 10 interface-te'
                                'mplate LAP_INTERFACE_TEMPLATE\n 24 map device-type regex Cisco-AIR-LAP\n 10 interface-template LAP_I'
                                'NTERFACE_TEMPLATE\n 60 map device-type regex Cisco-AIR-AP\n 20 interface-template AP_INTERFACE_TEMPL'
                                'ATE\n 70 map device-type regex Cisco-AIR-LAP\n 20 interface-template LAP_INTERFACE_TEMPLATE\n 110 ma'
                                'p device-type regex Cisco-CAT-LAP\n 10 interface-template LAP_INTERFACE_TEMPLATE\n!\naccess-session '
                                'mac-move deny\naccess-session interface-template sticky timer 30\n!\ntable-map policed-dscp\n map fr'
                                'om 0 to 8\n map from 10 to 8\n map from 18 to 8\n map from 24 to 8\n map from 46 to 8\n default copy'
                                '\ntable-map AutoConf-4.0-Trust-Cos-Table\n default copy\ntable-map AutoConf-4.0-Trust-Dscp-Table\n d'
                                'efault copy\n!\ndevice-tracking tracking\n!\ndevice-tracking policy IPDT_POLICY\n no protocol udp\n '
                                'tracking enable\n!\n!\ncrypto pki xxxxxxx\n enrollment selfsigned\n subject-name xxxxxxxx\n revocati'
                                'on-check null\n rsakeypair TP-self-signed- xxxxxxxx\n hash sha256\n!\ncrypto pki xxxxxxx\n enrollmen'
                                't pkcs12\n revocation-check crl\n hash sha256\n!\ncrypto pki xxxxxxx\n enrollment mode ra\n enrollme'
                                'nt terminal\n usage ssl-client\n revocation-check crl null\n source interface Loopback0\n hash sha25'
                                '6\n!\ncrypto pki xxxxxxx\n enrollment url http://204.192.1.214:80/ejbca/publicweb/apply/scep/sdnscep'
                                '\n fqdn SJ-EN-9300.cisco.local\n subject-name xxxxxxxx\n subject-alt-name SJ-EN-9300.cisco.local\n r'
                                'evocation-check crl\n source interface Loopback0\n rsakeypair xxxxxxxx\n auto-enroll 80 regenerate\n'
                                ' hash sha256\n!\n!\ncrypto pki certificate chain xxxxxxx\n certificate self-signed xxxxxxxx\n xxxx x'
                                'xxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx x'
                                'xxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx'
                                ' xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n'
                                ' xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxx'
                                'x xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xx'
                                'xx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xx'
                                'xx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx x'
                                'xxxx xxxx xxxx xxxx\nquit\ncrypto pki certificate chain xxxxxxx\n certificate ca xxxxxxxx\n xxxx xxx'
                                'xx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxx'
                                'x\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx x'
                                'xxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n '
                                'xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx '
                                'xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx'
                                ' xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx'
                                ' xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxx'
                                'xx xxxx xxxx xxxx\nquit\ncrypto pki certificate chain xxxxxxx\n certificate ca xxxxxxxx\n xxxx xxxxx'
                                ' xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n'
                                ' xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxx'
                                'x xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xx'
                                'xx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xx'
                                'xx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx x'
                                'xxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx x'
                                'xxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx'
                                ' xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n'
                                ' xxxx xxxxx xxxx xxxx xxxx\nquit\ncrypto pki certificate chain xxxxxxx\n xxxx xxxxx xxxx xxxx xxxx\n'
                                ' xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxx'
                                'x xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xx'
                                'xx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xx'
                                'xx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx x'
                                'xxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx x'
                                'xxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx'
                                ' xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n'
                                ' xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxx'
                                'x xxxx xxxx\nquit\n certificate ca xxxxxxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n'
                                ' xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxx'
                                'x xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xx'
                                'xx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xx'
                                'xx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx x'
                                'xxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx x'
                                'xxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx'
                                ' xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\n xxxx xxxxx xxxx xxxx xxxx\nquit\n!\ncts authorization '
                                'list dnac-cts-list\n!\nlicense boot level network-advantage addon dna-advantage\nservice-template DE'
                                'FAULT_LINKSEC_POLICY_MUST_SECURE\n linksec policy must-secure\nservice-template DEFAULT_LINKSEC_POLI'
                                'CY_SHOULD_SECURE\n linksec policy should-secure\nservice-template DEFAULT_CRITICAL_VOICE_TEMPLATE\n '
                                'voice vlan\nservice-template DEFAULT_CRITICAL_DATA_TEMPLATE\nservice-template webauth-global-inactiv'
                                'e\n inactivity-timer 3600 \nservice-template DefaultCriticalAuthVlan_SRV_TEMPLATE\n vlan 1029\nservi'
                                'ce-template DefaultCriticalVoice_SRV_TEMPLATE\n voice vlan\nservice-template DefaultCriticalAccess_S'
                                'RV_TEMPLATE\n access-group IPV4_CRITICAL_AUTH_ACL\n access-group IPV6_CRITICAL_AUTH_ACL\narchive\n l'
                                'og config\n logging enable\n logging size 1000\nmemory free low-watermark processor 134344\n!\ndevic'
                                'e classifier\nsystem mtu 9100\ndiagnostic bootup level minimal\n!\nspanning-tree mode rapid-pvst\nsp'
                                'anning-tree extend system-id\n!\n!\nerrdisable recovery cause udld\nerrdisable recovery cause bpdugu'
                                'ard\nerrdisable recovery cause security-violation\nerrdisable recovery cause channel-misconfig\nerrd'
                                'isable recovery cause pagp-flap\nerrdisable recovery cause dtp-flap\nerrdisable recovery cause link-'
                                'flap\nerrdisable recovery cause sfp-config-mismatch\nerrdisable recovery cause gbic-invalid\nerrdisa'
                                'ble recovery cause l2ptguard\nerrdisable recovery cause psecure-violation\nerrdisable recovery cause'
                                ' port-mode-failure\nerrdisable recovery cause dhcp-rate-limit\nerrdisable recovery cause pppoe-ia-ra'
                                'te-limit\nerrdisable recovery cause mac-limit\nerrdisable recovery cause storm-control\nerrdisable r'
                                'ecovery cause inline-power\nerrdisable recovery cause arp-inspection\nerrdisable recovery cause link'
                                '-monitor-failure\nerrdisable recovery cause oam-remote-failure\nerrdisable recovery cause loopback\n'
                                'errdisable recovery cause psp\nerrdisable recovery cause mrp-miscabling\nerrdisable recovery cause l'
                                'oopdetect\n!\nenable password 7 xxxxxxxx\n!\nusername wlcaccess privilege 15 password 7 xxxxxxxx\nus'
                                'ername cisco privilege 15 password 7 xxxxxxxx\nusername solution privilege 15 password 7 xxxxxxxx\nu'
                                'sername admin privilege 15 password 7 xxxxxxxx\n!\nredundancy\n mode sso\n!\n!\n!\n!\n!\ntransceiver'
                                ' type all\n monitoring\n!\nvlan configuration 1021-1024,1027-1030,2046\n ipv6 nd raguard\n ipv6 dhcp'
                                ' guard\n!\nvlan 1021\n name 80net_sub-WiredVNFB1\n!\nvlan 1022\n name 64net_sub-WiredVNFB1\n!\nvlan '
                                '1023\n name WSClients_sub-WirelessVNFB\n!\nvlan 1024\n name WClients_sub-WirelessVNFB\n!\nvlan 1025\n'
                                ' name EXT_POOL_sub-INFRA_VN\n!\nvlan 1027\n name SENSORPool_sub-WiredVNStatic\n!\nvlan 1028\n name '
                                '112net_sub-WiredVNFBLayer2\n!\nvlan 1029\n name CRITICAL_VLAN\n!\nvlan 1030\n name 96net_sub-WiredVN'
                                'FBLayer2\n!\nvlan 1031\n name GP_sub-WirelessVNFGuest\n!\nvlan 1032\n name SGT_Port_test_sub-SGT_Por'
                                't_test\n!\nvlan 2046\n name VOICE_VLAN\n!\nvlan 2160 \n!\nclass-map type control subscriber match-al'
                                'l AAA_SVR_DOWN_AUTHD_HOST\n match authorization-status authorized\n match result-type aaa-timeout\n!'
                                '\nclass-map type control subscriber match-all AAA_SVR_DOWN_UNAUTHD_HOST\n match authorization-status'
                                ' unauthorized\n match result-type aaa-timeout\n!\nclass-map type control subscriber match-all AUTHC_'
                                'SUCCESS-AUTHZ_FAIL\n match authorization-status unauthorized\n match result-type success\n!\nclass-m'
                                'ap type control subscriber match-all DOT1X\n match method dot1x\n!\nclass-map type control subscribe'
                                'r match-all DOT1X_FAILED\n match method dot1x\n match result-type method dot1x authoritative\n!\ncla'
                                'ss-map type control subscriber match-all DOT1X_MEDIUM_PRIO\n match authorizing-method-priority gt 20'
                                '\n!\nclass-map type control subscriber match-all DOT1X_NO_RESP\n match method dot1x\n match result-t'
                                'ype method dot1x agent-not-found\n!\nclass-map type control subscriber match-all DOT1X_TIMEOUT\n mat'
                                'ch method dot1x\n match result-type method dot1x method-timeout\n!\nclass-map type control subscribe'
                                'r match-any IN_CRITICAL_AUTH\n match activated-service-template DefaultCriticalVoice_SRV_TEMPLATE\n '
                                'match activated-service-template DefaultCriticalAuthVlan_SRV_TEMPLATE\n!\nclass-map type control sub'
                                'scriber match-any IN_CRITICAL_AUTH_CLOSED_MODE\n match activated-service-template DefaultCriticalAut'
                                'hVlan_SRV_TEMPLATE\n match activated-service-template DefaultCriticalVoice_SRV_TEMPLATE\n!\nclass-ma'
                                'p type control subscriber match-all MAB\n match method mab\n!\nclass-map type control subscriber mat'
                                'ch-all MAB_FAILED\n match method mab\n match result-type method mab authoritative\n!\nclass-map type'
                                ' control subscriber match-null NOT_IN_CRITICAL_AUTH\n match activated-service-template DefaultCritic'
                                'alVoice_SRV_TEMPLATE\n match activated-service-template DefaultCriticalAuthVlan_SRV_TEMPLATE\n!\ncla'
                                'ss-map type control subscriber match-null NOT_IN_CRITICAL_AUTH_CLOSED_MODE\n match activated-service'
                                '-template DefaultCriticalAuthVlan_SRV_TEMPLATE\n match activated-service-template DefaultCriticalVoi'
                                'ce_SRV_TEMPLATE\n!\n!\nclass-map match-any system-cpp-police-ewlc-control\n description EWLC Control'
                                ' \nclass-map match-any system-cpp-police-topology-control\n description Topology control\nclass-map '
                                'match-any system-cpp-police-sw-forward\n description Sw forwarding, L2 LVX data packets, LOGGING, Tr'
                                'ansit Traffic\nclass-map match-any AutoConf-4.0-Transaction-Class\n match access-group name AutoConf'
                                '-4.0-Acl-Transactional-Data\nclass-map match-any AutoConf-4.0-Output-Trans-Data-Queue\n match dscp a'
                                'f21 af22 af23 \n match cos 2 \nclass-map match-any AutoConf-4.0-Default-Class\n match access-group n'
                                'ame AutoConf-4.0-Acl-Default\nclass-map match-any system-cpp-default\n description EWLC Data, Inter '
                                'FED Traffic \nclass-map match-any system-cpp-police-sys-data\n description Openflow, Exception, EGR '
                                'Exception, NFL Sampled Data, RPF Failed\nclass-map match-any AutoConf-4.0-Output-Scavenger-Queue\n m'
                                'atch dscp cs1 \nclass-map match-any AutoConf-4.0-Output-Control-Mgmt-Queue\n match dscp cs2 cs3 cs6 '
                                'cs7 \n match cos 3 \nclass-map match-any AutoConf-4.0-Scavanger-Class\n match access-group name Auto'
                                'Conf-4.0-Acl-Scavanger\nclass-map match-any AutoConf-4.0-Signaling-Class\n match access-group name A'
                                'utoConf-4.0-Acl-Signaling\nclass-map match-any system-cpp-police-punt-webauth\n description Punt Web'
                                'auth\nclass-map match-any system-cpp-police-l2lvx-control\n description L2 LVX control packets\nclas'
                                's-map match-any system-cpp-police-forus\n description Forus Address resolution and Forus traffic\ncl'
                                'ass-map match-any system-cpp-police-multicast-end-station\n description MCAST END STATION\nclass-map'
                                ' match-any system-cpp-police-high-rate-app\n description High Rate Applications \nclass-map match-an'
                                'y AutoConf-4.0-Voip-Video-CiscoPhone-Class\n match cos 4 \nclass-map match-any system-cpp-police-mul'
                                'ticast\n description MCAST Data\nclass-map match-any system-cpp-police-l2-control\n description L2 c'
                                'ontrol\nclass-map match-any system-cpp-police-dot1x-auth\n description DOT1X Auth\nclass-map match-a'
                                'ny AutoConf-4.0-Output-Multimedia-ConfQueue\n match dscp af41 af42 af43 \n match cos 4 \nclass-map m'
                                'atch-any system-cpp-police-data\n description ICMP redirect, ICMP_GEN and BROADCAST\nclass-map match'
                                '-any system-cpp-police-stackwise-virt-control\n description Stackwise Virtual OOB\nclass-map match-a'
                                'ny AutoConf-4.0-Output-Multimedia-StrmQueue\n match dscp af31 af32 af33 \nclass-map match-any AutoCo'
                                'nf-4.0-Voip-Data-CiscoPhone-Class\n match cos 5 \nclass-map match-any AutoConf-4.0-Voip-SignalClass\n'
                                ' match dscp cs3 \n match cos 3 \nclass-map match-any non-client-nrt-class\nclass-map match-any syst'
                                'em-cpp-police-routing-control\n description Routing control and Low Latency\nclass-map match-any sys'
                                'tem-cpp-police-protocol-snooping\n description Protocol snooping\nclass-map match-any AutoConf-4.0-O'
                                'utput-Bulk-Data-Queue\n match dscp af11 af12 af13 \n match cos 1 \nclass-map match-any AutoConf-4.0-'
                                'Multimedia-Conf-Class\n match access-group name AutoConf-4.0-Acl-MultiEnhanced-Conf\nclass-map match'
                                '-any system-cpp-police-dhcp-snooping\n description DHCP snooping\nclass-map match-any AutoConf-4.0-B'
                                'ulk-Data-Class\n match access-group name AutoConf-4.0-Acl-Bulk-Data\nclass-map match-any system-cpp-'
                                'police-ios-routing\n description L2 control, Topology control, Routing control, Low Latency\nclass-m'
                                'ap match-any system-cpp-police-system-critical\n description System Critical and Gold Pkt\nclass-map'
                                ' match-any AutoConf-4.0-VoipSignal-CiscoPhone-Class\n match cos 3 \nclass-map match-any system-cpp-p'
                                'olice-ios-feature\n description ICMPGEN,BROADCAST,ICMP,L2LVXCntrl,ProtoSnoop,PuntWebauth,MCASTData,T'
                                'ransit,DOT1XAuth,Swfwd,LOGGING,L2LVXData,ForusTraffic,ForusARP,McastEndStn,Openflow,Exception,EGRExc'
                                'ption,NflSampled,RpfFailed\nclass-map match-any AutoConf-4.0-Output-Priority-Queue\n match dscp cs4 '
                                'cs5 ef \n match cos 5 \nclass-map match-any AutoConf-4.0-Voip-Data-Class\n match dscp ef \n match co'
                                's 5 \n!\n!\npolicy-map type control subscriber PMAP_DefaultWiredDot1xClosedAuth_1X_MAB\n event sessi'
                                'on-started match-all\n 10 class always do-until-failure\n 10 authenticate using dot1x retries 2 retr'
                                'y-time 0 priority 10\n event authentication-failure match-first\n 5 class DOT1X_FAILED do-until-fail'
                                'ure\n 10 terminate dot1x\n 20 authenticate using mab priority 20\n 10 class AAA_SVR_DOWN_UNAUTHD_HOS'
                                'T do-until-failure\n 10 activate service-template DefaultCriticalAuthVlan_SRV_TEMPLATE\n 20 activate'
                                ' service-template DefaultCriticalVoice_SRV_TEMPLATE\n 30 authorize\n 40 pause reauthentication\n 20 '
                                'class AAA_SVR_DOWN_AUTHD_HOST do-until-failure\n 10 pause reauthentication\n 20 authorize\n 30 class'
                                ' DOT1X_NO_RESP do-until-failure\n 10 terminate dot1x\n 20 authenticate using mab priority 20\n 40 cl'
                                'ass MAB_FAILED do-until-failure\n 10 terminate mab\n 20 authentication-restart 60\n 50 class DOT1X_T'
                                'IMEOUT do-until-failure\n 10 terminate dot1x\n 20 authenticate using mab priority 20\n 60 class alwa'
                                'ys do-until-failure\n 10 terminate dot1x\n 20 terminate mab\n 30 authentication-restart 60\n event a'
                                'aa-available match-all\n 10 class IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure\n 10 clear-session\n'
                                ' 20 class NOT_IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure\n 10 resume reauthentication\n event age'
                                'nt-found match-all\n 10 class always do-until-failure\n 10 terminate mab\n 20 authenticate using dot'
                                '1x retries 2 retry-time 0 priority 10\n event inactivity-timeout match-all\n 10 class always do-unti'
                                'l-failure\n 10 clear-session\n event authentication-success match-all\n event violation match-all\n '
                                '10 class always do-until-failure\n 10 restrict\n event authorization-failure match-all\n 10 class AU'
                                'THC_SUCCESS-AUTHZ_FAIL do-until-failure\n 10 authentication-restart 60\n!\npolicy-map type control s'
                                'ubscriber PMAP_DefaultWiredDot1xClosedAuth_MAB_1X\n event session-started match-all\n 10 class alway'
                                's do-until-failure\n 10 authenticate using mab priority 20\n event authentication-failure match-firs'
                                't\n 5 class DOT1X_FAILED do-until-failure\n 10 terminate dot1x\n 20 authentication-restart 60\n 10 c'
                                'lass AAA_SVR_DOWN_UNAUTHD_HOST do-until-failure\n 10 activate service-template DefaultCriticalAuthVl'
                                'an_SRV_TEMPLATE\n 20 activate service-template DefaultCriticalVoice_SRV_TEMPLATE\n 30 authorize\n 40'
                                ' pause reauthentication\n 20 class AAA_SVR_DOWN_AUTHD_HOST do-until-failure\n 10 pause reauthenticat'
                                'ion\n 20 authorize\n 30 class MAB_FAILED do-until-failure\n 10 terminate mab\n 20 authenticate using'
                                ' dot1x retries 2 retry-time 0 priority 10\n 40 class DOT1X_NO_RESP do-until-failure\n 10 terminate d'
                                'ot1x\n 20 authentication-restart 60\n 50 class DOT1X_TIMEOUT do-until-failure\n 10 terminate dot1x\n'
                                ' 20 authenticate using mab priority 20\n 60 class always do-until-failure\n 10 terminate mab\n 20 te'
                                'rminate dot1x\n 30 authentication-restart 60\n event aaa-available match-all\n 10 class IN_CRITICAL_'
                                'AUTH_CLOSED_MODE do-until-failure\n 10 clear-session\n 20 class NOT_IN_CRITICAL_AUTH_CLOSED_MODE do-'
                                'until-failure\n 10 resume reauthentication\n event agent-found match-all\n 10 class always do-until-'
                                'failure\n 10 terminate mab\n 20 authenticate using dot1x retries 2 retry-time 0 priority 10\n event '
                                'inactivity-timeout match-all\n 10 class always do-until-failure\n 10 clear-session\n event authentic'
                                'ation-success match-all\n event violation match-all\n 10 class always do-until-failure\n 10 restrict'
                                '\n event authorization-failure match-all\n 10 class AUTHC_SUCCESS-AUTHZ_FAIL do-until-failure\n 10 a'
                                'uthentication-restart 60\n!\npolicy-map type control subscriber PMAP_DefaultWiredDot1xLowImpactAuth_'
                                '1X_MAB\n event session-started match-all\n 10 class always do-until-failure\n 10 authenticate using '
                                'dot1x retries 2 retry-time 0 priority 10\n event authentication-failure match-first\n 5 class DOT1X_'
                                'FAILED do-until-failure\n 10 terminate dot1x\n 20 authenticate using mab priority 20\n 10 class AAA_'
                                'SVR_DOWN_UNAUTHD_HOST do-until-failure\n 10 activate service-template DefaultCriticalAuthVlan_SRV_TE'
                                'MPLATE\n 20 activate service-template DefaultCriticalVoice_SRV_TEMPLATE\n 25 activate service-templa'
                                'te DefaultCriticalAccess_SRV_TEMPLATE\n 30 authorize\n 40 pause reauthentication\n 20 class AAA_SVR_'
                                'DOWN_AUTHD_HOST do-until-failure\n 10 pause reauthentication\n 20 authorize\n 30 class DOT1X_NO_RESP'
                                ' do-until-failure\n 10 terminate dot1x\n 20 authenticate using mab priority 20\n 40 class MAB_FAILED'
                                ' do-until-failure\n 10 terminate mab\n 20 authentication-restart 60\n 50 class DOT1X_TIMEOUT do-unti'
                                'l-failure\n 10 terminate dot1x\n 20 authenticate using mab priority 20\n 60 class always do-until-fa'
                                'ilure\n 10 terminate dot1x\n 20 terminate mab\n 30 authentication-restart 60\n event aaa-available m'
                                'atch-all\n 10 class IN_CRITICAL_AUTH do-until-failure\n 10 clear-session\n 20 class NOT_IN_CRITICAL_'
                                'AUTH do-until-failure\n 10 resume reauthentication\n event agent-found match-all\n 10 class always d'
                                'o-until-failure\n 10 terminate mab\n 20 authenticate using dot1x retries 2 retry-time 0 priority 10\n'
                                ' event inactivity-timeout match-all\n 10 class always do-until-failure\n 10 clear-session\n event a'
                                'uthentication-success match-all\n event violation match-all\n 10 class always do-until-failure\n 10 '
                                'restrict\n event authorization-failure match-all\n 10 class AUTHC_SUCCESS-AUTHZ_FAIL do-until-failur'
                                'e\n 10 authentication-restart 60\n!\npolicy-map type control subscriber PMAP_DefaultWiredDot1xLowImp'
                                'actAuth_MAB_1X\n event session-started match-all\n 10 class always do-until-failure\n 10 authenticat'
                                'e using mab priority 20\n event authentication-failure match-first\n 5 class DOT1X_FAILED do-until-f'
                                'ailure\n 10 terminate dot1x\n 20 authentication-restart 60\n 10 class AAA_SVR_DOWN_UNAUTHD_HOST do-u'
                                'ntil-failure\n 10 activate service-template DefaultCriticalAuthVlan_SRV_TEMPLATE\n 20 activate servi'
                                'ce-template DefaultCriticalVoice_SRV_TEMPLATE\n 25 activate service-template DefaultCriticalAccess_S'
                                'RV_TEMPLATE\n 30 authorize\n 40 pause reauthentication\n 20 class AAA_SVR_DOWN_AUTHD_HOST do-until-f'
                                'ailure\n 10 pause reauthentication\n 20 authorize\n 30 class MAB_FAILED do-until-failure\n 10 termin'
                                'ate mab\n 20 authenticate using dot1x retries 2 retry-time 0 priority 10\n 40 class DOT1X_NO_RESP do'
                                '-until-failure\n 10 terminate dot1x\n 20 authentication-restart 60\n 50 class DOT1X_TIMEOUT do-until'
                                '-failure\n 10 terminate dot1x\n 20 authenticate using mab priority 20\n 60 class always do-until-fai'
                                'lure\n 10 terminate mab\n 20 terminate dot1x\n 30 authentication-restart 60\n event aaa-available ma'
                                'tch-all\n 10 class IN_CRITICAL_AUTH do-until-failure\n 10 clear-session\n 20 class NOT_IN_CRITICAL_A'
                                'UTH do-until-failure\n 10 resume reauthentication\n event agent-found match-all\n 10 class always do'
                                '-until-failure\n 10 terminate mab\n 20 authenticate using dot1x retries 2 retry-time 0 priority 10\n'
                                ' event inactivity-timeout match-all\n 10 class always do-until-failure\n 10 clear-session\n event au'
                                'thentication-success match-all\n event violation match-all\n 10 class always do-until-failure\n 10 r'
                                'estrict\n event authorization-failure match-all\n 10 class AUTHC_SUCCESS-AUTHZ_FAIL do-until-failure'
                                '\n 10 authentication-restart 60\n!\npolicy-map type control subscriber PMAP_DefaultWiredDot1xOpenAut'
                                'h_1X_MAB\n event session-started match-all\n 10 class always do-until-failure\n 10 authenticate usin'
                                'g dot1x retries 2 retry-time 0 priority 10\n event authentication-failure match-first\n 5 class DOT1'
                                'X_FAILED do-until-failure\n 10 terminate dot1x\n 20 authenticate using mab priority 20\n 10 class AA'
                                'A_SVR_DOWN_UNAUTHD_HOST do-until-failure\n 10 activate service-template DefaultCriticalAuthVlan_SRV_'
                                'TEMPLATE\n 20 activate service-template DefaultCriticalVoice_SRV_TEMPLATE\n 30 authorize\n 40 pause '
                                'reauthentication\n 20 class AAA_SVR_DOWN_AUTHD_HOST do-until-failure\n 10 pause reauthentication\n 2'
                                '0 authorize\n 30 class DOT1X_NO_RESP do-until-failure\n 10 terminate dot1x\n 20 authenticate using m'
                                'ab priority 20\n 40 class MAB_FAILED do-until-failure\n 10 terminate mab\n 20 authentication-restart'
                                ' 60\n 50 class DOT1X_TIMEOUT do-until-failure\n 10 terminate dot1x\n 20 authenticate using mab prior'
                                'ity 20\n 60 class always do-until-failure\n 10 terminate dot1x\n 20 terminate mab\n 30 authenticatio'
                                'n-restart 60\n event aaa-available match-all\n 10 class IN_CRITICAL_AUTH do-until-failure\n 10 clear'
                                '-session\n 20 class NOT_IN_CRITICAL_AUTH do-until-failure\n 10 resume reauthentication\n event agent'
                                '-found match-all\n 10 class always do-until-failure\n 10 terminate mab\n 20 authenticate using dot1x'
                                ' retries 2 retry-time 0 priority 10\n event inactivity-timeout match-all\n 10 class always do-until-'
                                'failure\n 10 clear-session\n event authentication-success match-all\n event violation match-all\n 10'
                                ' class always do-until-failure\n 10 restrict\n event authorization-failure match-all\n 10 class AUTH'
                                'C_SUCCESS-AUTHZ_FAIL do-until-failure\n 10 authentication-restart 60\n!\npolicy-map type control sub'
                                'scriber PMAP_DefaultWiredDot1xOpenAuth_MAB_1X\n event session-started match-all\n 10 class always do'
                                '-until-failure\n 10 authenticate using mab priority 20\n event authentication-failure match-first\n '
                                '5 class DOT1X_FAILED do-until-failure\n 10 terminate dot1x\n 20 authentication-restart 60\n 10 class'
                                ' AAA_SVR_DOWN_UNAUTHD_HOST do-until-failure\n 10 activate service-template DefaultCriticalAuthVlan_S'
                                'RV_TEMPLATE\n 20 activate service-template DefaultCriticalVoice_SRV_TEMPLATE\n 30 authorize\n 40 pau'
                                'se reauthentication\n 20 class AAA_SVR_DOWN_AUTHD_HOST do-until-failure\n 10 pause reauthentication\n'
                                ' 20 authorize\n 30 class MAB_FAILED do-until-failure\n 10 terminate mab\n 20 authenticate using dot'
                                '1x retries 2 retry-time 0 priority 10\n 40 class DOT1X_NO_RESP do-until-failure\n 10 terminate dot1x'
                                '\n 20 authentication-restart 60\n 50 class DOT1X_TIMEOUT do-until-failure\n 10 terminate dot1x\n 20 '
                                'authenticate using mab priority 20\n 60 class always do-until-failure\n 10 terminate mab\n 20 termin'
                                'ate dot1x\n 30 authentication-restart 60\n event aaa-available match-all\n 10 class IN_CRITICAL_AUTH'
                                ' do-until-failure\n 10 clear-session\n 20 class NOT_IN_CRITICAL_AUTH do-until-failure\n 10 resume re'
                                'authentication\n event agent-found match-all\n 10 class always do-until-failure\n 10 terminate mab\n'
                                ' 20 authenticate using dot1x retries 2 retry-time 0 priority 10\n event inactivity-timeout match-all'
                                '\n 10 class always do-until-failure\n 10 clear-session\n event authentication-success match-all\n ev'
                                'ent violation match-all\n 10 class always do-until-failure\n 10 restrict\n event authorization-failu'
                                're match-all\n 10 class AUTHC_SUCCESS-AUTHZ_FAIL do-until-failure\n 10 authentication-restart 60\n!\n'
                                'policy-map AutoConf-4.0-Trust-Cos-Input-Policy\n class class-default\n set cos cos table AutoConf-4'
                                '.0-Trust-Cos-Table\npolicy-map AutoConf-4.0-Output-Policy\n class AutoConf-4.0-Output-Priority-Queue'
                                '\n priority level 1 percent 30\n class AutoConf-4.0-Output-Control-Mgmt-Queue\n bandwidth remaining '
                                'percent 10 \n queue-limit dscp cs2 percent 80\n queue-limit dscp cs3 percent 90\n queue-limit dscp c'
                                's6 percent 100\n queue-limit dscp cs7 percent 100\n queue-buffers ratio 10\n class AutoConf-4.0-Outp'
                                'ut-Multimedia-ConfQueue\n bandwidth remaining percent 10 \n queue-buffers ratio 10\n class AutoConf-'
                                '4.0-Output-Trans-Data-Queue\n bandwidth remaining percent 10 \n queue-buffers ratio 10\n class AutoC'
                                'onf-4.0-Output-Bulk-Data-Queue\n bandwidth remaining percent 4 \n queue-buffers ratio 10\n class Aut'
                                'oConf-4.0-Output-Scavenger-Queue\n bandwidth remaining percent 1 \n queue-buffers ratio 10\n class A'
                                'utoConf-4.0-Output-Multimedia-StrmQueue\n bandwidth remaining percent 10 \n queue-buffers ratio 10\n'
                                ' class class-default\n bandwidth remaining percent 25 \n queue-buffers ratio 25\npolicy-map AutoConf'
                                '-4.0-CiscoSoftPhone-Input-Policy\n class AutoConf-4.0-Voip-Data-Class\n set dscp ef\n police cir 128'
                                '000 bc 8000\n conform-action transmit \n exceed-action set-dscp-transmit dscp table policed-dscp\n c'
                                'lass AutoConf-4.0-Voip-SignalClass\n set dscp cs3\n police cir 32000 bc 8000\n conform-action transm'
                                'it \n exceed-action set-dscp-transmit dscp table policed-dscp\n class AutoConf-4.0-Multimedia-Conf-C'
                                'lass\n set dscp af41\n police cir 5000000\n conform-action transmit \n exceed-action drop \n class A'
                                'utoConf-4.0-Bulk-Data-Class\n set dscp af11\n police cir 10000000\n conform-action transmit \n excee'
                                'd-action set-dscp-transmit dscp table policed-dscp\n class AutoConf-4.0-Transaction-Class\n set dscp'
                                ' af21\n police cir 10000000\n conform-action transmit \n exceed-action set-dscp-transmit dscp table '
                                'policed-dscp\n class AutoConf-4.0-Scavanger-Class\n set dscp cs1\n police cir 10000000\n conform-act'
                                'ion transmit \n exceed-action drop \n class AutoConf-4.0-Signaling-Class\n set dscp cs3\n police cir'
                                ' 32000 bc 8000\n conform-action transmit \n exceed-action drop \n class AutoConf-4.0-Default-Class\n'
                                ' set dscp default\n police cir 10000000\n conform-action transmit \n exceed-action set-dscp-transmit'
                                ' dscp table policed-dscp\npolicy-map system-cpp-policy\npolicy-map AutoConf-4.0-Trust-Dscp-Input-Pol'
                                'icy\n class class-default\n set dscp dscp table AutoConf-4.0-Trust-Dscp-Table\npolicy-map AutoConf-4'
                                '.0-CiscoPhone-Input-Policy\n class AutoConf-4.0-Voip-Data-CiscoPhone-Class\n set dscp ef\n police ci'
                                'r 128000 bc 8000\n conform-action transmit \n exceed-action set-dscp-transmit dscp table policed-dsc'
                                'p\n class AutoConf-4.0-Voip-Video-CiscoPhone-Class\n set dscp af41\n police cir 10000000 bc 8000\n c'
                                'onform-action transmit \n exceed-action set-dscp-transmit dscp table policed-dscp\n class AutoConf-4'
                                '.0-VoipSignal-CiscoPhone-Class\n set dscp cs3\n police cir 32000 bc 8000\n conform-action transmit \n'
                                ' exceed-action set-dscp-transmit dscp table policed-dscp\n class AutoConf-4.0-Default-Class\n set d'
                                'scp default\npolicy-map port_child_policy\n class non-client-nrt-class\n bandwidth remaining ratio 1'
                                '0\n!\n! \n!\n!\n!\n!\n!\n!\n!\n!\n!\nautoconf enable\n!\ntemplate AP_INTERFACE_TEMPLATE\n switchport'
                                ' mode trunk\n switchport nullgotiate\n switchport port-security maximum 3\n switchport port-security'
                                ' maximum 2 vlan access\n switchport port-security violation restrict\n switchport port-security agin'
                                'g time 2\n switchport port-security aging type inactivity\n switchport port-security\n service-polic'
                                'y input AutoConf-4.0-Trust-Cos-Input-Policy\n service-policy output AutoConf-4.0-Output-Policy\n!\nt'
                                'emplate DMP_INTERFACE_TEMPLATE\n spanning-tree portfast\n spanning-tree bpduguard enable\n switchpor'
                                't mode access\n switchport block unicast\n switchport port-security maximum 3\n switchport port-secu'
                                'rity maximum 2 vlan access\n switchport port-security violation restrict\n switchport port-security '
                                'aging time 2\n switchport port-security aging type inactivity\n switchport port-security\n service-p'
                                'olicy input AutoConf-4.0-Trust-Dscp-Input-Policy\n service-policy output AutoConf-4.0-Output-Policy\n'
                                '!\ntemplate DefaultWiredDot1xClosedAuth\n dot1x pae authenticator\n dot1x timeout supp-timeout 7\n '
                                'dot1x max-req 3\n switchport mode access\n switchport voice vlan 2046\n mab\n access-session closed\n'
                                ' access-session port-control auto\n authentication periodic\n authentication timer reauthenticate s'
                                'erver\n service-policy type control subscriber PMAP_DefaultWiredDot1xClosedAuth_1X_MAB\n!\ntemplate '
                                'DefaultWiredDot1xLowImpactAuth\n dot1x pae authenticator\n dot1x timeout supp-timeout 7\n dot1x max-'
                                'req 3\n switchport mode access\n switchport voice vlan 2046\n mab\n access-session port-control auto'
                                '\n authentication periodic\n authentication timer reauthenticate server\n service-policy type contro'
                                'l subscriber PMAP_DefaultWiredDot1xLowImpactAuth_1X_MAB\n!\ntemplate DefaultWiredDot1xOpenAuth\n dot'
                                '1x pae authenticator\n dot1x timeout supp-timeout 7\n dot1x max-req 3\n switchport mode access\n swi'
                                'tchport voice vlan 2046\n mab\n access-session port-control auto\n authentication periodic\n authent'
                                'ication timer reauthenticate server\n service-policy type control subscriber PMAP_DefaultWiredDot1xO'
                                'penAuth_1X_MAB\n!\ntemplate IP_CAMERA_INTERFACE_TEMPLATE\n spanning-tree portfast\n spanning-tree bp'
                                'duguard enable\n switchport mode access\n switchport block unicast\n switchport port-security maximu'
                                'm 3\n switchport port-security maximum 2 vlan access\n switchport port-security violation restrict\n'
                                ' switchport port-security aging time 2\n switchport port-security aging type inactivity\n switchport'
                                ' port-security\n service-policy input AutoConf-4.0-Trust-Dscp-Input-Policy\n service-policy output A'
                                'utoConf-4.0-Output-Policy\n!\ntemplate IP_PHONE_INTERFACE_TEMPLATE\n storm-control broadcast level p'
                                'ps 1k\n storm-control multicast level pps 2k\n storm-control action trap\n spanning-tree portfast\n '
                                'spanning-tree bpduguard enable\n switchport mode access\n switchport block unicast\n switchport port'
                                '-security maximum 3\n switchport port-security maximum 2 vlan access\n switchport port-security viol'
                                'ation restrict\n switchport port-security aging time 2\n switchport port-security aging type inactiv'
                                'ity\n switchport port-security\n service-policy input AutoConf-4.0-CiscoPhone-Input-Policy\n service'
                                '-policy output AutoConf-4.0-Output-Policy\n load-interval 30\n ip dhcp snooping limit rate 15\n!\nte'
                                'mplate LAP_INTERFACE_TEMPLATE\n storm-control broadcast level pps 1k\n storm-control multicast level'
                                ' pps 2k\n storm-control action trap\n spanning-tree portfast\n spanning-tree bpduguard enable\n swit'
                                'chport mode access\n switchport block unicast\n switchport port-security violation protect\n switchp'
                                'ort port-security aging time 2\n switchport port-security aging type inactivity\n switchport port-se'
                                'curity\n load-interval 30\n ip dhcp snooping limit rate 15\n!\ntemplate SWITCH_INTERFACE_TEMPLATE\n '
                                'switchport mode trunk\n!\ntemplate TP_INTERFACE_TEMPLATE\n storm-control broadcast level pps 1k\n st'
                                'orm-control multicast level pps 2k\n storm-control action trap\n spanning-tree portfast\n spanning-t'
                                'ree bpduguard enable\n switchport mode access\n switchport port-security maximum 3\n switchport port'
                                '-security maximum 2 vlan access\n switchport port-security violation restrict\n switchport port-secu'
                                'rity aging time 2\n switchport port-security aging type inactivity\n switchport port-security\n serv'
                                'ice-policy input AutoConf-4.0-Trust-Dscp-Input-Policy\n service-policy output AutoConf-4.0-Output-Po'
                                'licy\n load-interval 30\n ip dhcp snooping limit rate 15\n!\n!\ninterface Loopback0\n ip address 204'
                                '.1.2.1 255.255.255.255\n ip pim sparse-mode\n ip router isis \n!\ninterface LISP0\n!\ninterface LISP'
                                '0.4097\n!\ninterface LISP0.4098\n vrf forwarding DEFAULT_VN\n!\ninterface LISP0.4099\n vrf forwardin'
                                'g WirelessVNFGuest\n!\ninterface LISP0.4100\n vrf forwarding WiredVNFBLayer2\n!\ninterface LISP0.410'
                                '1\n vrf forwarding VN1\n!\ninterface LISP0.4102\n vrf forwarding WiredVNFB1\n!\ninterface LISP0.4103'
                                '\n vrf forwarding WiredVNStatic\n!\ninterface LISP0.4104\n vrf forwarding Fabric_VN\n!\ninterface LI'
                                'SP0.4105\n vrf forwarding WirelessVNFB\n!\ninterface LISP0.4106\n vrf forwarding IntraSubnet_VN\n!\n'
                                'interface LISP0.4107\n vrf forwarding VN3\n!\ninterface LISP0.4108\n vrf forwarding SGT_Port_test\n!'
                                '\ninterface LISP0.4109\n vrf forwarding VN2\n!\ninterface LISP0.4110\n vrf forwarding VN5\n!\ninterf'
                                'ace LISP0.4111\n vrf forwarding VN4\n!\ninterface LISP0.4112\n vrf forwarding VN7\n!\ninterface LISP'
                                '0.4113\n vrf forwarding VN6\n!\ninterface LISP0.4114\n vrf forwarding VN_SanJose_1\n!\ninterface L2L'
                                'ISP0\n ip access-group SDA-FABRIC-LISP in\n ip access-group SDA-FABRIC-LISP out\n!\ninterface L2LISP'
                                '0.8188\n!\ninterface L2LISP0.8189\n!\ninterface L2LISP0.8190\n!\ninterface L2LISP0.8191\n!\ninterfac'
                                'e L2LISP0.8192\n!\ninterface L2LISP0.8194\n!\ninterface L2LISP0.8195\n!\ninterface L2LISP0.8196\n!\n'
                                'interface L2LISP0.8197\n!\ninterface L2LISP0.8198\n!\ninterface L2LISP0.8199\n!\ninterface L2LISP0.8'
                                '200\n!\ninterface GigabitEthernet0/0\n vrf forwarding Mgmt-vrf\n no ip address\n shutdown\n negotiat'
                                'ion auto\n!\ninterface TwoGigabitEthernet1/0/1\n device-tracking attach-policy IPDT_POLICY\n!\ninter'
                                'face TwoGigabitEthernet1/0/2\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TwoGigabitEth'
                                'ernet1/0/3\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TwoGigabitEthernet1/0/4\n devic'
                                'e-tracking attach-policy IPDT_POLICY\n!\ninterface TwoGigabitEthernet1/0/5\n device-tracking attach-'
                                'policy IPDT_POLICY\n!\ninterface TwoGigabitEthernet1/0/6\n device-tracking attach-policy IPDT_POLICY'
                                '\n!\ninterface TwoGigabitEthernet1/0/7\n device-tracking attach-policy IPDT_POLICY\n!\ninterface Two'
                                'GigabitEthernet1/0/8\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TwoGigabitEthernet1/0'
                                '/9\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TwoGigabitEthernet1/0/10\n device-track'
                                'ing attach-policy IPDT_POLICY\n!\ninterface TwoGigabitEthernet1/0/11\n description AP PnP devices\n '
                                'switchport access vlan 2160\n switchport mode access\n!\ninterface TwoGigabitEthernet1/0/12\n descri'
                                'ption AP PnP devices\n switchport access vlan 2160\n switchport mode access\n!\ninterface TwoGigabit'
                                'Ethernet1/0/13\n description AP PnP devices\n switchport access vlan 2160\n switchport mode access\n'
                                '!\ninterface TwoGigabitEthernet1/0/14\n description AP PnP devices\n switchport access vlan 2160\n s'
                                'witchport mode access\n!\ninterface TwoGigabitEthernet1/0/15\n description AP PnP devices\n switchpo'
                                'rt access vlan 2160\n switchport mode access\n!\ninterface TwoGigabitEthernet1/0/16\n device-trackin'
                                'g attach-policy IPDT_POLICY\n!\ninterface TwoGigabitEthernet1/0/17\n device-tracking attach-policy I'
                                'PDT_POLICY\n!\ninterface TwoGigabitEthernet1/0/18\n device-tracking attach-policy IPDT_POLICY\n!\nin'
                                'terface TwoGigabitEthernet1/0/19\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TwoGigabi'
                                'tEthernet1/0/20\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TwoGigabitEthernet1/0/21\n'
                                ' device-tracking attach-policy IPDT_POLICY\n!\ninterface TwoGigabitEthernet1/0/22\n device-tracking '
                                'attach-policy IPDT_POLICY\n!\ninterface TwoGigabitEthernet1/0/23\n device-tracking attach-policy IPD'
                                'T_POLICY\n!\ninterface TwoGigabitEthernet1/0/24\n device-tracking attach-policy IPDT_POLICY\n!\ninte'
                                'rface TwoGigabitEthernet1/0/25\n description AP PnP devices\n switchport access vlan 2160\n switchpo'
                                'rt mode access\n!\ninterface TwoGigabitEthernet1/0/26\n description AP PnP devices\n switchport acce'
                                'ss vlan 2160\n switchport mode access\n!\ninterface TwoGigabitEthernet1/0/27\n device-tracking attac'
                                'h-policy IPDT_POLICY\n!\ninterface TwoGigabitEthernet1/0/28\n device-tracking attach-policy IPDT_POL'
                                'ICY\n!\ninterface TwoGigabitEthernet1/0/29\n device-tracking attach-policy IPDT_POLICY\n!\ninterface'
                                ' TwoGigabitEthernet1/0/30\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TwoGigabitEthern'
                                'et1/0/31\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TwoGigabitEthernet1/0/32\n device'
                                '-tracking attach-policy IPDT_POLICY\n!\ninterface TwoGigabitEthernet1/0/33\n device-tracking attach-'
                                'policy IPDT_POLICY\n!\ninterface TwoGigabitEthernet1/0/34\n device-tracking attach-policy IPDT_POLIC'
                                'Y\n!\ninterface TwoGigabitEthernet1/0/35\n device-tracking attach-policy IPDT_POLICY\n!\ninterface T'
                                'woGigabitEthernet1/0/36\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TenGigabitEthernet'
                                '1/0/37\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TenGigabitEthernet1/0/38\n device-t'
                                'racking attach-policy IPDT_POLICY\n!\ninterface TenGigabitEthernet1/0/39\n device-tracking attach-po'
                                'licy IPDT_POLICY\n!\ninterface TenGigabitEthernet1/0/40\n device-tracking attach-policy IPDT_POLICY\n'
                                '!\ninterface TenGigabitEthernet1/0/41\n device-tracking attach-policy IPDT_POLICY\n!\ninterface Ten'
                                'GigabitEthernet1/0/42\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TenGigabitEthernet1/'
                                '0/43\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TenGigabitEthernet1/0/44\n device-tra'
                                'cking attach-policy IPDT_POLICY\n!\ninterface TenGigabitEthernet1/0/45\n device-tracking attach-poli'
                                'cy IPDT_POLICY\n!\ninterface TenGigabitEthernet1/0/46\n device-tracking attach-policy IPDT_POLICY\n!'
                                '\ninterface TenGigabitEthernet1/0/47\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TenGi'
                                'gabitEthernet1/0/48\n device-tracking attach-policy IPDT_POLICY\n!\ninterface GigabitEthernet1/1/1\n'
                                ' device-tracking attach-policy IPDT_POLICY\n!\ninterface GigabitEthernet1/1/2\n device-tracking atta'
                                'ch-policy IPDT_POLICY\n!\ninterface GigabitEthernet1/1/3\n device-tracking attach-policy IPDT_POLICY'
                                '\n!\ninterface GigabitEthernet1/1/4\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TenGig'
                                'abitEthernet1/1/1\n description SJ-BN-9300\n no switchport\n ip address 204.1.1.2 255.255.255.252\n '
                                'no ip redirects\n no ip proxy-arp\n ip pim sparse-mode\n ip router isis \n load-interval 30\n bfd in'
                                'terval 750 min_rx 750 multiplier 3\n no bfd echo\n!\ninterface TenGigabitEthernet1/1/2\n device-trac'
                                'king attach-policy IPDT_POLICY\n!\ninterface TenGigabitEthernet1/1/3\n device-tracking attach-policy'
                                ' IPDT_POLICY\n!\ninterface TenGigabitEthernet1/1/4\n device-tracking attach-policy IPDT_POLICY\n!\ni'
                                'nterface TenGigabitEthernet1/1/5\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TenGigabi'
                                'tEthernet1/1/6\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TenGigabitEthernet1/1/7\n d'
                                'evice-tracking attach-policy IPDT_POLICY\n!\ninterface TenGigabitEthernet1/1/8\n device-tracking att'
                                'ach-policy IPDT_POLICY\n!\ninterface FortyGigabitEthernet1/1/1\n device-tracking attach-policy IPDT_'
                                'POLICY\n!\ninterface FortyGigabitEthernet1/1/2\n device-tracking attach-policy IPDT_POLICY\n!\ninter'
                                'face TwentyFiveGigE1/1/1\n device-tracking attach-policy IPDT_POLICY\n!\ninterface TwentyFiveGigE1/1'
                                '/2\n device-tracking attach-policy IPDT_POLICY\n!\ninterface AppGigabitEthernet1/0/1\n!\ninterface B'
                                'luetooth0/4\n vrf forwarding Mgmt-vrf\n no ip address\n shutdown\n negotiation auto\n enable\n!\nint'
                                'erface Vlan1\n no ip address\n shutdown\n!\ninterface Vlan1021\n description Configured from Catalys'
                                't Center\n mac-address 0000.0c9f.f718\n vrf forwarding WiredVNFB1\n ip address 204.1.80.1 255.255.25'
                                '5.0\n ip helper-address 204.192.3.40\n no ip redirects\n ip route-cache same-interface\n ipv6 addres'
                                's 2004:1:80::1:1/112\n ipv6 enable\n ipv6 nd dad attempts 0\n ipv6 nd managed-config-flag\n ipv6 nd '
                                'other-config-flag\n ipv6 nd router-preference High\n ipv6 dhcp relay destination 2004:192:3::40\n ip'
                                'v6 dhcp relay source-interface Vlan1021\n ipv6 dhcp relay trust\n no lisp mobility liveness test\n l'
                                'isp mobility 80net_sub-WiredVNFB1-IPV4\n lisp mobility 80net_sub-WiredVNFB1-IPV6\n!\ninterface Vlan1'
                                '022\n description Configured from Catalyst Center\n mac-address 0000.0c9f.fda7\n vrf forwarding Wire'
                                'dVNFB1\n ip address 204.1.64.1 255.255.255.0\n ip helper-address 204.192.3.40\n no ip redirects\n ip'
                                ' route-cache same-interface\n ipv6 address 2004:1:64::1:1/112\n ipv6 enable\n ipv6 nd dad attempts 0'
                                '\n ipv6 nd managed-config-flag\n ipv6 nd other-config-flag\n ipv6 nd router-preference High\n ipv6 d'
                                'hcp relay destination 2004:192:3::40\n ipv6 dhcp relay source-interface Vlan1022\n ipv6 dhcp relay t'
                                'rust\n no lisp mobility liveness test\n lisp mobility 64net_sub-WiredVNFB1-IPV4\n lisp mobility 64ne'
                                't_sub-WiredVNFB1-IPV6\n!\ninterface Vlan1023\n description Configured from Catalyst Center\n mac-add'
                                'ress 0000.0c9f.f37e\n vrf forwarding WirelessVNFB\n ip address 204.1.240.1 255.255.252.0\n ip helper'
                                '-address 204.192.3.40\n no ip redirects\n ip route-cache same-interface\n ipv6 address 2004:1:240::1'
                                ':1/112\n ipv6 enable\n ipv6 nd dad attempts 0\n ipv6 nd managed-config-flag\n ipv6 nd other-config-f'
                                'lag\n ipv6 nd router-preference High\n ipv6 dhcp relay destination 2004:192:3::40\n ipv6 dhcp relay '
                                'source-interface Vlan1023\n ipv6 dhcp relay trust\n no lisp mobility liveness test\n lisp mobility W'
                                'SClients_sub-WirelessVNFB-IPV4\n lisp mobility WSClients_sub-WirelessVNFB-IPV6\n!\ninterface Vlan102'
                                '4\n description Configured from Catalyst Center\n mac-address 0000.0c9f.feca\n vrf forwarding Wirele'
                                'ssVNFB\n ip address 204.1.224.1 255.255.252.0\n ip helper-address 204.192.3.40\n no ip redirects\n i'
                                'p route-cache same-interface\n ipv6 address 2004:1:224::1:1/112\n ipv6 enable\n ipv6 nd dad attempts'
                                ' 0\n ipv6 nd managed-config-flag\n ipv6 nd other-config-flag\n ipv6 nd router-preference High\n ipv6'
                                ' dhcp relay destination 2004:192:3::40\n ipv6 dhcp relay source-interface Vlan1024\n ipv6 dhcp relay'
                                ' trust\n no lisp mobility liveness test\n lisp mobility WClients_sub-WirelessVNFB-IPV4\n lisp mobili'
                                'ty WClients_sub-WirelessVNFB-IPV6\n!\ninterface Vlan1025\n description Configured from Catalyst Cent'
                                'er\n mac-address 0000.0c9f.f383\n ip address 204.1.32.1 255.255.255.0\n ip helper-address global 204'
                                '.192.3.40\n no ip redirects\n ip route-cache same-interface\n no lisp mobility liveness test\n lisp '
                                'mobility EXT_POOL_sub-INFRA_VN-IPV4\n!\ninterface Vlan1027\n description Configured from Catalyst Ce'
                                'nter\n mac-address 0000.0c9f.f966\n vrf forwarding WiredVNStatic\n ip address 204.1.48.1 255.255.255'
                                '.0\n ip helper-address 204.192.3.40\n no ip redirects\n ip route-cache same-interface\n ipv6 address'
                                ' 2004:1:48::1:1/112\n ipv6 enable\n ipv6 nd dad attempts 0\n ipv6 nd managed-config-flag\n ipv6 nd o'
                                'ther-config-flag\n ipv6 nd router-preference High\n ipv6 dhcp relay destination 2004:192:3::40\n ipv'
                                '6 dhcp relay source-interface Vlan1027\n ipv6 dhcp relay trust\n no lisp mobility liveness test\n li'
                                'sp mobility SENSORPool_sub-WiredVNStatic-IPV4\n lisp mobility SENSORPool_sub-WiredVNStatic-IPV6\n!\n'
                                'interface Vlan1028\n description Configured from Catalyst Center\n mac-address 0000.0c9f.f276\n vrf '
                                'forwarding WiredVNFBLayer2\n ip address 204.1.112.1 255.255.252.0\n ip helper-address 204.192.3.40\n'
                                ' no ip redirects\n ip route-cache same-interface\n ipv6 address 2004:1:112::1:1/112\n ipv6 enable\n '
                                'ipv6 nd dad attempts 0\n ipv6 nd managed-config-flag\n ipv6 nd other-config-flag\n ipv6 nd router-pr'
                                'eference High\n ipv6 dhcp relay destination 2004:192:3::40\n ipv6 dhcp relay source-interface Vlan10'
                                '28\n ipv6 dhcp relay trust\n no lisp mobility liveness test\n lisp mobility 112net_sub-WiredVNFBLaye'
                                'r2-IPV4\n lisp mobility 112net_sub-WiredVNFBLayer2-IPV6\n!\ninterface Vlan1029\n description Configu'
                                'red from Catalyst Center\n mac-address 0000.0c9f.f78a\n vrf forwarding WiredVNFBLayer2\n ip address '
                                '40.50.0.1 255.255.255.0\n ip helper-address 204.192.3.40\n no ip redirects\n ip route-cache same-int'
                                'erface\n ipv6 address 2040:50::1:0:1/96\n ipv6 enable\n ipv6 nd dad attempts 0\n ipv6 nd managed-con'
                                'fig-flag\n ipv6 nd other-config-flag\n ipv6 nd router-preference High\n ipv6 dhcp relay destination '
                                '2004:192:3::40\n ipv6 dhcp relay source-interface Vlan1029\n ipv6 dhcp relay trust\n no lisp mobilit'
                                'y liveness test\n lisp mobility CRITICAL_VLAN-IPV4\n lisp mobility CRITICAL_VLAN-IPV6\n!\ninterface '
                                'Vlan1030\n description Configured from Catalyst Center\n mac-address 0000.0c9f.f563\n vrf forwarding'
                                ' WiredVNFBLayer2\n ip address 204.1.96.1 255.255.252.0\n ip helper-address 204.192.3.40\n no ip redi'
                                'rects\n ip route-cache same-interface\n ipv6 address 2004:1:96::1:1/112\n ipv6 enable\n ipv6 nd dad '
                                'attempts 0\n ipv6 nd managed-config-flag\n ipv6 nd other-config-flag\n ipv6 nd router-preference Hig'
                                'h\n ipv6 dhcp relay destination 2004:192:3::40\n ipv6 dhcp relay source-interface Vlan1030\n ipv6 dh'
                                'cp relay trust\n no lisp mobility liveness test\n lisp mobility 96net_sub-WiredVNFBLayer2-IPV4\n lis'
                                'p mobility 96net_sub-WiredVNFBLayer2-IPV6\n!\ninterface Vlan1031\n description Configured from Catal'
                                'yst Center\n mac-address 0000.0c9f.f528\n vrf forwarding WirelessVNFGuest\n ip address 204.1.128.1 2'
                                '55.255.252.0\n ip helper-address 204.192.3.40\n no ip redirects\n ip route-cache same-interface\n no'
                                ' lisp mobility liveness test\n lisp mobility GP_sub-WirelessVNFGuest-IPV4\n!\ninterface Vlan1032\n d'
                                'escription Configured from Catalyst Center\n mac-address 0000.0c9f.fd46\n vrf forwarding SGT_Port_te'
                                'st\n ip address 123.123.0.1 255.255.240.0\n ip helper-address 204.192.3.40\n no ip redirects\n ip ro'
                                'ute-cache same-interface\n no lisp mobility liveness test\n lisp mobility SGT_Port_test_sub-SGT_Port'
                                '_test-IPV4\n!\ninterface Vlan2046\n description Configured from Catalyst Center\n mac-address 0000.0'
                                'c9f.f2f2\n vrf forwarding WiredVNFBLayer2\n ip address 40.50.10.1 255.255.255.0\n ip helper-address '
                                '204.192.3.40\n no ip redirects\n ip route-cache same-interface\n ipv6 address 2040:50::10:0:1/96\n i'
                                'pv6 enable\n ipv6 nd dad attempts 0\n ipv6 nd managed-config-flag\n ipv6 nd other-config-flag\n ipv6'
                                ' nd router-preference High\n ipv6 dhcp relay destination 2004:192:3::40\n ipv6 dhcp relay source-int'
                                'erface Vlan2046\n ipv6 dhcp relay trust\n no lisp mobility liveness test\n lisp mobility VOICE_VLAN-'
                                'IPV4\n lisp mobility VOICE_VLAN-IPV6\n!\ninterface Vlan2160\n ip address 204.1.216.1 255.255.255.192'
                                '\n no ip redirects\n no ip proxy-arp\n ip pim sparse-mode\n ip router isis \n load-interval 30\n bfd'
                                ' interval 750 min_rx 750 multiplier 3\n no bfd echo\n!\nrouter lisp\n domain-id 108343398\n locator-'
                                'table default\n locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n IPv4-interface Loopback0 pri'
                                'ority 10 weight 10\n exit-locator-set\n !\n locator default-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7a'
                                'e39f3\n service ipv4\n encapsulation vxlan\n itr map-resolver 204.1.2.3\n etr map-server 204.1.2.3 k'
                                'ey 7 *********\n etr map-server 204.1.2.3 proxy-reply\n etr\n sgt\n no map-cache away-eids send-map-'
                                'request\n proxy-itr 204.1.2.1\n exit-service-ipv4\n !\n service ipv6\n encapsulation vxlan\n itr map'
                                '-resolver 204.1.2.3\n etr map-server 204.1.2.3 key 7 *********\n etr map-server 204.1.2.3 proxy-repl'
                                'y\n etr\n sgt\n no map-cache away-eids send-map-request\n proxy-itr 204.1.2.1\n exit-service-ipv6\n '
                                '!\n service ethernet\n itr map-resolver 204.1.2.3\n itr\n etr map-server 204.1.2.3 key 7 *********\n'
                                ' etr map-server 204.1.2.3 proxy-reply\n etr\n exit-service-ethernet\n !\n instance-id 4097\n remote-'
                                'rloc-probe on-route-change\n dynamic-eid EXT_POOL_sub-INFRA_VN-IPV4\n database-mapping 204.1.32.0/24'
                                ' locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-dynamic-eid\n !\n service ipv4\n eid-t'
                                'able default\n exit-service-ipv4\n !\n service ipv6\n eid-table default\n exit-service-ipv6\n !\n ex'
                                'it-instance-id\n !\n instance-id 4098\n remote-rloc-probe on-route-change\n service ipv4\n eid-table'
                                ' vrf DEFAULT_VN\n map-cache 0.0.0.0/0 map-request\n exit-service-ipv4\n !\n service ipv6\n eid-table'
                                ' vrf DEFAULT_VN\n map-cache ::/0 map-request\n exit-service-ipv6\n !\n exit-instance-id\n !\n instan'
                                'ce-id 4099\n remote-rloc-probe on-route-change\n dynamic-eid GP_sub-WirelessVNFGuest-IPV4\n database'
                                '-mapping 204.1.128.0/22 locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-dynamic-eid\n !'
                                '\n service ipv4\n eid-table vrf WirelessVNFGuest\n map-cache 0.0.0.0/0 map-request\n exit-service-ip'
                                'v4\n !\n service ipv6\n eid-table vrf WirelessVNFGuest\n map-cache ::/0 map-request\n exit-service-i'
                                'pv6\n !\n exit-instance-id\n !\n instance-id 4100\n remote-rloc-probe on-route-change\n dynamic-eid '
                                '112net_sub-WiredVNFBLayer2-IPV4\n database-mapping 204.1.112.0/22 locator-set rloc_8e4e13a3-dc43-43b'
                                '8-97e1-c3d9c7ae39f3\n exit-dynamic-eid\n !\n dynamic-eid 112net_sub-WiredVNFBLayer2-IPV6\n database-'
                                'mapping 2004:1:112::1:0/112 locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-dynamic-eid'
                                '\n !\n dynamic-eid 96net_sub-WiredVNFBLayer2-IPV4\n database-mapping 204.1.96.0/22 locator-set rloc_'
                                '8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-dynamic-eid\n !\n dynamic-eid 96net_sub-WiredVNFBLayer2-'
                                'IPV6\n database-mapping 2004:1:96::1:0/112 locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n e'
                                'xit-dynamic-eid\n !\n dynamic-eid CRITICAL_VLAN-IPV4\n database-mapping 40.50.0.0/24 locator-set rlo'
                                'c_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-dynamic-eid\n !\n dynamic-eid CRITICAL_VLAN-IPV6\n dat'
                                'abase-mapping 2040:50::1:0:0/96 locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-dynamic'
                                '-eid\n !\n dynamic-eid VOICE_VLAN-IPV4\n database-mapping 40.50.10.0/24 locator-set rloc_8e4e13a3-dc'
                                '43-43b8-97e1-c3d9c7ae39f3\n exit-dynamic-eid\n !\n dynamic-eid VOICE_VLAN-IPV6\n database-mapping 20'
                                '40:50::10:0:0/96 locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-dynamic-eid\n !\n serv'
                                'ice ipv4\n eid-table vrf WiredVNFBLayer2\n map-cache 0.0.0.0/0 map-request\n exit-service-ipv4\n !\n'
                                ' service ipv6\n eid-table vrf WiredVNFBLayer2\n map-cache ::/0 map-request\n exit-service-ipv6\n !\n'
                                ' exit-instance-id\n !\n instance-id 4101\n remote-rloc-probe on-route-change\n service ipv4\n eid-ta'
                                'ble vrf VN1\n map-cache 0.0.0.0/0 map-request\n exit-service-ipv4\n !\n service ipv6\n eid-table vrf'
                                ' VN1\n map-cache ::/0 map-request\n exit-service-ipv6\n !\n exit-instance-id\n !\n instance-id 4102\n'
                                ' remote-rloc-probe on-route-change\n dynamic-eid 64net_sub-WiredVNFB1-IPV4\n database-mapping 204.1'
                                '.64.0/24 locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-dynamic-eid\n !\n dynamic-eid '
                                '64net_sub-WiredVNFB1-IPV6\n database-mapping 2004:1:64::1:0/112 locator-set rloc_8e4e13a3-dc43-43b8-'
                                '97e1-c3d9c7ae39f3\n exit-dynamic-eid\n !\n dynamic-eid 80net_sub-WiredVNFB1-IPV4\n database-mapping '
                                '204.1.80.0/24 locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-dynamic-eid\n !\n dynamic'
                                '-eid 80net_sub-WiredVNFB1-IPV6\n database-mapping 2004:1:80::1:0/112 locator-set rloc_8e4e13a3-dc43-'
                                '43b8-97e1-c3d9c7ae39f3\n exit-dynamic-eid\n !\n service ipv4\n eid-table vrf WiredVNFB1\n map-cache '
                                '0.0.0.0/0 map-request\n exit-service-ipv4\n !\n service ipv6\n eid-table vrf WiredVNFB1\n map-cache '
                                '::/0 map-request\n exit-service-ipv6\n !\n exit-instance-id\n !\n instance-id 4103\n remote-rloc-pro'
                                'be on-route-change\n dynamic-eid SENSORPool_sub-WiredVNStatic-IPV4\n database-mapping 204.1.48.0/24 '
                                'locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-dynamic-eid\n !\n dynamic-eid SENSORPoo'
                                'l_sub-WiredVNStatic-IPV6\n database-mapping 2004:1:48::1:0/112 locator-set rloc_8e4e13a3-dc43-43b8-9'
                                '7e1-c3d9c7ae39f3\n exit-dynamic-eid\n !\n service ipv4\n eid-table vrf WiredVNStatic\n map-cache 0.0'
                                '.0.0/0 map-request\n exit-service-ipv4\n !\n service ipv6\n eid-table vrf WiredVNStatic\n map-cache '
                                '::/0 map-request\n exit-service-ipv6\n !\n exit-instance-id\n !\n instance-id 4104\n remote-rloc-pro'
                                'be on-route-change\n service ipv4\n eid-table vrf Fabric_VN\n map-cache 0.0.0.0/0 map-request\n exit'
                                '-service-ipv4\n !\n service ipv6\n eid-table vrf Fabric_VN\n map-cache ::/0 map-request\n exit-servi'
                                'ce-ipv6\n !\n exit-instance-id\n !\n instance-id 4105\n remote-rloc-probe on-route-change\n dynamic-'
                                'eid WClients_sub-WirelessVNFB-IPV4\n database-mapping 204.1.224.0/22 locator-set rloc_8e4e13a3-dc43-'
                                '43b8-97e1-c3d9c7ae39f3\n exit-dynamic-eid\n !\n dynamic-eid WClients_sub-WirelessVNFB-IPV6\n databas'
                                'e-mapping 2004:1:224::1:0/112 locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-dynamic-e'
                                'id\n !\n dynamic-eid WSClients_sub-WirelessVNFB-IPV4\n database-mapping 204.1.240.0/22 locator-set r'
                                'loc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-dynamic-eid\n !\n dynamic-eid WSClients_sub-Wireless'
                                'VNFB-IPV6\n database-mapping 2004:1:240::1:0/112 locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39'
                                'f3\n exit-dynamic-eid\n !\n service ipv4\n eid-table vrf WirelessVNFB\n map-cache 0.0.0.0/0 map-requ'
                                'est\n exit-service-ipv4\n !\n service ipv6\n eid-table vrf WirelessVNFB\n map-cache ::/0 map-request'
                                '\n exit-service-ipv6\n !\n exit-instance-id\n !\n instance-id 4106\n remote-rloc-probe on-route-chan'
                                'ge\n service ipv4\n eid-table vrf IntraSubnet_VN\n map-cache 0.0.0.0/0 map-request\n exit-service-ip'
                                'v4\n !\n service ipv6\n eid-table vrf IntraSubnet_VN\n map-cache ::/0 map-request\n exit-service-ipv'
                                '6\n !\n exit-instance-id\n !\n instance-id 4107\n remote-rloc-probe on-route-change\n service ipv4\n'
                                ' eid-table vrf VN3\n map-cache 0.0.0.0/0 map-request\n exit-service-ipv4\n !\n service ipv6\n eid-ta'
                                'ble vrf VN3\n map-cache ::/0 map-request\n exit-service-ipv6\n !\n exit-instance-id\n !\n instance-i'
                                'd 4108\n remote-rloc-probe on-route-change\n dynamic-eid SGT_Port_test_sub-SGT_Port_test-IPV4\n data'
                                'base-mapping 123.123.0.0/20 locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-dynamic-eid'
                                '\n !\n service ipv4\n eid-table vrf SGT_Port_test\n map-cache 0.0.0.0/0 map-request\n exit-service-i'
                                'pv4\n !\n service ipv6\n eid-table vrf SGT_Port_test\n map-cache ::/0 map-request\n exit-service-ipv'
                                '6\n !\n exit-instance-id\n !\n instance-id 4109\n remote-rloc-probe on-route-change\n service ipv4\n'
                                ' eid-table vrf VN2\n map-cache 0.0.0.0/0 map-request\n exit-service-ipv4\n !\n service ipv6\n eid-ta'
                                'ble vrf VN2\n map-cache ::/0 map-request\n exit-service-ipv6\n !\n exit-instance-id\n !\n instance-i'
                                'd 4110\n remote-rloc-probe on-route-change\n service ipv4\n eid-table vrf VN5\n map-cache 0.0.0.0/0 '
                                'map-request\n exit-service-ipv4\n !\n service ipv6\n eid-table vrf VN5\n map-cache ::/0 map-request\n'
                                ' exit-service-ipv6\n !\n exit-instance-id\n !\n instance-id 4111\n remote-rloc-probe on-route-chang'
                                'e\n service ipv4\n eid-table vrf VN4\n map-cache 0.0.0.0/0 map-request\n exit-service-ipv4\n !\n ser'
                                'vice ipv6\n eid-table vrf VN4\n map-cache ::/0 map-request\n exit-service-ipv6\n !\n exit-instance-i'
                                'd\n !\n instance-id 4112\n remote-rloc-probe on-route-change\n service ipv4\n eid-table vrf VN7\n ma'
                                'p-cache 0.0.0.0/0 map-request\n exit-service-ipv4\n !\n service ipv6\n eid-table vrf VN7\n map-cache'
                                ' ::/0 map-request\n exit-service-ipv6\n !\n exit-instance-id\n !\n instance-id 4113\n remote-rloc-pr'
                                'obe on-route-change\n service ipv4\n eid-table vrf VN6\n map-cache 0.0.0.0/0 map-request\n exit-serv'
                                'ice-ipv4\n !\n service ipv6\n eid-table vrf VN6\n map-cache ::/0 map-request\n exit-service-ipv6\n !'
                                '\n exit-instance-id\n !\n instance-id 4114\n remote-rloc-probe on-route-change\n service ipv4\n eid-'
                                'table vrf VN_SanJose_1\n map-cache 0.0.0.0/0 map-request\n exit-service-ipv4\n !\n service ipv6\n ei'
                                'd-table vrf VN_SanJose_1\n map-cache ::/0 map-request\n exit-service-ipv6\n !\n exit-instance-id\n !'
                                '\n instance-id 8188\n remote-rloc-probe on-route-change\n service ethernet\n eid-table vlan 1021\n d'
                                'atabase-mapping mac locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-service-ethernet\n '
                                '!\n exit-instance-id\n !\n instance-id 8189\n remote-rloc-probe on-route-change\n service ethernet\n'
                                ' eid-table vlan 1022\n database-mapping mac locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n '
                                'exit-service-ethernet\n !\n exit-instance-id\n !\n instance-id 8190\n remote-rloc-probe on-route-cha'
                                'nge\n service ethernet\n eid-table vlan 1023\n broadcast-underlay 239.0.17.3\n flood unknown-unicast'
                                '\n database-mapping mac locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-service-etherne'
                                't\n !\n exit-instance-id\n !\n instance-id 8191\n remote-rloc-probe on-route-change\n service ethern'
                                'et\n eid-table vlan 1024\n broadcast-underlay 239.0.17.3\n flood unknown-unicast\n database-mapping '
                                'mac locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-service-ethernet\n !\n exit-instanc'
                                'e-id\n !\n instance-id 8192\n remote-rloc-probe on-route-change\n service ethernet\n eid-table vlan '
                                '1025\n database-mapping mac locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-service-eth'
                                'ernet\n !\n exit-instance-id\n !\n instance-id 8194\n remote-rloc-probe on-route-change\n service et'
                                'hernet\n eid-table vlan 1027\n database-mapping mac locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7a'
                                'e39f3\n exit-service-ethernet\n !\n exit-instance-id\n !\n instance-id 8195\n remote-rloc-probe on-r'
                                'oute-change\n service ethernet\n eid-table vlan 1028\n broadcast-underlay 239.0.17.3\n flood arp-nd\n'
                                ' flood unknown-unicast\n database-mapping mac locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3'
                                '\n exit-service-ethernet\n !\n exit-instance-id\n !\n instance-id 8196\n remote-rloc-probe on-route-'
                                'change\n service ethernet\n eid-table vlan 2046\n database-mapping mac locator-set rloc_8e4e13a3-dc4'
                                '3-43b8-97e1-c3d9c7ae39f3\n exit-service-ethernet\n !\n exit-instance-id\n !\n instance-id 8197\n rem'
                                'ote-rloc-probe on-route-change\n service ethernet\n eid-table vlan 1029\n database-mapping mac locat'
                                'or-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-service-ethernet\n !\n exit-instance-id\n !\n'
                                ' instance-id 8198\n remote-rloc-probe on-route-change\n service ethernet\n eid-table vlan 1030\n br'
                                'oadcast-underlay 239.0.17.3\n flood arp-nd\n flood unknown-unicast\n database-mapping mac locator-se'
                                't rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-service-ethernet\n !\n exit-instance-id\n !\n ins'
                                'tance-id 8199\n remote-rloc-probe on-route-change\n service ethernet\n eid-table vlan 1031\n databas'
                                'e-mapping mac locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-service-ethernet\n !\n ex'
                                'it-instance-id\n !\n instance-id 8200\n remote-rloc-probe on-route-change\n service ethernet\n eid-t'
                                'able vlan 1032\n database-mapping mac locator-set rloc_8e4e13a3-dc43-43b8-97e1-c3d9c7ae39f3\n exit-s'
                                'ervice-ethernet\n !\n exit-instance-id\n !\n ipv4 locator reachability minimum-mask-length 32\n ipv4'
                                ' source-locator Loopback0\n ipv6 locator reachability minimum-mask-length 128\n ipv6 source-locator '
                                'Loopback0\n exit-router-lisp\n!\nrouter isis\n net 49.0001.1111.1111.0013.00\n is-type level-2-only\n'
                                ' metric-style wide\n log-adjacency-changes\n bfd all-interfaces\n!\nip forward-protocol nd\nip http'
                                ' server\nip http authentication local\nip http secure-server\nip http client source-interface Loopba'
                                'ck0\nip pim rp-address 204.1.2.36\nip pim register-source Loopback0\nip pim ssm default\nip tftp sou'
                                'rce-interface GigabitEthernet0/0\nip route vrf Mgmt-vrf 0.0.0.0 0.0.0.0 10.22.40.1\nip ssh bulk-mode'
                                ' 131072\nip ssh source-interface Loopback0\nip scp server enable\n!\n!\nip access-list extended ACL_'
                                'WEBAUTH_REDIRECT\n 40 deny ip any host 172.23.241.229\n 500 permit tcp any any eq www\n 600 permit t'
                                'cp any any eq 443\n 700 permit tcp any any eq 8443\n 800 deny udp any any eq domain\n 900 deny udp a'
                                'ny eq bootpc any eq bootps\nip access-list extended AutoConf-4.0-Acl-Default\n 10 permit ip any any\n'
                                'ip access-list extended IPV4_CRITICAL_AUTH_ACL\n 10 permit ip any any\nip access-list extended IPV4'
                                '_PRE_AUTH_ACL\n 10 permit udp any any eq bootpc\n 20 permit udp any any eq bootps\n 30 permit udp an'
                                'y any eq domain\n 40 deny ip any any\nip access-list extended SDA-FABRIC-LISP\n 10 deny ip any host '
                                '224.0.0.22\n 20 deny ip any host 224.0.0.13\n 30 deny ip any host 224.0.0.1\n 40 permit ip any any\n'
                                '!\nip radius source-interface Loopback0 \nlogging source-interface Loopback0\nlogging host 6.6.6.6\n'
                                'logging host 204.192.1.214\n!\nsnmp-server group default v3 auth \nsnmp-server group default v3 priv'
                                ' \nsnmp-server trap-source Loopback0\nsnmp-server enable traps snmp authentication linkdown linkup c'
                                'oldstart warmstart\nsnmp-server enable traps flowmon\nsnmp-server enable traps entity-perf throughpu'
                                't-notif\nsnmp-server enable traps call-home message-send-fail server-fail\nsnmp-server enable traps '
                                'tty\nsnmp-server enable traps eigrp\nsnmp-server enable traps ospf state-change\nsnmp-server enable '
                                'traps ospf errors\nsnmp-server enable traps ospf retransmit\nsnmp-server enable traps ospf lsa\nsnmp'
                                '-server enable traps ospf cisco-specific state-change nssa-trans-change\nsnmp-server enable traps os'
                                'pf cisco-specific state-change shamlink interface\nsnmp-server enable traps ospf cisco-specific stat'
                                'e-change shamlink neighbor\nsnmp-server enable traps ospf cisco-specific errors\nsnmp-server enable '
                                'traps ospf cisco-specific retransmit\nsnmp-server enable traps ospf cisco-specific lsa\nsnmp-server '
                                'enable traps bfd\nsnmp-server enable traps smart-license\nsnmp-server enable traps auth-framework se'
                                'c-violation\nsnmp-server enable traps rep\nsnmp-server enable traps aaa_server\nsnmp-server enable t'
                                'raps memory bufferpeak\nsnmp-server enable traps config-copy\nsnmp-server enable traps config\nsnmp-'
                                'server enable traps config-ctid\nsnmp-server enable traps energywise\nsnmp-server enable traps fru-c'
                                'trl\nsnmp-server enable traps entity\nsnmp-server enable traps flash insertion removal lowspace\nsnm'
                                'p-server enable traps power-ethernet group 1 threshold 80\nsnmp-server enable traps power-ethernet p'
                                'olice\nsnmp-server enable traps cpu threshold\nsnmp-server enable traps syslog\nsnmp-server enable t'
                                'raps udld link-fail-rpt\nsnmp-server enable traps udld status-change\nsnmp-server enable traps vtp\n'
                                'snmp-server enable traps vlancreate\nsnmp-server enable traps vlandelete\nsnmp-server enable traps p'
                                'ort-security\nsnmp-server enable traps envmon\nsnmp-server enable traps stackwise\nsnmp-server enabl'
                                'e traps mvpn\nsnmp-server enable traps pw vc\nsnmp-server enable traps ipsla\nsnmp-server enable tra'
                                'ps dhcp\nsnmp-server enable traps event-manager\nsnmp-server enable traps ike policy add\nsnmp-serve'
                                'r enable traps ike policy delete\nsnmp-server enable traps ike tunnel start\nsnmp-server enable trap'
                                's ike tunnel stop\nsnmp-server enable traps ipsec cryptomap add\nsnmp-server enable traps ipsec cryp'
                                'tomap delete\nsnmp-server enable traps ipsec cryptomap attach\nsnmp-server enable traps ipsec crypto'
                                'map detach\nsnmp-server enable traps ipsec tunnel start\nsnmp-server enable traps ipsec tunnel stop\n'
                                'snmp-server enable traps ipsec too-many-sas\nsnmp-server enable traps ospfv3 state-change\nsnmp-ser'
                                'ver enable traps ospfv3 errors\nsnmp-server enable traps ipmulticast\nsnmp-server enable traps msdp\n'
                                'snmp-server enable traps pim neighbor-change rp-mapping-change invalid-pim-message\nsnmp-server ena'
                                'ble traps bridge newroot topologychange\nsnmp-server enable traps stpx inconsistency root-inconsiste'
                                'ncy loop-inconsistency\nsnmp-server enable traps bgp cbgp2\nsnmp-server enable traps hsrp\nsnmp-serv'
                                'er enable traps isis\nsnmp-server enable traps cef resource-failure peer-state-change peer-fib-state'
                                '-change inconsistency\nsnmp-server enable traps lisp\nsnmp-server enable traps nhrp nhs\nsnmp-server'
                                ' enable traps nhrp nhc\nsnmp-server enable traps nhrp nhp\nsnmp-server enable traps nhrp quota-excee'
                                'ded\nsnmp-server enable traps local-auth\nsnmp-server enable traps entity-diag boot-up-fail hm-test-'
                                'recover hm-thresh-reached scheduled-test-fail\nsnmp-server enable traps mpls rfc ldp\nsnmp-server en'
                                'able traps mpls ldp\nsnmp-server enable traps mpls rfc traffic-eng\nsnmp-server enable traps mpls tr'
                                'affic-eng\nsnmp-server enable traps mpls fast-reroute protected\nsnmp-server enable traps bulkstat c'
                                'ollection transfer\nsnmp-server enable traps mac-notification change move threshold\nsnmp-server ena'
                                'ble traps errdisable\nsnmp-server enable traps vlan-membership\nsnmp-server enable traps transceiver'
                                ' all\nsnmp-server enable traps vrfmib vrf-up vrf-down vnet-trunk-up vnet-trunk-down\nsnmp-server ena'
                                'ble traps rf\nsnmp-server enable traps mpls vpn\nsnmp-server enable traps mpls rfc vpn\nsnmp-server '
                                'host 204.192.1.214 version 3 priv xxxxxxxx \nsnmp-server host 8.8.8.8 version 3 priv xxxxxxxx \n!\nr'
                                'adius-server attribute 6 on-for-login-auth\nradius-server attribute 6 support-multiple\nradius-serve'
                                'r attribute 8 include-in-access-req\nradius-server attribute 25 access-request include\nradius-serve'
                                'r attribute 31 mac format ietf upper-case\nradius-server attribute 31 send nas-port-detail mac-only\n'
                                'radius-server dead-criteria time 5 tries 3\nradius-server deadtime 3\n!\nradius server dnac-radius_'
                                '172.23.241.229\n address ipv4 172.23.241.229 auth-port 1812 acct-port 1813\n timeout 4\n retransmit '
                                '3\n automate-tester username dummy ignore-acct-port probe-on\n pac key 7 xxxxxxxx\n!\n!\n!\nipv6 acc'
                                'ess-list IPV6_CRITICAL_AUTH_ACL\n sequence 10 permit ipv6 any any\n!\nipv6 access-list IPV6_PRE_AUTH'
                                '_ACL\n sequence 10 permit udp any any eq bootpc\n sequence 20 permit udp any any eq bootps\n sequenc'
                                'e 30 permit udp any any eq domain\n sequence 40 deny ipv6 any any\n!\ncontrol-plane\n service-policy'
                                ' input system-cpp-policy\n!\n!\ncts role-based enforcement\ncts role-based enforcement vlan-list 102'
                                '1-1024,1027-1032,2046\nbanner motd ^C This Device is part of Solution Automation Testbed\n Please lo'
                                'g off if you are not intended user\n Contact phannguy for further details\n ^C\n!\nline con 0\n exec'
                                '-timeout 0 0\n stopbits 1\n speed 115200\nline vty 0 4\n session-timeout 1440 \n exec-timeout 0 0\np'
                                'assword 7 xxxxxxxx\n authorization exec VTY_author\n login xxxxxx\n transport input all\nline vty 5 '
                                '15\n session-timeout 1440 \n exec-timeout 60 0\npassword 7 xxxxxxxx\n authorization exec VTY_author\n'
                                ' login xxxxxx\n transport input all\nline vty 16 31\n session-timeout 1440 \n exec-timeout 60 0\npa'
                                'ssword 7 xxxxxxxx\n transport input all\n!\ncall-home\n ! If contact email address in call-home is c'
                                'onfigured as sch-smart-licensing@cisco.com\n ! the email address configured in Cisco Smart License P'
                                'ortal will be used as contact email address to send SCH notifications.\n contact-email-addr sch-smar'
                                't-licensing@cisco.com\n profile CiscoTAC-1\n active\n destination transport-method http\nntp source '
                                'Loopback0\nntp server 204.192.3.40\n!\n!\n!\n!\n!\npnp startup-vlan 1025\n!\ntelemetry ietf subscrip'
                                'tion 500\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_oper/poe_port_detail\n rec'
                                'eiver-type protocol\n source-address 204.1.2.1\n stream native\n update-policy periodic 360000\n rec'
                                'eiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 501\n encoding encode-tdl\n filter t'
                                'dl-uri /services;serviceName=ios_oper/poe_module\n receiver-type protocol\n source-address 204.1.2.1'
                                '\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry '
                                'ietf subscription 502\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_oper/poe_stac'
                                'k\n receiver-type protocol\n source-address 204.1.2.1\n stream native\n update-policy periodic 36000'
                                '0\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 503\n encoding encode-tdl\n f'
                                'ilter tdl-uri /services;serviceName=ios_oper/poe_switch\n receiver-type protocol\n source-address 20'
                                '4.1.2.1\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntel'
                                'emetry ietf subscription 504\n encoding encode-tdl\n filter nested-uri /services;serviceName=ios_ope'
                                'r/platform_component;cname=0?platform_properties\n receiver-type protocol\n source-address 204.1.2.1'
                                '\n stream native\n update-policy periodic 30000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry i'
                                'etf subscription 550\n encoding encode-tdl\n filter tdl-uri /services;serviceName=smevent/sessioneve'
                                'nt\n receiver-type protocol\n source-address 204.1.2.1\n stream native\n update-policy on-change\n r'
                                'eceiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 551\n encoding encode-tdl\n filter'
                                ' tdl-uri /services;serviceName=sessmgr_oper/session_context_data\n receiver-type protocol\n source-a'
                                'ddress 204.1.2.1\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECE'
                                'IVER\ntelemetry ietf subscription 552\n encoding encode-tdl\n filter tdl-uri /services;serviceName=i'
                                'osevent/sisf_mac_oper_state\n receiver-type protocol\n source-address 204.1.2.1\n stream native\n up'
                                'date-policy on-change\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 553\n enc'
                                'oding encode-tdl\n filter tdl-uri /services;serviceName=ios_oper/sisf_db_wired_mac\n receiver-type p'
                                'rotocol\n source-address 204.1.2.1\n stream native\n update-policy periodic 360000\n receiver name D'
                                'NAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 554\n encoding encode-tdl\n filter tdl-uri /serv'
                                'ices;serviceName=ios_oper/cdp_neighbor_detail\n receiver-type protocol\n source-address 204.1.2.1\n '
                                'stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry iet'
                                'f subscription 555\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_oper/cdp_neighbo'
                                'r_detail\n receiver-type protocol\n source-address 204.1.2.1\n stream native\n update-policy on-chan'
                                'ge\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 600\n encoding encode-tdl\n '
                                'filter tdl-uri /services;serviceName=sessmgr_oper/tbl_aaa_servers_stat\n receiver-type protocol\n so'
                                'urce-address 204.1.2.1\n stream native\n update-policy periodic 60000\n receiver name DNAC_ASSURANCE'
                                '_RECEIVER\ntelemetry ietf subscription 601\n encoding encode-tdl\n filter tdl-uri /services;serviceN'
                                'ame=sessmgr_oper/tbl_aaa_servers_stat\n receiver-type protocol\n source-address 204.1.2.1\n stream n'
                                'ative\n update-policy on-change\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription'
                                ' 602\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_emul_oper/lisp_routers;top_id='
                                '0/sessions\n receiver-type protocol\n source-address 204.1.2.1\n stream native\n update-policy perio'
                                'dic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 603\n encoding encod'
                                'e-tdl\n filter tdl-uri /services;serviceName=iosevent/lisp_tcp_session_state\n receiver-type protoco'
                                'l\n source-address 204.1.2.1\n stream native\n update-policy on-change\n receiver name DNAC_ASSURANC'
                                'E_RECEIVER\ntelemetry ietf subscription 604\n encoding encode-tdl\n filter nested-uri /services;serv'
                                'iceName=ios_emul_oper/lisp_routers;top_id=0/instances;iid=0/af;iaftype=LISP_TDL_IAF_IPV4/lisp_publis'
                                'her\n receiver-type protocol\n source-address 204.1.2.1\n stream native\n update-policy periodic 360'
                                '000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 605\n encoding encode-tdl\n'
                                ' filter tdl-uri /services;serviceName=iosevent/lisp_pubsub_session_state\n receiver-type protocol\n '
                                'source-address 204.1.2.1\n stream native\n update-policy on-change\n receiver name DNAC_ASSURANCE_RE'
                                'CEIVER\ntelemetry ietf subscription 606\n encoding encode-tdl\n filter nested-uri /services;serviceN'
                                'ame=ios_emul_oper/lisp_routers;top_id=0/remote_locator_sets;name=default-etr-locator-set-ipv4/rem_lo'
                                'c_set_rlocs_si\n receiver-type protocol\n source-address 204.1.2.1\n stream native\n update-policy p'
                                'eriodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 607\n encoding e'
                                'ncode-tdl\n filter tdl-uri /services;serviceName=iosevent/lisp_etr_si_type\n receiver-type protocol\n'
                                ' source-address 204.1.2.1\n stream native\n update-policy on-change\n receiver name DNAC_ASSURANCE_'
                                'RECEIVER\ntelemetry ietf subscription 608\n encoding encode-tdl\n filter tdl-uri /services;serviceNa'
                                'me=ios_emul_oper/cts_env_data\n receiver-type protocol\n source-address 204.1.2.1\n stream native\n '
                                'update-policy periodic 60000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 60'
                                '9\n encoding encode-tdl\n filter tdl-uri /services;serviceName=ios_emul_oper/bgp_state;singleton_id='
                                '0/neighbor\n receiver-type protocol\n source-address 204.1.2.1\n stream native\n update-policy perio'
                                'dic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 610\n encoding encod'
                                'e-tdl\n filter tdl-uri /services;serviceName=ios_emul_oper/bgp_state;singleton_id=0/neighbor\n recei'
                                'ver-type protocol\n source-address 204.1.2.1\n stream native\n update-policy on-change\n receiver na'
                                'me DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 611\n encoding encode-tdl\n filter tdl-uri /'
                                'services;serviceName=iosevent/lisp_extranet_policy_state\n receiver-type protocol\n source-address 2'
                                '04.1.2.1\n stream native\n update-policy on-change\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetr'
                                'y ietf subscription 612\n encoding encode-tdl\n filter nested-uri /services;serviceName=ios_emul_ope'
                                'r/lisp_routers;top_id=0/instances;iid=1/extranets\n receiver-type protocol\n source-address 204.1.2.'
                                '1\n stream native\n update-policy periodic 360000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry'
                                ' ietf subscription 613\n encoding encode-tdl\n filter nested-uri /services;serviceName=ios_emul_oper'
                                '/lisp_routers;top_id=0/instances;iid=1/extranets;extranet_name=ext1/extranet_member_instances\n rece'
                                'iver-type protocol\n source-address 204.1.2.1\n stream native\n update-policy periodic 360000\n rece'
                                'iver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 614\n encoding encode-tdl\n filter ne'
                                'sted-uri /services;serviceName=ios_oper/nve_oper;unit_number=0/nve_vni_oper\n receiver-type protocol'
                                '\n source-address 204.1.2.1\n stream native\n update-policy periodic 960000\n receiver name DNAC_ASS'
                                'URANCE_RECEIVER\ntelemetry ietf subscription 615\n encoding encode-tdl\n filter nested-uri /services'
                                ';serviceName=ios_oper/nve_oper;unit_number=0/nve_peer_oper\n receiver-type protocol\n source-address'
                                ' 204.1.2.1\n stream native\n update-policy periodic 960000\n receiver name DNAC_ASSURANCE_RECEIVER\n'
                                'telemetry ietf subscription 616\n encoding encode-tdl\n filter nested-uri /services;serviceName=ios_'
                                'oper/nve_oper\n receiver-type protocol\n source-address 204.1.2.1\n stream native\n update-policy on'
                                '-change\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 750\n encoding encode-t'
                                'dl\n filter tdl-uri /services;serviceName=ios_emul_oper/environment_sensor\n receiver-type protocol\n'
                                ' source-address 204.1.2.1\n stream native\n update-policy periodic 30000\n receiver name DNAC_ASSUR'
                                'ANCE_RECEIVER\ntelemetry ietf subscription 751\n encoding encode-tdl\n filter tdl-uri /services;serv'
                                'iceName=ios_oper/platform_component\n receiver-type protocol\n source-address 204.1.2.1\n stream nat'
                                'ive\n update-policy periodic 30000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscript'
                                'ion 1020\n encoding encode-tdl\n filter tdl-uri /services;serviceName=iosevent/install_status\n rece'
                                'iver-type protocol\n source-address 204.1.2.1\n stream native\n update-policy on-change\n receiver n'
                                'ame DNAC_ASSURANCE_RECEIVER\ntelemetry ietf subscription 8882\n encoding encode-tdl\n filter tdl-tra'
                                'nsform trustSecCounterDelta\n receiver-type protocol\n source-address 204.1.2.1\n stream native\n up'
                                'date-policy periodic 90000\n receiver name DNAC_ASSURANCE_RECEIVER\ntelemetry receiver protocol DNAC'
                                '_ASSURANCE_RECEIVER\n host ip-address 204.192.1.214 25103\n protocol tls-native profile sdn-network-'
                                'infra-iwan\ntelemetry transform trustSecCounterDelta\n input table cts_rolebased_policy\n field dst_'
                                'sgt\n field src_sgt\n field sgacl_name\n field monitor_mode\n field num_of_sgacl\n field policy_life'
                                '_time\n field total_deny_count\n field last_updated_time\n field total_permit_count\n join-key cts_r'
                                'ole_based_policy_key\n logical-op and\n type mandatory\n uri /services;serviceName=ios_emul_oper/cts'
                                '_rolebased_policy\n operation 1\n output-field 1\n field cts_rolebased_policy.src_sgt\n output-field'
                                ' 2\n field cts_rolebased_policy.dst_sgt\n output-field 3\n field cts_rolebased_policy.total_permit_c'
                                'ount\n output-op type delta\n output-field 4\n field cts_rolebased_policy.total_deny_count\n output-'
                                'op type delta\n output-field 5\n field cts_rolebased_policy.sgacl_name\n output-field 6\n field cts_'
                                'rolebased_policy.monitor_mode\n output-field 7\n field cts_rolebased_policy.num_of_sgacl\n output-fi'
                                'eld 8\n field cts_rolebased_policy.policy_life_time\n output-field 9\n field cts_rolebased_policy.la'
                                'st_updated_time\n specified\nnetconf-yang\nend\n\n'
                            }
                        ]
                    }
                ]
            ],
        )

    def test_network_devices_info_workflow_manager_playbook_connected_device_info(self):
        """
        Tests retrieval of connected device details from the network devices info workflow.

        Verifies the workflow returns expected device info, including IP, capabilities,
        and neighbor details, without errors.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_connected_device_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices filtered from the provided filters are: ['204.192.4.200']",
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
                                        "neighborDevice": "NY-BN-9500.cisco.local",
                                        "neighborPort": "TenGigabitEthernet1/0/9"
                                    }
                                ],
                                "device_ip": "204.192.4.200"
                            },
                            {
                                "connected_device_details": [
                                    {
                                        "capabilities": [
                                            "IGMP_CONDITIONAL_FILTERING",
                                            "ROUTER",
                                            "SWITCH"
                                        ],
                                        "neighborDevice": "SJ-BN-9300.cisco.local",
                                        "neighborPort": "TenGigabitEthernet1/1/7"
                                    }
                                ],
                                "device_ip": "204.192.4.200"
                            },
                            {
                                "connected_device_details": [
                                    {
                                        "capabilities": [
                                            "IGMP_CONDITIONAL_FILTERING",
                                            "SWITCH"
                                        ],
                                        "neighborDevice": "DC-SW-11",
                                        "neighborPort": "TenGigabitEthernet1/0/13"
                                    }
                                ],
                                "device_ip": "204.192.4.200"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.192.4.200"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.192.4.200"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.192.4.200"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.192.4.200"
                            },
                            {
                                "connected_device_details": [
                                    {
                                        "capabilities": [
                                            "IGMP_CONDITIONAL_FILTERING",
                                            "SWITCH"
                                        ],
                                        "neighborDevice": "AMS2-MGMT-1",
                                        "neighborPort": "GigabitEthernet1/0/17"
                                    }
                                ],
                                "device_ip": "204.192.4.200"
                            },
                            {
                                "connected_device_details": [
                                    {
                                        "capabilities": [
                                            "IGMP_CONDITIONAL_FILTERING",
                                            "ROUTER",
                                            "SWITCH"
                                        ],
                                        "neighborDevice": "DC-FR-9300.cisco.local",
                                        "neighborPort": "TenGigabitEthernet1/1/7"
                                    }
                                ],
                                "device_ip": "204.192.4.200"
                            }
                        ]
                    }
                ]
            ],
        )

    def test_network_devices_info_workflow_manager_playbook_interface_vlan_info(self):
        """
        Test the Network Devices Info Workflow Manager's interface VLAN details retrieval process.

        This test verifies that the workflow correctly handles the retrieval of network device interface VLAN information,
        ensuring proper validation and expected behavior.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_interface_vlan_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices filtered from the provided filters are: ['204.1.2.1']",
                [
                    {
                        "interface_vlan_info": [
                            {
                                "device_ip": "204.1.2.1",
                                "interface_vlan_details": [
                                    {
                                        "interfaceName": "LISP0.4097",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4102",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4110",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4106",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4098",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4111",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4108",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4105",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4103",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4113",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4114",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4100",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4101",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4104",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4112",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4109",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4099",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "LISP0.4107",
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "Vlan1031",
                                        "ipAddress": "204.1.128.1",
                                        "networkAddress": "204.1.128.0",
                                        "numberOfIPs": 1024,
                                        "prefix": "22",
                                        "vlanNumber": 1031,
                                        "vlanType": "Configured from Catalyst Center"
                                    },
                                    {
                                        "interfaceName": "Vlan1021",
                                        "ipAddress": "204.1.80.1",
                                        "networkAddress": "204.1.80.0",
                                        "numberOfIPs": 256,
                                        "prefix": "24",
                                        "vlanNumber": 1021,
                                        "vlanType": "Configured from Catalyst Center"
                                    },
                                    {
                                        "interfaceName": "Vlan1022",
                                        "ipAddress": "2004:1:64::1:1",
                                        "prefix": "112",
                                        "vlanNumber": 1022,
                                        "vlanType": "Configured from Catalyst Center"
                                    },
                                    {
                                        "interfaceName": "Vlan1028",
                                        "ipAddress": "204.1.112.1",
                                        "networkAddress": "204.1.112.0",
                                        "numberOfIPs": 1024,
                                        "prefix": "22",
                                        "vlanNumber": 1028,
                                        "vlanType": "Configured from Catalyst Center"
                                    },
                                    {
                                        "interfaceName": "Vlan1024",
                                        "ipAddress": "2004:1:224::1:1",
                                        "prefix": "112",
                                        "vlanNumber": 1024,
                                        "vlanType": "Configured from Catalyst Center"
                                    },
                                    {
                                        "interfaceName": "Vlan2160",
                                        "ipAddress": "204.1.216.1",
                                        "networkAddress": "204.1.216.0",
                                        "numberOfIPs": 64,
                                        "prefix": "26",
                                        "vlanNumber": 2160,
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "Vlan1025",
                                        "ipAddress": "204.1.32.1",
                                        "networkAddress": "204.1.32.0",
                                        "numberOfIPs": 256,
                                        "prefix": "24",
                                        "vlanNumber": 1025,
                                        "vlanType": "Configured from Catalyst Center"
                                    },
                                    {
                                        "interfaceName": "Vlan2046",
                                        "ipAddress": "40.50.10.1",
                                        "networkAddress": "40.50.10.0",
                                        "numberOfIPs": 256,
                                        "prefix": "24",
                                        "vlanNumber": 2046,
                                        "vlanType": "Configured from Catalyst Center"
                                    },
                                    {
                                        "interfaceName": "Vlan1027",
                                        "ipAddress": "204.1.48.1",
                                        "networkAddress": "204.1.48.0",
                                        "numberOfIPs": 256,
                                        "prefix": "24",
                                        "vlanNumber": 1027,
                                        "vlanType": "Configured from Catalyst Center"
                                    },
                                    {
                                        "interfaceName": "Vlan1023",
                                        "ipAddress": "204.1.240.1",
                                        "networkAddress": "204.1.240.0",
                                        "numberOfIPs": 1024,
                                        "prefix": "22",
                                        "vlanNumber": 1023,
                                        "vlanType": "Configured from Catalyst Center"
                                    },
                                    {
                                        "interfaceName": "Vlan1032",
                                        "ipAddress": "123.123.0.1",
                                        "networkAddress": "123.123.0.0",
                                        "numberOfIPs": 4096,
                                        "prefix": "20",
                                        "vlanNumber": 1032,
                                        "vlanType": "Configured from Catalyst Center"
                                    },
                                    {
                                        "interfaceName": "Vlan1",
                                        "vlanNumber": 1,
                                        "vlanType": ""
                                    },
                                    {
                                        "interfaceName": "Vlan1029",
                                        "ipAddress": "2040:50::1:0:1",
                                        "prefix": "96",
                                        "vlanNumber": 1029,
                                        "vlanType": "Configured from Catalyst Center"
                                    },
                                    {
                                        "interfaceName": "Vlan1030",
                                        "ipAddress": "204.1.96.1",
                                        "networkAddress": "204.1.96.0",
                                        "numberOfIPs": 1024,
                                        "prefix": "22",
                                        "vlanNumber": 1030,
                                        "vlanType": "Configured from Catalyst Center"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            ],
        )

    def test_network_devices_info_workflow_manager_playbook_negative_scenario1(self):
        """
        Test validation failure when network_devices key is missing from config.
        Verifies proper error handling for incomplete configuration structure.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario1
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "'network_devices' key is missing in the config block"
        )

    def test_network_devices_info_workflow_manager_playbook_negative_scenario2(self):
        """
        Test validation failure when invalid key 'software_versions' is used.
        Verifies error handling for unrecognized configuration keys in network device entries.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario2
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            (
                "'software_versions' is not a valid key in network device entry. "
                "Allowed keys are: device_family, device_identifier, device_role, "
                "device_type, interval, os_type, output_file_info, requested_info, "
                "retries, site_hierarchy, software_version, timeout"
            )
        )

    def test_network_devices_info_workflow_manager_playbook_negative_scenario3(self):
        """
        Test validation failure when invalid key 'ip_addresses' is used in device_identifier.
        Verifies error handling for unrecognized keys in device identification configuration.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario3
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            (
                "Invalid or unrecognized key 'ip_addresses' found in device_identifier. "
                "Allowed keys are: hostname, ip_address, ip_address_range, "
                "mac_address, serial_number"
            )
        )

    def test_network_devices_info_workflow_manager_playbook_negative_scenario4(self):
        """
        Test validation failure when retries value is negative.
        Verifies error handling for invalid retry count configuration parameters.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario4
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "'retries' must be a non-negative integer"
        )

    def test_network_devices_info_workflow_manager_playbook_negative_scenario5(self):
        """
        Test validation failure when invalid requested_info value is provided.
        Verifies error handling for unrecognized return value types in configuration.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario5
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            (
                "'interface_vlan_infoo' is not a valid return value. Allowed values are: "
                "['all', 'connected_device_info', 'device_config_info', 'device_info', "
                "'device_interfaces_by_range_info', 'device_link_mismatch_info', "
                "'device_polling_interval_info', 'device_stack_info', 'device_summary_info', "
                "'interface_info', 'interface_vlan_info', 'line_card_info', 'module_count_info', "
                "'poe_info', 'supervisor_card_info']"
            )
        )

    def test_network_devices_info_workflow_manager_playbook_negative_scenario6(self):
        """
        Test validation failure when invalid key 'file_paths' is used in output_file_info.
        Verifies error handling for unrecognized configuration keys in file output settings.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario6
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "'file_paths' is not a valid key in 'output_file_info'. Allowed keys are: ['file_format', 'file_mode', 'file_path', 'timestamp']"
        )

    def test_network_devices_info_workflow_manager_playbook_negative_scenario7(self):
        """
        Test validation failure when invalid file_format value is provided.
        Verifies error handling for unsupported file format types in output configuration.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario7
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "'file_format' must be one of: json, yaml"
        )

    def test_network_devices_info_workflow_manager_playbook_negative_scenario8(self):
        """
        Test validation failure when invalid file_mode value is provided.
        Verifies error handling for unsupported file mode types in output configuration.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario8
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "'file_mode' must be one of: a, w"
        )

    def test_network_devices_info_workflow_manager_playbook_negative_scenario9(self):
        """
        Test validation when network device entry lacks required keys.
        Validates error handling for missing mandatory device identification fields.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario9
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            (
                "Each network device must contain at least one of the following keys: "
                "site_hierarchy, device_type, device_role, device_family, "
                "software_version, os_type, device_identifier."
            )
        )

    def test_network_devices_info_workflow_manager_playbook_no_network_device(self):
        """
        Test handling when no network devices are found for the given filters.
        Validates error messages for unreachable, unmanaged, or missing devices.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_no_network_device
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "No devices found for the following identifiers ip_address: 204.1.2.10. Device(s) may not be present in Catalyst Center inventory.",
                "No network devices found for the given filters."
            ]
        )

    def test_network_devices_info_workflow_manager_playbook_no_device(self):
        """
        Test retrieving device link mismatch information when no devices have mismatches.
        Validates handling of empty link mismatch details for speed-duplex and VLAN.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_no_device
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The network devices filtered from the provided filters are: ['204.1.216.9']",
                [
                    {
                        "device_link_mismatch_info": [
                            {
                                "device_ip": "204.1.216.9",
                                "speed-duplex": [
                                    {
                                        "device_ip": "204.1.216.9",
                                        "link_mismatch_details": []
                                    }
                                ],
                                "vlan": [
                                    {
                                        "device_ip": "204.1.216.9",
                                        "link_mismatch_details": []
                                    }
                                ]
                            }
                        ]
                    }
                ]
            ],
        )

    def test_network_devices_info_workflow_manager_playbook_negative_scenario11(self):
        """
        Test version compatibility for network device info workflow feature.
        Validates error handling when using unsupported DNA Center version.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.6",
                config=self.playbook_negative_scenario11
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "The specified version '2.3.7.6' does not support the 'network device info workflow' feature. Supported version(s) start from '2.3.7.9' onwards."
        )
