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


class TestDnacApplicationPolicyWorkflowManager(TestDnacModule):

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
    playbook_negative_scenario12 = test_data.get("playbook_negative_scenario12")
    playbook_negative_scenario13 = test_data.get("playbook_negative_scenario13")

    def setUp(self):
        super(TestDnacApplicationPolicyWorkflowManager, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacApplicationPolicyWorkflowManager, self).tearDown()
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
                self.test_data.get("get_fabric_sites2"),
                self.test_data.get("get_fabric_sites3"),
                self.test_data.get("get_fabric_devices5"),
                self.test_data.get("get_fabric_devices6"),
                self.test_data.get("get_fabric_devices7"),
                self.test_data.get("get_fabric_devices8"),
                self.test_data.get("get_fabric_devices9"),
                self.test_data.get("get_fabric_sites4"),
                self.test_data.get("get_fabric_devices10"),
                self.test_data.get("get_fabric_devices11"),
                self.test_data.get("get_fabric_devices12"),
                self.test_data.get("get_fabric_devices13"),
                self.test_data.get("get_fabric_devices14"),
            ]

        elif "playbook_handoff_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details1"),
                self.test_data.get("get_fabric_sites5"),
                self.test_data.get("get_fabric_sites6"),
                self.test_data.get("get_fabric_devices15"),
                self.test_data.get("get_fabric_devices16"),
                self.test_data.get("get_fabric_devices17"),
                self.test_data.get("get_fabric_devices18"),
                self.test_data.get("get_fabric_devices19"),
                self.test_data.get("get_fabric_sites7"),
                self.test_data.get("get_fabric_devices_layer3_handoffs_with_sda_transit_v1"),
                self.test_data.get("get_fabric_sites8"),
                self.test_data.get("get_fabric_devices_layer3_handoffs_with_ip_transit_v1"),
                self.test_data.get("get_fabric_sites10"),
                self.test_data.get("get_fabric_devices_layer2_handoffs_v1"),
            ]

        elif "playbook_health_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites"),
                self.test_data.get("get_site_assigned_network_devices"),
                self.test_data.get("get_device_list"),
                self.test_data.get("get_fabric_sites11"),
                self.test_data.get("get_fabric_sites12"),
                self.test_data.get("get_fabric_devices_20"),
                self.test_data.get("get_fabric_devices_21"),
                self.test_data.get("get_fabric_devices_22"),
                self.test_data.get("get_fabric_devices_23"),
                self.test_data.get("get_fabric_devices_24"),
                self.test_data.get("devices_v1"),
            ]

        elif "playbook_connected_device_info" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_details2"),
                self.test_data.get("get_fabric_sites13"),
                self.test_data.get("get_fabric_sites14"),
                self.test_data.get("get_fabric_devices_25"),
                self.test_data.get("get_fabric_devices_26"),
                self.test_data.get("get_fabric_devices_27"),
                self.test_data.get("get_fabric_devices_28"),
                self.test_data.get("get_fabric_devices_29"),
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
                self.test_data.get("get_device_details3"),
                self.test_data.get("get_fabric_sites15"),
                self.test_data.get("get_fabric_sites16"),
                self.test_data.get("get_fabric_devices_30"),
                self.test_data.get("get_fabric_devices_31"),
                self.test_data.get("get_fabric_devices_32"),
                self.test_data.get("get_fabric_devices_33"),
                self.test_data.get("get_fabric_devices_34"),
                self.test_data.get("issues"),
            ]

        elif "playbook_onboarding_info_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list5"),
                self.test_data.get("get_fabric_sites19"),
                self.test_data.get("get_fabric_sites20"),
                self.test_data.get("get_fabric_devices_40"),
                self.test_data.get("get_fabric_devices_41"),
                self.test_data.get("get_fabric_devices_42"),
                self.test_data.get("get_fabric_devices_43"),
                self.test_data.get("get_fabric_devices_44"),
                self.test_data.get("get_fabric_sites21"),
                self.test_data.get("get_port_assignments_v1"),
                self.test_data.get("provision_status1"),
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
                "No devices found for hostname = TB1-DM-Transit.solutionsanity1234.com. Data retrieval failed after maximum retries.",
                "",
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
                "The fabric devices filtered from the network devices are: ['91.1.1.2']",
                [
                    {
                        'fabric_info': [
                            {
                                'device_ip': '91.1.1.2',
                                'fabric_details': [
                                    {
                                        'id': 'a82b50c5-58e6-4491-ad7e-d149589593f3',
                                        'fabricId': '6ea62e10-cc4b-4f67-8251-d0939fdd4ad8',
                                        'networkDeviceId': '36680b59-39b2-446b-8ceb-5a1e157b5799',
                                        'deviceRoles': [
                                            'BORDER_NODE',
                                            'CONTROL_PLANE_NODE'
                                        ],
                                        'borderDeviceSettings': {
                                            'borderTypes': [
                                                'LAYER_3'
                                            ],
                                            'layer3Settings': {
                                                'localAutonomousSystemNumber': '6100',
                                                'importExternalRoutes': True,
                                                'borderPriority': 6,
                                                'prependAutonomousSystemCount': 7,
                                                'isDefaultExit': True
                                            }
                                        }
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
                        "fabric_devices_layer3_handoffs_sda_info": [
                            {
                                "device_ip": "91.1.1.2",
                                "handoff_info": "No handoff info found"
                            }
                        ]
                    }
                ],
                [
                    {
                        "fabric_devices_layer3_handoffs_ip_info": [
                            {
                                "device_ip": "91.1.1.2",
                                "handoff_info": "No handoff info found"
                            }
                        ]
                    }
                ],
                [
                    {
                        "fabric_devices_layer2_handoffs_info": [
                            {
                                "device_ip": "91.1.1.2",
                                "handoff_info": "No handoff info found"
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
                "The fabric devices filtered from the network devices are: ['204.1.2.129']",
                [
                    {
                        "device_health_info": [
                            {
                                "device_ip": "204.1.2.129",
                                "health_details": {
                                    "airQualityHealth": {},
                                    "apCount": 2,
                                    "avgTemperature": 3700.0,
                                    "band": {},
                                    "clientCount": {},
                                    "cpuHealth": 10,
                                    "cpuUlitilization": 2.25,
                                    "cpuUtilization": 2.25,
                                    "deviceFamily": "SWITCHES_AND_HUBS",
                                    "deviceType": "Cisco Catalyst 9300 Switch",
                                    "freeMemoryBufferHealth": -1,
                                    "freeTimerScore": -1,
                                    "interDeviceLinkAvailFabric": 10,
                                    "interDeviceLinkAvailHealth": 100,
                                    "interfaceLinkErrHealth": 10,
                                    "interferenceHealth": {},
                                    "ipAddress": "204.1.2.129",
                                    "issueCount": 1,
                                    "location": "Global/USA/New York/BLDNYC",
                                    "macAddress": "74:86:0B:0C:2F:00",
                                    "maxTemperature": 4800.0,
                                    "memoryUtilization": 65,
                                    "memoryUtilizationHealth": 10.0,
                                    "model": "Cisco Catalyst 9300 Switch",
                                    "name": "NY-Fiab-9300.cisco.com",
                                    "noiseHealth": {},
                                    "osVersion": "17.17.1prd6",
                                    "overallHealth": 10,
                                    "packetPoolHealth": -1,
                                    "reachabilityHealth": "REACHABLE",
                                    "utilizationHealth": {},
                                    "uuid": "e714d470-de0e-43a0-9469-099ddcf8467a",
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
        self.assertEqual(
            result.get("response"),
            [
                "The fabric devices filtered from the network devices are: ['204.192.5.2']",
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
                                        "neighborDevice": "TB17-Fusion.cisco.com",
                                        "neighborPort": "GigabitEthernet1/0/21"
                                    }
                                ],
                                "device_ip": "204.192.5.2"
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
        self.assertEqual(
            result.get("response"),
            [
                "The fabric devices filtered from the network devices are: ['204.192.5.2']",
                [
                    {
                        'device_issues_info': [
                            {
                                'device_ip': '204.192.5.2',
                                'issue_details': [
                                    {
                                        'issueId': '72090898-80f0-4eaa-8249-821faff48efd',
                                        'name': 'Excessive time lag between Cisco Catalyst Center and device TB17-eWLC-SJ.cisco.com',
                                        'siteId': '',
                                        'deviceId': '1841ff80-886b-47fa-9053-85000e4af745',
                                        'deviceRole': '',
                                        'aiDriven': 'No',
                                        'clientMac': None,
                                        'issue_occurence_count': 495,
                                        'status': 'active',
                                        'priority': 'P3',
                                        'category': 'Device',
                                        'last_occurence_time': 1752072623000
                                    },
                                    {
                                        'issueId': 'f29a9599-1bd3-442d-b775-06522244b52d',
                                        'name': 'Cisco Catalyst Center is not receiving data from TB17-eWLC-SJ.cisco.com Wireless Controller',
                                        'siteId': '',
                                        'deviceId': '1841ff80-886b-47fa-9053-85000e4af745',
                                        'deviceRole': '',
                                        'aiDriven': 'No',
                                        'clientMac': None,
                                        'issue_occurence_count': 1,
                                        'status': 'active',
                                        'priority': 'P3',
                                        'category': 'Availability',
                                        'last_occurence_time': 1752014700000
                                    }
                                ]
                            }
                        ]
                    }
                ]
            ]
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
                "The fabric devices filtered from the network devices are: ['204.192.5.2']",
                [
                    {
                        "device_onboarding_info": [
                            {
                                "device_ip": "204.192.5.2",
                                "port_details": "No port assignment details found"
                            }
                        ]
                    }
                ],
                [
                    {
                        "provision_status_info": [
                            {
                                "device_ip": "204.192.5.2",
                                "provision_status": {
                                    "description": "Wired Provisioned device detail retrieved successfully.",
                                    "deviceManagementIpAddress": "204.192.5.2",
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

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario2(self):
        """
        Test the Fabric Devices Info Workflow Manager with a playbook that has duplicate IP addresses.

        This test ensures that the module correctly identifies and handles duplicate IP addresses,
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
                config=self.playbook_negative_scenario2
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("response"),
            "Duplicate ip_address found: 204.192.5.2"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario3(self):
        """
        Test the Fabric Devices Info Workflow Manager with a playbook that has duplicate hostnames.

        This test ensures that the module correctly identifies and handles duplicate hostnames,
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
                config=self.playbook_negative_scenario3
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("response"),
            "Duplicate hostname found: AP0CD0.F894.0C44"
        )

    def test_fabric_devices_info_workflow_manager_playbook_negative_scenario4(self):
        """
        Test the Fabric Devices Info Workflow Manager with a playbook that has duplicate serial numbers.

        This test ensures that the module correctly identifies and handles duplicate serial numbers,
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
                config=self.playbook_negative_scenario4
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("response"),
            "Duplicate serial_number found: KWC22440QJ2"
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
            "Invalid parameters in playbook: ['onboarding_info : is not a valid list']"
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
        Test the Fabric Devices Info Workflow Manager with a playbook that has invalid data type for file_info.

        This test ensures that the module correctly identifies and handles invalid data type for file_info,
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
            "'file_path' in file_info must be a string"
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
            "'file_format' in file_info must be a string"
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
            "'file_mode' in file_info must be a string"
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
        Test the Fabric Devices Info Workflow Manager with a playbook that has invalid key in file_info.

        This test ensures that the module correctly identifies and handles an invalid key in file_info,
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
            "'file' is not a valid key in file_info. Allowed keys are: ['file_format', 'file_mode', 'file_path', 'timestamp']"
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
