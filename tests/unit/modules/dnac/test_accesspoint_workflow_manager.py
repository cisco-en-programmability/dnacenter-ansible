# Copyright (c) 2020 Cisco and/or its affiliates.
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

from ansible_collections.cisco.dnac.plugins.modules import accesspoint_workflow_manager
from .dnac_module import TestDnacModule, set_module_args

class TestDnacSiteIntent(TestDnacModule):
    def __init__(self):
        """
        Inheriting from the base class of dnac_module
        """

        module = accesspoint_workflow_manager
        super().__init__(module)

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for a specific device.

        Parameters:
        response (list, optional): The expected response data. Defaults to None.
        device (str, optional): The device for which to load fixtures. Defaults to an empty string.
        """

        if "site_exists" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
                self.test_data.get("site_exist_get_site_response")
            ]

        elif "site_exists_found" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("site_not_exist_get_site_response"),
            ]

        elif "accesspoint_workflow_update_needed" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("update_needed_get_site_response"),
            ]

        elif "accesspoint_workflow_update_needed" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("update_needed_get_site_response"),
                self.test_data.get("update_needed_update_site_response"),
                self.test_data.get("get_business_api_execution_details_response")
            ]

        elif "accesspoint_workflow_update_needed" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("update_needed_get_site_response"),
                self.test_data.get("update_needed_update_site_response"),
                self.test_data.get("get_business_api_execution_details_response")
            ]

        elif "delete_existing_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("delete_get_site_response"),
                self.test_data.get("delete_delete_site_response"),
                self.test_data.get("get_business_api_execution_details_response")
            ]
        elif "delete_non_existing_site" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception()
            ]
        elif "provision_device" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("delete_error_get_site_response"),
                self.test_data.get("delete_delete_site_response"),
                self.test_data.get("delete_execution_details_error")
            ]

        elif "wsl_provision" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("delete_error_get_site_response"),
                self.test_data.get("delete_delete_site_response"),
                self.test_data.get("delete_execution_details_error")
            ]

        elif "get_site_devic" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
                self.test_data.get("create_site_response"),
                self.test_data.get("delete_execution_details_error")
            ]

        elif "get_accesspoint_details" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
                self.test_data.get("create_site_response"),
                self.test_data.get("delete_execution_details_error")
            ]

    def test_validate_radio_series(self):
        """
        Test case for validate radio series method.

        This test case check for validation of the radio series 
        parameters when configuaring the access point in the specified DNAC.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Access Point series not supported for the radio type "
        )

    def test_validate_ap_config_parameters(self):
        """
        Test case for validate_ap_config_parameters.

        This test case check for validation of the validate 
        ap config parameters when configuaring the access point in the specified DNAC.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Successfully validated config params"
        )

    def test_site_exists_not_found(self):
        """
        Test case for site_exists method when site is not found.

        This test case checks the if site exists, when an update is not required for the specified site in the DNAC.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Site does not exist in DNAC"
        )

    def test_site_exists_found(self):
        """
        Test case for site_exists method when site is not found.

        This test case checks the if site exists, when an update is not required for the specified site in the DNAC.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Site present in Cisco Catalyst Center"
        )

    def test_accesspoint_workflow_update_needed(self):
        """
        Test case for access point when an update is needed.

        This test case checks the  update is required for the specified access point in the DNAC.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Access point configuration Updated Successfully"
        )

    def test_accesspoint_workflow_update_not_needed(self):
        """
        Test case for access point when an update is not needed.

        This test case checks the  update is not equired for the specified access point in the DNAC.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Access point configuration not required Update"
        )

    def test_accesspoint_workflow_invalid_param(self):
        """
        Test case for site intent with invalid parameters in the playbook.

        This test case checks the validation for access point workflow contains invalid parameters.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.test_data.get("playbook_config_invalid_param")
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertTrue(
            "Invalid parameters for access point workflow:" in result.get('msg')
        )

    def test_accesspoint_workflow_invalid_state(self):
        """
        Test case for access point workflow with an invalid 'state' parameter.

        This test case checks the behavior of the access point workflow when an invalid 'state' parameter is provided in the playbook.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merge",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "value of state must be one of: merged  got: merge"
        )

    def test_update_ap_configuration(self):
        """
        Test case for Access Point (AP) configuration based on the provided device data.

        This test case checks the behavior of the Access Point (AP) configuration based on the provided device dat in Cisco Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            " Access point configuration parameters Updated Successfully"
        )

    def test_provision_device(self):
        """
        Test case for checking Provision a device (AP) .

        This test case checks the behavior of the Provision a device (AP) in Cisco catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            " Device is Provisioned Successfully"
        )

    def test_wsl_provision(self):
        """
        Test case for checking Provision a device (AP) .

        This test case checks the behavior of the Provision a device (AP) in Cisco catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('msg'),
            " wireless controller is already Provisioned "
        )

    def test_get_site_device(self):
        """
        Test case for to check  if a given AP MAC address is present inside a Specific site or not.

        This test case checks the behavior of the fetching device information in Cisco Catalyst Center.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Device with MAC address is found "
        )

    def test_get_accesspoint_details(self):

        """
        Test case for Device exist or not in Cisco Catalyst Center.

        This test case checks if the  .
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertEqual(
            result.get('response').get('status'),
            "Device present in Cisco Catalyst Center"
        )

