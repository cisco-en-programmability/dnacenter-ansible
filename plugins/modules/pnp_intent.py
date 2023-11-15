#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2022, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Madhan Sankaranarayanan, Rishita Chowdhary, Abinash Mishra")

DOCUMENTATION = r"""
---
module: pnp_intent
short_description: Resource module for Site and PnP related functions
description:
- Manage operations add device, claim device and unclaim device of Onboarding Configuration(PnP) resource
- API to add device to pnp inventory and claim it to a site.
- API to delete device from the pnp inventory.
version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.intent_params
author: Madhan Sankaranarayanan (@madhansansel)
        Rishita Chowdhary (@rishitachowdhary)
        Abinash Mishra (@abimishr)
options:
  state:
    description: The state of DNAC after module completion.
    type: str
    choices: [ merged, deleted ]
    default: merged
  config:
    description:
    - List of details of device being managed.
    type: list
    elements: dict
    required: true
    suboptions:
      template_name:
        description: Name of template to be configured on the device.
        type: str
      image_name:
        description: Name of image to be configured on the device
        type: str
      golden_image:
        description: Is the image to be condifgured tagged as golden image
        type: bool
      site_name:
        description: Name of the site for which device will be claimed.
        type: str
      projectName:
        description: Name of the project under which the template is present
        type: str
        default: Onboarding Configuration
      pnp_type:
        description: Device type of the Pnp device (Default/CatalystWLC/AccessPoint)
        type: str
        default: Default
      staticIP:
        description: Management IP address of the Wireless Controller
        type: str
      subnetMask:
        description: Subnet Mask of the Management IP address of the Wireless Controller
        type: str
      gateway:
        description: Gateway IP address of the Wireless Controller for getting pinged
        type: str
      vlanId:
        description: Vlan Id allocated for claimimg of Wireless Controller
        type: str
      ipInterfaceName:
        description: Name of the Interface used for Pnp by the Wireless Controller
        type: str
      rfProfile:
        description: rfprofile of the AP being claimed (HIGH/LOW/TYPICAL)
        type: str
      deviceInfo:
        description: Pnp Device's deviceInfo.
        type: dict
        required: true
        suboptions:
          hostname:
            description: Pnp Device's hostname.
            type: str
          state:
            description: Pnp Device's onbording state (Unclaimed/Claimed/Provisioned).
            type: str
          pid:
            description: Pnp Device's pid.
            type: str
          serialNumber:
            description: Pnp Device's serialNumber.
            type: str
          add_device_method:
            description: Pnp Device's device addition method (Single/Bulk/Smart Account).
            type: str
          isSudiRequired:
            description: Sudi Authentication requiremnet's flag.
            type: bool

requirements:
- dnacentersdk == 2.6.5
- python >= 3.5
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.add_device,
    device_onboarding_pnp.DeviceOnboardingPnp.get_device_list,
    device_onboarding_pnp.DeviceOnboardingPnp.claim_a_device_to_a_site,
    device_onboarding_pnp.DeviceOnboardingPnp.delete_device_by_id_from_pnp,
    device_onboarding_pnp.DeviceOnboardingPnp.get_device_count,
    sites.Sites.get_site,
    software_image_management_swim.SoftwareImageManagementSwim.get_software_image_details,
    configuration_templates.ConfigurationTemplates.gets_the_templates_available

  - Paths used are
    post /dna/intent/api/v1/onboarding/pnp-device
    post /dna/intent/api/v1/onboarding/pnp-device/site-claim
    post /dna/intent/api/v1/onboarding/pnp-device/{id}
    get /dna/intent/api/v1/onboarding/pnp-device/count
    get /dna/intent/api/v1/onboarding/pnp-device
    get /dna/intent/api/v1/site
    get /dna/intent/api/v1/image/importation
    get /dna/intent/api/v1/template-programmer/template

"""

EXAMPLES = r"""
- name: Add a new device and claim the device
  cisco.dnac.pnp_intent:
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
        - template_name: string
          image_name: string
          golden_image: bool
          site_name: string
          projectName: string
          pnp_type: string
          staticIP: string
          subnetMask: string
          gateway: string
          vlanId: string
          ipInterfaceName: string
          rfProfile: string
          deviceInfo:
            hostname: string
            state: string
            pid: string
            serialNumber: string
            add_device_method: string
            isSudiRequired: string
"""

