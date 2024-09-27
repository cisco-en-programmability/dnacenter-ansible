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
    playbook_site_not_exist = test_data.get("playbook_site_not_exist")
    playbook_swim_image_invalid = test_data.get("playbook_swim_image_invalid")
    playbook_image_distribution_failed = test_data.get("playbook_image_distribution_failed")
    playbook_swim_image_golden_already_tagged = test_data.get("playbook_swim_image_golden_already_tagged")
    playbook_swim_image_cant_found = test_data.get("playbook_swim_image_cant_found")
    playbook_image_details_distribution_not_provided = test_data.get("playbook_image_details_distribution_not_provided")
    playbook_device_family_not_found = test_data.get("playbook_device_family_not_found")
    playbook_import_image_remote = test_data.get("playbook_import_image_remote")
    playbook_image_distribution_successfull = test_data.get("playbook_image_distribution_successfull")
    playbook_image_distribution_successfull_v2_3_7_6 = test_data.get("playbook_image_distribution_successfull_v2_3_7_6")
    playbook_swim_image_golden_tag = test_data.get("playbook_swim_image_golden_tag")
    playbook_inheritted_tag_cannot_be_untagged = test_data.get("playbook_inheritted_tag_cannot_be_untagged")
    playbook_import_cco_image = test_data.get("playbook_import_cco_image")
    playbook_activate_image = test_data.get("playbook_activate_image")

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
                self.test_data.get("untag_image_as_golden_and_load_on_device_responce")
            ]

        elif "playbook_import_image_already_exist" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details"),
                self.test_data.get("get_software_image_details_4"),
                self.test_data.get("import_image_already_exist_response"),
            ]

        elif "playbook_site_not_exist" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_site_not_exist"),
                Exception(),
                self.test_data.get("site_not_exist_response"),
            ]
        elif "playbook_swim_image_invalid" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_invalid_swim_image"),
                self.test_data.get("import_software_image_via_url_invalid_swim_image"),
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
                self.test_data.get("import__swim_image_golden_tag_responce"),
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
                self.test_data.get("swim_image_golden_already_tagged_responce"),
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
        elif "playbook_import_image_remote_v2_3_7_6" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_remote_import"),
                self.test_data.get("import_software_image_via_url_remote_import"),
                self.test_data.get("Task_Details_start"),
                self.test_data.get("Task_Details_end"),
                self.test_data.get("get_software_image_details_remote_import_1"),
                self.test_data.get("get_software_image_details_remote_import_2"),
                self.test_data.get("import_image_remote_responce"),
            ]
        elif "playbook_import_image_remote" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_remote_import"),
                self.test_data.get("import_software_image_via_url_remote_import"),
                self.test_data.get("Task_Details_start"),
                self.test_data.get("Task_Details_end"),
                self.test_data.get("get_software_image_details_remote_import_1"),
                self.test_data.get("get_software_image_details_remote_import_2"),
                self.test_data.get("import_image_remote_responce"),
            ]
        elif "playbook_image_distribution_successfull" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_image_distribution_successfull"),
                self.test_data.get("get_software_image_details_image_distribution_successfull"),
                self.test_data.get("get_device_list_image_distribution_successfull"),
                self.test_data.get("get_site_image_distribution_successfull_1"),
                self.test_data.get("get_membership_image_distribution_successfull"),
                self.test_data.get("get_device_list_image_distribution_successfull_1"),
                self.test_data.get("get_device_list_image_distribution_successfull_ep"),
                self.test_data.get("get_device_list_image_distribution_successfull_1"),
                self.test_data.get("trigger_software_image_distribution_image_distribution_successfull"),
                self.test_data.get("Task_Details_image_distribution_successfull_start"),
                self.test_data.get("Task_Details_image_distribution_successfull_end"),
                self.test_data.get("get_site_image_distribution_successfull_2"),
                self.test_data.get("get_software_image_details_image_distribution_successfull_1"),
                self.test_data.get("get_device_list_image_distribution_successfull_2"),
                self.test_data.get("get_software_image_details_image_distribution_successfull_2"),
                self.test_data.get("import_image_distribution_successfull"),
            ]

        elif "playbook_image_distribution_successfull_v2_3_7_6" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_image_distribution_successfull_v2_3_7_6"),
                self.test_data.get("get_sites_image_distribution_successfull_v2_3_7_6_1"),
                self.test_data.get("get_software_image_details_image_distribution_successfull_v2_3_7_6"),
                self.test_data.get("get_device_list_image_distribution_successfull_v2_3_7_6"),
                self.test_data.get("get_sites_image_distribution_successfull_v2_3_7_6_2"),
                self.test_data.get("get_sites_image_distribution_successfull_v2_3_7_6_3"),
                self.test_data.get("get_site_assigned_network_devices_image_distribution_successfull_v2_3_7_6"),
                self.test_data.get("device_list_response_image_distribution_successfull_v2_3_7_6_1"),
                self.test_data.get("device_list_response_image_distribution_successfull_v2_3_7_6_2"),
                self.test_data.get("device_list_response_image_distribution_successfull_v2_3_7_6_3"),
                self.test_data.get("device_list_response_image_distribution_successfull_v2_3_7_6_4"),
                self.test_data.get("get_device_list_image_distribution_successfull_v2_3_7_6_1"),
                self.test_data.get("trigger_software_image_distribution_image_distribution_successfull_v2_3_7_6"),
                self.test_data.get("TaskDetails_image_distribution_successfull_v2_3_7_6"),
                self.test_data.get("TaskDetails_image_distribution_successfull_v2_3_7_6_1"),
                self.test_data.get("get_sites_image_distribution_successfull_v2_3_7_6_4"),
                self.test_data.get("get_sites_image_distribution_successfull_v2_3_7_6_5"),
                self.test_data.get("get_software_image_details_image_distribution_successfull_v2_3_7_6_1"),
                self.test_data.get("get_device_list_image_distribution_successfull_v2_3_7_6_2"),
                self.test_data.get("get_software_image_details_image_distribution_successfull_v2_3_7_6_2"),
                self.test_data.get("image_distribution_successfull_v2_3_7_6_responce"),
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
                self.test_data.get("inheritted_tag_cannot_be_untagged_responce"),
            ]
        elif "playbook_import_cco_image" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_software_image_details_import_cco_image"),
                self.test_data.get("returns_list_of_software_images"),
                self.test_data.get("download_the_software_image"),
                self.test_data.get("TaskDetails"),
                self.test_data.get("get_software_image_details_import_cco_image_1"),
                self.test_data.get("get_software_image_details_import_cco_image_2"),
                self.test_data.get("import_cco_imageresponce"),
            ]
        elif "playbook_activate_image" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_site_activate_image"),
                self.test_data.get("get_software_image_details_"),
                self.test_data.get("get_device_list_activate_image"),
                self.test_data.get("get_site_activate_image_2"),
                self.test_data.get("get_membership_activate_image"),
                self.test_data.get("device_list_response_activate_image"),
                self.test_data.get("device_list_response_activate_image_1"),
                self.test_data.get("get_device_list_activate_image_1"),
                self.test_data.get("trigger_software_image_activation_activate_image"),
                self.test_data.get("TaskDetails_activate_image"),
                self.test_data.get("TaskDetails_activate_image_1"),
                self.test_data.get("get_software_image_details_activate_image"),
                self.test_data.get("get_site_activate_image_3"),
                self.test_data.get("get_device_list_activate_image_2"),
                self.test_data.get("get_software_image_details_activate_image_1"),
                self.test_data.get("activate_image_responce"),
            ]

    def test_swim_workflow_manager_playbook_activate_image(self):
        """
        Test case for swim workflow manager import image url
        This test case checks the behavior of activativating the image in the specified Cisco Catalyst Center.
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
                config=self.playbook_activate_image
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("msg"),
            "Image with Id 'None' activated successfully for all devices '204.1.2.4', '204.1.2.2', '204.1.2.3'"
        )

    def test_swim_workflow_manager_playbook_import_cco_image(self):
        """
        Test case for SWIM workflow manager to import an image from Cisco's cloud (CCO).
        This test case verifies the import of an image from the CCO into the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                dnac_version='2.3.7.6',
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_import_cco_image
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("msg"),
            "Image(s) cat9k_iosxe_npe.17.12.04.SPA.bin have been imported successfully in Cisco Catalyst Center"
        )

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
                state="merged",
                config=self.playbook_inheritted_tag_cannot_be_untagged
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("msg"),
            "NCSW10395: An inheritted tag cannot be un-tagged. Go to corresponding site to untag."
        )

    def test_swim_workflow_manager_playbook_import_image_remote_v2_3_7_6(self):
        """
        Test case for SWIM workflow manager to import an image from a remote server.
        This test case verifies the import of a remote image into the Cisco Catalyst Center for DNAC version 2.3.7.6.
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
                config=self.playbook_import_image_remote
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "Image(s) cat9k_iosxe.17.12.01.SPA.bin have been imported successfully into Cisco Catalyst Center."
        )

    def test_swim_workflow_manager_playbook_import_image_remote(self):
        """
        Test case for SWIM workflow manager to import an image from a remote server.
        This test case verifies the import of a remote image into the Cisco Catalyst Center for DNAC version 2.3.5.3.
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
                config=self.playbook_import_image_remote
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("msg"),
            "Image(s) cat9k_iosxe.17.12.01.SPA.bin have been imported successfully into Cisco Catalyst Center."
        )

    def test_swim_workflow_playbook_image_distribution_successfull(self):
        """
        Test case for SWIM workflow manager image distribution.
        This test case verifies the successful distribution of an image to all specified devices in the Cisco Catalyst Center.
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
                config=self.playbook_image_distribution_successfull
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("msg"),
            "Image with Id 1013afb0-49b0-4c90-96ae-57173c56aabd Distributed Successfully for all devices '204.1.2.2'"
        )

    def test_swim_workflow_playbook_image_distribution_successfull_v2_3_7_6(self):
        """
        Test case for SWIM workflow manager image distribution with DNAC version 2.3.7.6.
        This test case verifies the successful distribution of an image to all specified devices in the Cisco Catalyst Center for DNAC version 2.3.7.6.
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
                config=self.playbook_image_distribution_successfull_v2_3_7_6
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("msg"),
            "Image with Id 1013afb0-49b0-4c90-96ae-57173c56aabd Distributed Successfully for all devices '204.1.2.2'"
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
                dnac_version='2.3.5.3',
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
            "Image(s) cat9k_iosxe.17.12.02.SPA.bin were skipped as they already exist in Cisco Catalyst Center. No new images were imported."
        )

    def test_swim_workflow_manager_playbook_site_not_exist(self):
        """
        Test case for swim workflow manager when giving site not exist
        This test case checks the behavior of the swim workflow when giving site not exist
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
                config=self.playbook_site_not_exist
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "An exception occurred: Site 'Global/ltts/flor1' does not exist in the Cisco Catalyst Center"
        )

    def test_swim_workflow_manager_playbook_swim_image_invalid(self):
        """
        Test case for swim workflow manager when giving swim image invalid
        This test case checks the behavior of the swim workflow when giving swim image invalid
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
                config=self.playbook_swim_image_invalid
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "SWIM Image http://172.21.236.183/swim/V1712_2_CCO/cat9k_iosxe.17.12.32.SPA.bin seems to be invalid"
        )

    def test_swim_workflow_manager_playbook_image_distribution_failed(self):
        """
        Test case for swim workflow manager when giving image distribution failed
        This test case checks the behavior of the swim workflow when giving image distribution failed
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
                config=self.playbook_image_distribution_failed
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Image with Id c383ee35-d20e-49f2-b51c-bfe499abbbaa Distribution Failed"
        )

    def test_swim_workflow_manager_playbook_swim_image_golden_tag(self):
        """
        Test case for swim workflow manager when givingswim image golden already tagged
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
            "Tagging image  cat9k_iosxe.17.12.02.SPA.bin  golden for site  Global for family Cisco Catalyst 9300 Switch  for device deviceTag ALL successful."
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
            "SWIM Image 'cat9k_iosxe.17.12.02.SPA.bin' already tagged as Golden image in Cisco Catalyst Center"
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
                dnac_version='2.3.5.3',
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
