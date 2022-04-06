
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2022, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import copy
import time 
try:
    from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
        AnsibleArgSpecValidator,
    )
except ImportError:
    ANSIBLE_UTILS_IS_INSTALLED = False
else:
    ANSIBLE_UTILS_IS_INSTALLED = True
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DNACSDK,
    dnac_argument_spec,
    validate_list_of_dicts,
    log,
    get_dict_result,
    dnac_compare_equality,
)
from ansible.module_utils.basic import AnsibleModule



class DnacTemplate:


    def __init__(self, module):
        self.module = module
        self.params = module.params
        self.config = copy.deepcopy(module.params.get("config"))
        self.have_create = []
        self.want_create = []
        self.diff_create = []
        self.validated = []
        dnac_params = self.get_dnac_params(self.params)
        log(str(dnac_params))
        self.dnac = DNACSDK(params=dnac_params)

        self.result = dict(changed=False, diff=[], response=[], warnings=[])

    def get_state(self):
        return self.params.get("state")

    def validate_input(self):
        
        temp_spec = dict(
            project_name=dict(required=True, type='str'),
            template_content=dict(required=False, type='str'),
            language=dict(required=False, choices=['velocity', 'jinja']),
            device_types=dict(required=False, type='list', elements='dict'),
            software_type=dict(required=False, type='str'),
            software_variant=dict(required=False, type='str'),
            version_description=dict(required=False, type='str'),
            template_name=dict(required=True, type='str'),
            )

        if self.config:
            msg = None
            # Validate template params
            valid_temp, invalid_params = validate_list_of_dicts(
                self.config, temp_spec
            )

            if invalid_params:
                msg = "Invalid parameters in playbook: {0}".format(
                    "\n".join(invalid_params)
                )
                self.module.fail_json(msg=msg)

            log(str(valid_temp))
            self.validated = valid_temp
            log(str(self.validated))


    def get_dnac_params(self, params):
        dnac_params = dict(
            dnac_host=params.get("dnac_host"),
            dnac_port=params.get("dnac_port"),
            dnac_username=params.get("dnac_username"),
            dnac_password=params.get("dnac_password"),
            dnac_verify=params.get("dnac_verify"),
            dnac_debug=params.get("dnac_debug"),
        )
        return dnac_params

    def get_temp_params(self, params):
        temp_params = dict(
            tags=params.get("template_tag"),
            author=params.get("author"),
            composite=params.get("composite"),
            containingTemplates=params.get("containingTemplates"),
            createTime=params.get("createTime"),
            customParamsOrder=params.get("customParamsOrder"),
            description=params.get("description"),
            deviceTypes=params.get("device_types"),
            failurePolicy=params.get("failurePolicy"),
            id=params.get("templateId"),
            language=params.get("language").upper(),
            lastUpdateTime=params.get("lastUpdateTime"),
            latestVersionTime=params.get("latestVersionTime"),
            name=params.get("template_name"),
            parentTemplateId=params.get("parentTemplateId"),
            projectId=params.get("projectId"),
            projectName=params.get("project_name"),
            rollbackTemplateContent=params.get("rollbackTemplateContent"),
            rollbackTemplateParams=params.get("rollbackTemplateParams"),
            softwareType=params.get("software_type"),
            softwareVariant=params.get("software_variant"),
            softwareVersion=params.get("softwareVersion"),
            templateContent=params.get("template_content"),
            templateParams=params.get("templateParams"),
            validationErrors=params.get("validationErrors"),
            version=params.get("version"),
            project_id=params.get("projectId"),
        )
        return temp_params


    def get_version_params(self, params):
        version_params = dict(
            comments=params.get("version_description"),
            templateId=params.get("templateId"),
        )
        return version_params

    def check_required_parameters(self):
        for temp in self.validated:
            if not temp.get("language") or not temp.get("device_types") \
                    or not temp.get("software_type"):
                    msg = "missing required arguments: language or deviceTypes or softwareType"
                    self.module.fail_json(msg=msg)

    def get_template(self):

        result = None
        for temp in self.validated:
            items = self.dnac.exec(
                family="configuration_templates",
                function="get_template_details",
                params={"template_id": temp.get("templateId")}
            )
            if items:
                result = items
                log(str(items))

        self.result['response'] = items 
        return result

    def template_exists(self):
        prev_obj = None
        temp_exists = False

        #Get available templates. Filter templates based on provided projectName
        for temp in self.validated:
            template_list = self.dnac.exec(
                family="configuration_templates",
                function='gets_the_templates_available',
                params={"project_names":temp.get("project_name")},
            )
            #API execution error returns a dict
            if template_list and isinstance(template_list, list):
                template_details = get_dict_result(template_list, 'name', temp.get("template_name"))
                if template_details:
                    temp["templateId"] = template_details.get("templateId")
                    prev_obj = self.get_template()
                    log(str(prev_obj))

                temp_exists = prev_obj is not None and isinstance(prev_obj, dict)
                return(temp_exists, prev_obj)
            else:
                self.module.fail_json(msg="Project Not Found")

    def requires_update(self, current_obj):

        for temp in self.validated:
            requested_obj = self.get_temp_params(temp)

            obj_params = [
                ("tags", "tags"),
                ("author", "author"),
                ("composite", "composite"),
                ("containingTemplates", "containingTemplates"),
                ("createTime", "createTime"),
                ("customParamsOrder", "customParamsOrder"),
                ("description", "description"),
                ("deviceTypes", "deviceTypes"),
                ("failurePolicy", "failurePolicy"),
                ("id", "id"),
                ("language", "language"),
                ("lastUpdateTime", "lastUpdateTime"),
                ("latestVersionTime", "latestVersionTime"),
                ("name", "name"),
                ("parentTemplateId", "parentTemplateId"),
                ("projectId", "projectId"),
                ("projectName", "projectName"),
                ("rollbackTemplateContent", "rollbackTemplateContent"),
                ("rollbackTemplateParams", "rollbackTemplateParams"),
                ("softwareType", "softwareType"),
                ("softwareVariant", "softwareVariant"),
                ("softwareVersion", "softwareVersion"),
                ("templateContent", "templateContent"),
                ("templateParams", "templateParams"),
                ("validationErrors", "validationErrors"),
                ("version", "version"),
                #("templateId", "template_id"),
            ]
            return any(not dnac_compare_equality(current_obj.get(dnac_param),
                                                 requested_obj.get(ansible_param))
                       for (dnac_param, ansible_param) in obj_params)

    def version_template(self):
            
        for temp in self.validated:
            response = self.dnac.exec(
                family="configuration_templates",
                function='version_template',
                op_modifies=True,
                params=self.get_version_params(temp)
            )
 

        log("Template Committed")
        self.result['changed'] = True
        self.result['response'] = response
        self.result['diff'] = self.validated

    def update(self):

        for temp in self.validated:
            response = self.dnac.exec(
                family="configuration_templates",
                function="update_template",
                params=self.get_temp_params(temp),
                op_modifies=True,
            )

        log("Updating Existing Template")
        self.version_template()
        self.dnac.object_updated()

    def get_project_id(self):

        for temp in self.validated:
            items = self.dnac.exec(
                family="configuration_templates",
                function='get_projects',
                params={"name":temp.get("project_name")},
            )

            temp["projectId"] = items[0].get("id")

        log(str(self.validated))

    def get_task_details(self, id):
        result = None
        response = self.dnac.exec(
            family="task",
            function='get_task_by_id',
            params={"task_id":id},
        )
        if isinstance(response, dict):
            result = response.get("response")
        return result

    def create_template(self):

        self.get_project_id()
        template_id = None

        for temp in self.validated:
            response = self.dnac.exec(
                family="configuration_templates",
                function='create_template',
                op_modifies=True,
                params=self.get_temp_params(temp),
            )
            time.sleep(10) 
            log("Template created. Get template_id for versioning")
            if isinstance(response, dict):
                task_id = response.get("response").get("taskId")
                if task_id:
                    task_details = self.get_task_details(task_id)
                    log(str(task_details))
                    if task_details and isinstance(task_details, dict) \
                        and (task_details.get("isError")==False):
                        template_id = task_details.get("data")
            if template_id:
                temp["templateId"] = template_id
                self.version_template()
                self.dnac.object_created()

        log(str(self.validated))

    def delete_template(self):
        for temp in self.validated:
            response = self.dnac.exec(
                family="configuration_templates",
                function="deletes_the_template",
                params={"template_id": temp.get("templateId")},
            )

        self.dnac.object_deleted()
        self.result['changed'] = True
        self.result['response'] = response


