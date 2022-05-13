# Copyright (c) 2020-2022 Cisco and/or its affiliates.
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
import pdb

from ansible_collections.ansible.netcommon.tests.unit.compat.mock import patch, MagicMock

from ansible_collections.cisco.dnac.plugins.modules import template_module
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData

import json
import copy

class TestDnacTemplateModule(TestDnacModule):

    module = pnp_module 

    test_data = loadPlaybookData("template_module")

    playbook_config = test_data.get("playbook_config")
    playbook_config_missing_param = test_data.get("playbook_config_missing_param")


    def setUp(self):
        super(TestDnacTemplateModule, self).setUp()
   
        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]

        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.exec"
            )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):
        super(TestDnacTemplateModule, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):

        if "create_template" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("create_template_list_response"),
                self.test_data.get("create_template_get_project_response"),
                self.test_data.get("create_template_response"),
                self.test_data.get("create_template_task_details_for_create"),
                self.test_data.get("create_template_version_template_response"),
                self.test_data.get("create_template_task_details_for_versioning")
            ]


    def test_template_module_create_template(self):

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
            result.get('response').get('progress'),
            "Successfully committed template ANSIBLE-TEST to version 1"
            )

