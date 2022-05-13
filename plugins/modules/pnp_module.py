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
        self.have = []
        self.want = []
        self.diff = []
        self.validated = []
        dnac_params = self.get_dnac_params(self.params)
        log(str(dnac_params))
        self.dnac = DNACSDK(params=dnac_params)
        self.log = dnac_params.get("dnac_log")

        self.result = dict(changed=False, diff=[], response=[], warnings=[])


    def get_state(self):
        return self.params.get("state")


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
        try:
            response = self.dnac.exec(
                family="sites",
                function='get_site',
                params={"name":self.want.get("site_name")},
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
            site_exists = True
    
        if self.log:
            log(str(self.validated))
        return (site_exists, current_site)


    def get_site_name(self, site):
        parent_name = site.get("site").get("building").get("parentName")
        building_name = site.get("site").get("building").get("name")

        site_name = '/'.join([parent_name, building_name])
        if self.log:
            log(site_name)
        return site_name

    def get_pnp_params(self,params):
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


    def get_site_params(self, params):
        site_params = dict(
            type=params.get("type"),
            site=params.get("site"),
        )
        return site_params


    def get_image_params(self,params):
        image_params = dict(
            image_name=params.get("image_name"),
            is_tagged_golden=params.get("golden_image"),
        )
        return image_params


    def site_requires_update(self):
        requested_site = self.want.get("site_params")
        current_site = self.have.get("current_site")

        if self.log:
            log("Current Site: " + str(current_site))
            log("Requested Site: " + str(requested_site))

        obj_params = [
            ("type", "type"),
            ("site", "site")
        ]
        return any(not dnac_compare_equality(current_site.get(dnac_param),
                                             requested_site.get(ansible_param))
                   for (dnac_param, ansible_param) in obj_params)


    def update_site(self):
        site_params = self.want.get("site_params")
        site_params["site_id"] = self.have.get("site_id")

        response = self.dnac.exec(
            family="sites",
            function='update_site',
            op_modifies=True,
            params=site_params,
        )
        if self.log:
            log(str(response))

    
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
        response = self.dnac.exec(
            family="sites",
            function='create_site',
            op_modifies=True,
            params=self.want.get("site_params"),
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
                                                   
            #Get the site id of the newly created site.                                                   
            (site_exists, current_site) = self.site_exists()
            if site_exists:
                self.have["site_id"] = current_site.get("site_id") 

    
    def get_claim_params(self):
       
        imageinfo = dict(
            imageId = self.have.get("image_id")
        )
        configinfo = dict(
            configId = self.have.get("template_id"),
            configParameters = [dict(
                key="",
                value=""
            )]
        )
        claim_params = dict(
            deviceId=self.have.get("device_id"),
            siteId=self.have.get("site_id"),
            type=self.want.get("pnp_type"),
            hostname=self.want.get("hostname"),
            imageInfo=imageinfo,
            configInfo=configinfo,
        )
        return claim_params


    def get_have(self):

        have = {}

        #check if given image exists, if exists store image_id
        image_response = self.dnac.exec(
            family="software_image_management_swim",
            function='get_software_image_details',
            params=self.want.get("image_params"),
        )
        if self.log:
            log(str(image_response))
        image_list = image_response.get("response")
        if (len(image_list)==1):
            have["image_id"]=image_list[0].get("imageUuid")
            if self.log:
                log("Image Id: " + str(have["image_id"]))
        else:
            self.module.fail_json(msg="Image not found")


        #check if given template exists, if exists store template id
        template_list = self.dnac.exec(
            family="configuration_templates",
            function='gets_the_templates_available',
            params={"project_names":self.want.get("project_name")},
        )
        if self.log:
            log(str(template_list))

        if template_list and isinstance(template_list, list): #API execution error returns a dict
            template_details = get_dict_result(template_list, 'name', self.want.get("template_name"))
            if template_details:
                have["template_id"] = template_details.get("templateId")
                if self.log:
                    log("Template Id: " + str(have["template_id"]))
            else:
                self.module.fail_json(msg="Template not found")
        else:
            self.module.fail_json(msg="Project Not Found")


        #check if given site exits, if exists store current site info
        (site_exists, current_site) = self.site_exists()
        if self.log:
            log("Site Exists: " + str(site_exists) + "\n Current Site:" + str(current_site))
        if site_exists:
            have["site_id"] = current_site.get("site_id")

        have["site_exists"] = site_exists
        have["current_site"] = current_site


        #check if given device exists in pnp inventory, store device Id
        device_response = self.dnac.exec(
            family="device_onboarding_pnp",
            function='get_device_list',
            params={"serial_number":self.want.get("serial_number")}
        )
        if self.log:
            log(str(device_response))
        if device_response and (len(device_response)==1):
            have["device_id"] = device_response[0].get("id")
            have["device_found"] = True
            if self.log:
                log("Device Id: " + str(have["device_id"]))
        else:
            have["device_found"] = False

        self.have = have



    def get_want(self):

        for params in self.validated:
            want = dict(
                site_params = self.get_site_params(params), 
                site_name = self.get_site_name(params),
                image_params = self.get_image_params(params),
                pnp_params = self.get_pnp_params(params),
                pnp_type = params.get("pnp_type"),
                serial_number = params.get("deviceInfo").get("serialNumber"),
                hostname = params.get("deviceInfo").get("hostname"),
                project_name = params.get("project_name"),
                template_name = params.get("template_name")
            )

        self.want = want


    def get_diff_merge(self):

        #check if the given site exists and/or needs to be updated/created.
        if self.have.get("site_exists"):
            if self.site_requires_update():
                log("Existing Site requires update")
                self.update_site()
        else:
            log("Creating New Site")
            self.create_site()

        #if given device doesnot exist then add it to pnp database and get the device id
        if not self.have.get("device_found"):
            log("Adding device to pnp database")
            response = self.dnac.exec(
                family="device_onboarding_pnp",
                function="add_device",
                params=self.want.get("pnp_params"),
                op_modifies=True,
            )
            self.have["device_id"] = response.get("id")
            if self.log:
                log(str(response))
                log(self.have.get("device_id"))

        claim_params = self.get_claim_params()
        claim_response = self.dnac.exec(
            family="device_onboarding_pnp",
            function='claim_a_device_to_a_site',
            op_modifies=True,
            params=claim_params,
        )
        if self.log:
            log(str(claim_response))
        if (claim_response.get("response")=="Device Claimed"):
            self.result['changed'] = True
            self.result['response'] = claim_response
            self.result['diff'] = self.validated
        else:
            self.module.fail_json(msg="Device Claim Failed")


def main():
    """ main entry point for module execution
    """

    element_spec = dict(
        dnac_host=dict(required=True, type='str'),
        dnac_port=dict(required=False, type='str', default='443'),
        dnac_username=dict(required=True, type='str', no_log=True),
        dnac_password=dict(required=True, type='str', no_log=True),
        dnac_verify=dict(required=False, type='bool', default='False'),
        dnac_debug=dict(required=False, type='bool', default='False'),
        dnac_log=dict(required=False, type='bool', default='False'),
        config=dict(required=False, type='list', elements='dict'),
        state=dict(
            default='merged',
            choices=['merged', 'delete']
        )
    )

    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    dnac_pnp = DnacPnp(module)
    dnac_pnp.validate_input()
    state = dnac_pnp.get_state()

    dnac_pnp.get_want()
    dnac_pnp.get_have()

    if state == "merged":
        dnac_pnp.get_diff_merge()

    module.exit_json(**dnac_pnp.result)


if __name__ == '__main__':
    main()
