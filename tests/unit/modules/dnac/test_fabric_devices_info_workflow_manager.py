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

    playbook_no_fabric_devices = test_data.get("playbook_no_fabric_devices")
    playbook_error_handling1_novalid_filter = test_data.get("playbook_error_handling1_novalid_filter")
    playbook_error_handling2_novalid_filter = test_data.get("playbook_error_handling2_novalid_filter")
    playbook_nofabricdevice_and_no_networkdevice = test_data.get("playbook_nofabricdevice_and_no_networkdevice")
    playbook_with_fabric_info = test_data.get("playbook_with_fabric_info")
    playbook_handoff_info = test_data.get("playbook_handoff_info")
    playbook_health_info = test_data.get("playbook_health_info")
    playbook_connected_device_info = test_data.get("playbook_connected_device_info")
    playbook_issues_info = test_data.get("playbook_issues_info")
    playbook_onboarding_info_details = test_data.get("playbook_onboarding_info_details")
    playbook_negative_scenario1 = test_data.get("playbook_negative_scenario1")
    playbook_negative_scenario3 = test_data.get("playbook_negative_scenario3")
    playbook_negative_scenario4 = test_data.get("playbook_negative_scenario4")
    playbook_negative_scenario5 = test_data.get("playbook_negative_scenario5")
    playbook_negative_scenario6 = test_data.get("playbook_negative_scenario6")
    playbook_negative_scenario7 = test_data.get("playbook_negative_scenario7")
    playbook_negative_scenario8 = test_data.get("playbook_negative_scenario8")
    playbook_negative_scenario9 = test_data.get("playbook_negative_scenario9")
    playbook_negative_scenario10 = test_data.get("playbook_negative_scenario10")
    playbook_negative_scenario11 = test_data.get("playbook_negative_scenario11")
    playbook_negative_scenario12 = test_data.get("playbook_negative_scenario12")
    playbook_negative_scenario13 = test_data.get("playbook_negative_scenario13")

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

        if "playbook_no_fabric_devices" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("device_details"),
                self.test_data.get("get_fabric_sites"),
                self.test_data.get("get_fabric_sites1"),
                self.test_data.get("get_fabric_devices"),
                self.test_data.get("get_fabric_devices1"),
                self.test_data.get("get_fabric_devices2"),
                self.test_data.get("get_fabric_devices3"),
                self.test_data.get("get_fabric_devices4"),
            ]

        elif "playbook_error_handling1_novalid_filter" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
            ]

        elif "playbook_error_handling2_novalid_filter" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
            ]

        elif "playbook_nofabricdevice_and_no_networkdevice" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("device_details_2"),
                self.test_data.get("get_fabric_sites_v1"),
                self.test_data.get("get_fabric_sites_v2"),
            ]

        elif "playbook_with_fabric_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details"),
                self.test_data.get("get_fabric_sites4"),
                self.test_data.get("get_fabric_sites5"),
                self.test_data.get("get_fabric_devices5"),
                self.test_data.get("get_fabric_devices6"),
                self.test_data.get("get_fabric_devices7"),
                self.test_data.get("get_fabric_devices8"),
                self.test_data.get("get_fabric_devices9"),
                self.test_data.get("get_fabric_devices10"),
                self.test_data.get("get_fabric_devices11"),
                self.test_data.get("get_fabric_devices12"),
                self.test_data.get("get_fabric_devices13"),
                self.test_data.get("get_fabric_devices14"),
                self.test_data.get("get_fabric_devices15"),
                self.test_data.get("get_fabric_devices16"),
                self.test_data.get("get_fabric_sites6"),
                self.test_data.get("get_fabric_devices17"),
                self.test_data.get("get_fabric_devices18"),
                self.test_data.get("get_fabric_devices19"),
                self.test_data.get("get_fabric_devices20"),
                self.test_data.get("get_fabric_devices21"),
                self.test_data.get("get_fabric_devices22"),
            ]

        elif "playbook_handoff_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details1"),
                self.test_data.get("get_fabric_sites7"),
                self.test_data.get("get_fabric_sites8"),
                self.test_data.get("get_fabric_devices23"),
                self.test_data.get("get_fabric_devices24"),
                self.test_data.get("get_fabric_devices25"),
                self.test_data.get("get_fabric_devices26"),
                self.test_data.get("get_fabric_devices27"),
                self.test_data.get("get_fabric_devices28"),
                self.test_data.get("get_fabric_devices29"),
                self.test_data.get("get_fabric_devices30"),
                self.test_data.get("get_fabric_devices31"),
                self.test_data.get("get_fabric_devices32"),
                self.test_data.get("get_fabric_devices33"),
                self.test_data.get("get_fabric_devices34"),
                self.test_data.get("get_fabric_devices_layer3_handoffs_with_sda_transit"),
                self.test_data.get("get_fabric_devices_layer3_handoffs_with_ip_transit"),
                self.test_data.get("get_fabric_devices_layer2_handoffs"),
            ]

        elif "playbook_health_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details3"),
                self.test_data.get("get_fabric_sites13"),
                self.test_data.get("get_fabric_sites14"),
                self.test_data.get("get_fabric_devices59"),
                self.test_data.get("get_fabric_devices60"),
                self.test_data.get("get_fabric_devices61"),
                self.test_data.get("get_fabric_devices62"),
                self.test_data.get("get_fabric_devices63"),
                self.test_data.get("get_fabric_devices64"),
                self.test_data.get("get_fabric_devices65"),
                self.test_data.get("get_fabric_devices66"),
                self.test_data.get("get_fabric_devices67"),
                self.test_data.get("get_fabric_devices68"),
                self.test_data.get("get_fabric_devices69"),
                self.test_data.get("get_fabric_devices70"),
                self.test_data.get("health_info"),
            ]

        elif "playbook_connected_device_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details2"),
                self.test_data.get("get_fabric_sites11"),
                self.test_data.get("get_fabric_sites12"),
                self.test_data.get("get_fabric_devices47"),
                self.test_data.get("get_fabric_devices48"),
                self.test_data.get("get_fabric_devices49"),
                self.test_data.get("get_fabric_devices50"),
                self.test_data.get("get_fabric_devices51"),
                self.test_data.get("get_fabric_devices52"),
                self.test_data.get("get_fabric_devices53"),
                self.test_data.get("get_fabric_devices54"),
                self.test_data.get("get_fabric_devices55"),
                self.test_data.get("get_fabric_devices56"),
                self.test_data.get("get_fabric_devices57"),
                self.test_data.get("get_fabric_devices58"),
                self.test_data.get("get_interface_info_by_id"),
                self.test_data.get("connected_info_1"),
                self.test_data.get("connected_info_2"),
                self.test_data.get("connected_info_3"),
                self.test_data.get("connected_info_4"),
                self.test_data.get("connected_info_5"),
                self.test_data.get("connected_info_6"),
                self.test_data.get("connected_info_7"),
                self.test_data.get("connected_info_8"),
            ]
        elif "playbook_issues_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites1"),
                self.test_data.get("get_sites3"),
                self.test_data.get("get_device_list4"),
                self.test_data.get("get_fabric_sites15"),
                self.test_data.get("get_fabric_sites16"),
                self.test_data.get("get_fabric_devices71"),
                self.test_data.get("get_fabric_devices72"),
                self.test_data.get("get_fabric_devices73"),
                self.test_data.get("get_fabric_devices74"),
                self.test_data.get("get_fabric_devices75"),
                self.test_data.get("get_fabric_devices76"),
                self.test_data.get("get_fabric_devices77"),
                self.test_data.get("get_fabric_devices78"),
                self.test_data.get("get_fabric_devices79"),
                self.test_data.get("get_fabric_devices80"),
                self.test_data.get("get_fabric_devices81"),
                self.test_data.get("get_fabric_devices82"),
                self.test_data.get("issues"),
            ]

        elif "playbook_onboarding_info_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list5"),
                self.test_data.get("get_fabric_sites9"),
                self.test_data.get("get_fabric_sites10"),
                self.test_data.get("get_fabric_devices35"),
                self.test_data.get("get_fabric_devices36"),
                self.test_data.get("get_fabric_devices37"),
                self.test_data.get("get_fabric_devices38"),
                self.test_data.get("get_fabric_devices39"),
                self.test_data.get("get_fabric_devices40"),
                self.test_data.get("get_fabric_devices41"),
                self.test_data.get("get_fabric_devices42"),
                self.test_data.get("get_fabric_devices43"),
                self.test_data.get("get_fabric_devices44"),
                self.test_data.get("get_fabric_devices45"),
                self.test_data.get("get_fabric_devices46"),
                self.test_data.get("get_port_assignments"),
                self.test_data.get("get_network_device_by_ip"),
                self.test_data.get("get_provision_status"),
            ]

        elif "playbook_negative_scenario1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
            ]

        elif "playbook_negative_scenario2" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
            ]

        elif "playbook_negative_scenario3" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
            ]

        elif "playbook_negative_scenario4" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
            ]

        elif "playbook_negative_scenario5" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
            ]

        elif "playbook_negative_scenario6" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
            ]

        elif "playbook_negative_scenario7" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
            ]

        elif "playbook_negative_scenario8" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
            ]

        elif "playbook_negative_scenario9" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
            ]

    def test_fabric_devices_info_workflow_manager_playbook_no_fabric_devices(self):
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
                config=self.playbook_no_fabric_devices
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "No fabric devices found for the given filters."
            ]
        )

    def test_fabric_devices_info_workflow_manager_playbook_error_handling1_novalid_filter(self):
        """
        Test error handling in Fabric Devices Info Workflow Manager with no valid filters.

        This test verifies that the workflow appropriately handles cases where the input
        filters do not match.
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
                config=self.playbook_error_handling1_novalid_filter
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("response"),
            "Each fabric device must contain at least one of: ip_address, hostname, serial_number, device_role, site_hierarchy, device_type."
        )

    def test_fabric_devices_info_workflow_manager_playbook_error_handling2_novalid_filter(self):
        """
        Test error handling in Fabric Devices Info Workflow Manager with no valid filters for requested_info.

        This test verifies that the workflow appropriately handles cases where the input
        filters do not match, ensuring that informative error messages are logged and
        no unexpected failures occur.
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
                config=self.playbook_error_handling2_novalid_filter
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("response"),
            "'fabric_infoo' is not a valid return value. Allowed values are: "
            "['all', 'connected_devices_info', 'device_health_info', 'device_issues_info', "
            "'fabric_info', 'handoff_info', 'onboarding_info']"
        )

    def test_fabric_devices_info_workflow_manager_playbook_nofabricdevice_and_no_networkdevice(self):
        """
        Test the Fabric Devices Info Workflow Manager with no fabric and no network devices.

        This test ensures that the workflow behaves correctly when the system returns
        neither fabric-enabled devices nor general network devices, verifying that it
        handles the absence of device data gracefully and logs appropriate messages.
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
                config=self.playbook_nofabricdevice_and_no_networkdevice
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            [
                "No devices found for hostname = TB1-DM-Transit.solutionsanity1234.com after 1 retry attempts within 1 second timeout",
                "No matching network devices were found for the given filter criteria.",
                "No fabric devices found for the given filters."
            ],
        )

    def test_fabric_devices_info_workflow_manager_playbook_with_fabric_info(self):
        """
        Test the Fabric Devices Info Workflow Manager with fabric information.

        This test verifies that the workflow correctly retrieves and processes
        fabric-related information from the specified devices.
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
                config=self.playbook_with_fabric_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get("response"),
            [
                "The fabric devices filtered from the network devices are: ['204.192.5.2']",
                [
                    {
                        "fabric_info": [
                            {
                                "device_ip": "204.192.5.2",
                                "fabric_details": [
                                    {
                                        "deviceRoles": [
                                            "WIRELESS_CONTROLLER_NODE"
                                        ],
                                        "fabricId": "6ea62e10-cc4b-4f67-8251-d0939fdd4ad8",
                                        "id": "e36cb88e-1a21-44a5-861f-693d9dc19e7b",
                                        "networkDeviceId": "1841ff80-886b-47fa-9053-85000e4af745"
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
        Test the Fabric Devices Info Workflow Manager with handoff information.
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
        self.assertEqual(
            result.get("response"),
            [
                "The fabric devices filtered from the network devices are: ['91.1.1.2']",
                [
                    {
                        'fabric_devices_layer3_handoffs_sda_info': [
                            {
                                'device_ip': '91.1.1.2',
                                'handoff_info': [
                                    {
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': '02f92f56-e9c8-4534-b7f1-e06635061de9',
                                        'connectedToInternet': True,
                                        'isMulticastOverTransitEnabled': False
                                    }
                                ]
                            }
                        ]
                    }
                ],
                [
                    {
                        'fabric_devices_layer3_handoffs_ip_info': [
                            {
                                'device_ip': '91.1.1.2',
                                'handoff_info': [
                                    {
                                        'id': 'f10250af-bd72-4175-ad9b-ea2831e74a15',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'DEFAULT_VN',
                                        'vlanId': 3000,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.69/30',
                                        'remoteIpAddress': '204.1.16.70/30',
                                        'localIpv6Address': '2004:1:16::1:0:45/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:46/126'
                                    },
                                    {
                                        'id': '3cd81271-4621-40fd-aac7-8b8499127c0c',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'Fabric_VN',
                                        'vlanId': 3001,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.73/30',
                                        'remoteIpAddress': '204.1.16.74/30',
                                        'localIpv6Address': '2004:1:16::1:0:49/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:4a/126'
                                    },
                                    {
                                        'id': 'cdad28e7-8df2-432d-8550-666a9fcfc21c',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'INFRA_VN',
                                        'vlanId': 3002,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.77/30',
                                        'remoteIpAddress': '204.1.16.78/30',
                                        'localIpv6Address': '2004:1:16::1:0:4d/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:4e/126'
                                    },
                                    {
                                        'id': '8711bdb5-7a92-4ab0-a7d7-b4053e1db84c',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'IntraSubnet_VN',
                                        'vlanId': 3003,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.81/30',
                                        'remoteIpAddress': '204.1.16.82/30',
                                        'localIpv6Address': '2004:1:16::1:0:51/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:52/126'
                                    },
                                    {
                                        'id': '66b48881-e72f-44cc-aedb-6819af25bd27',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'SGT_Port_test',
                                        'vlanId': 3004,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.85/30',
                                        'remoteIpAddress': '204.1.16.86/30',
                                        'localIpv6Address': '2004:1:16::1:0:55/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:56/126'
                                    },
                                    {
                                        'id': '6dd7d005-74aa-4762-a59e-1c280a975425',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'VN1',
                                        'vlanId': 3005,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.89/30',
                                        'remoteIpAddress': '204.1.16.90/30',
                                        'localIpv6Address': '2004:1:16::1:0:59/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:5a/126'
                                    },
                                    {
                                        'id': 'a13167ae-d900-4048-92a6-0d41bd1bd531',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'VN2',
                                        'vlanId': 3006,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.93/30',
                                        'remoteIpAddress': '204.1.16.94/30',
                                        'localIpv6Address': '2004:1:16::1:0:5d/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:5e/126'
                                    },
                                    {
                                        'id': '932cd9d7-9067-4224-ab1d-922a7cd79b5b',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'VN3',
                                        'vlanId': 3007,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.97/30',
                                        'remoteIpAddress': '204.1.16.98/30',
                                        'localIpv6Address': '2004:1:16::1:0:61/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:62/126'
                                    },
                                    {
                                        'id': '9c09c4a8-5a7f-4b06-ac28-4d895293cfe7',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'VN4',
                                        'vlanId': 3008,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.101/30',
                                        'remoteIpAddress': '204.1.16.102/30',
                                        'localIpv6Address': '2004:1:16::1:0:65/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:66/126'
                                    },
                                    {
                                        'id': 'df69abf3-266a-4678-84d2-ca8d9340b4c2',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'VN5',
                                        'vlanId': 3009,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.105/30',
                                        'remoteIpAddress': '204.1.16.106/30',
                                        'localIpv6Address': '2004:1:16::1:0:69/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:6a/126'
                                    },
                                    {
                                        'id': 'd95e8a82-7a71-4f4a-a31a-85385c1e1ef8',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'VN6',
                                        'vlanId': 3010,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.109/30',
                                        'remoteIpAddress': '204.1.16.110/30',
                                        'localIpv6Address': '2004:1:16::1:0:6d/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:6e/126'
                                    },
                                    {
                                        'id': '27171568-3f08-4f13-8991-a8904bc7e2a6',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'VN7',
                                        'vlanId': 3011,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.113/30',
                                        'remoteIpAddress': '204.1.16.114/30',
                                        'localIpv6Address': '2004:1:16::1:0:71/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:72/126'
                                    },
                                    {
                                        'id': 'bb704a7d-8988-4d8c-80e5-4c02bb9ab042',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'WiredVNFB1',
                                        'vlanId': 3012,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.117/30',
                                        'remoteIpAddress': '204.1.16.118/30',
                                        'localIpv6Address': '2004:1:16::1:0:75/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:76/126'
                                    },
                                    {
                                        'id': '8d814e72-25af-490d-8f69-dec10af9e790',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'WiredVNFBLayer2',
                                        'vlanId': 3013,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.121/30',
                                        'remoteIpAddress': '204.1.16.122/30',
                                        'localIpv6Address': '2004:1:16::1:0:79/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:7a/126'
                                    },
                                    {
                                        'id': 'b01aa3a2-61c8-4179-a568-6dcdbafe993f',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'WiredVNStatic',
                                        'vlanId': 3014,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.125/30',
                                        'remoteIpAddress': '204.1.16.126/30',
                                        'localIpv6Address': '2004:1:16::1:0:7d/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:7e/126'
                                    },
                                    {
                                        'id': 'a4f61e60-b75c-4bcd-b7c4-e3bd68ec324d',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'WirelessVNFB',
                                        'vlanId': 3015,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.129/30',
                                        'remoteIpAddress': '204.1.16.130/30',
                                        'localIpv6Address': '2004:1:16::1:0:81/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:82/126'
                                    },
                                    {
                                        'id': '43761af5-509f-4d07-9d2c-8b09f6ba2114',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'transitNetworkId': 'bbf16d41-031b-4061-b9b6-ae75768ae196',
                                        'interfaceName': 'TenGigabitEthernet1/0/2',
                                        'externalConnectivityIpPoolName': 'BorderHandOff_sub',
                                        'virtualNetworkName': 'WirelessVNFGuest',
                                        'vlanId': 3016,
                                        'tcpMssAdjustment': 0,
                                        'localIpAddress': '204.1.16.133/30',
                                        'remoteIpAddress': '204.1.16.134/30',
                                        'localIpv6Address': '2004:1:16::1:0:85/126',
                                        'remoteIpv6Address': '2004:1:16::1:0:86/126'
                                    }
                                ]
                            }
                        ]
                    }
                ],
                [
                    {
                        'fabric_devices_layer2_handoffs_info': [
                            {
                                'device_ip': '91.1.1.2',
                                'handoff_info': [
                                ]
                            }
                        ]
                    }
                ]
            ]
        )

    def test_fabric_devices_info_workflow_manager_playbook_health_info(self):
        """
        Test the Fabric Devices Info Workflow Manager with health information.
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
        self.assertEqual(
            result.get("response"),
            [
                "The fabric devices filtered from the network devices are: ['204.192.5.2']",
                [
                    {
                        "device_health_info": [
                            {
                                "device_ip": "204.192.5.2",
                                "health_details": {
                                    "airQualityHealth": {},
                                    "avgTemperature": 3511.1111111111113,
                                    "band": {},
                                    "clientCount": {},
                                    "cpuHealth": -1,
                                    "deviceFamily": "WIRELESS_CONTROLLER",
                                    "deviceType": "Cisco Catalyst 9800-40 Wireless Controller",
                                    "freeMemoryBufferHealth": -1,
                                    "freeTimerScore": -1,
                                    "interDeviceLinkAvailFabric": -1,
                                    "interDeviceLinkAvailHealth": 100,
                                    "interfaceLinkErrHealth": -1,
                                    "interferenceHealth": {},
                                    "ipAddress": "204.192.5.2",
                                    "issueCount": 2,
                                    "location": "Global/USA/SAN JOSE/BLD23",
                                    "macAddress": "4C:E1:75:02:2B:0B",
                                    "maxTemperature": 5300.0,
                                    "memoryUtilizationHealth": -1.0,
                                    "model": "Cisco Catalyst 9800-40 Wireless Controller",
                                    "name": "TB17-eWLC-SJ.cisco.com",
                                    "noiseHealth": {},
                                    "osVersion": "17.15.2b",
                                    "overallHealth": -1,
                                    "packetPoolHealth": -1,
                                    "reachabilityHealth": "REACHABLE",
                                    "utilizationHealth": {},
                                    "uuid": "1841ff80-886b-47fa-9053-85000e4af745",
                                    "wanLinkUtilization": -1.0,
                                    "wqePoolsHealth": -1
                                }
                            }
                        ]
                    }
                ]
            ]
        )

    def test_fabric_devices_info_workflow_manager_playbook_connected_device_info(self):
        """
        Test the Fabric Devices Info Workflow Manager with connected device information.
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
                config=self.playbook_connected_device_info
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(111111111)
        print(result)
        print(111111111)
        self.maxDiff = None
        self.assertEqual(
            result.get("response"),
            [
                "The fabric devices filtered from the network devices are: ['204.192.5.2']",
                [
                    {
                        'connected_device_info': [
                            {
                                'device_ip': '204.192.5.2',
                                'connected_device_details': [
                                ]
                            },
                            {
                                'device_ip': '204.192.5.2',
                                'connected_device_details': [
                                ]
                            },
                            {
                                'device_ip': '204.192.5.2',
                                'connected_device_details': [
                                ]
                            },
                            {
                                'device_ip': '204.192.5.2',
                                'connected_device_details': [
                                ]
                            },
                            {
                                'device_ip': '204.192.5.2',
                                'connected_device_details': [
                                    {
                                        'neighborDevice': 'TB17-Fusion.cisco.com',
                                        'neighborPort': 'GigabitEthernet1/0/21',
                                        'capabilities': [
                                            'IGMP_CONDITIONAL_FILTERING',
                                            'ROUTER',
                                            'SWITCH'
                                        ]
                                    }
                                ]
                            },
                            {
                                'device_ip': '204.192.5.2',
                                'connected_device_details': [
                                ]
                            },
                            {
                                'device_ip': '204.192.5.2',
                                'connected_device_details': [
                                ]
                            },
                            {
                                'device_ip': '204.192.5.2',
                                'connected_device_details': [
                                ]
                            }
                        ]
                    }
                ]
            ]
        )

    def test_fabric_devices_info_workflow_manager_playbook_issues_info(self):
        """
        Test the Fabric Devices Info Workflow Manager with issues information.
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
                "The fabric devices filtered from the network devices are: ['204.1.2.129']",
                [
                    {
                        'device_issues_info': [
                            {
                                'device_ip': '204.1.2.129',
                                'issue_details': [
                                    {
                                        'issueId': '291b9e86-30e5-4c45-8978-d98c92957707',
                                        'name': (
                                            'Cisco TrustSec environment data is not complete on Fabric EDGE:BORDER:WLC:MAP-SERVER '
                                            'node NY-Fiab-9300.cisco.com in Fabric site Global/USA/New York'
                                        ),
                                        'siteId': '',
                                        'deviceId': 'e714d470-de0e-43a0-9469-099ddcf8467a',
                                        'deviceRole': '',
                                        'aiDriven': 'No',
                                        'clientMac': None,
                                        'issue_occurence_count': 228,
                                        'status': 'active',
                                        'priority': 'P1',
                                        'category': 'Connected',
                                        'last_occurence_time': 1755758565019
                                    }
                                ]
                            }
                        ]
                    }
                ]
            ],
        )

    def test_fabric_devices_info_workflow_manager_playbook_onboarding_info_details(self):
        """
        Test the Fabric Devices Info Workflow Manager with onboarding information details.
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
                config=self.playbook_onboarding_info_details
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get("response"),
            [
                "The fabric devices filtered from the network devices are: ['91.1.1.2']",
                [
                    {
                        "device_onboarding_info": [
                            {
                                "device_ip": "91.1.1.2",
                                "port_details": []
                            }
                        ]
                    }
                ],
                [
                    {
                        "ssid_info": [
                            {
                                "device_ip": "91.1.1.2",
                                "ssid_details": "The device is not wireless; therefore, SSID information retrieval is not applicable."
                            }
                        ]
                    }
                ],
                [
                    {
                        "provision_status_info": [
                            {
                                "device_ip": "91.1.1.2",
                                "provision_status": {
                                    "description": "Wired Provisioned device detail retrieved successfully.",
                                    "deviceManagementIpAddress": "91.1.1.2",
                                    "siteNameHierarchy": "Global/USA/SAN JOSE/BLD23",
                                    "status": "success"
                                }
                            }
                        ]
                    }
                ]
            ]
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario1(self):
        """
        Test the Fabric Devices Info Workflow Manager with a playbook that has no 'fabric_devices' key.

        This test ensures that the module correctly identifies and handles the absence of the required key,
        returning an appropriate error message.
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
                config=self.playbook_negative_scenario1
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("response"),
            "'fabric_devices' key is missing in the config block"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario5(self):
        """
        Test the Fabric Devices Info Workflow Manager with a playbook that has invalid data type.

        This test ensures that the module correctly identifies and handles invalid data type,
        returning an appropriate error message.
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
                config=self.playbook_negative_scenario5
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("response"),
            '''Invalid parameters in playbook: ["'requested_info': 'onboarding_info' is invalid. Reason: expected type: 'list'. Provided type: 'str'. "]'''
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario6(self):
        """
        Test the Fabric Devices Info Workflow Manager with a playbook that has invalid timeout value.

        This test ensures that the module correctly identifies and handles negative timeout value,
        returning an appropriate error message.
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
                config=self.playbook_negative_scenario6
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("response"),
            "'timeout' must be a non-negative integer"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario7(self):
        """
        Test the Fabric Devices Info Workflow Manager with a playbook that has invalid data type for output_file_info.

        This test ensures that the module correctly identifies and handles invalid data type for output_file_info,
        returning an appropriate error message.
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
                config=self.playbook_negative_scenario7
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("response"),
            '''Invalid parameters in playbook: ["'file_path': '['/Users/priyadharshini/Downloads/device_pireeeeya']' is invalid. '''
            '''Reason: '['/Users/priyadharshini/Downloads/device_pireeeeya']' is not a string and conversion is not allowed. "]'''
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario8(self):
        """
        Test the Fabric Devices Info Workflow Manager with a playbook that has invalid data type for file_format.

        This test ensures that the module correctly identifies and handles invalid data type for file_format,
        returning an appropriate error message.
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
                config=self.playbook_negative_scenario8
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("response"),
            '''Invalid parameters in playbook: ["'file_format': '['yaml']' is invalid. Reason: '['yaml']' is not a string and conversion is not allowed. "]'''
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario9(self):
        """
        Test the Fabric Devices Info Workflow Manager with a playbook that has invalid data type for file_mode.

        This test ensures that the module correctly identifies and handles invalid data type for file_mode,
        returning an appropriate error message.
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
                config=self.playbook_negative_scenario9
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("response"),
            '''Invalid parameters in playbook: ["'file_mode': '['a']' is invalid. Reason: '['a']' is not a string and conversion is not allowed. "]'''
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario10(self):
        """
        Test the Fabric Devices Info Workflow Manager with a playbook that has invalid file_mode value.

        This test ensures that the module correctly identifies and handles an invalid file_mode value,
        returning an appropriate error message.
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
                config=self.playbook_negative_scenario10
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("response"),
            "'file_mode' must be one of: a, w"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario11(self):
        """
        Test the Fabric Devices Info Workflow Manager with a playbook that has invalid value for file_format.

        This test ensures that the module correctly identifies and handles invalid value for file_format,
        returning an appropriate error message.
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
                config=self.playbook_negative_scenario11
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("response"),
            "'file_format' must be one of: json, yaml"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario12(self):
        """
        Test the Fabric Devices Info Workflow Manager with a playbook that has invalid key in output_file_info.

        This test ensures that the module correctly identifies and handles an invalid key in output_file_info,
        returning an appropriate error message.
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
                config=self.playbook_negative_scenario12
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("response"),
            "'file' is not a valid key in 'output_file_info'. Allowed keys are: ['file_format', 'file_mode', 'file_path', 'timestamp']"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario13(self):
        """
        Test the Fabric Devices Info Workflow Manager with a playbook that uses an unsupported DNAC version.

        This test ensures that the module correctly identifies and handles unsupported DNAC versions,
        returning an appropriate error message.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                dnac_version="2.3.5.3",
                config=self.playbook_negative_scenario13
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("msg"),
            "The specified version '2.3.5.3' does not support the 'fabric device info workflow' feature. Supported version(s) start from '2.3.7.9' onwards."
        )
