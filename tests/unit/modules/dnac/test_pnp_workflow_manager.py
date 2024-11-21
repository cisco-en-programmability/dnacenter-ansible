# Copyright (c) 2024 Cisco and/or its affiliates.
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
                self.test_data.get("get_site_detail"),
                self.test_data.get("add_devices"),
                self.test_data.get("get_device_by_id"),
                self.test_data.get("get_device_by_id"),
            ]
        elif "claim_ap_claimed_old" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail"),
                self.test_data.get("get_software_image_detail"),
                self.test_data.get("get_template_configuration"),
                self.test_data.get("get_device_by_id"),
                self.test_data.get("get_site_detail_old"),
                self.test_data.get("get_site_detail_old"),
                self.test_data.get("get_site_detail_old"),
                self.test_data.get("add_devices"),
                self.test_data.get("get_device_by_id"),
                self.test_data.get("device_claimed"),
                self.test_data.get("device_claimed"),
                self.test_data.get("get_device_by_id"),
            ]
        elif "claim_switch" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_detail_sw"),
                self.test_data.get("get_software_image_detail_sw"),
                self.test_data.get("get_template_configuration_sw"),
                self.test_data.get("get_device_by_id_sw"),
                self.test_data.get("get_site_detail_sw"),
                self.test_data.get("get_site_detail_sw"),
                self.test_data.get("get_site_detail_sw"),
                self.test_data.get("get_device_by_id_sw"),
                self.test_data.get("get_site_detail_sw"),
                self.test_data.get("device_claimed"),
            ]
        elif "device_delete" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_delete"),
                self.test_data.get("get_device_detail_delete"),
                self.test_data.get("get_device_detail_delete"),
                self.test_data.get("get_device_detail_delete"),
            ]
        elif "claim_switch_wlc_vlan" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_wlc")
            ]
        elif "wlc_error" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_sw"),
                self.test_data.get("get_software_image_detail"),
                self.test_data.get("get_template_configuration_sw"),
                self.test_data.get("get_device_by_id_wlc"),
                self.test_data.get("get_site_detail_sw"),
                self.test_data.get("get_device_by_id_wlc"),
                self.test_data.get("get_device_by_id_wlc"),
                self.test_data.get("get_device_by_id_wlc"),
                self.test_data.get("device_claim_site"),
                self.test_data.get("device_claimed"),
            ]
        elif "sw_err" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_detail_sw"),
                self.test_data.get("get_software_image_detail_sw"),
                self.test_data.get("get_template_configuration_sw"),
                self.test_data.get("get_device_by_id_sw_err"),
                self.test_data.get("get_site_detail_sw")
            ]

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
                config=self.playbook_config_accesspoint
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Device is already claimed"
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
            "Only Device Claimed Successfully"
        )

    def test_pnp_workflow_manager_claim_switch(self):
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
            "Device Claim Failed"
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

    def test_pnp_workflow_manager_claim_switch_wlc_vlan(self):
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
