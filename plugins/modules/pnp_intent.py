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
                type: str
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
    device_onboarding_pnp.DeviceOnboardingPnp.delete_device_by_id_from_pnp,

  - Paths used are
    post /dna/intent/api/v1/onboarding/pnp-device
    post /dna/intent/api/v1/onboarding/pnp-device/site-claim
    post /dna/intent/api/v1/onboarding/pnp-device/{id}

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
        template_name: string
        image_name: string
        site_name: string
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
          validLicenseLevels: string
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
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
            The method returns an instance of the class with updated attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either 'success' or 'failed').
                - self.validated_config: If successful, a validated version of
                the 'config' parameter.
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

    def site_exists(self):

        """
        Check whether the site exists or not
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
            The method returns an instance of the class with updated attributes:
                - site_exits: A boolean value indicating the existence of the site.
                - site_id: The Id of the site i.e. required to claim a device to site.
        Example:
            Post creation of the validated input, we this method gets the site_id and checks
            whether the site exists or not
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
            site_id = site[0].get("id")
            site_exists = True

        return (site_exists, site_id)

    def get_site_type(self):

        """
        Fetches the type of site
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
            The method returns an instance of the class with updated attributes:
                - site_type: A string indicating the type of the site (area/building/floor).
        Example:
            Post creation of the validated input, we this method gets the type of the site
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
        Store pnp parameters from the playbook for pnp processing in DNAC
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
            params: The validated params passed from the playbook
        Returns:
            The method returns an instance of the class with updated attributes:
                - pnp_params: A dictionary containing all the values indicating
                the type of the site (area/building/floor).
        Example:
            Post creation of the validated input, it fetches the required paramters
            and stores it for further processing and calling the parameters in
            other APIs
        """

        pnp_params = {
            '_id': params.get('_id'),
            'deviceInfo': params.get('deviceInfo'),
            'runSummaryList': params.get('runSummaryList'),
            'systemResetWorkflow': params.get('systemResetWorkflow'),
            'systemWorkflow': params.get('systemWorkflow'),
            'tenantId': params.get('tenantId'),
            'version': params.get('device_version'),
            'workflow': params.get('workflow'),
            'workflowParameters': params.get('workflowParameters')
        }
        return pnp_params

    def get_image_params(self, params):

        """
        Get image name and the confirmation whether it's tagged golden or not
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
            params: The validated params passed from the playbook
        Returns:
            The method returns an instance of the class with updated attributes:
                - image_params: A dictionary containing all the values indicating
                name of the image and its golden image status.
        Example:
            Post creation of the validated input, it fetches the required paramters
            and stores it for further processing and calling the parameters in
            other APIs
        """

        image_params = {
            'image_name': params.get('image_name'),
            'is_tagged_golden': params.get('golden_image')
        }
        return image_params

    def get_claim_params(self):

        """
        Get the paramters needed for claiming the device to site
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
            The method returns an instance of the class with updated attributes:
                - claim_params: A dictionary needed for calling the POST call for claim
                a device to a site API
        Example:
            The stored dictionary can be used to call the API claim a device to a site via SDK
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
        Get the current image, template and site details from the DNAC
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
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
            if isinstance(self.want.get("site_name"), str):
                site_name = self.want.get("site_name")
                (site_exists, site_id) = self.site_exists()

            if site_exists:
                have["site_id"] = site_id
                self.log("Site Exists: " + str(site_exists) + "\n Site_id:" + str(site_id))
                self.log("Site Name:" + str(site_name))
                if self.want.get("pnp_type") == "AccessPoint":
                    if self.get_site_type() != "floor":
                        self.module.fail_json(msg="Type of the site must \
                            be a floor for claiming an AP", response=[])
                if len(image_list) == 1:
                    have["image_id"] = image_list[0].get("imageUuid")
                    self.log("Image Id: " + str(have["image_id"]))
                if template_list and isinstance(template_list, list):
                    # API execution error returns a dict
                    if self.want.get("template_name"):
                        template_details = get_dict_result(template_list, 'name', self.want.get("template_name"))

                        if template_details:
                            have["template_id"] = template_details.get("templateId")
                        else:
                            self.module.fail_json(msg="Template Not Found", response=[])
                else:
                    self.module.fail_json(msg="Project Not Found or Project is Empty", response=[])
            else:
                self.module.fail_json(msg="Site not found", response=[])

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
        information from playbook that is needed to be created in DNAC
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
            config: validated config passed from the playbook
        Returns:
            The method returns an instance of the class with updated attributes:
                - self.want: A dictionary of paramters obtained from the playbook
                - self.msgt: A message indicating all the paramters from the playbook are
                collected
                - self.status: Success
        Example:
            It stores all the paramters passed from the playbook for further processing
            before calling the APIs
        """

        self.want = {
            'image_params': self.get_image_params(config),
            'pnp_params': self.get_pnp_params(config),
            'pnp_type': config.get('pnp_type'),
            'site_name': config.get('site_name'),
            'serial_number': config.get('deviceInfo').get('serialNumber'),
            'hostname': config.get('deviceInfo').get('hostname'),
            'project_name': config.get('project_name'),
            'template_name': config.get('template_name')
        }

        if self.want["pnp_type"] == "CatalystWLC":
            self.want["staticIP"] = config.get('staticIP')
            self.want["subnetMask"] = config.get('subnetMask')
            self.want["gateway"] = config.get('gateway')
            self.want["vlanId"] = config.get('vlanId')
            self.want["ipInterfaceName"] = config.get('ipInterfaceName')

        if self.want["pnp_type"] == "AccessPoint":
            if self.get_site_type == "floor":
                self.want["rfProfile"] = config.get("rfProfile")

        self.msg = "Successfully collected all parameters from playbook " + \
            "for comparison"
        self.status = "success"

        return self

    def get_diff_merged(self):

        """
        If given device doesnot exist
        then add it to pnp database and get the device id
        Args:
            self: An instance of a class used for interacting with Cisco DNA Center.
        Returns:
            object: An instance of the class with updated results and status
            based on the processing of differences.
        Description:
            The function processes the differences and, depending on the
            changes required, it may add, update,or resynchronize devices in
            Cisco DNA Center. The updated results and status are stored in the
            class instance for further use.
        """

        if not self.have.get("device_found"):
            self.log("Adding device to pnp database")
            response = self.dnac_apply['exec'](
                family="device_onboarding_pnp",
                function="add_device",
                params=self.want.get("pnp_params"),
                op_modifies=True,
            )

            self.have["device_id"] = response.get("id")
            self.log(str(response))
            self.log(self.have.get("device_id"))

        claim_params = self.get_claim_params()
        claim_response = self.dnac_apply['exec'](
            family="device_onboarding_pnp",
            function='claim_a_device_to_a_site',
            op_modifies=True,
            params=claim_params,
        )

        self.log(str(claim_response))

        if claim_response.get("response") == "Device Claimed":
            self.result['changed'] = True
            self.result['msg'] = "Device Claimed Successfully"
            self.result['response'] = claim_response
            self.result['diff'] = self.validated_config
        else:
            self.module.fail_json(msg="Device Claim Failed", response=claim_response)

        return self

    def get_diff_deleted(self):

        """
        If the given device is added to pnp database
        and is in unclaimed or failed state delete the
        given device
        Args:
            self: An instance of a class used for interacting with Cisco DNA Center
        Returns:
            self: An instance of the class with updated results and status based on
            the deletion operation.
        Description:
            This function is responsible for removing devices from the Cisco DNA Center PnP GUI and
            raise Exception if any error occured.
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
            self.module.fail_json(msg="Device Not Found", response=[])

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
