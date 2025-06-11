# Copyright (c) 2025 Cisco and/or its affiliates.
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

# Authors:
#   Archit Soni <soni.archit03@gmail.com>
#
# Description:
#   Unit tests for the Ansible module `template_workflow_manager`.
#   These tests cover various template operations such as creation,
#   update, deletion, import, export, deploy and validation logic using mocked Catalyst Center responses.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import template_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacTemplateWorkflow(TestDnacModule):

    module = template_workflow_manager
    test_data = loadPlaybookData("template_workflow_manager")

    playbook_config_create_template_playbook_case_1 = test_data.get(
        "create_template_playbook_case_1"
    )
    playbook_config_update_template_playbook_case_2 = test_data.get(
        "update_template_playbook_case_2"
    )
    playbook_config_delete_template_playbook_case_3 = test_data.get(
        "delete_template_playbook_case_3"
    )
    playbook_config_export_project_playbook_case_4 = test_data.get(
        "export_project_playbook_case_4"
    )
    playbook_config_export_template_playbook_case_5 = test_data.get(
        "export_template_playbook_case_5"
    )
    playbook_config_import_project_playbook_case_6 = test_data.get(
        "import_project_playbook_case_6"
    )
    playbook_config_import_template_playbook_case_7 = test_data.get(
        "import_template_playbook_case_7"
    )

    def setUp(self):
        super(TestDnacTemplateWorkflow, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__"
        )
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()
        self.load_fixtures()

    def tearDown(self):
        super(TestDnacTemplateWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "invalid_delete_config" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                # self.test_data.get(""),
            ]
        elif "test_create_template_playbook_case_1" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_projects_response_case_1_call_1"),
                self.test_data.get("get_task_id_case_1_call_1"),
                self.test_data.get("get_task_details_by_id_case_1_call_1"),
                self.test_data.get("get_task_details_by_id_case_1_call_2"),
                self.test_data.get("get_task_id_case_1_call_2"),
                self.test_data.get("get_task_details_by_id_case_1_call_3"),
                self.test_data.get("get_task_details_by_id_case_1_call_4"),
                self.test_data.get("get_projects_response_case_1_call_2"),
                self.test_data.get("gets_the_templates_available_case_1_call_1"),
                self.test_data.get("get_template_details_case_1_call_1"),
            ]
        elif "test_update_template_playbook_case_2" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_projects_response_case_2_call_1"),
                self.test_data.get("gets_the_templates_available_case_2_call_1"),
                self.test_data.get("get_task_id_case_2_call_1"),
                self.test_data.get("get_task_id_case_2_call_1"),
                self.test_data.get("get_task_details_by_id_case_2_call_1"),
                self.test_data.get("get_task_id_case_2_call_2"),
                self.test_data.get("get_task_details_by_id_case_2_call_2"),
                self.test_data.get("get_task_details_by_id_case_2_call_3"),
                self.test_data.get("get_projects_response_case_2_call_2"),
                self.test_data.get("gets_the_templates_available_case_2_call_2"),
                self.test_data.get("get_template_details_case_2_call_2"),
            ]
        elif "test_delete_template_playbook_case_3" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_projects_response_case_3_call_1"),
                self.test_data.get("gets_the_templates_available_case_3_call_1"),
                self.test_data.get("get_template_details_case_3_call_1"),
                self.test_data.get("get_task_id_case_3_call_1"),
                self.test_data.get("get_task_details_by_id_case_3_call_1"),
                self.test_data.get("gets_the_templates_available_case_3_call_2"),
            ]
        elif "test_export_project_playbook_case_4" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_task_id_case_4_call_1"),
                self.test_data.get("get_task_details_by_id_case_4_call_1"),
            ]
        elif "test_export_template_playbook_case_5" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_export_template_values_case_5_call_1"),
                self.test_data.get("get_task_id_case_5_call_1"),
                self.test_data.get("get_task_details_by_id_case_5_call_1"),
            ]
        elif "test_import_project_playbook_case_6" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_projects_response_case_6_call_1"),
                self.test_data.get("get_task_id_case_6_call_1"),
                self.test_data.get("get_task_details_by_id_case_6_call_1"),
            ]
        elif "test_import_template_playbook_case_7" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_projects_response_case_7_call_1"),
                self.test_data.get("get_task_id_case_7_call_1"),
                self.test_data.get("get_task_details_by_id_case_7_call_1"),
                self.test_data.get("get_task_details_by_id_case_7_call_2"),
            ]

    def test_create_template_playbook_case_1(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_create_template_playbook_case_1,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("response")[0].get("configurationTemplate").get("msg"),
            "Successfully committed template test_template to version 1",
        )

    def test_update_template_playbook_case_2(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_update_template_playbook_case_2,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("response")[0].get("configurationTemplate").get("msg"),
            "Successfully committed template test_template to version 3",
        )

    def test_delete_template_playbook_case_3(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.6",
                dnac_log=True,
                state="deleted",
                config_verify=True,
                config=self.playbook_config_delete_template_playbook_case_3,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("msg"), "Task: deletes_the_template is successful for parameters: {'template_id': '4023de96-169b-427c-a5eb-2daafc623d87'}"
        )

    def test_export_project_playbook_case_4(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_export_project_playbook_case_4,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("response")[1]
            .get("export")
            .get("response")
            .get("exportProject"),
            '[{"name":"sample_project","tags":[],"id":"ea8f12b6-067e-48f7-a552-61939f27bf3a","templates":[],"isDeletable":true}]',
        )

    def test_export_template_playbook_case_5(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_export_template_playbook_case_5,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("response")[1]
            .get("export")
            .get("response")
            .get("exportTemplate"),
            '[{"name":"AP_Onboarding","description":"","tags":[],"author":"admin",'
            '"deviceTypes":[{"productFamily":"Cisco Cloud Services Platform",'
            '"productSeries":"Cisco Cloud Services Platform 5000"}],"softwareType":"IOS",'
            '"softwareVariant":"","templateContent":"","templateParams":[],"rollbackTemplateParams":[],"composite":false,'
            '"containingTemplates":[],"language":"JINJA","promotedTemplateContent":"","promotedTemplateParams":[],"customParamsOrder":false,'
            '"createTime":1744111435353,"lastUpdateTime":1744111435353,"latestVersionTime":1744111435374,"projectName":"Onboarding Configuration",'
            '"projectId":"15922b60-be60-45e1-951a-4d9d7cb18a10","parentTemplateId":"17bc2a4c-06e8-4e1a-9711-852cf56477a3",'
            '"validationErrors":{"templateErrors":[],"rollbackTemplateErrors":[],"templateId":"17bc2a4c-06e8-4e1a-9711-852cf56477a3",'
            '"templateVersion":null},"noOfConflicts":0,"documentDatabase":false,"projectAssociated":true},'
            '{"name":"Test-ansible-composite","description":"","tags":[],"author":"admin",'
            '"deviceTypes":[{"productFamily":"Switches and Hubs","productSeries":"Cisco Catalyst 9500 Series Switches"}],'
            '"softwareType":"IOS","softwareVariant":"","templateParams":[],"rollbackTemplateParams":[],"composite":true,'
            '"containingTemplates":[{"name":"Test-ansible-regular","composite":false,"language":"JINJA","description":"",'
            '"templateParams":[],"projectName":"Test_Ansible","deviceTypes":[{"productFamily":"Switches and Hubs",'
            '"productSeries":"Cisco Catalyst 9500 Series Switches"}],"promotedTemplateParams":[],"tags":[],'
            '"parentTemplateId":"c353a7cf-732f-4d38-809d-17259a1655c4"}],'
            '"language":"JINJA","promotedTemplateContent":"[{\\"name\\":\\"Test-ansible-regular\\",\\"id\\":\\"c353a7cf-732f-4d38-809d-17259a1655c4\\",'
            '\\"composite\\":false,\\"language\\":\\"JINJA\\",\\"description\\":\\"\\"}]",'
            '"promotedTemplateParams":[],"customParamsOrder":false,"createTime":1744823885075,"lastUpdateTime":1744823895200,'
            '"latestVersionTime":1744823896547,"projectName":"Test_Ansible","projectId":"240e5e18-c285-4554-b4bf-f392f48a510a",'
            '"parentTemplateId":"a5854e9f-0f54-4364-8489-2361467ef9b0","validationErrors":{"templateErrors":[],"rollbackTemplateErrors":[],'
            '"templateId":"a5854e9f-0f54-4364-8489-2361467ef9b0",'
            '"templateVersion":null},"noOfConflicts":0,"documentDatabase":false,"projectAssociated":true}]',
        )

    def test_import_project_playbook_case_6(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="merged",
                config_verify=True,
                config=self.playbook_config_import_project_playbook_case_6,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("response")[2]
            .get("import")
            .get("response")
            .get("importProject"),
            "Successfully imported the project(s).",
        )

    def test_import_template_playbook_case_7(self):

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                dnac_log_level="DEBUG",
                state="merged",
                config_verify=True,
                config=self.playbook_config_import_template_playbook_case_7,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get("response")[2]
            .get("import")
            .get("response")
            .get("importTemplate"),
            "Successfully imported the templates",
        )