RETURN = r"""
#Case_1: When the device is claimed successfully.
response_1:
  description: A dictionary with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response":
        {
          "response": String,
          "version": String
        },
      "msg": String
    }

#Case_2: Given site/image/template/project not found or Device is not found for deletion
response_2:
  description: A list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  sample: >
    {
      "response": [],
      "msg": String
    }

#Case_3: Error while deleting/claiming a device
response_3:
  description: A string with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": String,
      "msg": String
    }
"""
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    get_dict_result
)


class DnacPnp(DnacBase):
    def __init__(self, module):
        super().__init__(module)

    def validate_input(self):
        """
        Validate the fields provided in the playbook.  Checks the
        configuration provided in the playbook against a predefined
        specification to ensure it adheres to the expected structure
        and data types.

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          - self.msg: A message describing the validation result.
          - self.status: The status of the validation (either 'success' or 'failed').
          - self.validated_config: If successful, a validated version of the
                                   'config' parameter.
        Example:
          To use this method, create an instance of the class and call
          'validate_input' on it.If the validation succeeds, 'self.status'
          will be 'success'and 'self.validated_config' will contain the
          validated configuration. If it fails, 'self.status' will be
          'failed', and 'self.msg' will describe the validation issues.
        """

        if not self.config:
            self.msg = "config not available in playbook for validation"
            self.status = "success"
            return self

        pnp_spec = {
            'template_name': {'type': 'str', 'required': False},
            'project_name': {'type': 'str', 'required': False,
                             'default': 'Onboarding Configuration'},
            'site_name': {'type': 'str', 'required': False},
            'image_name': {'type': 'str', 'required': False},
            'golden_image': {'type': 'bool', 'required': False},
            'deviceInfo': {'type': 'dict', 'required': True},
            'pnp_type': {'type': 'str', 'required': False, 'default': 'Default'},
            "rfProfile": {'type': 'str', 'required': False},
            "staticIP": {'type': 'str', 'required': False},
            "subnetMask": {'type': 'str', 'required': False},
            "gateway": {'type': 'str', 'required': False},
            "vlanId": {'type': 'str', 'required': False},
            "ipInterfaceName": {'type': 'str', 'required': False},
            "sensorProfile": {'type': 'str', 'required': False}
        }

        # Validate pnp params
        valid_pnp, invalid_params = validate_list_of_dicts(
            self.config, pnp_spec
        )

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(
                "\n".join(invalid_params))
            self.status = "failed"
            return self

        self.validated_config = valid_pnp
        self.log(str(valid_pnp))

        self.msg = "Successfully validated input"
        self.status = "success"
        return self

    def get_site_details(self):
        """
        Check whether the site exists or not, along with side id

        Parameters:
          - self: The instance of the class containing the 'config'
                  attribute to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          - site_exits: A boolean value indicating the existence of the site.
          - site_id: The Id of the site i.e. required to claim device to site.
        Example:
          Post creation of the validated input, we this method gets the
          site_id and checks whether the site exists or not
        """

        site_exists = False
        site_id = None
        response = None

        try:
            response = self.dnac_apply['exec'](
                family="sites",
                function='get_site',
                params={"name": self.want.get("site_name")},
            )
        except Exception:
            self.module.fail_json(msg="Site not found", response=[])

        if response:
            self.log(str(response))
            site = response.get("response")
            if len(site) == 1:
                site_id = site[0].get("id")
                site_exists = True

        return (site_exists, site_id)

    def get_site_type(self):
        """
        Fetches the type of site

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          - site_type: A string indicating the type of the
                       site (area/building/floor).
        Example:
          Post creation of the validated input, we this method gets the
          type of the site.
        """

        try:
            response = self.dnac_apply['exec'](
                family="sites",
                function='get_site',
                params={"name": self.want.get("site_name")},
            )
        except Exception:
            self.module.fail_json(msg="Site not found", response=[])

        if response:
            self.log(str(response))
            site = response.get("response")
            site_additional_info = site[0].get("additionalInfo")
            for item in site_additional_info:
                if item["nameSpace"] == "Location":
                    site_type = item.get("attributes").get("type")

        return site_type

    def get_pnp_params(self, params):
        """
        Store pnp parameters from the playbook for pnp processing in DNAC.

        Parameters:
          - self: The instance of the class containing the 'config'
                  attribute to be validated.
          - params: The validated params passed from the playbook.
        Returns:
          The method returns an instance of the class with updated attributes:
          - pnp_params: A dictionary containing all the values indicating
                        the type of the site (area/building/floor).
        Example:
          Post creation of the validated input, it fetches the required paramters
          and stores it for further processing and calling the parameters in
          other APIs.
        """

        pnp_params = {
            'deviceInfo': params.get('deviceInfo')
        }
        return pnp_params

    def get_image_params(self, params):
        """
        Get image name and the confirmation whether it's tagged golden or not

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
          - params: The validated params passed from the playbook.
        Returns:
          The method returns an instance of the class with updated attributes:
          - image_params: A dictionary containing all the values indicating
                          name of the image and its golden image status.
        Example:
          Post creation of the validated input, it fetches the required
          paramters and stores it for further processing and calling the
          parameters in other APIs.
        """

        image_params = {
            'image_name': params.get('image_name'),
            'is_tagged_golden': params.get('golden_image')
        }
        return image_params

    def get_claim_params(self):
        """
        Get the paramters needed for claiming the device to site.
        Parameters:
          - self: The instance of the class containing the 'config'
                  attribute to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          - claim_params: A dictionary needed for calling the POST call
                          for claim a device to a site API.
        Example:
          The stored dictionary can be used to call the API claim a device
          to a site via SDK
        """

        imageinfo = {
            'imageId': self.have.get('image_id')
        }

        configinfo = {
            'configId': self.have.get('template_id'),
            'configParameters': [
                {
                    'key': '',
                    'value': ''
                }
            ]
        }

        claim_params = {
            'deviceId': self.have.get('device_id'),
            'siteId': self.have.get('site_id'),
            'type': self.want.get('pnp_type'),
            'hostname': self.want.get('hostname'),
            'imageInfo': imageinfo,
            'configInfo': configinfo,
        }

        if claim_params["type"] == "CatalystWLC":
            claim_params["staticIP"] = self.validated_config[0]['staticIP']
            claim_params["subnetMask"] = self.validated_config[0]['subnetMask']
            claim_params["gateway"] = self.validated_config[0]['gateway']
            claim_params["vlanId"] = str(self.validated_config[0]['vlanId'])
            claim_params["ipInterfaceName"] = self.validated_config[0]['ipInterfaceName']

        if claim_params["type"] == "AccessPoint":
            claim_params["rfProfile"] = self.validated_config[0]["rfProfile"]

        return claim_params

    def get_have(self):
        """
        Get the current image, template and site details from the DNAC.

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          - self.image_response: A list of image passed by the user
          - self.template_list: A list of template under project
          - self.device_response: Gets the device_id and stores it
        Example:
          Stored paramters are used to call the APIs to get the current image,
          template and site details to call the API for various types of devices
        """

        have = {}
        if self.params.get("state") == "merged":
            # check if given image exists, if exists store image_id
            image_response = self.dnac_apply['exec'](
                family="software_image_management_swim",
                function='get_software_image_details',
                params=self.want.get("image_params"),
            )
            image_list = image_response.get("response")
            self.log(str(image_response))

            # check if project has templates or not
            template_list = self.dnac_apply['exec'](
                family="configuration_templates",
                function='gets_the_templates_available',
                params={"project_names": self.want.get("project_name")},
            )
            self.log(str(template_list))

            # check if given site exits, if exists store current site info
            site_exists = False
            if not isinstance(self.want.get("site_name"), str) and \
                    not self.want.get('pnp_params').get('deviceInfo').get('add_device_method'):
                self.msg = "Name of the site must be a string"
                self.status = "failed"
                return self

            site_name = self.want.get("site_name")
            (site_exists, site_id) = self.get_site_details()

            if site_exists:
                have["site_id"] = site_id
                self.log("Site Exists: " + str(site_exists) + "\n Site_id:" + str(site_id))
                self.log("Site Name:" + str(site_name))
                if self.want.get("pnp_type") == "AccessPoint":
                    if self.get_site_type() != "floor":
                        self.msg = "Type of the site must \
                            be a floor for claiming an AP"
                        self.status = "failed"
                        return self

                if len(image_list) == 1:
                    have["image_id"] = image_list[0].get("imageUuid")
                    self.log("Image Id: " + str(have["image_id"]))

                template_name = self.want.get("template_name")
                if template_name:
                    if not (template_list and isinstance(template_list, list)):
                        self.msg = "Project Not Found \
                            or Project is Empty"
                        self.status = "failed"
                        return self

                    template_details = get_dict_result(template_list, 'name', template_name)
                    if template_details:
                        have["template_id"] = template_details.get("templateId")
                    else:
                        self.msg = "Template Not found"
                        self.status = "failed"
                        return self

            else:
                if not self.want.get('pnp_params').get('deviceInfo').get('add_device_method'):
                    self.msg = "Either Site Name or Device addition method must be provided"
                    self.status = "failed"
                    return self

        # check if given device exists in pnp inventory, store device Id
        device_response = self.dnac_apply['exec'](
            family="device_onboarding_pnp",
            function='get_device_list',
            params={"serial_number": self.want.get("serial_number")}
        )

        self.log(str(device_response))

        if device_response and (len(device_response) == 1):
            have["device_id"] = device_response[0].get("id")
            have["device_found"] = True

            self.log("Device Id: " + str(have["device_id"]))
        else:
            have["device_found"] = False
        self.msg = "Successfully collected all project and template \
                    parameters from dnac for comparison"
        self.status = "success"
        self.have = have

        return self

    def get_want(self, config):
        """
        Get all the image, template and site and pnp related
        information from playbook that is needed to be created in DNAC.

        Parameters:
          - self: The instance of the class containing the 'config'
                  attribute to be validated.
          - config: validated config passed from the playbook
        Returns:
          The method returns an instance of the class with updated attributes:
          - self.want: A dictionary of paramters obtained from the playbook.
          - self.msg: A message indicating all the paramters from the playbook
                      are collected.
          - self.status: Success.
        Example:
            It stores all the paramters passed from the playbook for further
            processing before calling the APIs
        """

        self.want = {
            'image_params': self.get_image_params(config),
            'pnp_params': self.get_pnp_params(config),
            'pnp_type': config.get('pnp_type'),
            'site_name': config.get('site_name'),
            'serial_number': config.get('deviceInfo').get('serialNumber'),
            'hostname': config.get('deviceInfo').get('hostname'),
            'project_name': config.get('project_name'),
            'template_name': config.get('template_name'),
            'add_device_method': config.get('deviceInfo').get('add_device_method'),
            'isSudiRequired': config.get('deviceInfo').get('isSudiRequired')
        }

        if self.want["pnp_type"] == "CatalystWLC":
            self.want["staticIP"] = config.get('staticIP')
            self.want["subnetMask"] = config.get('subnetMask')
            self.want["gateway"] = config.get('gateway')
            self.want["vlanId"] = config.get('vlanId')
            self.want["ipInterfaceName"] = config.get('ipInterfaceName')

        elif self.want["pnp_type"] == "AccessPoint":
            if self.get_site_type() == "floor":
                self.want["rfProfile"] = config.get("rfProfile")

        self.msg = "Successfully collected all parameters from playbook " + \
            "for comparison"
        self.status = "success"

        return self

    def get_diff_merged(self):
        """
        If given device doesnot exist then add it to pnp database and
        get the device id.

        Parameters:
          - self: An instance of a class used for interacting with
                  Cisco DNA Center.
        Returns:
          - object: An instance of the class with updated results and status
                    based on the processing of differences.
        Description:
          The function processes the differences and, depending on the
          changes required, it may add, update,or resynchronize devices in
          Cisco DNA Center. The updated results and status are stored in the
          class instance for further use.
        """

        device_count_params = {
            "serial_number": self.want.get("serial_number"),
            "state": "Provisioned"
        }

        if not self.have.get("device_found"):
            if not self.want["add_device_method"]:
                self.msg = "Device needs to be added before claiming"
                self.status = "failed"
                return self

            if not self.want["site_name"]:
                if self.want["add_device_method"] == "Single":
                    self.log("Adding device to pnp database")
                    dev_add_response = self.dnac_apply['exec'](
                        family="device_onboarding_pnp",
                        function="add_device",
                        params=self.want.get("pnp_params"),
                        op_modifies=True,
                    )

                    self.have["deviceInfo"] = dev_add_response.get("deviceInfo")
                    self.log(str(dev_add_response))
                    if self.have["deviceInfo"]:
                        self.result['msg'] = "Only Device Added Successfully"
                        self.result['response'] = dev_add_response
                        self.result['diff'] = self.validated_config
                        self.result['changed'] = True
                    else:
                        self.msg = "Device Addition Failed"
                        self.status = "failed"
                        return self

            else:
                if self.want["add_device_method"] == "Single":
                    self.log("Adding device to pnp database")
                    dev_add_response = self.dnac_apply['exec'](
                        family="device_onboarding_pnp",
                        function="add_device",
                        params=self.want.get("pnp_params"),
                        op_modifies=True,
                    )
                    self.have["deviceInfo"] = dev_add_response.get("deviceInfo")
                    self.log(str(dev_add_response))
                claim_params = self.get_claim_params()
                claim_params["deviceId"] = dev_add_response.get("id")
                claim_response = self.dnac_apply['exec'](
                    family="device_onboarding_pnp",
                    function='claim_a_device_to_a_site',
                    op_modifies=True,
                    params=claim_params,
                )

                self.log(str(claim_response))
                if claim_response.get("response") == "Device Claimed" \
                        and self.have["deviceInfo"]:
                    self.result['msg'] = "Device Added and Claimed Successfully"
                    self.result['response'] = claim_response
                    self.result['diff'] = self.validated_config
                    self.result['changed'] = True
                else:
                    self.msg = "Device Claim Failed"
                    self.status = "failed"
                    return self

        else:
            device_count_response = self.dnac_apply['exec'](
                family="device_onboarding_pnp",
                function='get_device_count',
                op_modifies=True,
                params=device_count_params,
            )
            if not self.want["site_name"]:
                self.result['response'] = self.have.get("device_found")
                self.result['msg'] = "Device is already added"
            else:
                if device_count_response.get("response") == 0:
                    claim_params = self.get_claim_params()
                    self.log(str(claim_params))
                    claim_response = self.dnac_apply['exec'](
                        family="device_onboarding_pnp",
                        function='claim_a_device_to_a_site',
                        op_modifies=True,
                        params=claim_params,
                    )
                    self.log(str(claim_response))
                    if claim_response.get("response") == "Device Claimed":
                        self.result['msg'] = "Only Device Claimed Successfully"
                        self.result['response'] = claim_response
                        self.result['diff'] = self.validated_config
                        self.result['changed'] = True
                else:
                    self.result['response'] = self.have.get("device_found")
                    self.result['msg'] = "Device is already claimed"

        return self

    def get_diff_deleted(self):
        """
        If the given device is added to pnp database and is in unclaimed or
        failed state delete the given device.

        Parameters:
          - self: An instance of a class used for interacting with
                  Cisco DNA Center.
        Returns:
          - self: An instance of the class with updated results and status
                  based on the deletion operation.
        Description:
          This function is responsible for removing devices from the
          Cisco DNA Center PnP GUI and raise Exception if any error occured.
        """

        if self.have.get("device_found"):
            try:
                response = self.dnac_apply['exec'](
                    family="device_onboarding_pnp",
                    function="delete_device_by_id_from_pnp",
                    op_modifies=True,
                    params={"id": self.have.get("device_id")},
                )

                self.log(str(response))

                if response.get("deviceInfo").get("state") == "Deleted":
                    self.result['changed'] = True
                    self.result['response'] = response
                    self.result['diff'] = self.validated_config
                    self.result['msg'] = "Device Deleted Successfully"
                else:
                    self.result['response'] = response
                    self.result['msg'] = "Error while deleting the device"

            except Exception as errorstr:
                response = str(errorstr)
                msg = "Device Deletion Failed"
                self.module.fail_json(msg=msg, response=response)

        else:
            self.msg = "Device Not Found"
            self.status = "failed"
            return self

        return self


