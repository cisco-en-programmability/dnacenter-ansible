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
from ansible_collections.cisco.dnac.plugins.modules import network_settings_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacNetworkSettings(TestDnacModule):

    module = network_settings_workflow_manager
    test_data = loadPlaybookData("network_settings_workflow_manager")
    playbook_config_network = test_data.get("playbook_config_network")
    playbook_update_network = test_data.get("playbook_update_network")
    playbook_config_update_not_req = test_data.get("playbook_config_update_not_req")
    playbook_config_aaa_req = test_data.get("playbook_config_aaa_req")
    playbook_global_pool_creation = test_data.get("playbook_global_pool_creation")
    playbook_global_pool_updation = test_data.get("playbook_global_pool_updation")
    playbook_config_reserve_pool = test_data.get("playbook_config_reserve_pool")
    playbook_config_reserve_pool_deletion = test_data.get("playbook_config_reserve_pool_deletion")
    playbook_config_global_pool_deletion = test_data.get("playbook_config_global_pool_deletion")

    def setUp(self):
        super(TestDnacNetworkSettings, self).setUp()

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
        super(TestDnacNetworkSettings, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "network_not_need_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_network"),
                self.test_data.get("get_network_v2_2"),
                self.test_data.get("get_network_v2"),
            ]

        if "null_network_params" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_network"),
                self.test_data.get("get_network_v2_2"),
                self.test_data.get("get_network_v2"),
            ]

        if "not_verified" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
                self.test_data.get("ntp_get"),
                self.test_data.get("timeZone_get"),
                self.test_data.get("banner_get"),
                self.test_data.get("AAA_get"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
                self.test_data.get("ntp_get"),
                self.test_data.get("timeZone_get"),
                self.test_data.get("banner_get"),
                self.test_data.get("AAA_get"),
            ]

        if "network_update" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
                self.test_data.get("ntp_get"),
                self.test_data.get("timeZone_get"),
                self.test_data.get("banner_get"),
                self.test_data.get("AAA_get"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("get_sites_test"),
                self.test_data.get("get_dhcp"),
                self.test_data.get("get_dns"),
                self.test_data.get("get_telemetry"),
                self.test_data.get("get_ntp"),
                self.test_data.get("get_timezone"),
                self.test_data.get("get_banner"),
                self.test_data.get("get_AAA"),
            ]

        if "exception_update_dhcp" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
                self.test_data.get("ntp_get"),
                self.test_data.get("timeZone_get"),
                self.test_data.get("banner_get"),
                self.test_data.get("AAA_get"),
            ]

        if "exception_update_ntp" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
                self.test_data.get("ntp_get"),
                self.test_data.get("timeZone_get"),
                self.test_data.get("banner_get"),
                self.test_data.get("AAA_get"),
                self.test_data.get("update"),
                self.test_data.get("task"),
            ]

        if "exception_update_timezone" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
                self.test_data.get("ntp_get"),
                self.test_data.get("timeZone_get"),
                self.test_data.get("banner_get"),
                self.test_data.get("AAA_get"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
            ]

        if "exception_update_dns" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
                self.test_data.get("ntp_get"),
                self.test_data.get("timeZone_get"),
                self.test_data.get("banner_get"),
                self.test_data.get("AAA_get"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
            ]

        if "exception_update_banner" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
                self.test_data.get("ntp_get"),
                self.test_data.get("timeZone_get"),
                self.test_data.get("banner_get"),
                self.test_data.get("AAA_get"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
            ]

        if "exception_update_aaa" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
                self.test_data.get("ntp_get"),
                self.test_data.get("timeZone_get"),
                self.test_data.get("banner_get"),
                self.test_data.get("AAA_get"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
            ]

        if "exception_site_not_exist" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
                self.test_data.get("ntp_get"),
                self.test_data.get("timeZone_get"),
                self.test_data.get("banner_get"),
                self.test_data.get("AAA_get"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
            ]

        if "exception_update_telemetry" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
                self.test_data.get("ntp_get"),
                self.test_data.get("timeZone_get"),
                self.test_data.get("banner_get"),
                self.test_data.get("AAA_get"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
                self.test_data.get("update"),
                self.test_data.get("task"),
            ]

        if "exception_dns_get" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
            ]

        if "exception_telemetry_get" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
            ]

        if "exception_ntp_get" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
            ]

        if "exception_timezone_get" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
                self.test_data.get("ntp_get"),
            ]

        if "exception_banner_get" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
                self.test_data.get("ntp_get"),
                self.test_data.get("timeZone_get"),
            ]

        if "exception_aaa_get" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
                self.test_data.get("ntp_get"),
                self.test_data.get("timeZone_get"),
                self.test_data.get("banner_get"),
            ]

        if "exception_dhcp_get" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
            ]

        if "mandatory_aaa_param" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
                self.test_data.get("ntp_get"),
                self.test_data.get("timeZone_get"),
                self.test_data.get("banner_get"),
                self.test_data.get("AAA_get"),
                self.test_data.get("get_sites_test"),
            ]

        if "update_not_required" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("dhcp_get"),
                self.test_data.get("dns_get"),
                self.test_data.get("telemetry_get"),
                self.test_data.get("ntp_get"),
                self.test_data.get("timeZone_get"),
                self.test_data.get("banner_get"),
                self.test_data.get("get_AAA"),
                self.test_data.get("get_sites_test"),
            ]

        if "null_network_params" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites_test"),
                self.test_data.get("clear_dnac_network"),
            ]

        if "global_pool_creation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("global_pool_exist_ipv6"),
                self.test_data.get("global_pool_exist_ipv4"),
                self.test_data.get("global_pool_creation"),
                self.test_data.get("global_pool_creation_task"),
                self.test_data.get("global_pool_creation_task"),
                self.test_data.get("global_pool_creation_task"),
                self.test_data.get("global_pool_ipv6_exist2"),
                self.test_data.get("global_pool_ipv4_exist2")
            ]

        if "global_pool_deletion" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("deletion_global_pool_exist"),
                self.test_data.get("global_pool_deletion"),
                self.test_data.get("global_pool_deletion_task"),
                self.test_data.get("global_pool_deletion_task"),
                self.test_data.get("global_pool_deletion_task"),
                self.test_data.get("global_pool_exist_deletion"),
                self.test_data.get("global_pool_exist_deletion2"),
            ]

        if "reserve_pool_deletion" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("site_reserve_deletion"),
                self.test_data.get("get_reserved_ip_subpool_deletion"),
                self.test_data.get("delete_reserve_pool"),
                self.test_data.get("delete_reserve_pool_task"),
                self.test_data.get("delete_reserve_pool_task"),
                self.test_data.get("site_reserve_deletion_2"),
                self.test_data.get("get_reserved_ip_subpool_deletion_2"),
            ]

        if "reserve_pool_creation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("site_reserve_deletion"),
                self.test_data.get("get_reserved_ip_subpool_deletion_2"),
                self.test_data.get("site_reserve_deletion"),
                self.test_data.get("create_reserve_pool"),
                self.test_data.get("create_reserve_pool_task"),
                self.test_data.get("site_reserve_deletion"),
                self.test_data.get("get_reserve_pool_creation"),
                self.test_data.get("get_reserve_pool_creation_2"),
            ]

        if "global_pool_Updation_not_req" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("Global_Pool1"),
                self.test_data.get("Global_Pool2"),
                self.test_data.get("update_global_pool"),
                self.test_data.get("update_global_pool_task"),
                self.test_data.get("Global_Pool_1"),
                self.test_data.get("Global_Pool_2")
            ]

    def test_Network_settings_workflow_manager_network_network_not_need_update(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Successfully retrieved details from the playbook"
        )

    def test_Network_settings_workflow_manager_not_verified(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_config_network
            )
        )
        result = self.execute_module(changed=True, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Network Functions Config is not applied to the Cisco Catalyst Center"
        )

    def test_Network_settings_workflow_manager_network_update(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_update_network
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result['response'][2]['network']['msg'],
            {'Global/Testing/test': 'Network Updated successfully'}
        )

    def test_Network_settings_workflow_manager_network_exception_update_dhcp(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_update_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Exception occurred while updating DHCP settings for site b08d92c9-663f-43f3-9575-5af52d4d75a7: "
        )

    def test_Network_settings_workflow_manager_network_exception_update_ntp(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_update_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Exception occurred while updating NTP settings for site b08d92c9-663f-43f3-9575-5af52d4d75a7: "
        )

    def test_Network_settings_workflow_manager_network_exception_update_timezone(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_update_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Exception occurred while updating time zone settings for site b08d92c9-663f-43f3-9575-5af52d4d75a7: "
        )

    def test_Network_settings_workflow_manager_network_exception_update_dns(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_update_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Exception occurred while updating DNS settings for site b08d92c9-663f-43f3-9575-5af52d4d75a7: "
        )

    def test_Network_settings_workflow_manager_network_exception_update_banner(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_update_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Exception occurred while updating banner settings for site b08d92c9-663f-43f3-9575-5af52d4d75a7: "
        )

    def test_Network_settings_workflow_manager_network_exception_update_aaa(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_update_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Exception occurred while updating AAA settings for site b08d92c9-663f-43f3-9575-5af52d4d75a7: "
        )

    def test_Network_settings_workflow_manager_network_exception_update_telemetry(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_config_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Exception occurred while updating telemetry settings for site b08d92c9-663f-43f3-9575-5af52d4d75a7: "
        )

    def test_Network_settings_workflow_manager_network_exception_site_not_exist(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_config_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "An exception occurred: Site 'Global/Vietnam' does not exist in the Cisco Catalyst Center."
        )

    def test_Network_settings_workflow_manager_network_exception_telemetry_get(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_config_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Exception occurred while getting telemetry settings for site b08d92c9-663f-43f3-9575-5af52d4d75a7: "
        )

    def test_Network_settings_workflow_manager_network_exception_dns_get(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_config_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Exception occurred while getting DNS settings for site b08d92c9-663f-43f3-9575-5af52d4d75a7: "
        )

    def test_Network_settings_workflow_manager_network_exception_ntp_get(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_config_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Exception occurred while getting NTP server settings for site b08d92c9-663f-43f3-9575-5af52d4d75a7: "
        )

    def test_Network_settings_workflow_manager_network_exception_timezone_get(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_config_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Exception occurred while getting time zone settings for site b08d92c9-663f-43f3-9575-5af52d4d75a7: "
        )

    def test_Network_settings_workflow_manager_network_exception_dhcp_gett(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_config_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Exception occurred while getting DHCP settings for site b08d92c9-663f-43f3-9575-5af52d4d75a7: "
        )

    def test_Network_settings_workflow_manager_network_exception_banner_get(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_config_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Exception occurred while getting banner settings for site b08d92c9-663f-43f3-9575-5af52d4d75a7: "
        )

    def test_Network_settings_workflow_manager_network_exception_aaa_get(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_config_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Exception occurred while getting AAA settings for site b08d92c9-663f-43f3-9575-5af52d4d75a7: "
        )

    def test_Network_settings_workflow_manager_network_mandatory_aaa_param(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_config_aaa_req
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "The 'network_aaa' and 'clientAndEndpoint_aaa' both fields are required for AAA server updation."
        )

    def test_Network_settings_workflow_manager_network_update_not_required(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                dnac_version="2.3.7.6",
                state="merged",
                config=self.playbook_config_update_not_req
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result['response'][2]['network']['msg'],
            {'Global/Testing/test': "Network doesn't require an update"}
        )

    def test_Network_settings_workflow_manager_network_null_network_params(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
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
                config=self.playbook_config_update_not_req
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Successfully retrieved details from the playbook"
        )

    def test_Network_settings_workflow_manager_global_pool_creation(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_global_pool_creation
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result["response"][0].get("globalPool").get("msg"))
        self.assertEqual(
            result["response"][0].get("globalPool").get("msg"),
            {'Global_Pool2': 'Global Pool Created Successfully', 'Global_Pool3': 'Global Pool Created Successfully'}

        )

    def test_Network_settings_workflow_manager_global_pool_Updation_not_req(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_global_pool_updation
            )
        )
        result = self.execute_module(changed=True, failed=True)
        # print(result["response"][0].get("globalPool").get("msg"))
        # print(result)
        self.assertEqual(
            result["response"][0].get("globalPool").get("msg"),
            {'Global_Pool2': "Global pool doesn't require an update", 'Global_Pool3': "Global pool doesn't require an update"}

        )

    def test_Network_settings_workflow_manager_global_pool_deletion(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                config=self.playbook_config_global_pool_deletion
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result["response"][0].get("globalPool").get("msg"))
        self.assertEqual(
            result["response"][0].get("globalPool").get("msg"),
            {'Global_Pool2': 'Global pool deleted successfully'}
        )

    def test_Network_settings_workflow_manager_reserve_pool_deletion(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                config=self.playbook_config_reserve_pool_deletion
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result['response'][1]['reservePool']['msg'],
            {'IP_Pool_3': 'Ip subpool reservation released successfully'}

        )

    def test_Network_settings_workflow_manager_reserve_pool_creation(self):
        """
        Test case for site workflow manager when creating a site.

        This test case checks the behavior of the site workflow manager when creating a new site in the specified DNAC.
        """
        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_reserve_pool
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result['response'][1]['reservePool']['msg'])
        self.assertEqual(
            result['response'][1]['reservePool']['msg'],
            {'IP_Pool_3': 'Ip Subpool Reservation Created Successfully'}

        )
