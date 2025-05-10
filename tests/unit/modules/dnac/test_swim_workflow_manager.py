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

    playbook_untag_image_as_golden_and_load_on_device = test_data.get("playbook_untag_image_as_golden_and_load_on_device")
    playbook_import_image_already_exist = test_data.get("playbook_import_image_already_exist")
    playbook_swim_image_golden_already_tagged = test_data.get("playbook_swim_image_golden_already_tagged")
    playbook_swim_image_cant_found = test_data.get("playbook_swim_image_cant_found")
    playbook_image_details_distribution_not_provided = test_data.get("playbook_image_details_distribution_not_provided")
    playbook_device_family_not_found = test_data.get("playbook_device_family_not_found")
    playbook_swim_image_golden_tag = test_data.get("playbook_swim_image_golden_tag")
    playbook_inheritted_tag_cannot_be_untagged = test_data.get("playbook_inheritted_tag_cannot_be_untagged")
    playbook_image_activation = test_data.get("playbook_image_activation")
    playbook_import_image = test_data.get("playbook_import_image")
    playbook_multiple_image_distribution_1 = test_data.get("playbook_multiple_image_distribution_1")

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
        if "playbook_untag_image_as_golden_and_load_on_device" in self._testMethodName:
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
                self.test_data.get("untag_image_as_golden_and_load_on_device_response")
            ]

        elif "playbook_import_image_already_exist" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details"),
                self.test_data.get("get_software_image_details_4"),
                self.test_data.get("import_image_already_exist_response"),
            ]

        elif "playbook_swim_image_golden_tag" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_swim_image_golden_tag"),
                self.test_data.get("get_device_family_identifiers_swim_image_golden_tag"),
                self.test_data.get("get_software_image_details_swim_image_golden_tag_1"),
                self.test_data.get("get_golden_tag_status_of_an_image_swim_image_golden_tag"),
                self.test_data.get("tag_as_golden_image_swim_image_golden_tag"),
                self.test_data.get("TaskDetails_start"),
                self.test_data.get("TaskDetails_end"),
                self.test_data.get("get_software_image_details_swim_image_golden_tag_2"),
                self.test_data.get("get_device_family_identifiers_swim_image_golden_tag_1"),
                self.test_data.get("get_software_image_details_swim_image_golden_tag_3"),
                self.test_data.get("get_golden_tag_status_of_an_image_swim_image_golden_tag_1"),
                self.test_data.get("import__swim_image_golden_tag_response"),
            ]

        elif "playbook_swim_image_golden_already_tagged" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_8"),
                self.test_data.get("get_site"),
                self.test_data.get("get_device_family_identifiers"),
                self.test_data.get("get_software_image_details_5"),
                self.test_data.get("get_golden_tag_status_of_an_image"),
                self.test_data.get("get_software_image_details_6"),
                self.test_data.get("get_site_2"),
                self.test_data.get("get_device_family_identifiers_2"),
                self.test_data.get("get_software_image_details_7"),
                self.test_data.get("get_golden_tag_status_of_an_image_2"),
                self.test_data.get("swim_image_golden_already_tagged_response"),
            ]

        elif "playbook_swim_image_cant_found" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_swim_image_cant_found"),
                self.test_data.get("swim_image_cant_found_response"),
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

        elif "playbook_inheritted_tag_cannot_be_untagged" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_playbook_inheritted_tag_cannot_be_untagged"),
                self.test_data.get("get_site_playbook_inheritted_tag_cannot_be_untagged"),
                self.test_data.get("get_device_family_identifiers_playbook_inheritted_tag_cannot_be_untagged"),
                self.test_data.get("get_software_image_details_playbook_inheritted_tag_cannot_be_untagged_1"),
                self.test_data.get("get_golden_tag_status_of_an_image_playbook_inheritted_tag_cannot_be_untagged"),
                self.test_data.get("remove_golden_tag_for_image_playbook_inheritted_tag_cannot_be_untagged"),
                self.test_data.get("TaskDetails_end_1"),
                self.test_data.get("inheritted_tag_cannot_be_untagged_response"),
            ]

        elif "playbook_import_image" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_52"),
                self.test_data.get("import_software_image_via_url"),
                self.test_data.get("task_details_50"),
                self.test_data.get("task_details_51"),
                self.test_data.get("get_software_image_details_53"),
                self.test_data.get("get_software_image_details_54"),
                self.test_data.get("import_image_response"),
            ]

        elif "playbook_image_activation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_65"),
                self.test_data.get("get_site_type"),
                self.test_data.get("get_sites_65"),
                self.test_data.get("get_sites_66"),
                self.test_data.get("get_sites_67"),
                self.test_data.get("get_site_assigned_network_devices_65"),
                self.test_data.get("get_site_assigned_network_devices_66"),
                self.test_data.get("get_device_list_65"),
                self.test_data.get("device_list_response_65"),
                self.test_data.get("device_list_response68"),
                self.test_data.get("get_device_list69"),
                self.test_data.get("get_software_image_details_66"),
                self.test_data.get("get_device_list_66"),
                self.test_data.get("compliance_details_of_device_65"),
                self.test_data.get("get_device_list_67"),
                self.test_data.get("activation_api_response"),
                self.test_data.get("Taskdetails_1"),
                self.test_data.get("Taskdetails"),
                self.test_data.get("get_software_image_details_67"),
                self.test_data.get("get_sites_68"),
                self.test_data.get("get_software_image_details_68"),
                self.test_data.get("image_activation_response"),
            ]

        elif "playbook_multiple_image_distribution_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_10"),
                self.test_data.get("get_software_image_details_10"),
                self.test_data.get("get_site_type"),
                self.test_data.get("get_sites_11"),
                self.test_data.get("get_sites_12"),
                self.test_data.get("get_site_assigned_network_devices_1"),
                self.test_data.get("get_site_assigned_network_devices_2"),
                self.test_data.get("get_device_list_10"),
                self.test_data.get("device_list_response_10"),
                self.test_data.get("device_list_response_11"),
                self.test_data.get("get_device_list_11"),
                self.test_data.get("get_software_image_details_11"),
                self.test_data.get("get_device_list_12"),
                self.test_data.get("compliance_details_of_device_10"),
                self.test_data.get("get_device_list_13"),
                self.test_data.get("task_10"),
                self.test_data.get("task_details_10"),
                self.test_data.get("task_details_11"),
                self.test_data.get("get_sites_13"),
                self.test_data.get("get_software_image_details_12"),
                self.test_data.get("get_software_image_details_13"),
                self.test_data.get("multiple_image_distribution_response_1"),
            ]

    def test_swim_workflow_manager_playbook_inheritted_tag_cannot_be_untagged(self):
        """
        Test case for SWIM workflow manager inherited tag untagging.
        This test case checks the behavior when attempting to untag an inherited tag in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_version='2.3.7.6',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_inheritted_tag_cannot_be_untagged
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("msg"),
            "NCSW10395: An inheritted tag cannot be un-tagged. Go to corresponding site to untag."
        )

    def test_swim_workflow_manager_playbook_untag_image_as_golden_and_load_on_device(self):
        """
        Test case for swim workflow manager when giving untag image as golden and load on device
        This test case checks the behavior of the swim workflow when giving untag image as golden and load on device
        """
        set_module_args(
            dict(
                dnac_version='2.3.5.3',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_untag_image_as_golden_and_load_on_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            (
                "Un-Tagging image cat9k_iosxe.17.12.02.SPA.bin golden for site Global/LTTS "
                "for family Cisco Catalyst 9000 UADP 8 Port Virtual Switch for device role ALL successful."
            )
        )

    def test_swim_workflow_manager_playbook_swim_image_golden_tag(self):
        """
        Test case for swim workflow manager when giving swim image golden already tagged
        This test case checks the behavior of the swim workflow when giving swim image golden tagged
        """
        set_module_args(
            dict(
                dnac_version='2.3.5.3',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_swim_image_golden_tag
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Tagging image cat9k_iosxe.17.12.02.SPA.bin golden for site Global for family Cisco Catalyst 9300 Switch for device role ALL successful."
        )

    def test_swim_workflow_manager_playbook_swim_image_cant_found(self):
        """
        Test case for swim workflow manager when giving swim image cant found
        This test case checks the behavior of the swim workflow when giving swim image cant found
        """
        set_module_args(
            dict(
                dnac_version='2.3.5.3',
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

    def test_swim_workflow_manager_playbook_image_details_distribution_not_provided(self):
        """
        Test case for swim workflow manager when giving image details distribution not provided
        This test case checks the behavior of the swim workflow when giving image details distribution not provided
        """
        set_module_args(
            dict(
                dnac_version='2.3.7.6',
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
                dnac_version='2.3.5.3',
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

    def test_swim_workflow_manager_playbook_import_image(self):
        """
        Test SWIM workflow manager's image import functionality.

        This test verifies that the workflow correctly processes image import requests,
        ensuring proper handling of different device families and validating expected behavior.
        """
        set_module_args(
            dict(
                dnac_version='2.3.5.3',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_import_image
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Image(s) cat9k_iosxe.17.07.01.SPA.bin have been imported successfully into Cisco Catalyst Center."
        )

    def test_swim_workflow_manager_playbook_swim_image_golden_already_tagged(self):
        """
        Test case for swim workflow manager when givingswim image golden already tagged
        This test case checks the behavior of the swim workflow when giving swim image golden already tagged
        """
        set_module_args(
            dict(
                dnac_version='2.3.5.3',
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
            "SWIM Image 'cat9k_iosxe.17.12.02.SPA.bin' already tagged as Golden image in Cisco Catalyst Center for the roles - ALL."
        )

    def test_swim_workflow_manager_playbook_import_image_already_exist(self):
        """
        Test case for swim workflow manager when giving import image already exist
        This test case checks the behavior of the swim workflow when giving import image already exist
        """
        set_module_args(
            dict(
                dnac_version='2.3.5.3',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_import_image_already_exist
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Image(s) cat9k_iosxe.17.12.02.SPA.bin were skipped as they already exist in Cisco Catalyst Center."
        )

    def test_swim_workflow_manager_playbook_multiple_image_distribution_1(self):
        """
        Test SWIM workflow manager's multiple image distribution process.

        This test verifies that the workflow correctly handles the distribution of multiple
        images across devices, ensuring proper execution and expected outcomes.
        """

        set_module_args(
            dict(
                dnac_version='2.3.7.9',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_multiple_image_distribution_1
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Successfully distributed: cat9k_iosxe.17.12.03.SPA.bin to 204.1.1.2"
        )

    def test_swim_workflow_manager_playbook_image_activation(self):
        """
        Test SWIM workflow manager's image activation process.

        This test verifies that the workflow correctly handles image activation,
        ensuring that an already imported image can be activated successfully
        and behaves as expected.
        """

        set_module_args(
            dict(
                dnac_version='2.3.7.9',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                config_verify=True,
                state="merged",
                config=self.playbook_image_activation
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Successfully activated: cat9k_iosxe.17.12.02.SPA.bin to 204.1.1.26"
        )