def main():
    """
    main entry point for module execution
    """

    element_spec = {'dnac_host': {'required': True, 'type': 'str'},
                    'dnac_port': {'type': 'str', 'default': '443'},
                    'dnac_username': {'type': 'str', 'default': 'admin', 'aliases': ['user']},
                    'dnac_password': {'type': 'str', 'no_log': True},
                    'dnac_verify': {'type': 'bool', 'default': 'True'},
                    'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
                    'dnac_debug': {'type': 'bool', 'default': False},
                    'dnac_log': {'type': 'bool', 'default': False},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged', 'deleted']}
                    }

    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)
    dnac_pnp = DnacPnp(module)

    state = dnac_pnp.params.get("state")
    if state not in dnac_pnp.supported_states:
        dnac_pnp.status = "invalid"
        dnac_pnp.msg = "State {0} is invalid".format(state)
        dnac_pnp.check_return_status()

    dnac_pnp.validate_input().check_return_status()

    for config in dnac_pnp.validated_config:
        dnac_pnp.reset_values()
        dnac_pnp.get_want(config).check_return_status()
        dnac_pnp.get_have().check_return_status()
        dnac_pnp.get_diff_state_apply[state]().check_return_status()

    module.exit_json(**dnac_pnp.result)


if __name__ == '__main__':
    main()
