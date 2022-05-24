#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2022, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = (
            "Madhan Sankaranarayanan, Rishita Chowdhary"
            )

DOCUMENTATION = r"""
---
module: template_module
short_description: Resource module for Site and PnP related functions
description:
- Manage operations add device, claim device and unclaim device of Onboarding Configuration(PnP) resource 
- API to add device to pnp inventory and claim it to a site.
- API to unclaim a device from a site.
- API will also create/add specified site it not found or needs update.
version_added: '6.4.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rishita Chowdhary (@rischowd)
options:
  state:
    description: The state of DNAC after module completion.
    type: str
    choices:
      - merged
      - deleted
    default: merged
  config:
    description:
    - List of details of device and site being managed. 
    type: list
    elements: dict
    suboptions:
      template_name:
        description: Name of template to be configured.
        type: str
      image_name:
        description: Name of image to be configured
        type: str
      golden_image:
        description: Is the image tagged golden_image
        type: bool
      type:
        description: Type of site to create (eg area, building, floor).
        type: str
      site:
        description: Site Details.
        type: dict
        suboptions:
          building:
            description: Building Details.
            type: dict
              suboptions:
                address:
                  description: Address of the building to be created.
                  type: str
                latitude:
                  description: Latitude coordinate of the building (eg 37.338).
                  type: int
                longitude:
                  description: Longitude coordinate of the building (eg -121.832).
                  type: int
                name:
                  description: Name of the building (eg building1).
                  type: str
                parentName:
                  description: Parent name of building to be created.
                  type: str
      deviceInfo:
        description: Pnp Device's deviceInfo.
        type: dict
        suboptions:
          aaaCredentials:
            description: Pnp Device's aaaCredentials.
            type: dict
            suboptions:
              password:
                description: Pnp Device's password.
                type: str
              username:
                description: Pnp Device's username.
                type: str        
          addedOn:
            description: Pnp Device's addedOn.
            type: int
          addnMacAddrs:
            description: Pnp Device's addnMacAddrs.
            elements: str
            type: list
          agentType:
            description: Pnp Device's agentType.
            type: str
          authStatus:
            description: Pnp Device's authStatus.
            type: str
          authenticatedSudiSerialNo:
            description: Pnp Device's authenticatedSudiSerialNo.
            type: str
          capabilitiesSupported:
            description: Pnp Device's capabilitiesSupported.
            elements: str
            type: list
          cmState:
            description: Pnp Device's cmState.
            type: str
          description:
            description: Pnp Device's description.
            type: str
          deviceSudiSerialNos:
            description: Pnp Device's deviceSudiSerialNos.
            elements: str
            type: list
          deviceType:
            description: Pnp Device's deviceType.
            type: str
          featuresSupported:
            description: Pnp Device's featuresSupported.
            elements: str
            type: list
          fileSystemList:
            description: Pnp Device's fileSystemList.
            type: list
            elements: dict
            suboptions:
              freespace:
                description: Pnp Device's freespace.
                type: int
              name:
                description: Pnp Device's name.
                type: str
              readable:
                description: Readable flag.
                type: bool
              size:
                description: Pnp Device's size.
                type: int
              type:
                description: Pnp Device's type.
                type: str
              writeable:
                description: Writeable flag.
                type: bool        
          firstContact:
            description: Pnp Device's firstContact.
            type: int
          hostname:
            description: Pnp Device's hostname.
            type: str
          httpHeaders:
            description: Pnp Device's httpHeaders.
            type: list
            elements: dict
            suboptions:
              key:
                description: Pnp Device's key.
                type: str
              value:
                description: Pnp Device's value.
                type: str        
          imageFile:
            description: Pnp Device's imageFile.
            type: str
          imageVersion:
            description: Pnp Device's imageVersion.
            type: str
          ipInterfaces:
            description: Pnp Device's ipInterfaces.
            elements: dict
            type: list
            suboptions:
              ipv4Address:
                description: Pnp Device's ipv4Address.
                type: dict
              ipv6AddressList:
                description: Pnp Device's ipv6AddressList.
                elements: dict
                type: list
              macAddress:
                description: Pnp Device's macAddress.
                type: str
              name:
                description: Pnp Device's name.
                type: str
              status:
                description: Pnp Device's status.
                type: str        
          lastContact:
            description: Pnp Device's lastContact.
            type: int
          lastSyncTime:
            description: Pnp Device's lastSyncTime.
            type: int
          lastUpdateOn:
            description: Pnp Device's lastUpdateOn.
            type: int
          location:
            description: Pnp Device's location.
            type: dict
            suboptions:
              address:
                description: Pnp Device's address.
                type: str
              altitude:
                description: Pnp Device's altitude.
                type: str
              latitude:
                description: Pnp Device's latitude.
                type: str
              longitude:
                description: Pnp Device's longitude.
                type: str
              siteId:
                description: Pnp Device's siteId.
                type: str       
          macAddress:
            description: Pnp Device's macAddress.
            type: str
          mode:
            description: Pnp Device's mode.
            type: str
          name:
            description: Pnp Device's name.
            type: str
          neighborLinks:
            description: Pnp Device's neighborLinks.
            type: list
            elements: dict
            suboptions:
              localInterfaceName:
                description: Pnp Device's localInterfaceName.
                type: str
              localMacAddress:
                description: Pnp Device's localMacAddress.
                type: str
              localShortInterfaceName:
                description: Pnp Device's localShortInterfaceName.
                type: str
              remoteDeviceName:
                description: Pnp Device's remoteDeviceName.
                type: str
              remoteInterfaceName:
                description: Pnp Device's remoteInterfaceName.
                type: str
              remoteMacAddress:
                description: Pnp Device's remoteMacAddress.
                type: str
              remotePlatform:
                description: Pnp Device's remotePlatform.
                type: str
              remoteShortInterfaceName:
                description: Pnp Device's remoteShortInterfaceName.
                type: str
              remoteVersion:
                description: Pnp Device's remoteVersion.
                type: str        
          onbState:
            description: Pnp Device's onbState.
            type: str
          pid:
            description: Pnp Device's pid.
            type: str
          pnpProfileList:
            description: Pnp Device's pnpProfileList.
            type: list
            elements: dict
            suboptions:
              createdBy:
                description: Pnp Device's createdBy.
                type: str
              discoveryCreated:
                description: DiscoveryCreated flag.
                type: bool
              primaryEndpoint:
                description: Pnp Device's primaryEndpoint.
                type: dict
                suboptions:
                  certificate:
                    description: Pnp Device's certificate.
                    type: str
                  fqdn:
                    description: Pnp Device's fqdn.
                    type: str
                  ipv4Address:
                    description: Pnp Device's ipv4Address.
                    type: dict
                  ipv6Address:
                    description: Pnp Device's ipv6Address.
                    type: dict
                  port:
                    description: Pnp Device's port.
                    type: int
                  protocol:
                    description: Pnp Device's protocol.
                    type: str            
              profileName:
                description: Pnp Device's profileName.
                type: str
              secondaryEndpoint:
                description: Pnp Device's secondaryEndpoint.
                type: dict
                suboptions:
                  certificate:
                    description: Pnp Device's certificate.
                    type: str
                  fqdn:
                    description: Pnp Device's fqdn.
                    type: str
                  ipv4Address:
                    description: Pnp Device's ipv4Address.
                    type: dict
                  ipv6Address:
                    description: Pnp Device's ipv6Address.
                    type: dict
                  port:
                    description: Pnp Device's port.
                    type: int
                  protocol:
                    description: Pnp Device's protocol.
                    type: str           
          populateInventory:
            description: PopulateInventory flag.
            type: bool
          preWorkflowCliOuputs:
            description: Pnp Device's preWorkflowCliOuputs.
            type: list
            elements: dict
            suboptions:
              cli:
                description: Pnp Device's cli.
                type: str
              cliOutput:
                description: Pnp Device's cliOutput.
                type: str        
          projectId:
            description: Pnp Device's projectId.
            type: str
          projectName:
            description: Pnp Device's projectName.
            type: str
          reloadRequested:
            description: ReloadRequested flag.
            type: bool
          serialNumber:
            description: Pnp Device's serialNumber.
            type: str
          smartAccountId:
            description: Pnp Device's smartAccountId.
            type: str
          source:
            description: Pnp Device's source.
            type: str
          stack:
            description: Stack flag.
            type: bool
          stackInfo:
            description: Pnp Device's stackInfo.
            type: dict
            suboptions:
              isFullRing:
                description: IsFullRing flag.
                type: bool
              stackMemberList:
                description: Pnp Device's stackMemberList.
                type: list
                elements: dict
                suboptions:
                  hardwareVersion:
                    description: Pnp Device's hardwareVersion.
                    type: str
                  licenseLevel:
                    description: Pnp Device's licenseLevel.
                    type: str
                  licenseType:
                    description: Pnp Device's licenseType.
                    type: str
                  macAddress:
                    description: Pnp Device's macAddress.
                    type: str
                  pid:
                    description: Pnp Device's pid.
                    type: str
                  priority:
                    description: Pnp Device's priority.
                    type: int
                  role:
                    description: Pnp Device's role.
                    type: str
                  serialNumber:
                    description: Pnp Device's serialNumber.
                    type: str
                  softwareVersion:
                    description: Pnp Device's softwareVersion.
                    type: str
                  stackNumber:
                    description: Pnp Device's stackNumber.
                    type: int
                  state:
                    description: Pnp Device's state.
                    type: str
                  sudiSerialNumber:
                    description: Pnp Device's sudiSerialNumber.
                    type: str           
              stackRingProtocol:
                description: Pnp Device's stackRingProtocol.
                type: str
              supportsStackWorkflows:
                description: SupportsStackWorkflows flag.
                type: bool
              totalMemberCount:
                description: Pnp Device's totalMemberCount.
                type: int
              validLicenseLevels:
                description: Pnp Device's validLicenseLevels.
                elements: str        
          state:
            description: Pnp Device's state.
            type: str
          sudiRequired:
            description: SudiRequired flag.
            type: bool
          tags:
            description: Pnp Device's tags.
            type: dict
          userSudiSerialNos:
            description: Pnp Device's userSudiSerialNos.
            elements: str
            type: list
          virtualAccountId:
            description: Pnp Device's virtualAccountId.
            type: str
          workflowId:
            description: Pnp Device's workflowId.
            type: str
          workflowName:
            description: Pnp Device's workflowName.
            type: str
        

requirements:
- dnacentersdk == 2.4.5
- python >= 3.5
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.add_device,
    device_onboarding_pnp.DeviceOnboardingPnp.claim_a_device_to_a_site,
    device_onboarding_pnp.DeviceOnboardingPnp.un_claim_device,
    device_onboarding_pnp.DeviceOnboardingPnp.get_device_list

  - Paths used are
    post /dna/intent/api/v1/onboarding/pnp-device
    post /dna/intent/api/v1/onboarding/pnp-device/site-claim
    post /dna/intent/api/v1/onboarding/pnp-device/unclaim
    get /dna/intent/api/v1/onboarding/pnp-device

"""
EXAMPLES = r"""
- name: claim device
  cisco.dnac.pnp_module:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    state: merged
    config:
        template_name: string
        image_name: string
        type: string
        site:
        building:
            address: string
            latitude: 0
            longitude: 0
            name: string
            parentName: string
        deviceInfo:
        aaaCredentials:
            password: string
            username: string
        addedOn: 0
        addnMacAddrs:
        - string
        agentType: string
        authStatus: string
        authenticatedSudiSerialNo: string
        capabilitiesSupported:
        - string
        cmState: string
        description: string
        deviceSudiSerialNos:
        - string
        deviceType: string
        featuresSupported:
        - string
        fileSystemList:
        - freespace: 0
            name: string
            readable: true
            size: 0
            type: string
            writeable: true
        firstContact: 0
        hostname: string
        httpHeaders:
        - key: string
            value: string
        imageFile: string
        imageVersion: string
        ipInterfaces:
        - ipv4Address: {}
            ipv6AddressList:
            - {}
            macAddress: string
            name: string
            status: string
        lastContact: 0
        lastSyncTime: 0
        lastUpdateOn: 0
        location:
            address: string
            altitude: string
            latitude: string
            longitude: string
            siteId: string
        macAddress: string
        mode: string
        name: string
        neighborLinks:
        - localInterfaceName: string
            localMacAddress: string
            localShortInterfaceName: string
            remoteDeviceName: string
            remoteInterfaceName: string
            remoteMacAddress: string
            remotePlatform: string
            remoteShortInterfaceName: string
            remoteVersion: string
        onbState: string
        pid: string
        pnpProfileList:
        - createdBy: string
          discoveryCreated: true
          primaryEndpoint:
            certificate: string
            fqdn: string
            ipv4Address: {}
            ipv6Address: {}
            port: 0
            protocol: string
          profileName: string
          secondaryEndpoint:
            certificate: string
            fqdn: string
            ipv4Address: {}
            ipv6Address: {}
            port: 0
            protocol: string
        populateInventory: true
        preWorkflowCliOuputs:
        - cli: string
          cliOutput: string
        projectId: string
        projectName: string
        reloadRequested: true
        serialNumber: string
        smartAccountId: string
        source: string
        stack: true
        stackInfo:
            isFullRing: true
            stackMemberList:
            - hardwareVersion: string
              licenseLevel: string
              licenseType: string
              macAddress: string
              pid: string
              priority: 0
              role: string
              serialNumber: string
              softwareVersion: string
              stackNumber: 0
                state: string
                sudiSerialNumber: string
            stackRingProtocol: string
            supportsStackWorkflows: true
            totalMemberCount: 0
            validLicenseLevels:
            - string
        state: string
        sudiRequired: true
        tags: {}
        userSudiSerialNos:
        - string
        virtualAccountId: string
        workflowId: string
        workflowName: string
"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": String,
	  "version": 0
    }
"""
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

        if self.params.get("state") == "merged":

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


    def get_diff_delete(self):

        if self.have.get("device_found"):

            unclaim_params = dict(
                deviceIdList=[self.have.get("device_id")],
            )
            unclaim_response = self.dnac.exec(
                family="device_onboarding_pnp",
                function='un_claim_device',
                op_modifies=True,
                params=unclaim_params,
            )
            if self.log:
                log(str(unclaim_response))
             
            if (unclaim_response.get("message")=="Device(s) Unclaimed"):
                self.result['changed'] = True
                self.result['response'] = unclaim_response
                self.result['diff'] = self.validated
            else:
                self.module.fail_json(msg="Device Un-Claim Failed")
        else:
            self.module.fail_json(msg="Device Not Found")
        


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

    if state == "delete":
        dnac_pnp.get_diff_delete()

    module.exit_json(**dnac_pnp.result)


if __name__ == '__main__':
    main()
