# Copyright (c) 2025 Cisco and/or its affiliates.
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
#   -  A Mohamed Rafeek <mabdulk2@cisco.com>

"""
Unit tests for the pnp_workflow_manager Ansible module.

This module is responsible for managing pnp workflows in Cisco Catalyst Center.
"""

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import pnp_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacPnpWorkflow(TestDnacModule):
    """
    Unit test class for PNP workflow manager
    """
    module = pnp_workflow_manager
    test_data = loadPlaybookData("pnp_workflow_manager")

    playbook_config_accesspoint = test_data.get("playbook_config_accesspoint")
    playbook_config_switch = test_data.get("playbook_config_switch")
    playbook_config_delete = test_data.get("playbook_config_delete")
    playbook_config_wlc_vlan = test_data.get("playbook_config_wlc_vlan")
    playbook_config_wlc_error = test_data.get("playbook_config_wlc_error")
    playbook_config_pnp = test_data.get("playbook_config_pnp")
    playbook_config_switch_site_issue = test_data.get("playbook_config_switch_site_issue")
    playbook_config_reset_device = test_data.get("playbook_config_reset_device")
    playbook_config_bulk_pnp = test_data.get("playbook_config_bulk_pnp")
    playbook_config_wrong_serial_pnp = test_data.get("playbook_config_wrong_serial_pnp")
    playbook_config_invalid_site = test_data.get("playbook_config_invalid_site")

    def setUp(self):
        super(TestDnacPnpWorkflow, self).setUp()

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
        super(TestDnacPnpWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for PNP devices.
        """

        if "claim_ap_claimed_new" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail"),
                self.test_data.get("get_software_image_detail"),
                self.test_data.get("get_template_configuration"),
                self.test_data.get("get_device_by_id"),
                self.test_data.get("get_site_detail"),
                self.test_data.get("get_site_detail"),
                self.test_data.get("get_device_detail"),
                self.test_data.get("get_device_by_id"),
                self.test_data.get("get_device_by_id"),
                self.test_data.get("get_site_detail"),
                self.test_data.get("add_devices"),
                self.test_data.get("get_device_by_id"),
                self.test_data.get("device_claimed")
            ]
        elif "invalid_site_hierarchy" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_site"),
                self.test_data.get("get_software_image_detail_site"),
                self.test_data.get("get_template_configuration_site"),
                self.test_data.get("get_device_by_id_site"),
                self.test_data.get("get_site_detail_invalid")
            ]

        elif "claim_ap_claimed_old" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail"),
                self.test_data.get("get_software_image_detail"),
                self.test_data.get("get_template_configuration"),
                self.test_data.get("get_device_by_id"),
                self.test_data.get("get_site_detail"),
                self.test_data.get("get_site_detail_old"),
                self.test_data.get("get_device_detail"),
                self.test_data.get("get_device_by_id"),
                self.test_data.get("get_device_by_id"),
                self.test_data.get("get_site_detail_old"),
                self.test_data.get("add_devices"),
                self.test_data.get("get_device_by_id"),
                self.test_data.get("device_claimed")
            ]
        elif "device_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_delete"),
                self.test_data.get("get_device_detail_delete"),
                self.test_data.get("get_device_detail_delete"),
                self.test_data.get("get_device_detail_delete"),
            ]
        elif "claim_wlc_switch_vlan" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_wlc"),
                self.test_data.get("get_software_image_detail_sw"),
                self.test_data.get("get_template_configuration_sw"),
                self.test_data.get("get_device_by_id_wlc"),
                self.test_data.get("get_site_detail_sw"),
                self.test_data.get("get_device_detail_wlc"),
                self.test_data.get("get_device_detail_wlc"),
                self.test_data.get("get_device_by_id_wlc"),
                self.test_data.get("get_device_by_id_wlc"),
                self.test_data.get("get_device_by_id_wlc"),
                self.test_data.get("get_reset_response")
            ]
        elif "wlc_error" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_sw"),
                self.test_data.get("get_software_image_detail"),
                self.test_data.get("get_template_configuration_sw"),
                self.test_data.get("get_device_by_id_wlc"),
                self.test_data.get("get_site_detail_sw")
            ]
        elif "sw_err" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_sw"),
                self.test_data.get("get_software_image_detail_sw"),
                self.test_data.get("get_template_configuration_sw"),
                self.test_data.get("get_device_by_id_sw_err"),
                self.test_data.get("get_site_detail_sw")
            ]
        elif "import_devices_in_bulk_new" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_empty"),
                self.test_data.get("get_device_empty"),
                self.test_data.get("get_import_devices_in_bulk"),
                self.test_data.get("get_device_detail_bulk_authorize"),
                self.test_data.get("authorize_response")
            ]
        elif "devices_idempotent" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_exist1"),
                self.test_data.get("get_device_detail_exist2"),
                self.test_data.get("get_device_detail_exist1"),
                self.test_data.get("get_device_detail_exist2")
            ]
        elif "device_claim_idempotent" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_exist3"),
                self.test_data.get("get_device_detail_exist4"),
                self.test_data.get("get_device_detail_exist3"),
                self.test_data.get("get_device_detail_exist4")
            ]
        elif "site_error" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_sw_error"),
                self.test_data.get("get_software_image_detail_sw_error"),
                self.test_data.get("get_template_configuration_sw_error"),
                self.test_data.get("get_device_by_id_sw"),
                self.test_data.get("get_site_detail_building"),
                self.test_data.get("get_site_detail_building"),
                self.test_data.get("get_site_detail_building")
            ]
        elif "image_error" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_sw_error"),
                self.test_data.get("get_software_image_detail_sw_error"),
                self.test_data.get("get_template_configuration_sw_error"),
                self.test_data.get("get_device_by_id_sw"),
                self.test_data.get("get_site_detail_floor"),
                self.test_data.get("get_site_detail_floor")
            ]
        elif "temp_error" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_sw_error"),
                self.test_data.get("get_software_image_detail_sw"),
                self.test_data.get("get_template_configuration_sw_error"),
                self.test_data.get("get_device_by_id_sw"),
                self.test_data.get("get_site_detail_floor"),
                self.test_data.get("get_site_detail_floor")
            ]
        elif "device_reset" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_state_error"),
                self.test_data.get("get_software_image_detail_sw"),
                self.test_data.get("get_template_configuration_sw_error"),
                self.test_data.get("get_device_by_id_sw"),
                self.test_data.get("get_site_detail_floor"),
                self.test_data.get("get_device_state_error"),
                self.test_data.get("get_reset_response"),
                self.test_data.get("get_reset_response")
            ]
        elif "device_error_reset" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_state_error"),
                self.test_data.get("get_software_image_detail_sw"),
                self.test_data.get("get_template_configuration_sw_error"),
                self.test_data.get("get_device_by_id_sw"),
                self.test_data.get("get_site_detail_floor"),
                self.test_data.get("get_device_state_error"),
                self.test_data.get("get_reset_response"),
                self.test_data.get("get_reset_error_response")
            ]
        elif "device_input_error" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail")
            ]
        elif "wlc_check_param" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_sw"),
                self.test_data.get("get_software_image_detail"),
                self.test_data.get("get_template_configuration_sw"),
                self.test_data.get("get_device_by_id_wlc"),
                self.test_data.get("get_site_detail_sw"),
                self.test_data.get("get_device_detail_ewlc"),
                self.test_data.get("get_device_detail_ewlc"),
                self.test_data.get("get_reset_response"),
            ]

    def test_pnp_workflow_manager_invalid_site_hierarchy(self):
        """
        Test validation of invalid site hierarchy paths
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_invalid_site
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("adding the device to database", result.get('msg').lower())

    def test_pnp_workflow_manager_missing_required_fields(self):
        """
        Test validation of missing required fields
        """
        invalid_config = [
            {
                "device_info": [
                    {
                        "hostname": "test-device",
                        "pid": "C9300-24P"
                    }
                ]
            }
        ]
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=invalid_config
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("invalid parameters in playbook", result.get('msg').lower())

    def test_pnp_workflow_manager_invalid_device_type(self):
        """
        Test handling of invalid device types
        """
        invalid_config = [
            {
                "device_info": [
                    {
                        "serial_number": "TEST123",
                        "hostname": "test-device",
                        "pid": "INVALID-PID-TYPE"
                    }
                ]
            }
        ]
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=invalid_config
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("unable to import", result.get('msg').lower())

    def test_pnp_workflow_manager_version_2_3_5_3_features(self):
        """
        Test features available in version 2.3.5.3
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.5.3",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_switch
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Device Claim Failed", result.get('msg'))

    def test_pnp_workflow_manager_version_3_1_0_features(self):
        """
        Test enhanced features in version 3.1.0+
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.0.0",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_bulk_pnp
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Unable to import below 0 device(s).",
            result.get('msg')
        )

    def test_pnp_workflow_manager_claim_ap_claimed_new(self):
        """
        Test case for PNP workflow manager when add and claim switch device.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_accesspoint
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "Device is already claimed and Device 'KWC24160JLL' updated successfully."
        )

    def test_pnp_workflow_manager_claim_ap_claimed_old(self):
        """
        Test case for PNP workflow manager when add and claim switch device.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.5.3",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_accesspoint
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Device is already claimed and Device 'KWC24160JLL' updated successfully."
        )

    def test_pnp_workflow_manager_device_delete(self):
        """
        Test case for PNP workflow manager when add and claim switch device.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                config_verify=True,
                state="deleted",
                config=self.playbook_config_delete
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'), "Device(s) Not Found"
        )

    def test_pnp_workflow_manager_claim_wlc_switch_vlan(self):
        """
        Test case for PNP workflow manager when add and claim switch device.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_wlc_vlan
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "Please provide the Vlan ID to claim a wireless controller. This is a required field for the process " +
            "to create and set the specified port as trunk during PnP."
        )

    def test_pnp_workflow_manager_wlc_error(self):
        """
        Test case for PNP workflow manager when add and claim switch device.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_wlc_error
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "Successfully collected all project and template                     parameters from Cisco Catalyst Center for comparison"
        )

    def test_pnp_workflow_manager_sw_err(self):
        """
        Test case for PNP workflow manager when add and claim switch device.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_switch
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Successfully collected all project and template                     parameters from Cisco Catalyst Center for comparison"
        )

    def test_pnp_workflow_manager_import_devices_in_bulk_new(self):
        """
        Test case for PNP workflow manager when add bulk device.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="3.1.3.0",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_bulk_pnp
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "2 device(s) imported successfully 1 device(s) authorized successfully"
        )

    def test_pnp_workflow_manager_devices_idempotent(self):
        """
        Test case for PNP workflow manager when idempotent switch device.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_pnp
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "All specified devices already exist and cannot be imported again: ['FJC24501BK2', 'FJC24441MSV']."
        )

    def test_pnp_workflow_manager_device_claim_idempotent(self):
        """
        Test case for PNP workflow manager when idempotent switch device.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_pnp
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "All specified devices already exist and cannot be imported again: ['FJC24501BK2', 'FJC24441MSV']."
        )

    def test_pnp_workflow_manager_version_check(self):
        """
        Test case for PNP workflow manager when danc_version is old.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.5.2",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_pnp
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "The specified version '2.3.5.2' does not support the PNP workflow feature.Supported version(s) start from '2.3.5.3' onwards."
        )

    def test_pnp_workflow_manager_state_check(self):
        """
        Test case for PNP workflow manager when playbood state is updated device.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                config_verify=True,
                state="updated",
                config=self.playbook_config_pnp
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "value of state must be one of: merged, deleted, got: updated"
        )

    def test_pnp_workflow_manager_site_error(self):
        """
        Test case for PNP workflow manager when site name is not provided device.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_switch_site_issue
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Please ensure that the site type is specified as 'floor' when claiming an AP. The site type is " +
            "given as 'building'. Please change the 'site_type' into 'floor' to proceed."
        )

    def test_pnp_workflow_manager_image_error(self):
        """
        Test case for PNP workflow manager when site name is not provided device.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_switch_site_issue
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "The image 'cat9k_iosxe.17.15.01.SPA.bin' is either not present or not tagged as 'Golden' " +
            "in the Cisco Catalyst Center. Please verify its existence and its tag status."
        )

    def test_pnp_workflow_manager_temp_error(self):
        """
        Test case for PNP workflow manager when site name is not provided device.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_switch_site_issue
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Either project not found or it is Empty."
        )

    def test_pnp_workflow_manager_device_reset(self):
        """
        Test case for PNP workflow manager when site name is not provided device.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_reset_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "All specified devices already exist and cannot be imported again: ['FJC24501BK2']. " +
            "Devices reset done (['FJC24501BK2'])"
        )

    def test_pnp_workflow_manager_device_error_reset(self):
        """
        Test case for PNP workflow manager when site name is not provided device.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_reset_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertEqual(
            result.get('msg'),
            "All specified devices already exist and cannot be imported again: " +
            "['FJC24501BK2']. Devices reset done (['FJC24501BK2'])"
        )

    def test_pnp_workflow_manager_device_input_error(self):
        """
        Test case for PNP workflow manager when Serial Number and Pid are invalid.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_wrong_serial_pnp
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertIn(
            "Invalid parameters", result.get('msg')
        )

    def test_pnp_workflow_manager_wlc_check_params(self):
        """
        Test case for PNP workflow manager when add and claim switch device.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_config_wlc_error
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertIn(
            "Successfully collected all project and template",
            result.get('msg')
        )
