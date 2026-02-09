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

from ansible_collections.cisco.dnac.plugins.modules import brownfield_pnp_playbook_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacBrownfieldPnpPlaybookGenerator(TestDnacModule):

    module = brownfield_pnp_playbook_generator

    test_data = loadPlaybookData("brownfield_pnp_playbook_generator")

    playbook_pnp_generate_all_configurations = test_data.get("playbook_pnp_generate_all_configurations")
    playbook_component_global_specific_filter = test_data.get("playbook_component_global_specific_filter")
    playbook_no_config = test_data.get("playbook_no_config")

    def setUp(self):
        super(TestDnacBrownfieldPnpPlaybookGenerator, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacBrownfieldPnpPlaybookGenerator, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """

        if "playbook_pnp_generate_all_configurations" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("PnPdevices"),
            ]

        elif "playbook_component_global_specific_filter" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("PnPdevices1"),
                self.test_data.get("site_response1"),
                self.test_data.get("site_response2"),
                self.test_data.get("site_response3"),
            ]

        elif "playbook_no_config" in self._testMethodName:
            pass

    def test_brownfield_pnp_playbook_generator_playbook_pnp_generate_all_configurations(self):
        """
        Test the PnP Playbook Generator's configuration generation process.

        This test verifies that the generator correctly creates YAML configurations
        from all PnP devices, ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_pnp_generate_all_configurations
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response").get("message"),
            "YAML config generation succeeded for module 'pnp_workflow_manager'."
        )

    def test_brownfield_pnp_playbook_generator_playbook_component_global_specific_filter(self):
        """
        Test the PnP Playbook Generator with component and global filters.

        This test verifies that the generator correctly handles specific filtering
        of PnP devices, ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_component_global_specific_filter
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response").get("message"),
            "YAML config generation succeeded for module 'pnp_workflow_manager'."
        )

    def test_brownfield_pnp_playbook_generator_playbook_no_config(self):
        """
        Test the PnP Playbook Generator with no configuration.

        This test verifies that the generator correctly handles scenarios
        where no PnP devices are found, ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_no_config
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("response").get("message"),
            "No PnP devices found matching specified filters. Verify device inventory and filter criteria."
        )
