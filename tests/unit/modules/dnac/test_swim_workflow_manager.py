# Copyright (c) 2024 Cisco and/or its affiliates.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function
__metaclass__ = type

from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import swim_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestswimWorkflowManager(TestDnacModule):

    module = swim_workflow_manager
    test_data = loadPlaybookData("swim_workflow_manager")

    playbook_config_invalid_param_import_image_url_tag_golden_load = test_data.get("playbook_config_invalid_param_import_image_url_tag_golden_load")
    playbook_untag_image_as_golden_and_load_on_device = test_data.get("playbook_untag_image_as_golden_and_load_on_device")
    playbook_import_image_already_exist = test_data.get("playbook_import_image_already_exist")
    playbook_site_not_exist = test_data.get("playbook_site_not_exist")
    playbook_swim_image_invalid = test_data.get("playbook_swim_image_invalid")
    playbook_image_distribution_failed = test_data.get("playbook_image_distribution_failed")
    playbook_image_distribution_partially_successfull = test_data.get("playbook_image_distribution_partially_successfull")
    playbook_swim_image_golden_already_tagged = test_data.get("playbook_swim_image_golden_already_tagged")
    playbook_swim_image_golden_already_untagged = test_data.get("playbook_swim_image_golden_already_untagged")
    playbook_swim_image_cant_found = test_data.get("playbook_swim_image_cant_found")
    playbook_distribution_failed_for_all_devices = test_data.get("playbook_distribution_failed_for_all_devices")
    playbook_image_details_distribution_not_provided = test_data.get("playbook_image_details_distribution_not_provided")
    playbook_device_family_not_found = test_data.get("playbook_device_family_not_found")
    playbook_import_image_details_not_provided = test_data.get("playbook_import_image_details_not_provided")
    playbook_verify_merged = test_data.get("playbook_verify_merged")

    def setUp(self):
        super(TestswimWorkflowManager, self).setUp()
        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__"
        )
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]

        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestswimWorkflowManager, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "playbook_config_invalid_param_import_image_url_tag_golden_load" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details"),
                self.test_data.get("import_software_image_via_url"),
                self.test_data.get("Task_details_inprogress_1"),
                self.test_data.get("task_details"),
                self.test_data.get("get_software_image_1_details"),
                self.test_data.get("get_software_image_1_details"),
                self.test_data.get("get_site"),
                self.test_data.get("get_device_family_identifiers"),
                self.test_data.get("get_software_image_1_details"),
                self.test_data.get("get_device_list"),
                self.test_data.get("get_software_image_1_details"),
                self.test_data.get("get_device_list"),
                self.test_data.get("get_software_image_1_details"),
                self.test_data.get("get_golden_tag_status_of_an_image"),
                self.test_data.get("tag_as_golden_image"),
                self.test_data.get("Task_details_inprogress_2"),
                self.test_data.get("task_1_details"),
                self.test_data.get("get_1_site"),
                self.test_data.get("get_membership"),
                self.test_data.get("trigger_software_image_distribution"),
                self.test_data.get("Task_details_inprogress_3"),
                self.test_data.get("task_2_details"),
                self.test_data.get("get_1_site"),
                self.test_data.get("get_1_membership"),
                self.test_data.get("trigger_software_image_activation"),
                self.test_data.get("Task_details_inprogress_4"),
                self.test_data.get("task_4_details"),
                self.test_data.get("playbook_config_invalid_param_import_image_url_tag_golden_load_response")
            ]
        elif "playbook_untag_image_as_golden_and_load_on_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_2_software_image_details"),
                self.test_data.get("get_2_site"),
                self.test_data.get("get_2_device_family_identifiers"),
                self.test_data.get("get_software_image_details_1"),
                self.test_data.get("get_2_golden_tag_status_of_an_image"),
                self.test_data.get("remove_golden_tag_for_image"),
                self.test_data.get("Task_details"),
                self.test_data.get("get_software_image_details_2"),
                self.test_data.get("get_site_1"),
                self.test_data.get("get_device_family_identifiers_1"),
                self.test_data.get("get_software_image_details_3"),
                self.test_data.get("get_golden_tag_status_of_an_image_1"),
                self.test_data.get("untag_image_as_golden_and_load_on_device_responce")
            ]

        elif "playbook_import_image_already_exist" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_already_tagged"),
                self.test_data.get("get_software_image_details_already_tagged_1"),
                self.test_data.get("get_image_details"),
                self.test_data.get("get_image_details"),
                self.test_data.get("get_software_image_details_already_tagged_2"),
                self.test_data.get("import_image_already_exist_response"),
            ]

        elif "playbook_site_not_exist" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_site_not_exist"),
                self.test_data.get("get_software_image_details_site_not_exist_1"),
                self.test_data.get("get_software_image_details_site_not_exist_2"),
                Exception(),
                self.test_data.get("site_not_exist_response"),
            ]
        elif "playbook_swim_image_invalid" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_invalid_swim_image"),
                self.test_data.get("import_software_image_via_url_invalid_swim_image"),
                self.test_data.get("Task_details_invalid_swim_image"),
                self.test_data.get("Task_details_invalid_swim_image_end"),
                self.test_data.get("invalid_swim_image_response"),
            ]
        elif "playbook_image_distribution_failed" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_image_distribution_failed"),
                self.test_data.get("get_device_list_image_distribution_failed"),
                self.test_data.get("get_site_image_distribution_failed"),
                self.test_data.get("get_membership_image_distribution_failed"),
                self.test_data.get("trigger_software_image_distribution_image_distribution_failed"),
                self.test_data.get("task_details_running_image_distribution_failed"),
                self.test_data.get("task_details_image_distribution_failed"),
                self.test_data.get("image_distribution_failed_response"),
            ]
        elif "playbook_image_distribution_partially_successfull" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_ps"),
                self.test_data.get("get_device_list_ps"),
                self.test_data.get("get_site_ps"),
                self.test_data.get("get_membership_ps"),
                self.test_data.get("get_device_uuids"),
                self.test_data.get("get_device_uuids_1"),
                self.test_data.get("get_device_list_ps_1"),
                self.test_data.get("trigger_software_image_distribution_ps"),
                self.test_data.get("get_device_list_ps_2"),
                self.test_data.get("trigger_software_image_distribution_ps_1"),
                self.test_data.get("get_device_list_ps_3"),
                self.test_data.get("trigger_software_image_distribution_ps_2"),
                self.test_data.get("get_device_list_ps_4"),
                self.test_data.get("trigger_software_image_distribution_ps_3"),
                self.test_data.get("get_device_list_ps_5"),
                self.test_data.get("trigger_software_image_distribution_ps_4"),
                self.test_data.get("task_details_ps1"),
                self.test_data.get("task_details_ps2"),
                self.test_data.get("task_details_ps3"),
                self.test_data.get("task_details_ps4"),
                self.test_data.get("task_details_ps5"),
                self.test_data.get("task_details_ps6"),
                self.test_data.get("get_software_image_details_ps_1"),
                self.test_data.get("get_device_list_ps_6"),
                self.test_data.get("get_software_image_details_ps_2"),
                self.test_data.get("image_distribution_partially_successfull"),
            ]
        elif "playbook_swim_image_golden_already_tagged" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_golden_already_tagged"),
                self.test_data.get("get_software_image_details_golden_already_tagged_1"),
                self.test_data.get("get_software_image_details_golden_already_tagged_2"),
                self.test_data.get("get_device_family_identifiers_golden_already_tagged"),
                self.test_data.get("get_software_image_details_golden_already_tagged_3"),
                self.test_data.get("get_golden_tag_status_of_an_image_golden_already_tagged"),
                self.test_data.get("get_software_image_details_golden_already_tagged_4"),
                self.test_data.get("get_device_family_identifiers_golden_already_tagged_1"),
                self.test_data.get("get_software_image_details_golden_already_tagged_5"),
                self.test_data.get("get_software_image_details_golden_already_tagged_6"),
                self.test_data.get("get_golden_tag_status_of_an_image_golden_already_tagged_2"),
                self.test_data.get("image_golden_already_tagged_response"),
            ]
        elif "playbook_swim_image_golden_already_untagged" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_golden_already_tagged"),
                self.test_data.get("get_software_image_details_golden_already_tagged_1"),
                self.test_data.get("get_software_image_details_golden_already_tagged_2"),
                self.test_data.get("get_device_family_identifiers_golden_already_tagged"),
                self.test_data.get("get_software_image_details_golden_already_tagged_3"),
                self.test_data.get("get_golden_tag_status_of_an_image_golden_already_untagged"),
                self.test_data.get("get_software_image_details_golden_already_tagged_4"),
                self.test_data.get("get_device_family_identifiers_golden_already_tagged_1"),
                self.test_data.get("get_software_image_details_golden_already_tagged_5"),
                self.test_data.get("get_software_image_details_golden_already_tagged_6"),
                self.test_data.get("get_golden_tag_status_of_an_image_golden_already_untagged_1"),
                self.test_data.get("image_golden_already_untagged_response"),
            ]
        elif "playbook_swim_image_cant_found" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_swim_image_cant_found"),
                self.test_data.get("swim_image_cant_found_response"),
            ]
        elif "playbook_distribution_failed_for_all_devices" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_failed_for_all_devices"),
                self.test_data.get("get_software_image_details_failed_for_all_devices"),
                self.test_data.get("get_device_list_failed_for_all_devices"),
                self.test_data.get("get_site_failed_for_all_devices_1"),
                self.test_data.get("get_membership_failed_for_all_devices"),
                self.test_data.get("get_device_list_failed_for_all_devices_1"),
                self.test_data.get("distribution_params"),
                self.test_data.get("trigger_software_image_distribution_failed_for_all_devices"),
                self.test_data.get("Task_details_failed_for_all_devices"),
                self.test_data.get("distribution_failed_for_all_devices_response"),
            ]
        elif "playbook_image_details_distribution_not_provided" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_image_details_distribution_not_provided"),
                self.test_data.get("distribution_failed_for_all_devicesresponse"),
            ]
        elif "playbook_device_family_not_found" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_device_family_not_found"),
                self.test_data.get("get_site_device_family_not_found"),
                self.test_data.get("get_device_family_identifiers_device_family_not_found"),
                self.test_data.get("device_family_not_found_response"),
            ]
        elif "playbook_import_image_details_not_provided" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("import_image_details_not_provided_response"),]

    def test_swim_workflow_manager_playbook_config_invalid_param_import_image_url_tag_golden_load(self):
        """
        Test case for swim workflow manager when giving invalid param import image url tag golden load
        This test case checks the behavior of the swim workflow when giving invalid param in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_invalid_param_import_image_url_tag_golden_load
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("msg"),
            "Activation for Image with Id '4a3cccfa-dc92-4fad-a7d3-c59876cbebe6' gets failed"
        )

    def test_swim_workflow_manager_playbook_untag_image_as_golden_and_load_on_device(self):
        """
        Test case for swim workflow manager when giving untag image as golden and load on device
        This test case checks the behavior of the swim workflow when giving untag image as golden and load on device
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_untag_image_as_golden_and_load_on_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Untagging of image  cat9k_iosxe.17.12.02.SPA.bin for site  LTTS for family Cisco \
Catalyst 9000 UADP 8 Port Virtual Switch  for device deviceTag ALL successful."
        )

    def test_swim_workflow_manager_playbook_import_image_already_exist(self):
        """
        Test case for swim workflow manager when giving import image already exist
        This test case checks the behavior of the swim workflow when giving import image already exist
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_import_image_already_exist
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Image 'cat9k_iosxe.17.12.02.SPA.bin' already exists in the Cisco Catalyst Center"
        )

    def test_swim_workflow_manager_playbook_site_not_exist(self):
        """
        Test case for swim workflow manager when giving site not exist
        This test case checks the behavior of the swim workflow when giving site not exist
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_site_not_exist
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "An exception occurred: Site 'Global/LTTS/FLOOR2' does not exist in the Cisco Catalyst Center"
        )

    def test_swim_workflow_manager_playbook_swim_image_invalid(self):
        """
        Test case for swim workflow manager when giving swim image invalid
        This test case checks the behavior of the swim workflow when giving swim image invalid
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_swim_image_invalid
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "SWIM Image http://172.21.236.183/swim/V1712_2_CCO/cat9k_iosxe.17.12.02.SPA.bin seems to be invalid"
        )

    def test_swim_workflow_manager_playbook_image_distribution_failed(self):
        """
        Test case for swim workflow manager when giving image distribution failed
        This test case checks the behavior of the swim workflow when giving image distribution failed
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_image_distribution_failed
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Image with Id c383ee35-d20e-49f2-b51c-bfe499abbbaa Distribution Failed"
        )

    def test_swim_workflow_manager_playbook_image_distribution_partially_successfull(self):
        """
        Test case for swim workflow manager when giving image distribution partially successfull
        This test case checks the behavior of the swim workflow when giving image distribution partially successfull
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_image_distribution_partially_successfull
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Image with Id 'c383ee35-d20e-49f2-b51c-bfe499abbbaa' Distributed and partially successfull"
        )

    def test_swim_workflow_manager_playbook_swim_image_golden_already_tagged(self):
        """
        Test case for swim workflow manager when givingswim image golden already tagged
        This test case checks the behavior of the swim workflow when giving swim image golden already tagged
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_swim_image_golden_already_tagged
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('msg'),
            "SWIM Image 'cat9k_iosxe.17.12.02.SPA.bin' already tagged as Golden image in Cisco Catalyst Center"
        )

    def test_swim_workflow_manager_playbook_swim_image_golden_already_untagged(self):
        """
        Test case for swim workflow manager when giving swim image golden already untagged
        This test case checks the behavior of the swim workflow when giving swim image golden already untagged
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_swim_image_golden_already_untagged
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('msg'),
            "SWIM Image 'cat9k_iosxe.17.12.02.SPA.bin' already un-tagged from Golden image in Cisco Catalyst Center"
        )

    def test_swim_workflow_manager_playbook_swim_image_cant_found(self):
        """
        Test case for swim workflow manager when giving swim image cant found
        This test case checks the behavior of the swim workflow when giving swim image cant found
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_swim_image_cant_found
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "SWIM image 'cat9k_iosxe.17.12.022.SPA.bin' could not be found"
        )

    def test_swim_workflow_manager_playbook_distribution_failed_for_all_devices(self):
        """
        Test case for swim workflow manager when giving distribution failed for all devices
        This test case checks the behavior of the swim workflow when giving distribution failed for all devices
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_distribution_failed_for_all_devices
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Image with Id c383ee35-d20e-49f2-b51c-bfe499abbbaa Distribution Failed for all devices"
        )

    def test_swim_workflow_manager_playbook_image_details_distribution_not_provided(self):
        """
        Test case for swim workflow manager when giving image details distribution not provided
        This test case checks the behavior of the swim workflow when giving image details distribution not provided
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_image_details_distribution_not_provided
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Image details required for distribution have not been provided"
        )

    def test_swim_workflow_manager_playbook_device_family_not_found(self):
        """
        Test case for swim workflow manager when giving device family not found
        This test case checks the behavior of the swim workflow when giving device family not found
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_device_family_not_found
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Device Family: None not found"
        )

    def test_swim_workflow_manager_playbook_import_image_details_not_provided(self):
        """
        Test case for swim workflow manager when giving import image details not provided
        This test case checks the behavior of the swim workflow when giving import image details not provided
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_import_image_details_not_provided
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Error: Import image details are not provided in the playbook, or the Import Image API was not\n                 triggered successfully.\
 Please ensure the necessary details are provided and verify the status of the Import Image process."
        )
