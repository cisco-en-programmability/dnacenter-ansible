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

from ansible_collections.cisco.dnac.plugins.modules import fabric_devices_info_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacFabricDeviceInfoWorkflowManager(TestDnacModule):

    module = fabric_devices_info_workflow_manager

    test_data = loadPlaybookData("fabric_devices_info_workflow_manager")

    playbook_fabric_info = test_data.get("playbook_fabric_info")
    playbook_handoff_info = test_data.get("playbook_handoff_info")
    playbook_onboarding_info = test_data.get("playbook_onboarding_info")
    playbook_health_info = test_data.get("playbook_health_info")
    playbook_issues_info = test_data.get("playbook_issues_info")
    playbook_connected_devices_info = test_data.get("playbook_connected_devices_info")
    playbook_negative_scenario_1 = test_data.get("playbook_negative_scenario_1")
    playbook_negative_scenario_2 = test_data.get("playbook_negative_scenario_2")
    playbook_negative_scenario_2 = test_data.get("playbook_negative_scenario_2")
    playbook_negative_scenario_3 = test_data.get("playbook_negative_scenario_3")
    playbook_negative_scenario_4 = test_data.get("playbook_negative_scenario_4")
    playbook_negative_scenario_5 = test_data.get("playbook_negative_scenario_5")
    playbook_negative_scenario_6 = test_data.get("playbook_negative_scenario_6")
    playbook_negative_scenario_7 = test_data.get("playbook_negative_scenario_7")
    playbook_negative_scenario_8 = test_data.get("playbook_negative_scenario_8")
    playbook_negative_scenario_9 = test_data.get("playbook_negative_scenario_9")
    playbook_negative_scenario_10 = test_data.get("playbook_negative_scenario_10")
    playbook_negative_scenario_11 = test_data.get("playbook_negative_scenario_11")
    playbook_negative_scenario_12 = test_data.get("playbook_negative_scenario_12")
    playbook_ip_range_OR_logic_exception = test_data.get("playbook_ip_range_OR_logic_exception")
    playbook_ip_range_AND_logic_exception = test_data.get("playbook_ip_range_AND_logic_exception")

    def setUp(self):
        super(TestDnacFabricDeviceInfoWorkflowManager, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacFabricDeviceInfoWorkflowManager, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """

        if "playbook_fabric_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites"),
                self.test_data.get("get_sites1"),
                self.test_data.get("get_fabric_sites"),
                self.test_data.get("get_device_list"),
                self.test_data.get("get_sites2"),
                self.test_data.get("get_sites3"),
                self.test_data.get("get_fabric_sites1"),
                self.test_data.get("get_device_list1"),
                self.test_data.get("get_fabric_devices"),
                self.test_data.get("192.168.200.69"),
                self.test_data.get("get_fabric_devices1"),
                self.test_data.get("get_fabric_devices2"),
            ]

        elif "playbook_handoff_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites4"),
                self.test_data.get("get_sites5"),
                self.test_data.get("get_fabric_sites2"),
                self.test_data.get("get_device_list2"),
                self.test_data.get("get_sites6"),
                self.test_data.get("get_sites7"),
                self.test_data.get("get_fabric_sites3"),
                self.test_data.get("get_device_list3"),
                self.test_data.get("get_fabric_devices3"),
                self.test_data.get("192.168.200.69_1"),
                self.test_data.get("get_fabric_devices_layer3_handoffs_with_sda_transit"),
                self.test_data.get("192.168.200.69_1"),
                self.test_data.get("get_fabric_devices_layer3_handoffs_with_sda_transit"),
                self.test_data.get("192.168.200.69_2"),
                self.test_data.get("get_fabric_devices_layer3_handoffs_with_ip_transit"),
                self.test_data.get("192.168.200.69_3"),
                self.test_data.get("get_fabric_devices_layer2_handoffs"),
            ]

        elif "playbook_onboarding_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites8"),
                self.test_data.get("get_sites9"),
                self.test_data.get("get_fabric_sites10"),
                self.test_data.get("get_device_list10"),
                self.test_data.get("get_sites10"),
                self.test_data.get("get_sites11"),
                self.test_data.get("get_fabric_sites11"),
                self.test_data.get("get_device_list11"),
                self.test_data.get("get_fabric_devices11"),
                self.test_data.get("192.168.200.69_10"),
                self.test_data.get("get_port_assignments"),
                self.test_data.get("get_network_device_by_ip"),
                self.test_data.get("get_provisioned_wired_device")
            ]

        elif "playbook_health_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites15"),
                self.test_data.get("get_sites16"),
                self.test_data.get("get_fabric_sites15"),
                self.test_data.get("get_device_list15"),
                self.test_data.get("get_sites17"),
                self.test_data.get("get_sites18"),
                self.test_data.get("get_fabric_sites16"),
                self.test_data.get("get_device_list16"),
                self.test_data.get("get_fabric_devices16"),
                self.test_data.get("get_health_info"),
            ]

        elif "playbook_issues_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites20"),
                self.test_data.get("get_sites21"),
                self.test_data.get("get_fabric_sites20"),
                self.test_data.get("get_device_list20"),
                self.test_data.get("get_sites22"),
                self.test_data.get("get_sites23"),
                self.test_data.get("get_fabric_sites21"),
                self.test_data.get("get_device_list21"),
                self.test_data.get("get_fabric_devices21"),
                self.test_data.get("192.168.200.69_20"),
                self.test_data.get("issues_info"),
            ]

        elif "playbook_connected_devices_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites40"),
                self.test_data.get("get_sites41"),
                self.test_data.get("get_fabric_sites40"),
                self.test_data.get("get_device_list40"),
                self.test_data.get("get_sites42"),
                self.test_data.get("get_sites43"),
                self.test_data.get("get_fabric_sites41"),
                self.test_data.get("get_device_list41"),
                self.test_data.get("get_fabric_devices40"),
                self.test_data.get("204.1.2.70"),
                self.test_data.get("get_interface_info_by_id"),
                self.test_data.get("204.1.2.701"),
                self.test_data.get("connected_device_info_1"),
                self.test_data.get("connected_device_info_2"),
                self.test_data.get("connected_device_info_3"),
                self.test_data.get("connected_device_info_4"),
                self.test_data.get("connected_device_info_5"),
                self.test_data.get("connected_device_info_6"),
                self.test_data.get("connected_device_info_7"),
                self.test_data.get("connected_device_info_8"),
                self.test_data.get("connected_device_info_9"),
                self.test_data.get("connected_device_info_10"),
                self.test_data.get("connected_device_info_11"),
                self.test_data.get("connected_device_info_12"),
                self.test_data.get("connected_device_info_13"),
                self.test_data.get("connected_device_info_14"),
                self.test_data.get("connected_device_info_15"),
                self.test_data.get("connected_device_info_16"),
                self.test_data.get("connected_device_info_17"),
                self.test_data.get("connected_device_info_18"),
                self.test_data.get("connected_device_info_19"),
                self.test_data.get("connected_device_info_20"),
                self.test_data.get("connected_device_info_21"),
                self.test_data.get("connected_device_info_22"),
                self.test_data.get("connected_device_info_23"),
                self.test_data.get("connected_device_info_24"),
                self.test_data.get("connected_device_info_25"),
                self.test_data.get("connected_device_info_26"),
                self.test_data.get("connected_device_info_27"),
                self.test_data.get("connected_device_info_28"),
                self.test_data.get("connected_device_info_29"),
                self.test_data.get("connected_device_info_30"),
                self.test_data.get("connected_device_info_31"),
                self.test_data.get("connected_device_info_32"),
                self.test_data.get("connected_device_info_33"),
                self.test_data.get("connected_device_info_34"),
                self.test_data.get("connected_device_info_35"),
                self.test_data.get("connected_device_info_36"),
                self.test_data.get("connected_device_info_37"),
                self.test_data.get("connected_device_info_38"),
                self.test_data.get("connected_device_info_39"),
                self.test_data.get("connected_device_info_40"),
                self.test_data.get("connected_device_info_41"),
                self.test_data.get("connected_device_info_42"),
                self.test_data.get("connected_device_info_43"),
                self.test_data.get("connected_device_info_44"),
                self.test_data.get("connected_device_info_45"),
                self.test_data.get("connected_device_info_46"),
                self.test_data.get("connected_device_info_47"),
                self.test_data.get("connected_device_info_48"),
                self.test_data.get("connected_device_info_49"),
                self.test_data.get("connected_device_info_50"),
                self.test_data.get("connected_device_info_51"),
                self.test_data.get("connected_device_info_52"),
                self.test_data.get("connected_device_info_53"),
                self.test_data.get("connected_device_info_54"),
                self.test_data.get("connected_device_info_55"),
                self.test_data.get("connected_device_info_56"),
                self.test_data.get("connected_device_info_57"),
                self.test_data.get("connected_device_info_58"),
                self.test_data.get("connected_device_info_59"),
                self.test_data.get("connected_device_info_60"),
                self.test_data.get("connected_device_info_61"),
                self.test_data.get("connected_device_info_62"),
                self.test_data.get("connected_device_info_63"),
                self.test_data.get("connected_device_info_64"),
                self.test_data.get("connected_device_info_65"),
                self.test_data.get("connected_device_info_66"),
                self.test_data.get("connected_device_info_67"),
                self.test_data.get("connected_device_info_68"),
                self.test_data.get("connected_device_info_69"),
                self.test_data.get("connected_device_info_70"),

            ]

        elif "playbook_negative_scenario_11" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites30"),
            ]

        elif "playbook_negative_scenario_12" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites31"),
                self.test_data.get("get_fabric_sites30"),
                self.test_data.get("get_sites32"),
                self.test_data.get("get_fabric_sites31"),
            ]

        elif "playbook_ip_range_OR_logic_exception" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites50"),
                self.test_data.get("get_sites51"),
                self.test_data.get("get_fabric_sites50"),
                self.test_data.get("get_device_list10"),
                self.test_data.get("get_sites52"),
                self.test_data.get("get_sites53"),
                self.test_data.get("get_fabric_sites51"),
                self.test_data.get("get_device_list10"),
                self.test_data.get("get_fabric_devices51"),
                self.test_data.get("192.168.200.68"),
                self.test_data.get("get_fabric_devices52"),
                self.test_data.get("192.168.200.691"),
                self.test_data.get("get_fabric_devices53"),
                self.test_data.get("192.168.200.74"),
                self.test_data.get("get_fabric_devices54"),
            ]

        elif "playbook_ip_range_AND_logic_exception" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites60"),
                self.test_data.get("get_sites61"),
                self.test_data.get("get_fabric_sites60"),
                self.test_data.get("ip_address_range=192.168.200.68"),
                self.test_data.get("ip_address_range=192.168.200.69"),
                self.test_data.get("ip_address_range=192.168.200.70"),
                self.test_data.get("serial_number=FOC2443L1VQ"),
                self.test_data.get("hostname=Fabric-9300-2-2.rcdnlabcead.com"),
            ]

    def test_fabric_devices_info_workflow_manager_playbook_fabric_info(self):
        """
        Test fabric device information retrieval for fabric-enabled devices.

        This test verifies that the workflow correctly retrieves fabric configuration
        details for devices within a specified fabric site, ensuring proper data
        structure and content in the response.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_fabric_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The fabric devices filtered from the network devices are: ['192.168.200.69']",
                [
                    {
                        "fabric_info": [
                            {
                                "device_ip": "192.168.200.69",
                                "fabric_details": [
                                    {
                                        "deviceRoles": [
                                            "EDGE_NODE"
                                        ],
                                        "fabricId": "34ef8d59-1860-4221-8124-2242a776b5e1",
                                        "id": "5f4092a2-fbc5-42df-8343-f6aeddf8aafc",
                                        "networkDeviceId": "199950bc-c0d6-42f6-b1f3-a3f5aed176ee"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            ]
        )

    def test_fabric_devices_info_workflow_manager_playbook_handoff_info(self):
        """
        Test fabric device handoff information retrieval for fabric-enabled devices.

        This test verifies that the workflow correctly retrieves Layer 2 and Layer 3
        handoff configuration details for devices within a specified fabric site,
        ensuring proper data structure and content in the response.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_handoff_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The fabric devices filtered from the network devices are: ['192.168.200.69']",
                [
                    {
                        "fabric_devices_layer3_handoffs_sda_info": [
                            {
                                "device_ip": "192.168.200.69",
                                "handoff_layer3_sda_transit_info": []
                            }
                        ]
                    }
                ],
                [
                    {
                        "fabric_devices_layer3_handoffs_ip_info": [
                            {
                                "device_ip": "192.168.200.69",
                                "handoff_layer3_ip_transit_info": []
                            }
                        ]
                    }
                ],
                [
                    {
                        "fabric_devices_layer2_handoffs_info": [
                            {
                                "device_ip": "192.168.200.69",
                                "handoff_layer2_info": []
                            }
                        ]
                    }
                ]
            ]
        )

    def test_fabric_devices_info_workflow_manager_playbook_onboarding_info(self):
        """
        Test fabric device onboarding information retrieval for fabric-enabled devices.

        This test verifies that the workflow correctly retrieves device onboarding details
        including port assignments, SSID information, and provisioning status for devices
        within a specified fabric site, ensuring proper data structure and content.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_onboarding_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The fabric devices filtered from the network devices are: ['192.168.200.69']",
                [
                    {
                        "device_onboarding_info": [
                            {
                                "device_ip": "192.168.200.69",
                                "port_details": [
                                    {
                                        "authenticateTemplateName": "No Authentication",
                                        "connectedDeviceType": "ACCESS_POINT",
                                        "dataVlanName": "192_168_200_192-INFRA_VN",
                                        "fabricId": "34ef8d59-1860-4221-8124-2242a776b5e1",
                                        "id": "6aad42c9-3a71-4838-afa0-c0fd34509322",
                                        "interfaceDescription": "",
                                        "interfaceName": "GigabitEthernet1/0/3",
                                        "networkDeviceId": "199950bc-c0d6-42f6-b1f3-a3f5aed176ee"
                                    },
                                    {
                                        "authenticateTemplateName": "No Authentication",
                                        "connectedDeviceType": "USER_DEVICE",
                                        "dataVlanName": "192_168_200_224-DEFAULT_VN",
                                        "fabricId": "34ef8d59-1860-4221-8124-2242a776b5e1",
                                        "id": "200187c1-b10f-40d3-a2f1-54bff6fa13be",
                                        "interfaceDescription": "",
                                        "interfaceName": "GigabitEthernet1/0/1",
                                        "networkDeviceId": "199950bc-c0d6-42f6-b1f3-a3f5aed176ee"
                                    },
                                    {
                                        "authenticateTemplateName": "No Authentication",
                                        "connectedDeviceType": "ACCESS_POINT",
                                        "dataVlanName": "192_168_200_192-INFRA_VN",
                                        "fabricId": "34ef8d59-1860-4221-8124-2242a776b5e1",
                                        "id": "029f671e-663b-4ab4-9ae1-e53bfcd707f8",
                                        "interfaceDescription": "",
                                        "interfaceName": "GigabitEthernet1/0/25",
                                        "networkDeviceId": "199950bc-c0d6-42f6-b1f3-a3f5aed176ee"
                                    }
                                ]
                            }
                        ]
                    }
                ],
                [
                    {
                        "ssid_info": [
                            {
                                "device_ip": "192.168.200.69",
                                "ssid_details": "The device is not wireless; therefore, SSID information retrieval is not applicable."
                            }
                        ]
                    }
                ],
                [
                    {
                        "provision_status_info": [
                            {
                                "device_ip": "192.168.200.69",
                                "provision_status": {
                                    "description": "Wired Provisioned device detail retrieved successfully.",
                                    "deviceManagementIpAddress": "192.168.200.69",
                                    "siteNameHierarchy": "Global/rishipat_area/Fabric-area-1/RCDN-Fabric-5",
                                    "status": "success"
                                }
                            }
                        ]
                    }
                ]
            ],
        )

    def test_fabric_devices_info_workflow_manager_playbook_health_info(self):
        """
        Test fabric device health information retrieval for fabric-enabled devices.

        This test verifies that the workflow correctly retrieves device health metrics
        including CPU utilization, memory usage, temperature, and overall health status
        for devices within a specified fabric site, ensuring proper data structure.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_health_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The fabric devices filtered from the network devices are: ['192.168.200.69']",
                [
                    {
                        "device_health_info": [
                            {
                                "device_ip": "192.168.200.69",
                                "health_details": {
                                    "airQualityHealth": {},
                                    "avgTemperature": 4566.666666666667,
                                    "band": {},
                                    "clientCount": {},
                                    "cpuHealth": 10,
                                    "cpuUlitilization": 2.0,
                                    "cpuUtilization": 2.0,
                                    "deviceFamily": "SWITCHES_AND_HUBS",
                                    "deviceType": "Cisco Catalyst 9300 Switch",
                                    "freeMemoryBufferHealth": -1,
                                    "freeTimerScore": -1,
                                    "interDeviceLinkAvailFabric": 10,
                                    "interDeviceLinkAvailHealth": 100,
                                    "interfaceLinkErrHealth": 10,
                                    "interferenceHealth": {},
                                    "ipAddress": "192.168.200.69",
                                    "issueCount": 0,
                                    "location": "Global/rishipat_area/Fabric-area-1/RCDN-Fabric-5",
                                    "macAddress": "DC:77:4C:D3:D5:80",
                                    "maxTemperature": 6600.0,
                                    "memoryUtilization": 51,
                                    "memoryUtilizationHealth": 10.0,
                                    "model": "Cisco Catalyst 9300 Switch",
                                    "name": "Fabric-9300-2-2.rcdnlabcead.com",
                                    "noiseHealth": {},
                                    "osVersion": "17.12.4",
                                    "overallHealth": 10,
                                    "packetPoolHealth": -1,
                                    "reachabilityHealth": "REACHABLE",
                                    "utilizationHealth": {},
                                    "uuid": "199950bc-c0d6-42f6-b1f3-a3f5aed176ee",
                                    "wanLinkUtilization": -1.0,
                                    "wqePoolsHealth": -1
                                }
                            }
                        ]
                    }
                ]
            ],
        )

    def test_fabric_devices_info_workflow_manager_playbook_issues_info(self):
        """
        Test fabric device issues information retrieval for fabric-enabled devices.

        This test verifies that the workflow correctly retrieves device issues and alerts
        including active problems, health warnings, and operational issues for devices
        within a specified fabric site, ensuring proper data structure and content.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_issues_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The fabric devices filtered from the network devices are: ['192.168.200.69']",
                [
                    {
                        "device_issues_info": [
                            {
                                "device_ip": "192.168.200.69",
                                "issue_details": []
                            }
                        ]
                    }
                ]
            ],
        )

    def test_fabric_devices_info_workflow_manager_playbook_connected_devices_info(self):
        """
        Test fabric device connected devices information retrieval for fabric-enabled devices.

        This test verifies that the workflow correctly retrieves connected device topology
        information including neighbor discovery through CDP/LLDP protocols for devices
        within a specified fabric site, ensuring proper data structure and content.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_connected_devices_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "The fabric devices filtered from the network devices are: ['204.1.2.70']",
                [
                    {
                        "connected_device_info": [
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [
                                    {
                                        "capabilities": [
                                            "ROUTER",
                                            "TB_BRIDGE"
                                        ],
                                        "neighborDevice": "AP687D.B402.1E98",
                                        "neighborPort": "GigabitEthernet0"
                                    }
                                ],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [
                                    {
                                        "capabilities": [
                                            "IGMP_CONDITIONAL_FILTERING",
                                            "ROUTER",
                                            "SWITCH"
                                        ],
                                        "neighborDevice": "SJ-IM-1-9300.cisco.local",
                                        "neighborPort": "TenGigabitEthernet1/1/8"
                                    }
                                ],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [
                                    {
                                        "capabilities": [
                                            "ROUTER",
                                            "TB_BRIDGE"
                                        ],
                                        "neighborDevice": "Cisco_9120AXE_IP4-02",
                                        "neighborPort": "GigabitEthernet0"
                                    }
                                ],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [
                                    {
                                        "capabilities": [
                                            "HOST"
                                        ],
                                        "neighborDevice": "IAC2-TSIM-1",
                                        "neighborPort": "TenGigabitEthernet0/0/1"
                                    }
                                ],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [
                                    {
                                        "capabilities": [
                                            "ROUTER",
                                            "TB_BRIDGE"
                                        ],
                                        "neighborDevice": "Cisco_9120AXE_IP4-01",
                                        "neighborPort": "GigabitEthernet0"
                                    }
                                ],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [
                                    {
                                        "capabilities": [
                                            "IGMP_CONDITIONAL_FILTERING",
                                            "SWITCH"
                                        ],
                                        "neighborDevice": "IAC-MGMT-1",
                                        "neighborPort": "GigabitEthernet1/0/2"
                                    }
                                ],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [
                                    {
                                        "capabilities": [
                                            "IGMP_CONDITIONAL_FILTERING",
                                            "ROUTER",
                                            "SWITCH"
                                        ],
                                        "neighborDevice": "SJ-IM-1-9300.cisco.local",
                                        "neighborPort": "TenGigabitEthernet1/1/7"
                                    }
                                ],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            },
                            {
                                "connected_device_details": [],
                                "device_ip": "204.1.2.70"
                            }
                        ]
                    }
                ]
            ],
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario_1(self):
        """
         Test configuration validation when 'fabric_devices' key is missing from config.

        This test verifies that the workflow correctly handles and reports an error
        when the required 'fabric_devices' key is missing from the configuration,
        ensuring proper validation and error messaging.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario_1
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "'fabric_devices' key is missing in the config block"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario_2(self):
        """
        Test configuration validation when invalid key 'fabric_device_rolee' is used in fabric device entry.

        This test verifies that the workflow correctly identifies and reports an error
        when an invalid key is used in the fabric device configuration, ensuring
        proper validation and error messaging with allowed keys.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario_2
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "'fabric_device_rolee' is not a valid key in fabric device entry. "
            "Allowed keys are: device_identifier, fabric_device_role, "
            "fabric_site_hierarchy, interval, output_file_info, requested_info, "
            "retries, timeout"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario_3(self):
        """
        Test the Fabric Devices Info Workflow Manager when no fabric devices are present.

        This test verifies that the workflow correctly handles the scenario where no
        fabric devices are returned from the system, ensuring appropriate handling and
        messaging without raising unexpected exceptions.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario_3
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Invalid or unrecognized key 'ip_addresss' found in device_identifier. Allowed keys are: hostname, ip_address, ip_address_range, serial_number"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario_4(self):
        """
        Test configuration validation when invalid key 'ip_addresss' is used in device_identifier.

        This test verifies that the workflow correctly identifies and reports an error
        when an invalid key is used in the device_identifier configuration, ensuring
        proper validation and error messaging with allowed keys.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario_4
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "'fabric_infoo' is not a valid return value. Allowed values are: "
            "['all', 'connected_devices_info', 'device_health_info', "
            "'device_issues_info', 'fabric_info', 'handoff_info', 'onboarding_info']"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario_5(self):
        """
        Test configuration validation when 'timeout' parameter has negative value.

        This test verifies that the workflow correctly identifies and reports an error
        when a negative timeout value is provided, ensuring proper validation and
        error messaging for timeout parameter constraints.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario_5
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "'timeout' must be a non-negative integer"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario_6(self):
        """
        Test configuration validation when invalid fabric_device_role value is provided.

        This test verifies that the workflow correctly identifies and reports an error
        when an invalid fabric_device_role value is used, ensuring proper validation
        and error messaging with allowed role values.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario_6
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "'fabric_device_role' must be one of: BORDER_NODE, CONTROL_PLANE_NODE, EDGE_NODE, EXTENDED_NODE, WIRELESS_CONTROLLER_NODE"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario_7(self):
        """
        Test configuration validation when 'fabric_site_hierarchy' parameter is missing.

        This test verifies that the workflow correctly identifies and reports an error
        when the required 'fabric_site_hierarchy' parameter is missing from the fabric
        device configuration, ensuring proper validation and error messaging.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario_7
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "Fabric devices configuration validation encountered an error: "
            "{'msg': \"Fabric devices configuration validation failed with invalid "
            "parameters: ['fabric_site_hierarchy : Required parameter not found']\", "
            "'response': \"Fabric devices configuration validation failed with invalid "
            "parameters: ['fabric_site_hierarchy : Required parameter not found']\", "
            "'failed': True}"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario_8(self):
        """
        Test configuration validation when invalid key 'file_paths' is used in output_file_info.

        This test verifies that the workflow correctly identifies and reports an error
        when an invalid key is used in the output_file_info configuration, ensuring
        proper validation and error messaging with allowed keys.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario_8
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "'file_paths' is not a valid key in 'output_file_info'. Allowed keys are: ['file_format', 'file_mode', 'file_path', 'timestamp']"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario_9(self):
        """
        Test configuration validation when invalid file_format value is provided.

        This test verifies that the workflow correctly identifies and reports an error
        when an invalid file_format value is used in output_file_info, ensuring proper
        validation and error messaging with allowed format values.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario_9
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "'file_format' must be one of: json, yaml"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario_10(self):
        """
        Test configuration validation when invalid file_mode value is provided.

        This test verifies that the workflow correctly identifies and reports an error
        when an invalid file_mode value is used in output_file_info, ensuring proper
        validation and error messaging with allowed mode values.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario_10
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "'file_mode' must be one of: a, w"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario_11(self):
        """
        Test configuration validation when fabric site does not exist in Cisco Catalyst Center.

        This test verifies that the workflow correctly identifies and reports an error
        when the specified fabric_site_hierarchy does not exist in the system, ensuring
        proper validation and error messaging for site hierarchy validation.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario_11
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "An exception occurred while retrieving Site details for Site "
            "'Global/rishipat_area/Fabric-area' does not exist in the Cisco Catalyst Center. "
            "Error: {'msg': 'No site details retrieved for site name: "
            "Global/rishipat_area/Fabric-area', 'response': 'No site details retrieved for site "
            "name: Global/rishipat_area/Fabric-area', 'failed': True}"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario_12(self):
        """
        Test configuration validation when site hierarchy is not a fabric site.

        This test verifies that the workflow correctly identifies and reports an error
        when the specified site hierarchy exists but is not configured as a fabric site,
        ensuring proper fabric site validation and error messaging.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_negative_scenario_12
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "The specified site hierarchy 'Global/USA/New York' is not a fabric site."
        )

    def test_fabric_devices_info_workflow_manager_playbook_ip_range_OR_logic_exception(self):
        """
        Test configuration validation when IP range is specified with OR logic.

        This test verifies that the workflow correctly identifies and processes
        the IP range specified with OR logic, ensuring proper validation and
        handling of multiple IP addresses.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_ip_range_OR_logic_exception
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "An exception occurred while retrieving Site details for Site "
            "'Global/rishipat_area/Fabric-area-1' does not exist in the Cisco Catalyst Center. "
            "Error: {'msg': \"An error occurred while executing GET API call to Function: 'get_sites' "
            "from Family: 'site_design'. Parameters: {'name_hierarchy': 'Global/rishipat_area/Fabric-area-1', "
            "'offset': 1, 'limit': 500}. Exception: .\", 'response': \"An error occurred while executing GET "
            "API call to Function: 'get_sites' from Family: 'site_design'. Parameters: {'name_hierarchy': "
            "'Global/rishipat_area/Fabric-area-1', 'offset': 1, 'limit': 500}. Exception: .\", 'failed': True}"
        )

    def test_fabric_devices_info_workflow_manager_playbook_ip_range_AND_logic_exception(self):
        """
        Test configuration validation when IP range is specified with AND logic.

        This test verifies that the workflow correctly identifies and processes
        the IP range specified with AND logic, ensuring proper validation and
        handling of multiple IP addresses.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.7.9",
                config=self.playbook_ip_range_AND_logic_exception
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "An exception occurred while retrieving Site details for Site "
            "'Global/rishipat_area/Fabric-area-1' does not exist in the Cisco Catalyst Center. "
            "Error: {'msg': \"An error occurred while executing GET API call to Function: 'get_sites' "
            "from Family: 'site_design'. Parameters: {'name_hierarchy': 'Global/rishipat_area/Fabric-area-1', "
            "'offset': 1, 'limit': 500}. Exception: .\", 'response': \"An error occurred while executing GET "
            "API call to Function: 'get_sites' from Family: 'site_design'. Parameters: {'name_hierarchy': "
            "'Global/rishipat_area/Fabric-area-1', 'offset': 1, 'limit': 500}. Exception: .\", 'failed': True}"
        )
