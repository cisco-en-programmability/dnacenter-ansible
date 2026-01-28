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

from ansible_collections.cisco.dnac.plugins.modules import brownfield_provision_playbook_generator
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacBrownfieldProvisionPlaybookGenerator(TestDnacModule):

    module = brownfield_provision_playbook_generator

    test_data = loadPlaybookData("brownfield_provision_playbook_generator")

    playbook_global_filters = test_data.get("playbook_global_filters")

    def setUp(self):
        super(TestDnacBrownfieldProvisionPlaybookGenerator, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacBrownfieldProvisionPlaybookGenerator, self).tearDown()
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

    def test_brownfield_provision_playbook_generator_playbook_global_filters(self):
        """
        Test the Application Policy Workflow Manager's profile creation process.

        This test verifies that the workflow correctly handles the creation of a new
        application policy profile, ensuring proper validation and expected behavior.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="gathered",
                dnac_version="2.3.7.9",
                config=self.playbook_global_filters
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get("msg"),
            "No devices found matching the provided filters for module 'provision_workflow_manager'. Global filters: "
            "{'management_ip_address': ['204.192.4.200']}, Component filters: {'components_list': ['wired', 'wireless']}"
        )