def main():
    """ main entry point for module execution
    """

    element_spec = dict(
        dnac_host=dict(required=False, type='str'),
        dnac_port=dict(required=False, type='str', default='443'),
        dnac_username=dict(required=False, type='str', no_log=True),
        dnac_password=dict(required=False, type='str', no_log=True),
        dnac_verify=dict(required=False, type='bool', default='False'),
        dnac_debug=dict(required=False, type='bool', default='False'),
        config=dict(required=False, type='list', elements='dict'),
        state=dict(default='merged',
            choices=['merged', 'delete', 'query']),
        )

    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    dnac_template = DnacTemplate(module)
    dnac_template.validate_input()
    state = dnac_template.get_state()

    prev_template = None
    template_exists = False
    (template_exists, prev_template) = dnac_template.template_exists()
    
    if state == "merged":
        dnac_template.check_required_parameters()
        if template_exists:
            #if template exists, update if needed.
            if dnac_template.requires_update(prev_template):
                dnac_template.update()
            else:
                log("Template does not need update")
                dnac_template.result['response'] = prev_template
                module.exit_json(msg="Template does not need update")
        else:
            log("Create new template")
            dnac_template.create_template()

    elif state == "query":
        if template_exists:
            dnac_template.get_template()
        else:
            #module.fail_json(msg="Template not found")
            module.exit_json(msg="Template not found")

    elif state == "delete":
        if template_exists:
            dnac_template.delete_template()
        else:
            #module.fail_json("Template not found")
            module.exit_json(msg="Template not found")
    
    module.exit_json(**dnac_template.result)

if __name__ == '__main__':
    main()
