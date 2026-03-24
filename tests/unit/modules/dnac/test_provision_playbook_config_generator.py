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

from ansible_collections.cisco.dnac.plugins.modules import provision_playbook_config_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacProvisionPlaybookGenerator(TestDnacModule):

    module = provision_playbook_config_generator

    test_data = loadPlaybookData("provision_playbook_config_generator")

    playbook_global_filters = test_data.get("playbook_global_filters")

    def _build_generator_for_validation(self, config=None, params=None):
        generator = self.module.ProvisionPlaybookGenerator.__new__(
            self.module.ProvisionPlaybookGenerator
        )
        generator.config = config
        generator.params = params or {}
        generator.msg = None
        generator.status = None
        generator.validated_config = None
        generator.log = lambda *args, **kwargs: None

        def set_operation_result(status, changed, msg, level):
            generator.status = status
            generator.msg = msg
            return generator

        generator.set_operation_result = set_operation_result
        return generator

    def setUp(self):
        super(TestDnacProvisionPlaybookGenerator, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacProvisionPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """

        if "playbook_global_filters" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_sites"),
                self.test_data.get("response1"),
                self.test_data.get("response2"),
                self.test_data.get("response3"),
                self.test_data.get("response4"),
                self.test_data.get("response5"),
                self.test_data.get("response6"),
                self.test_data.get("response7"),
                self.test_data.get("response8"),
                self.test_data.get("response9"),
                self.test_data.get("response10"),
                self.test_data.get("response11"),
                self.test_data.get("response12"),
                self.test_data.get("response13"),
                self.test_data.get("response14"),
                self.test_data.get("response15"),
                self.test_data.get("response16"),
                self.test_data.get("response17"),
                self.test_data.get("response18"),
                self.test_data.get("response19"),
                self.test_data.get("response20"),
                self.test_data.get("response21"),
                self.test_data.get("response22"),
                self.test_data.get("response23"),
                self.test_data.get("response24"),
                self.test_data.get("response25"),
                self.test_data.get("response26"),
                self.test_data.get("response27"),
                self.test_data.get("response28"),
                self.test_data.get("response29"),
                self.test_data.get("response30"),
                self.test_data.get("response31"),
                self.test_data.get("response32"),
                self.test_data.get("response33"),
                self.test_data.get("response34"),
                self.test_data.get("response35"),
                self.test_data.get("response36"),
                self.test_data.get("response37"),
                self.test_data.get("response38"),
                self.test_data.get("response39"),
                self.test_data.get("response40"),
                self.test_data.get("response41"),
                self.test_data.get("response42"),
                self.test_data.get("response43"),
                self.test_data.get("response44"),
                self.test_data.get("response45"),
                self.test_data.get("response46"),
                self.test_data.get("response47"),
                self.test_data.get("response48"),
                self.test_data.get("response49"),
                self.test_data.get("response50"),
                self.test_data.get("response51"),
                self.test_data.get("response52"),
                self.test_data.get("response53"),
                self.test_data.get("response54"),
                self.test_data.get("response55"),
                self.test_data.get("response56"),
                self.test_data.get("response57"),
                self.test_data.get("response58"),
                self.test_data.get("response59"),
                self.test_data.get("response60"),
                self.test_data.get("response61"),
                self.test_data.get("response62"),
                self.test_data.get("response63"),
                self.test_data.get("response64"),
                self.test_data.get("response65"),
                self.test_data.get("response66"),
                self.test_data.get("response67"),
                self.test_data.get("response68"),
                self.test_data.get("response69"),
                self.test_data.get("response70"),
                self.test_data.get("response71"),
                self.test_data.get("response72"),
                self.test_data.get("response73"),
                self.test_data.get("response74"),
                self.test_data.get("response75"),
                self.test_data.get("response76"),
                self.test_data.get("response77"),
                self.test_data.get("response78"),
                self.test_data.get("response79"),
                self.test_data.get("response80"),
                self.test_data.get("response81"),
                self.test_data.get("response82"),
                self.test_data.get("response83"),
                self.test_data.get("response84"),
                self.test_data.get("error_response"),
                self.test_data.get("response85"),
                self.test_data.get("response86"),
                self.test_data.get("response87"),
                self.test_data.get("response88"),
            ]

    def test_provision_playbook_config_generator_playbook_global_filters(self):
        """
        Validate that legacy config keys are rejected by the new contract.

        This test verifies that generate_all_configurations/global_filters under config
        now fail validation.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                file_path=(
                    "/Users/syedkahm/ansible/dnac/work/collections/ansible_collections/cisco/dnac/"
                    "playbooks/brownfield_provision_workflow_playbook.yml"
                ),
                file_mode="overwrite",
            )
        )
        result = self.execute_module(changed=True, failed=False)
        expected_file_path = (
            "/Users/syedkahm/ansible/dnac/work/collections/ansible_collections/cisco/dnac/"
            "playbooks/brownfield_provision_workflow_playbook.yml"
        )
        self.assertEqual(
            result.get("response"),
            {
                "YAML config generation Task succeeded for module 'provision_workflow_manager'.": {
                    "file_path": expected_file_path,
                    "devices_count": 6
                }
            }
        )

    def test_provision_playbook_config_generator_duplicate_components_list_fails(self):
        """
        Validate that duplicate component names in components_list are rejected.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config={
                    "component_specific_filters": {
                        "components_list": ["wired", "wired"]
                    }
                },
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Duplicate component names found in 'components_list': ['wired']",
            result.get("msg", "")
        )

    def test_provision_playbook_config_generator_playbook_global_filters_default_file_path(self):
        """
        Validate that omitting both config and file_path still generates YAML using a default filename.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
            )
        )

        default_file_path = "provision_playbook_config_test.yml"
        with patch.object(
            provision_playbook_config_generator.ProvisionPlaybookGenerator,
            "generate_filename",
            return_value=default_file_path,
        ), patch.object(
            provision_playbook_config_generator.ProvisionPlaybookGenerator,
            "write_dict_to_yaml",
            return_value=True,
        ):
            result = self.execute_module(changed=True, failed=False)

        self.assertEqual(
            result.get("response"),
            {
                "YAML config generation Task succeeded for module 'provision_workflow_manager'.": {
                    "file_path": default_file_path,
                    "devices_count": 6,
                }
            }
        )

    def test_validate_input_accepts_list_values_for_component_filters(self):
        generator = self._build_generator_for_validation(
            config={
                "component_specific_filters": {
                    "wired": [
                        {
                            "management_ip_address": ["204.1.2.5", "204.1.2.6"],
                            "site_name_hierarchy": ["Global/USA/SAN JOSE/SJ_BLD23"],
                            "device_family": ["Switches and Hubs", "Routers"],
                        }
                    ]
                }
            }
        )

        generator.validate_input()

        self.assertEqual(generator.status, "success")
        wired_filter = generator.validated_config["component_specific_filters"]["wired"][0]
        self.assertEqual(
            wired_filter["management_ip_address"], ["204.1.2.5", "204.1.2.6"]
        )
        self.assertEqual(
            wired_filter["device_family"], ["Switches and Hubs", "Routers"]
        )
        self.assertEqual(
            generator.validated_config["component_specific_filters"]["components_list"],
            ["wired"],
        )

    def test_validate_input_rejects_invalid_management_ip_in_filter_list(self):
        generator = self._build_generator_for_validation(
            config={
                "component_specific_filters": {
                    "wired": [
                        {
                            "management_ip_address": ["204.1.2.5", "bad-ip"],
                        }
                    ]
                }
            }
        )

        generator.validate_input()

        self.assertEqual(generator.status, "failed")
        self.assertIn(
            "Invalid IPv4 address values ['bad-ip'] in wired filters.management_ip_address",
            generator.msg,
        )

    def test_apply_device_filters_matches_list_values(self):
        generator = self.module.ProvisionPlaybookGenerator.__new__(
            self.module.ProvisionPlaybookGenerator
        )
        generator.log = lambda *args, **kwargs: None
        generator.transform_device_management_ip = lambda device: device.get(
            "management_ip_address"
        )
        generator.transform_device_site_hierarchy = lambda device: device.get(
            "site_name_hierarchy"
        )
        generator.transform_device_family_info = lambda device: device.get("device_family")

        devices = [
            {
                "management_ip_address": "204.1.2.5",
                "site_name_hierarchy": "Global/USA/SAN JOSE/SJ_BLD23",
                "device_family": "Switches and Hubs",
            },
            {
                "management_ip_address": "204.1.2.6",
                "site_name_hierarchy": "Global/USA/SAN JOSE/SJ_BLD24",
                "device_family": "Routers",
            },
            {
                "management_ip_address": "204.1.2.7",
                "site_name_hierarchy": "Global/USA/SAN JOSE/SJ_BLD25",
                "device_family": "Wireless Controller",
            },
        ]

        filters = [
            {
                "management_ip_address": ["204.1.2.5", "204.1.2.6"],
                "site_name_hierarchy": [
                    "Global/USA/SAN JOSE/SJ_BLD23",
                    "Global/USA/SAN JOSE/SJ_BLD24",
                ],
                "device_family": ["Switches and Hubs", "Routers"],
            }
        ]

        filtered_devices = generator.apply_device_filters(devices, filters)

        self.assertEqual(len(filtered_devices), 2)
        self.assertEqual(
            [device.get("management_ip_address") for device in filtered_devices],
            ["204.1.2.5", "204.1.2.6"],
        )
