# Copyright (c) 2024 Cisco and/or its affiliates.

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

from ansible_collections.cisco.dnac.plugins.modules import inventory_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacInventoryWorkflow(TestDnacModule):

    module = inventory_workflow_manager

    test_data = loadPlaybookData("inventory_workflow_manager")

    playbook_add_device = test_data.get("playbook_add_device")
    playbook_delete_a_device = test_data.get("playbook_delete_a_device")
    playbook_add_existing_devices = test_data.get("playbook_add_existing_devices")
    playbook_add_udf = test_data.get("playbook_add_udf")
    playbook_provision_failed_for_site = test_data.get("playbook_provision_failed_for_site")
    playbook_delete_provisioned_device = test_data.get("playbook_delete_provisioned_device")
    playbook_update_interface_details = test_data.get("playbook_update_interface_details")
    playbook_update_role = test_data.get("playbook_update_role")
    playbook_delete_device_udf = test_data.get("playbook_delete_device_udf")
    playbook_missing_mand_params = test_data.get("playbook_missing_mand_params")
    playbook_update_mgmt_ip = test_data.get("playbook_update_mgmt_ip")
    playbook_provision_device = test_data.get("playbook_provision_device")
    playbook_del_provisioned_device_2353 = test_data.get("playbook_del_provisioned_device_2353")
    playbook_prov_device_2353 = test_data.get("playbook_prov_device_2353")

    def setUp(self):
        super(TestDnacInventoryWorkflow, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacInventoryWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "playbook_add_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list_add_device"),
                self.test_data.get("get_device_list_add_device_2"),
                self.test_data.get("add_device_add_device"),
                self.test_data.get("TaskDetails_add_device_start"),
                self.test_data.get("TaskDetails_add_device_end"),
                self.test_data.get("get_device_list_add_device_3"),
                self.test_data.get("get_device_list_add_device_5"),
                self.test_data.get("add_device_response"), ]
        elif "playbook_delete_a_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list1_seema"),
                self.test_data.get("get_device_list2_seema"),
                self.test_data.get("get_device_list3_seema"),
                self.test_data.get("get_provisioned_devices1_seema"),
                self.test_data.get("get_device_list4_seema"),
                self.test_data.get("deleted_device_by_id1_seema"),
                self.test_data.get("Task_Details1_seema"),
                self.test_data.get("Task_Details2_seema"),
                self.test_data.get("get_device_list5_seema"),
                self.test_data.get("get_device_list6_seema"),
                self.test_data.get("delete_device_response1_seema"),]
        elif "playbook_add_existing_devices" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list1_existing_devices"),
                self.test_data.get("get_device_list2_existing_devices"),
                self.test_data.get("get_device_list3_existing_devices"),
                self.test_data.get("get_device_list4_existing_devices"),
                self.test_data.get("add_existing_devices_response"),]
        elif "playbook_add_udf" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list1_add_udf"),
                self.test_data.get("get_device_list2_add_udf"),
                self.test_data.get("get_all_user_defined_fields"),
                self.test_data.get("create_user_defined_field"),
                self.test_data.get("get_device_list3_add_udf"),
                self.test_data.get("get_device_list4_add_udf"),
                self.test_data.get("add_user_defined_field_to_device1"),
                self.test_data.get("add_user_defined_field_to_device2"),
                self.test_data.get("get_device_list5_add_udf"),
                self.test_data.get("get_device_list6_add_udf"),
                self.test_data.get("get_all_user_defined_fields2"),
                self.test_data.get("add_udf_response"),]
        elif "playbook_provision_failed_for_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list1_provision_failed_for_site"),
                self.test_data.get("get_device_list2_provision_failed_for_site"),
                self.test_data.get("povisioning_failed_response"),]
        elif "playbook_delete_provisioned_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list1_delete_provisioned_device"),
                self.test_data.get("get_device_list2_delete_provisioned_device"),
                self.test_data.get("get_device_list3_delete_provisioned_device"),
                self.test_data.get("get_provisioned_devices_delete_provisioned_device"),
                self.test_data.get("delete_provisioned_devices"),
                self.test_data.get("Task_Details1_delete_provisioned_device"),
                self.test_data.get("Task_Details2_delete_provisioned_device"),
                self.test_data.get("get_device_list4_delete_provisioned_device"),
                self.test_data.get("get_device_list5_delete_provisioned_device"),
                self.test_data.get("delete_provisioned_response"),]
        elif "playbook_update_interface_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list1_update_interface"),
                self.test_data.get("get_device_list2_update_interface"),
                self.test_data.get("get_device_list3_update_interface"),
                self.test_data.get("get_interface_details1_update_interface"),
                self.test_data.get("get_device_list4_update_interface"),
                self.test_data.get("update_interface_details"),
                self.test_data.get("Task_Details1_update_interface"),
                self.test_data.get("Task_Details2_update_interface"),
                self.test_data.get("get_device_list5_update_interface"),
                self.test_data.get("get_device_list6_update_interface"),
                self.test_data.get("get_device_list7_update_interface"),
                self.test_data.get("get_interface_details2_update_interface"),
                self.test_data.get("update_interface_details_response"),]
        elif "playbook_update_role" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list1_update_role"),
                self.test_data.get("get_device_list2_update_role"),
                self.test_data.get("get_device_list3_update_role"),
                self.test_data.get("get_device_list4_update_role"),
                self.test_data.get("update_device_role"),
                self.test_data.get("Task_Details_update_role"),
                self.test_data.get("get_device_list5_update_role"),
                self.test_data.get("get_device_list6_update_role"),
                self.test_data.get("get_device_list7_update_role"),
                self.test_data.get("update_role_response"),]
        elif "playbook_missing_mand_params" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list1_missing_mand_params"),
                self.test_data.get("get_device_list2_missing_mand_params"),
                self.test_data.get("response_missing_uname_pwd_in_adding_device"),]
        elif "playbook_delete_device_udf" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list1_delete_device_udf"),
                self.test_data.get("get_device_list2_delete_device_udf"),
                self.test_data.get("get_device_list3_delete_device_udf"),
                self.test_data.get("get_provisioned_devices_delete_device_udf"),
                self.test_data.get("get_device_list4_delete_device_udf"),
                self.test_data.get("deleted_device_by_id_delete_device_udf"),
                self.test_data.get("Task_Details1_delete_device_udf"),
                self.test_data.get("Task_Details2_delete_device_udf"),
                self.test_data.get("get_device_list5_delete_device_udf"),
                self.test_data.get("get_device_list6_delete_device_udf"),
                self.test_data.get("delete_device_udf_response"),]
        elif "playbook_update_mgmt_ip" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list1_update_mgmt_ip"),
                self.test_data.get("get_device_list2_update_mgmt_ip"),
                self.test_data.get("get_device_list3_update_mgmt_ip"),
                self.test_data.get("get_device_list4_update_mgmt_ip"),
                self.test_data.get("export_device_list_update_mgmt_ip"),
                self.test_data.get("Task_Details2_update_mgmt_ip"),
                self.test_data.get("download_a_file_by_fileid_update_mgmt_ip"),
                self.test_data.get("sync_devices_update_mgmt_ip"),
                self.test_data.get("Task_Details3_update_mgmt_ip"),
                self.test_data.get("get_device_list5_update_mgmt_ip"),
                self.test_data.get("get_device_list6_update_mgmt_ip"),
                self.test_data.get("get_device_list7_update_mgmt_ip"),
                self.test_data.get("export_device_list2_update_mgmt_ip"),
                self.test_data.get("Task_Details3_update_mgmt_ip"),
                self.test_data.get("Task_Details4_update_mgmt_ip"),
                self.test_data.get("download_a_file_by_fileid2_update_mgmt_ip"),
                self.test_data.get("response_update_mgmt_ipaddress"),]
        elif "playbook_provision_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list1_provision_device"),
                self.test_data.get("get_device_list2_provision_device"),
                self.test_data.get("get_sites1_provision_device"),
                self.test_data.get("get_sites2_provision_device"),
                self.test_data.get("get_device_list3_provision_device"),
                self.test_data.get("get_sites3_provision_device"),
                self.test_data.get("get_sites4_provision_device"),
                self.test_data.get("get_device_list4_provision_device"),
                self.test_data.get("get_provisioned_devices1_provision_device"),
                self.test_data.get("assign_network_devices_to_a_site_provision_device"),
                self.test_data.get("Task_Details1_provision_device"),
                self.test_data.get("provision_devices"),
                self.test_data.get("Task_Details2_provision_device"),
                self.test_data.get("Task_Details3_provision_device"),
                self.test_data.get("get_device_list5_provision_device"),
                self.test_data.get("get_device_list6_provision_device"),
                self.test_data.get("get_device_list7_provision_device"),
                self.test_data.get("get_provision_devices2_provision_device"),
                self.test_data.get("provisioned_success_response"),]
        elif "playbook_del_provisioned_device_2353" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list1_del_prov_dev2353"),
                self.test_data.get("get_device_list2_del_prov_dev2353"),
                self.test_data.get("get_provisioned_wired_device_del_prov_dev2353"),
                self.test_data.get("delete_provisioned_wired_device_del_prov_dev2353"),
                self.test_data.get("get_execution_details_device_del_prov_dev2353"),
                self.test_data.get("get_device_list3_del_prov_dev2353"),
                self.test_data.get("get_device_list4_del_prov_dev2353"),
                self.test_data.get("response_del_provisioned_device_2353"),]
        elif "playbook_prov_device_2353" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_device_list1_prov_device_2353"),
                self.test_data.get("get_device_list2_prov_device_2353"),
                self.test_data.get("get_site1_prov_device_2353"),
                self.test_data.get("get_device_list3_prov_device_2353"),
                self.test_data.get("provision_wired_device_prov_device_2353"),
                self.test_data.get("Task_Details_prov_device_2353"),
                self.test_data.get("get_device_list4_prov_device_2353"),
                self.test_data.get("get_device_list5_prov_device_2353"),
                self.test_data.get("get_provisioned_wired_devices_prov_device_2353"),
                self.test_data.get("prov_device_2353_response"),]

    def test_inventory_workflow_manager_playbook_add_device(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_add_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "device(s) '60.1.1.1', '50.1.1.1' added successfully in Cisco Catalyst Center."
        )

    def test_inventory_workflow_manager_playbook_add_existing_devices(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_version="2.3.5.3",
                state="merged",
                config_verify=True,
                config=self.playbook_add_existing_devices
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "device(s) '70.2.2.2', '80.2.2.2' already present in Cisco Catalyst Center."
        )

    def test_inventory_workflow_manager_playbook_add_udf(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_add_udf
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "device(s) '70.2.2.2', '80.2.2.2' already present in Cisco Catalyst Center."
        )

    def test_inventory_workflow_manager_playbook_delete_a_device(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_version="2.3.7.6",
                state="deleted",
                config_verify=True,
                config=self.playbook_delete_a_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "device(s) '1.1.1.1' successfully deleted in Cisco Catalyst Center"
        )

    def test_inventory_workflow_manager_playbook_delete_provisioned_device(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_version="2.3.7.6",
                state="deleted",
                config_verify=True,
                config=self.playbook_delete_provisioned_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "provisioned device(s) '204.1.2.4' successfully deleted in Cisco Catalyst Center."
        )

    def test_inventory_workflow_manager_playbook_provision_failed_for_site(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_provision_failed_for_site
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Wired Device Provisioning failed for all devices"
        )

    def test_inventory_workflow_manager_playbook_update_interface_details(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_version="2.3.7.6",
                state="merged",
                config_verify=True,
                config=self.playbook_update_interface_details
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Successfully updated the Interface Details for device '204.1.2.4'."
        )

    def test_inventory_workflow_manager_playbook_update_role(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_version="2.3.7.6",
                state="merged",
                config_verify=True,
                config=self.playbook_update_role
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Device(s) '['2.2.2.2']' role updated successfully to '['ACCESS']'"
        )

    def test_inventory_workflow_manager_playbook_missing_mand_params(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_version="2.3.7.6",
                state="merged",
                config_verify=True,
                config=self.playbook_missing_mand_params
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Required parameters ['password', 'username'] for adding devices '['70.2.2.2', '80.2.2.2']' are not present"
        )

    def test_inventory_workflow_manager_playbook_delete_device_udf(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_version="2.3.7.6",
                state="deleted",
                config_verify=True,
                config=self.playbook_delete_device_udf
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "device(s) '70.2.2.2' successfully deleted in Cisco Catalyst Center"
        )

    def test_inventory_workflow_manager_playbook_update_mgmt_ip(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_version="2.3.7.6",
                state="merged",
                config_verify=True,
                config=self.playbook_update_mgmt_ip
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Device '1.1.1.1' present in Cisco Catalyst Center and new management ip '12.12.12.12' have been updated successfully "
        )

    def test_inventory_workflow_manager_playbook_provision_device(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_version="2.3.7.6",
                state="merged",
                config_verify=True,
                config=self.playbook_provision_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "device(s) '204.1.2.4' provisioned successfully in Cisco Catalyst Center."
        )

    def test_inventory_workflow_manager_playbook_del_provisioned_device_2353(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_version="2.3.5.3",
                state="deleted",
                config_verify=True,
                config=self.playbook_del_provisioned_device_2353
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "provisioned device(s) '204.1.2.4' successfully deleted in Cisco Catalyst Center. "
        )

    def test_inventory_workflow_manager_playbook_prov_device_2353(self):
        """
        Test case for add device with full crendentials.

        This test case checks the addition of new network device added with full credentials in Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_version="2.3.5.3",
                state="merged",
                config_verify=True,
                config=self.playbook_prov_device_2353
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "device(s) '204.1.2.4' provisioned successfully in Cisco Catalyst Center. "
        )
