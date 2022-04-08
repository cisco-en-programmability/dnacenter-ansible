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



class DnacPnp:


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
        self.log = dnac_params.get("dnac_log")

        self.result = dict(changed=False, diff=[], response=[], warnings=[])


    def validate_input(self):
        
        pnp_spec = dict(
            type=dict(required=False, type='str'),
            template_name=dict(required=True, type='str'),
            project_name=dict(required=False, type='str', default="Onboarding Configuration"),
            site=dict(required=True, type='dict'),
            image_name=dict(required=True, type='str'),
            golden_image=dict(required=False, type='bool'),
            deviceInfo=dict(required=True, type='dict'),
            pnp_type=dict(required=False, type=str, default="Default")
            #template_tag=dict(required=False, type='str'),
            #device_version=dict(required=False, type='str'),
            )

        if self.config:
            msg = None
            # Validate template params
            if self.log:
                log(str(self.config))
            valid_pnp, invalid_params = validate_list_of_dicts(
                self.config, pnp_spec
            )

            if invalid_params:
                msg = "Invalid parameters in playbook: {0}".format(
                    "\n".join(invalid_params)
                )
                self.module.fail_json(msg=msg)

            self.validated = valid_pnp
            if self.log:
                log(str(valid_pnp))
                log(str(self.validated))


    def get_dnac_params(self, params):
        dnac_params = dict(
            dnac_host=params.get("dnac_host"),
            dnac_port=params.get("dnac_port"),
            dnac_username=params.get("dnac_username"),
            dnac_password=params.get("dnac_password"),
            dnac_verify=params.get("dnac_verify"),
            dnac_debug=params.get("dnac_debug"),
            dnac_log=params.get("dnac_log")
        )
        return dnac_params


    def get_site_params(self, params):
        site_params = dict(
            type=params.get("type"),
            site=params.get("site"),
            site_id=params.get("siteId")
        )
        return site_params

    def get_image_params(self, params):
        image_params = dict(
            image_name=params.get("image_name"),
            is_tagged_golden=params.get("golden_image"),
        )
        return image_params


    def get_pnp_params(self, params):
        pnp_params = {}
        pnp_params['_id'] = params.get('_id')
        pnp_params['deviceInfo'] = params.get('deviceInfo')
        pnp_params['runSummaryList'] = params.get('runSummaryList')
        pnp_params['systemResetWorkflow'] = params.get('systemResetWorkflow')
        pnp_params['systemWorkflow'] = params.get('systemWorkflow')
        pnp_params['tenantId'] = params.get('tenantId')
        pnp_params['version'] = params.get('device_version')
        pnp_params['workflow'] = params.get('workflow')
        pnp_params['workflowParameters'] = params.get('workflowParameters')
        return pnp_params


    def get_claim_params(self, params):
        claim_params = dict(
            deviceId=params.get("deviceId"),
            siteId=params.get("siteId"),
            type=params.get("pnp_type"),
            #imageInfo={},
            #configInfo={},
            imageInfo=params.get("imageInfo"),
            configInfo=params.get("configInfo"),
            hostname=params.get("hostname"),
        )
        return claim_params

    def get_site_name(self, site):
        parent_name = site.get("site").get("building").get("parentName")
        building_name = site.get("site").get("building").get("name")

        site_name = '/'.join([parent_name, building_name])
        if self.log:
            log(site_name)
        return site_name

    def get_current_site(self,site):
            site_info = {}
            type = site[0].get("additionalInfo")[0].get("attributes").get("type")
            if (type=="building"):
                site_info = dict(
                    building=dict(
                        name= site[0].get("name"),
                        parentName = site[0].get("siteNameHierarchy").split("/"+site[0].get("name"))[0],
                        address=site[0].get("additionalInfo")[0].get("attributes").get("address"),
                        latitude = site[0].get("additionalInfo")[0].get("attributes").get("latitude"),
                        longitude = site[0].get("additionalInfo")[0].get("attributes").get("longitude"),
                    )
                )
            current_site = dict(
                type=type,
                site=site_info,
                site_id=site[0].get("id")
            )
            if self.log:
                log(str(current_site))
            return current_site

    def site_exists(self):
        site_exists = False
        current_site = {}
        response = None
        for site in self.validated:
            try:
                response = self.dnac.exec(
                    family="sites",
                    function='get_site',
                    params={"name":self.get_site_name(site)},
                )
            except:
                if self.log:
                    log("The input site is not valid or site is not present.")
                pass

            if response:
                if self.log:
                    log(str(response))
                response = response.get("response")
                current_site = self.get_current_site(response) 
                site["siteId"] = current_site.get("site_id")
                site_exists = True
    
        if self.log:
            log(str(self.validated))
        return (site_exists, current_site)

    def site_requires_update(self, curr_site):
        for site in self.validated:
            requested_obj = self.get_site_params(site)
            if self.log:
                log(str(requested_obj))
        
        obj_params = [
            ("type", "type"),
            ("site", "site")
        ]
        return any(not dnac_compare_equality(curr_site.get(dnac_param),
                                             requested_obj.get(ansible_param))
                   for (dnac_param, ansible_param) in obj_params)

    def update_site(self):
        for site in self.validated:
            response = self.dnac.exec(
                family="sites",
                function='update_site',
                op_modifies=True,
                params=self.get_site_params(site),
            )
        if self.log:
            log("Site Updated")

    def get_execution_details(self, id):
        response = None
        response = self.dnac.exec(
            family="task",
            function='get_business_api_execution_details',
            params={"execution_id":id}
        )
        if self.log:
            log(str(response))
        if response and isinstance(response, dict):
            return response

    def create_site(self):
        for site in self.validated:
            response = self.dnac.exec(
                family="sites",
                function='create_site',
                op_modifies=True,
                params=self.get_site_params(site),
            )
            if self.log:
                log(str(response))
            if response and isinstance(response, dict):
                executionId = response.get("executionId")
                while (True):
                    execution_details = self.get_execution_details(executionId)
                    if (execution_details.get("status")=="SUCCESS"):
                        break
                    if execution_details.get("bapiError"):
                        self.module.fail_json(msg=execution_details.get("bapiError"))
                        break

                self.result['changed'] = True
                if self.log:
                    log("Site Created Successfully")
                self.site_exists()#Used for storing site_id

    def get_image_id(self):
        for image in self.validated:
            imageinfo = dict(imageId=None)
            response = self.dnac.exec(
                family="software_image_management_swim",
                function='get_software_image_details',
                params=self.get_image_params(image),
            )
            if self.log:
                log(str(response))
            image_list = response.get("response")
            if (len(image_list)==1):
                image["imageUuid"] = image_list[0].imageUuid
                imageinfo["imageId"]=image_list[0].imageUuid
                image["imageInfo"] = imageinfo
                if self.log:
                    log(str(image["imageInfo"]))
                    log(str(self.validated))
            else:
                self.module.fail_json(msg="Image not found")
    
    def get_template_id(self):
        for temp in self.validated:
            configinfo = dict(configId=None, configParameters=[dict(key="", value="")])
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
                    configinfo["configId"] = template_details.get("templateId")
                    temp["configInfo"] = configinfo
                    if self.log:
                        log(temp["templateId"])
                        log(str(self.validated))
                else:
                    self.module.fail_json(msg="Template not found")
            else:
                self.module.fail_json(msg="Project Not Found")

    def find_device_pnp(self):
        device_found = False
        for device in self.validated:
            response = self.dnac.exec(
                family="device_onboarding_pnp",
                function='get_device_list',
                params={"serial_number":device.get("deviceInfo").get("serialNumber")},
            )
            if self.log:
                log(str(response))
            if response and (len(response)==1):
                device["deviceId"] = response[0].get("id") 
                if self.log:
                    log(device["deviceId"])
                device_found = True
        return device_found

    def add_device_to_pnp_db(self):
        for device in self.validated:
            response = self.dnac.exec(
                family="device_onboarding_pnp",
                function="add_device",
                params=self.get_pnp_params(device),
                op_modifies=True,
            )
            device["deviceId"] = response.id
            if self.log:
                log(str(response))
                log(device["deviceId"])

    def claim_device_to_site(self):
        for info in self.validated:
            response = self.dnac.exec(
                family="device_onboarding_pnp",
                function='claim_a_device_to_a_site',
                op_modifies=True,
                params=self.get_claim_params(info),
            )
            if self.log:
                log(str(response))
            if (response.get("response")=="Device Claimed"):
                self.result['changed'] = True
                self.result['response'] = response
                self.result['diff'] = self.validated
            else:
                self.module.fail_json(msg="Device Claim Failed")

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
        dnac_log=dict(required=False, type='bool', default='False'),
        config=dict(required=False, type='list', elements='dict'),
        )

    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    dnac_pnp = DnacPnp(module)
    dnac_pnp.validate_input()

    dnac_pnp.get_image_id()
    dnac_pnp.get_template_id()

    (site_exists, prev_site) = dnac_pnp.site_exists()
    if site_exists:
        if dnac_pnp.site_requires_update(prev_site):
            log("site requires update")
            dnac_pnp.update_site()
    else:
        log("Creating new site")
        dnac_pnp.create_site()


    device_in_pnp_db = dnac_pnp.find_device_pnp()
    if not device_in_pnp_db:
        log("Adding device to PnP Database")
        dnac_pnp.add_device_to_pnp_db()

    dnac_pnp.claim_device_to_site()

    module.exit_json(**dnac_pnp.result)

if __name__ == '__main__':
    main()
