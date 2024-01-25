#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2022, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Madhan Sankaranarayanan, Rishita Chowdhary, Abhishek Maheshwari")

DOCUMENTATION = r"""
---
module: swim_intent
short_description: Intent module for SWIM related functions
description:
- Manage operation related to image importation, distribution, activation and tagging image as golden
- API to fetch a software image from remote file system using URL for HTTP/FTP and upload it to DNA Center.
  Supported image files extensions are bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2.
- API to fetch a software image from local file system and upload it to DNA Center
  Supported image files extensions are bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2.
- API to tag/untag image as golen for a given family of devices
- API to distribute a software image on a given device. Software image must be imported successfully into
  DNA Center before it can be distributed.
- API to activate a software image on a given device. Software image must be present in the device flash.
version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.intent_params
author: Madhan Sankaranarayanan (@madhansansel)
        Rishita Chowdhary (@rishitachowdhary)
        Abhishek Maheshwari (@abmahesh)
options:
  dnac_log_level:
    description: Specifies the log level for Cisco Catalyst Center logging, categorizing logs by severity.
        Options- [CRITICAL, ERROR, WARNING, INFO, DEBUG]
    type: str
    default: INFO
  state:
    description: The state of DNAC after module completion.
    type: str
    choices: [ merged ]
    default: merged
  config:
    description: List of details of SWIM image being managed
    type: list
    elements: dict
    required: True
    suboptions:
      import_image_details:
        description: Details of image being imported
        type: dict
        suboptions:
          type:
            description: The source of import, supports url import or local import.
            type: str
          local_image_details:
            description: Details of the local path of the image to be imported.
            type: dict
            suboptions:
              file_path:
                description: File absolute path.
                type: str
              is_third_party:
                description: IsThirdParty query parameter. Third party Image check.
                type: bool
              third_party_application_type:
                description: ThirdPartyApplicationType query parameter. Third Party Application Type.
                type: str
              third_party_image_family:
                description: ThirdPartyImageFamily query parameter. Third Party image family.
                type: str
              third_party_vendor:
                description: ThirdPartyVendor query parameter. Third Party Vendor.
                type: str
          url_details:
            description: URL details for SWIM import
            type: dict
            suboptions:
              payload:
                description: Swim Import Via Url's payload.
                type: list
                elements: dict
                suboptions:
                  application_type:
                    description: Swim Import Via Url's applicationType.
                    type: str
                  image_family:
                    description: Swim Import Via Url's imageFamily.
                    type: str
                  source_url:
                    description: Swim Import Image Via Url.
                    type: str
                  third_party:
                    description: ThirdParty flag.
                    type: bool
                  vendor:
                    description: Swim Import Via Url's vendor.
                    type: str
              schedule_at:
                description: ScheduleAt query parameter. Epoch Time (The number of milli-seconds since
                  January 1 1970 UTC) at which the distribution should be scheduled (Optional).
                type: str
              schedule_desc:
                description: ScheduleDesc query parameter. Custom Description (Optional).
                type: str
              schedule_origin:
                description: ScheduleOrigin query parameter. Originator of this call (Optional).
                type: str
      tagging_details:
        description: Details for tagging or untagging an image as golden
        type: dict
        suboptions:
          image_name:
            description: SWIM image name which will be tagged or untagged as golden.
            type: str
          device_role:
            description: Device Role. Permissible Values ALL, UNKNOWN, ACCESS, BORDER ROUTER,
              DISTRIBUTION and CORE.
            type: str
          device_family_name:
            description: Device family name(Eg Switches and Hubs)
            type: str
          device_type:
            description: Type of the device (Eg Cisco Catalyst 9300 Switch)
            type: str
          site_name:
            description: Site name for which SWIM image will be tagged/untagged as golden.
              If not provided, SWIM image will be mapped to global site.
            type: str
          tagging:
            description: Booelan value to tag/untag SWIM image as golden
              If True then the given image will be tagged as golden.
              If False then the given image will be un-tagged as golden.
            type: bool
      image_distribution_details:
        description: Details for SWIM image distribution. Device on which the image needs to distributed
          can be speciifed using any of the following parameters - deviceSerialNumber,
          deviceIPAddress, deviceHostname or deviceMacAddress.
        type: dict
        suboptions:
          device_role:
            description: Device Role. Permissible Values ALL, UNKNOWN, ACCESS, BORDER ROUTER,
              DISTRIBUTION and CORE.
            type: str
          device_family_name:
            description: Device family name
            type: str
          site_name:
            description: Used to get device details associated to this site.
            type: str
          image_name:
            description: SWIM image's name
            type: str
          device_serial_number:
            description: Device serial number where the image needs to be distributed
            type: str
          device_ip_address:
            description: Device IP address where the image needs to be distributed
            type: str
          device_hostname:
            description: Device hostname where the image needs to be distributed
            type: str
          device_mac_address:
            description: Device MAC address where the image needs to be distributed
            type: str
      image_activation_details:
        description: Details for SWIM image activation. Device on which the image needs to activated
          can be speciifed using any of the following parameters - deviceSerialNumber,
          deviceIPAddress, deviceHostname or deviceMacAddress.
        type: dict
        suboptions:
          device_role:
            description: Device Role. Permissible Values ALL, UNKNOWN, ACCESS, BORDER ROUTER,
              DISTRIBUTION and CORE.
            type: str
          device_family_name:
            description: Device family name
            type: str
          site_name:
            description: Used to get device details associated to this site.
            type: str
          activate_lower_image_version:
            description: ActivateLowerImageVersion flag.
            type: bool
          device_upgrade_mode:
            description: Swim Trigger Activation's deviceUpgradeMode.
            type: str
          distributeIfNeeded:
            description: DistributeIfNeeded flag.
            type: bool
          image_name:
            description: SWIM image's name
            type: str
          device_serial_number:
            description: Device serial number where the image needs to be activated
            type: str
          device_ip_address:
            description: Device IP address where the image needs to be activated
            type: str
          device_hostname:
            description: Device hostname where the image needs to be activated
            type: str
          device_mac_address:
            description: Device MAC address where the image needs to be activated
            type: str
          schedule_validate:
            description: ScheduleValidate query parameter. ScheduleValidate, validates data
              before schedule (Optional).
            type: bool
requirements:
- dnacentersdk == 2.4.5
- python >= 3.5
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.import_software_image_via_url,
    software_image_management_swim.SoftwareImageManagementSwim.tag_as_golden_image,
    software_image_management_swim.SoftwareImageManagementSwim.trigger_software_image_distribution,
    software_image_management_swim.SoftwareImageManagementSwim.trigger_software_image_activation,

  - Paths used are
    post /dna/intent/api/v1/image/importation/source/url,
    post /dna/intent/api/v1/image/importation/golden,
    post /dna/intent/api/v1/image/distribution,
    post /dna/intent/api/v1/image/activation/device,

"""

EXAMPLES = r"""
- name: Import an image from a URL, tag it as golden and load it on device
  cisco.dnac.swim_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: True
    config:
    - import_image_details:
        type: string
        url_details:
          payload:
          - source_url: string
            third_party: bool
            image_family: string
            vendor: string
            application_type: string
          schedule_at: string
          schedule_desc: string
          schedule_origin: string
      tagging_details:
        image_name: string
        device_role: string
        device_family_name: string
        site_name: string
        tagging: bool
      image_distribution_details:
        image_name: string
        device_serial_number: string
      image_activation_details:
        schedule_validate: bool
        activate_lower_image_version: bool
        distribute_if_needed: bool
        device_serial_number: string
        image_name: string

- name: Import an image from local, tag it as golden.
  cisco.dnac.swim_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: True
    config:
    - import_image_details:
        type: string
        local_image_details:
            file_path: string
            is_third_party: bool
            third_party_vendor: string
            third_party_image_family: string
            third_party_application_type: string
      tagging_details:
        image_name: string
        device_role: string
        device_family_name: string
        device_type: string
        site_name: string
        tagging: bool

- name: Tag the given image as golden and load it on device
  cisco.dnac.swim_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: True
    config:
    - tagging_details:
        image_name: string
        device_role: string
        device_family_name: string
        device_type: string
        site_name: string
        tagging: bool

- name: Distribute the given image on devices associated to that site with specified role.
  cisco.dnac.swim_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: True
    config:
    - image_distribution_details:
        image_name: string
        site_name: string
        device_role: string
        device_family_name: string

- name: Activate the given image on devices associated to that site with specified role.
  cisco.dnac.swim_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: True
    config:
    - image_activation_details:
        image_name: string
        site_name: string
        device_role: string
        device_family_name: string
        scehdule_validate: bool
        activate_lower_image_version: bool
        distribute_if_needed: bool

"""

RETURN = r"""
#Case: SWIM image is successfully imported, tagged as golden, distributed and activated on a device
response:
  description: A dictionary with activation details as returned by the DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
                        "additionalStatusURL": String,
                        "data": String,
                        "endTime": 0,
                        "id": String,
                        "instanceTenantId": String,
                        "isError": bool,
                        "lastUpdate": 0,
                        "progress": String,
                        "rootId": String,
                        "serviceType": String,
                        "startTime": 0,
                        "version": 0
                  },
      "msg": String
    }

"""

from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    get_dict_result,
)
from ansible.module_utils.basic import AnsibleModule


class DnacSwims(DnacBase):
    """Class containing member attributes for Swim intent module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged"]

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.
        Parameters:
          - self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          - self.msg: A message describing the validation result.
          - self.status: The status of the validation (either 'success' or 'failed').
          - self.validated_config: If successful, a validated version of 'config' parameter.
        Example:
            To use this method, create an instance of the class and call 'validate_input' on it.
          If the validation succeeds, 'self.status' will be 'success' and 'self.validated_config'
          will contain the validated configuration. If it fails, 'self.status' will be 'failed',
          'self.msg' will describe the validation issues.
        """

        if not self.config:
            self.msg = "config not available in playbook for validattion"
            self.status = "success"
            return self

        temp_spec = dict(
            import_image_details=dict(type='dict'),
            tagging_details=dict(type='dict'),
            image_distribution_details=dict(type='dict'),
            image_activation_details=dict(type='dict'),
        )

        # Validate swim params
        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.status = "failed"
            return self

        self.validated_config = valid_temp
        self.log(str(valid_temp))
        self.msg = "Successfully validated input"
        self.status = "success"
        return self

    def site_exists(self, site_name):
        """
        Parameters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Returns:
            tuple: A tuple containing two values:
            - site_exists (bool): A boolean indicating whether the site exists (True) or not (False).
            - site_id (str or None): The ID of the site if it exists, or None if the site is not found.
        Description:
            This method checks the existence of a site in the DNAC. If the site is found,it sets 'site_exists' to True,
            retrieves the site's ID, and returns both values in a tuple. If the site does not exist, 'site_exists' is set
            to False, and 'site_id' is None. If an exception occurs during the site lookup, an exception is raised.
        """

        site_exists = False
        site_id = None
        response = None
        try:
            response = self.dnac._exec(
                family="sites",
                function='get_site',
                params={"name": site_name},
            )
        except Exception as e:
            self.module.fail_json(msg="Site not found")

        if response:
            self.log(str(response))

            site = response.get("response")
            site_id = site[0].get("id")
            site_exists = True

        return (site_exists, site_id)

    def get_image_id(self, name):
        """
        Retrieve the unique image ID based on the provided image name.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            name (str): The name of the software image to search for.
        Returns:
            str: The unique image ID (UUID) corresponding to the given image name.
        Raises:
            AnsibleFailJson: If the image is not found in the response.
        Description:
            This function sends a request to Cisco DNAC to retrieve details about a software image based on its name.
            It extracts and returns the image ID if a single matching image is found. If no image or multiple
            images are found with the same name, it raises an exception.
        """

        image_response = self.dnac._exec(
            family="software_image_management_swim",
            function='get_software_image_details',
            params={"image_name": name},
        )

        self.log(str(image_response))

        image_list = image_response.get("response")
        if (len(image_list) == 1):
            image_id = image_list[0].get("imageUuid")
            self.log("Image Id: " + str(image_id))
        else:
            error_message = "Image {0} not found".format(name)
            self.log(error_message)
            self.module.fail_json(msg="Image not found", response=image_response)

        return image_id

    def is_image_exist(self, name):
        """
        Retrieve the unique image ID based on the provided image name.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            name (str): The name of the software image to search for.
        Returns:
            str: The unique image ID (UUID) corresponding to the given image name.
        Raises:
            AnsibleFailJson: If the image is not found in the response.
        Description:
            This function sends a request to Cisco DNAC to retrieve details about a software image based on its name.
            It extracts and returns the image ID if a single matching image is found. If no image or multiple
            images are found with the same name, it raises an exception.
        """

        image_exist = False
        image_response = self.dnac._exec(
            family="software_image_management_swim",
            function='get_software_image_details',
            params={"image_name": name},
        )
        self.log(str(image_response))
        image_list = image_response.get("response")
        if (len(image_list) == 1):
            image_exist = True

        return image_exist

    def get_device_id(self, params):
        """
        Retrieve the unique device ID based on the provided parameters.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            params (dict): A dictionary containing parameters to filter devices.
        Returns:
            str: The unique device ID corresponding to the filtered device.
        Description:
            This function sends a request to Cisco DNA Center to retrieve a list of devices based on the provided
            filtering parameters. If a single matching device is found, it extracts and returns the device ID. If
            no device or multiple devices match the criteria, it raises an exception.
        """
        device_id = None
        response = self.dnac._exec(
            family="devices",
            function='get_device_list',
            params=params,
        )
        self.log(str(response))

        device_list = response.get("response")
        if (len(device_list) == 1):
            device_id = device_list[0].get("id")
            self.log("Device Id: " + str(device_id))
        else:
            self.log("Device not found")

        return device_id

    def get_device_uuids(self, site_name, device_family, device_role):
        """
        Retrieve a list of device UUIDs based on the specified criteria.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            site_name (str): The name of the site for which device UUIDs are requested.
            device_family (str): The family/type of devices to filter on.
            device_role (str): The role of devices to filter on. If None, all roles are considered.
        Returns:
            list: A list of device UUIDs that match the specified criteria.
        Description:
            The function checks the reachability status and role of devices in the given site.
            Only devices with "Reachable" status are considered, and filtering is based on the specified
            device family and role (if provided).
        """

        device_uuid_list = []
        if not site_name:
            return device_uuid_list

        (site_exists, site_id) = self.site_exists(site_name)
        if not site_exists:
            return device_uuid_list

        site_params = {
            "site_id": site_id,
            "device_family": device_family
        }
        response = self.dnac._exec(
            family="sites",
            function='get_membership',
            op_modifies=True,
            params=site_params,
        )
        response = response['device'][0]['response']
        if len(response) > 0:
            for item in response:
                if item["reachabilityStatus"] != "Reachable":
                    continue
                if "role" in item and (device_role is None or item["role"] == device_role.upper() or device_role.upper() == "ALL"):
                    device_uuid_list.append(item["instanceUuid"])

        return device_uuid_list

    def get_device_family_identifier(self, family_name):
        """
        Retrieve and store the device family identifier based on the provided family name.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            family_name (str): The name of the device family for which to retrieve the identifier.
        Returns:
            None
        Raises:
            AnsibleFailJson: If the family name is not found in the response.
        Description:
            This function sends a request to Cisco DNA Center to retrieve a list of device family identifiers.It then
            searches for a specific family name within the response and stores its associated identifier. If the family
            name is found, the identifier is stored; otherwise, an exception is raised.
        """

        have = {}
        response = self.dnac._exec(
            family="software_image_management_swim",
            function='get_device_family_identifiers',
        )
        self.log(str(response))
        device_family_db = response.get("response")
        if device_family_db:
            device_family_details = get_dict_result(device_family_db, 'deviceFamily', family_name)
            if device_family_details:
                device_family_identifier = device_family_details.get("deviceFamilyIdentifier")
                have["device_family_identifier"] = device_family_identifier
                self.log("Family device indentifier:" + str(device_family_identifier))
            else:
                self.module.fail_json(msg="Family Device Name not found", response=[])
            self.have.update(have)

    def get_have(self):
        """
        Retrieve and store various software image and device details based on user-provided information.
        Returns:
            self: The current instance of the class with updated 'have' attributes.
        Raises:
            AnsibleFailJson: If required image or device details are not provided.
        Description:
            This function populates the 'have' dictionary with details related to software images, site information,
            device families, distribution devices, and activation devices based on user-provided data in the 'want' dictionary.
            It validates and retrieves the necessary information from Cisco DNAC to support later actions.
        """

        if self.want.get("tagging_details"):
            have = {}
            tagging_details = self.want.get("tagging_details")
            if tagging_details.get("image_name"):
                name = tagging_details.get("image_name").split("/")[-1]
                image_id = self.get_image_id(name)
                have["tagging_image_id"] = image_id

            elif self.have.get("imported_image_id"):
                have["tagging_image_id"] = self.have.get("imported_image_id")

            else:
                self.module.fail_json(msg="Image details for tagging not provided", response=[])

            # check if given site exists, store siteid
            # if not then use global site
            site_name = tagging_details.get("site_name")
            if site_name:
                site_exists = False
                (site_exists, site_id) = self.site_exists(site_name)
                if site_exists:
                    have["site_id"] = site_id
                    self.log("Site Exists: " + str(site_exists) + "\n Site_id:" + str(site_id))
            else:
                # For global site, use -1 as siteId
                have["site_id"] = "-1"
                self.log("Site Name not given by user. Using global site.")

            self.have.update(have)
            # check if given device family name exists, store indentifier value
            family_name = tagging_details.get("device_type")
            self.get_device_family_identifier(family_name)

        if self.want.get("distribution_details"):
            have = {}
            distribution_details = self.want.get("distribution_details")
            site_name = distribution_details.get("site_name")
            if site_name:
                site_exists = False
                (site_exists, site_id) = self.site_exists(site_name)

                if site_exists:
                    have["site_id"] = site_id
                    self.log("Site Exists: " + str(site_exists) + "\n Site_id:" + str(site_id))

            # check if image for distributon is available
            if distribution_details.get("image_name"):
                name = distribution_details.get("image_name").split("/")[-1]
                image_id = self.get_image_id(name)
                have["distribution_image_id"] = image_id

            elif self.have.get("imported_image_id"):
                have["distribution_image_id"] = self.have.get("imported_image_id")

            else:
                self.module.fail_json(msg="Image details for distribution not provided", response=[])

            device_params = dict(
                hostname=distribution_details.get("device_hostname"),
                serialNumber=distribution_details.get("device_serial_number"),
                managementIpAddress=distribution_details.get("device_ip_address"),
                macAddress=distribution_details.get("device_mac_address"),
            )
            device_id = self.get_device_id(device_params)
            if device_id is not None:
                have["distribution_device_id"] = device_id
            self.have.update(have)

        if self.want.get("activation_details"):
            have = {}
            activation_details = self.want.get("activation_details")
            # check if image for activation is available
            if activation_details.get("image_name"):
                name = activation_details.get("image_name").split("/")[-1]
                image_id = self.get_image_id(name)
                have["activation_image_id"] = image_id

            elif self.have.get("imported_image_id"):
                have["activation_image_id"] = self.have.get("imported_image_id")

            else:
                self.module.fail_json(msg="Image details for activation not provided", response=[])

            site_name = activation_details.get("site_name")
            if site_name:
                site_exists = False
                (site_exists, site_id) = self.site_exists(site_name)
                if site_exists:
                    have["site_id"] = site_id
                    self.log("Site Exists: " + str(site_exists) + "\n Site_id:" + str(site_id))

            device_params = dict(
                hostname=activation_details.get("device_hostname"),
                serialNumber=activation_details.get("device_serial_number"),
                managementIpAddress=activation_details.get("device_ip_address"),
                macAddress=activation_details.get("device_mac_address"),
            )
            device_id = self.get_device_id(device_params)
            if device_id is not None:
                have["activation_device_id"] = device_id
            self.have.update(have)

        return self

    def get_want(self, config):
        """
        Retrieve and store import, tagging, distribution, and activation details from playbook configuration.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            config (dict): The configuration dictionary containing image import and other details.
        Returns:
            self: The current instance of the class with updated 'want' attributes.
        Raises:
            AnsibleFailJson: If an incorrect import type is specified.
        Description:
            This function parses the playbook configuration to extract information related to image
            import, tagging, distribution, and activation. It stores these details in the 'want' dictionary
            for later use in the Ansible module.
        """

        want = {}
        if config.get("import_image_details"):
            want["import_image"] = True
            want["import_type"] = config.get("import_image_details").get("type").lower()
            if want["import_type"] == "url":
                want["url_import_details"] = config.get("import_image_details").get("url_details")
            elif want["import_type"] == "local":
                want["local_import_details"] = config.get("import_image_details").get("local_image_details")
            else:
                self.module.fail_json(msg="Incorrect import type. Supported Values: local or url")

        want["tagging_details"] = config.get("tagging_details")
        want["distribution_details"] = config.get("image_distribution_details")
        want["activation_details"] = config.get("image_activation_details")

        self.want = want
        self.log(str(self.want))

        return self

    def get_diff_import(self):
        """
        Check the image import type and fetch the image ID for the imported image for further use.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Returns:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Description:
            This function checks the type of image import (URL or local) and proceeds with the import operation accordingly.
            It then monitors the import task's progress and updates the 'result' dictionary. If the operation is successful,
            'changed' is set to True.
            Additionally, if tagging, distribution, or activation details are provided, it fetches the image ID for the
            imported image and stores it in the 'have' dictionary for later use.
        """

        try:
            import_type = self.want.get("import_type")

            if not import_type:
                self.msg = "Error: Details required for importing SWIM image. Please provide the necessary information."
                self.result['msg'] = self.msg
                self.log(self.msg, "WARNING")
                self.status = "success"
                self.result['changed'] = False
                return self

            if import_type == "url":
                image_name = self.want.get("url_import_details").get("payload")[0].get("source_url")
            else:
                image_name = self.want.get("local_import_details").get("file_path")

            # Code to check if the image already exists in DNAC
            name = image_name.split('/')[-1]
            image_exist = self.is_image_exist(name)

            import_key_mapping = {
                'source_url': 'sourceURL',
                'image_family': 'imageFamily',
                'application_type': 'applicationType',
                'third_party': 'thirdParty',
            }

            if image_exist:
                image_id = self.get_image_id(name)
                self.have["imported_image_id"] = image_id
                self.msg = "Image {0} already exists in the Cisco DNA Center".format(name)
                self.result['msg'] = self.msg
                self.log(self.msg)
                self.status = "success"
                self.result['changed'] = False
                return self

            if self.want.get("import_type") == "url":
                import_payload_dict = {}
                temp_payload = self.want.get("url_import_details").get("payload")[0]
                keys_to_change = list(import_key_mapping.keys())

                for key, val in temp_payload.items():
                    if key in keys_to_change:
                        api_key_name = import_key_mapping[key]
                        import_payload_dict[api_key_name] = val

                import_image_payload = [import_payload_dict]
                import_params = dict(
                    payload=import_image_payload,
                    scheduleAt=self.want.get("url_import_details").get("schedule_at"),
                    scheduleDesc=self.want.get("url_import_details").get("schedule_desc"),
                    scheduleOrigin=self.want.get("url_import_details").get("schedule_origin"),
                )
                import_function = 'import_software_image_via_url'
            else:
                import_params = dict(
                    is_third_party=self.want.get("local_import_details").get("is_third_party"),
                    third_party_vendor=self.want.get("local_import_details").get("third_party_vendor"),
                    third_party_image_family=self.want.get("local_import_details").get("third_party_image_family"),
                    third_party_application_type=self.want.get("local_import_details").get("third_party_application_type"),
                    file_path=self.want.get("local_import_details").get("file_path"),
                )
                import_function = 'import_local_software_image'

            response = self.dnac._exec(
                family="software_image_management_swim",
                function=import_function,
                op_modifies=True,
                params=import_params,
            )

            self.log(str(response))

            task_details = {}
            task_id = response.get("response").get("taskId")

            while (True):
                task_details = self.get_task_details(task_id)
                name = image_name.split('/')[-1]

                if task_details and \
                        ("completed successfully" in task_details.get("progress").lower()):
                    self.result['changed'] = True
                    self.status = "success"
                    self.msg = "Swim Image {0} imported successfully".format(name)
                    self.result['msg'] = self.msg
                    self.log(self.msg)
                    break

                if task_details and task_details.get("isError"):
                    if "already exists" in task_details.get("failureReason", ""):
                        self.msg = "SWIM Image {0} already exists in the Cisco DNA Center".format(name)
                        self.result['msg'] = self.msg
                        self.log(self.msg)
                        self.status = "success"
                        self.result['changed'] = False
                        break
                    else:
                        self.status = "failed"
                        self.msg = task_details.get("failureReason", "SWIM Image {0} seems to be invalid".format(image_name))
                        self.log(self.msg)
                        self.result['response'] = self.msg
                        return self

            self.result['response'] = task_details if task_details else response

            # Fetch image_id for the imported image for further use
            image_name = image_name.split('/')[-1]
            image_id = self.get_image_id(image_name)
            self.have["imported_image_id"] = image_id

            return self

        except Exception as e:
            self.status = "failed"
            self.msg = """Error: Import image details are not provided in the playbook, or the Import Image API was not
                 triggered successfully. Please ensure the necessary details are provided and verify the status of the Import Image process."""
            self.log(self.msg, "ERROR")
            self.result['response'] = self.msg

        return self

    def get_diff_tagging(self):
        """
        Tag or untag a software image as golden based on provided tagging details.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Returns:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Description:
            This function tags or untags a software image as a golden image in Cisco DNAC based on the provided
            tagging details. The tagging action is determined by the value of the 'tagging' attribute
            in the 'tagging_details' dictionary.If 'tagging' is True, the image is tagged as golden, and if 'tagging'
            is False, the golden tag is removed. The function sends the appropriate request to Cisco DNAC and updates the
            task details in the 'result' dictionary. If the operation is successful, 'changed' is set to True.
        """

        tagging_details = self.want.get("tagging_details")
        tag_image_golden = tagging_details.get("tagging")

        if tag_image_golden:
            image_params = dict(
                imageId=self.have.get("tagging_image_id"),
                siteId=self.have.get("site_id"),
                deviceFamilyIdentifier=self.have.get("device_family_identifier"),
                deviceRole=tagging_details.get("device_role")
            )
            self.log("Image params for tagging image as golden:" + str(image_params))

            response = self.dnac._exec(
                family="software_image_management_swim",
                function='tag_as_golden_image',
                op_modifies=True,
                params=image_params
            )
            self.log(str(response))

        else:
            image_params = dict(
                image_id=self.have.get("tagging_image_id"),
                site_id=self.have.get("site_id"),
                device_family_identifier=self.have.get("device_family_identifier"),
                device_role=tagging_details.get("device_role")
            )
            self.log("Image params for un-tagging image as golden:" + str(image_params))

            response = self.dnac._exec(
                family="software_image_management_swim",
                function='remove_golden_tag_for_image',
                op_modifies=True,
                params=image_params
            )
            self.log(str(response))

        if response:
            task_details = {}
            task_id = response.get("response").get("taskId")
            task_details = self.get_task_details(task_id)
            if not task_details.get("isError"):
                self.result['changed'] = True
                self.result['msg'] = task_details.get("progress")
                self.status = "success"

            self.result['response'] = task_details if task_details else response

        return self

    def get_device_ip_from_id(self, device_id):
        """
        Retrieve the management IP address of a device from Cisco DNA Center using its ID.
        Args:
            - self (object): An instance of a class used for interacting with Cisco DNA Center.
            - device_id (str): The unique identifier of the device in Cisco DNA Center.
        Returns:
            str: The management IP address of the specified device.
        Raises:
            Exception: If there is an error while retrieving the response from Cisco DNA Center.
        Description:
            This method queries Cisco DNA Center for the device details based on its unique identifier (ID).
            It uses the 'get_device_list' function in the 'devices' family, extracts the management IP address
            from the response, and returns it. If any error occurs during the process, an exception is raised
            with an appropriate error message logged.
        """

        try:
            response = self.dnac._exec(
                family="devices",
                function='get_device_list',
                params={"id": device_id}
            )
            response = response.get('response')[0]
            device_ip = response.get("managementIpAddress")

            return device_ip
        except Exception as e:
            error_message = "Error while getting the response of device from Cisco DNA Center - {0}".format(str(e))
            self.log(error_message, "ERROR")
            raise Exception(error_message)

    def get_diff_distribution(self):
        """
        Get image distribution parameters from the playbook and trigger image distribution.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Returns:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Description:
            This function retrieves image distribution parameters from the playbook's 'distribution_details' and triggers
            the distribution of the specified software image to the specified device. It monitors the distribution task's
            progress and updates the 'result' dictionary. If the operation is successful, 'changed' is set to True.
        """

        distribution_details = self.want.get("distribution_details")
        site_name = distribution_details.get("site_name")
        device_family = distribution_details.get("device_family_name")
        device_role = distribution_details.get("device_role")
        device_uuid_list = self.get_device_uuids(site_name, device_family, device_role)
        image_id = self.have.get("distribution_image_id")

        if self.have.get("distribution_device_id"):
            distribution_params = dict(
                payload=[dict(
                    deviceUuid=self.have.get("distribution_device_id"),
                    imageUuid=image_id
                )]
            )
            self.log("Distribution Params: " + str(distribution_params))

            response = self.dnac._exec(
                family="software_image_management_swim",
                function='trigger_software_image_distribution',
                op_modifies=True,
                params=distribution_params,
            )
            if response:
                task_details = {}
                task_id = response.get("response").get("taskId")

                while (True):
                    task_details = self.get_task_details(task_id)

                    if not task_details.get("isError") and \
                            ("completed successfully" in task_details.get("progress")):
                        self.result['changed'] = True
                        self.status = "success"
                        self.result['msg'] = "Image with Id {0} Distributed Successfully".format(image_id)
                        break

                    if task_details.get("isError"):
                        self.status = "failed"
                        self.msg = "Image with Id {0} Distribution Failed".format(image_id)
                        self.log(self.msg)
                        self.result['response'] = task_details
                        break

                    self.result['response'] = task_details if task_details else response

            return self

        if len(device_uuid_list) == 0:
            self.status = "failed"
            msg = "No devices found for Image Distribution"
            self.result['msg'] = msg
            self.log(msg)
            return self

        self.log("List of device UUID's for Image Distribution " + str(device_uuid_list))
        device_distribution_count = 0
        device_ips_list = []
        for device_uuid in device_uuid_list:
            device_management_ip = self.get_device_ip_from_id(device_uuid)
            distribution_params = dict(
                payload=[dict(
                    deviceUuid=device_uuid,
                    imageUuid=image_id
                )]
            )
            self.log("Distribution Params: " + str(distribution_params))
            response = self.dnac._exec(
                family="software_image_management_swim",
                function='trigger_software_image_distribution',
                op_modifies=True,
                params=distribution_params,
            )
            if response:
                task_details = {}
                task_id = response.get("response").get("taskId")

                while (True):
                    task_details = self.get_task_details(task_id)

                    if not task_details.get("isError") and \
                            ("completed successfully" in task_details.get("progress")):
                        self.result['changed'] = True
                        self.status = "success"
                        self.result['msg'] = "Image with Id {0} Distributed Successfully".format(image_id)
                        device_distribution_count += 1
                        break

                    if task_details.get("isError"):
                        error_msg = "Image with Id {0} Distribution Failed".format(image_id)
                        self.log(error_msg)
                        self.result['response'] = task_details
                        device_ips_list.append(device_management_ip)
                        break

        if device_distribution_count == 0:
            self.status = "failed"
            self.msg = "Image with Id {0} Distribution Failed for all devices".format(image_id)
        elif device_distribution_count == len(device_uuid_list):
            self.result['changed'] = True
            self.status = "success"
            self.msg = "Image with Id {0} Distributed Successfully for all devices".format(image_id)
        else:
            self.result['changed'] = True
            self.status = "success"
            self.msg = "Image with Id {0} Distributed and partially Successfull".format(image_id)
            self.log("For Devices {0} Image Distribution gets Failed".format(str(device_ips_list)), "CRITICAL")

        self.result['msg'] = self.msg
        self.log(self.msg)

        return self

    def get_diff_activation(self):
        """
        Get image activation parameters from the playbook and trigger image activation.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Returns:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Description:
            This function retrieves image activation parameters from the playbook's 'activation_details' and triggers the
            activation of the specified software image on the specified device. It monitors the activation task's progress and
            updates the 'result' dictionary. If the operation is successful, 'changed' is set to True.
        """

        activation_details = self.want.get("activation_details")
        site_name = activation_details.get("site_name")
        device_family = activation_details.get("device_family_name")
        device_role = activation_details.get("device_role")
        device_uuid_list = self.get_device_uuids(site_name, device_family, device_role)
        image_id = self.have.get("activation_image_id")

        if self.have.get("activation_device_id"):
            payload = [dict(
                activateLowerImageVersion=activation_details.get("activate_lower_image_version"),
                deviceUpgradeMode=activation_details.get("device_upgrade_mode"),
                distributeIfNeeded=activation_details.get("distribute_if_needed"),
                deviceUuid=self.have.get("activation_device_id"),
                imageUuidList=[image_id]
            )]

            activation_params = dict(
                schedule_validate=activation_details.get("scehdule_validate"),
                payload=payload
            )
            self.log("Activation Params: " + str(activation_params))

            response = self.dnac._exec(
                family="software_image_management_swim",
                function='trigger_software_image_activation',
                op_modifies=True,
                params=activation_params,
            )
            task_details = {}
            task_id = response.get("response").get("taskId")

            while (True):
                task_details = self.get_task_details(task_id)

                if not task_details.get("isError") and \
                        ("completed successfully" in task_details.get("progress")):
                    self.result['changed'] = True
                    self.result['msg'] = "Image Activated successfully"
                    self.status = "success"
                    break

                if task_details.get("isError"):
                    error_msg = "Activation for Image with Id - {0} gets Failed".format(image_id)
                    self.status = "failed"
                    self.result['response'] = task_details
                    self.msg = error_msg
                    return self

            self.result['response'] = task_details if task_details else response

            return self

        if len(device_uuid_list) == 0:
            self.status = "failed"
            msg = "No Devices found for Image Activation"
            self.result['msg'] = msg
            self.log(msg)
            return self

        # if len(device_uuid_list) > 0:
        self.log("List of device UUID's for Image Activation" + str(device_uuid_list))
        device_activation_count = 0
        device_ips_list = []

        for device_uuid in device_uuid_list:
            device_management_ip = self.get_device_ip_from_id(device_uuid)
            payload = [dict(
                activateLowerImageVersion=activation_details.get("activate_lower_image_version"),
                deviceUpgradeMode=activation_details.get("device_upgrade_mode"),
                distributeIfNeeded=activation_details.get("distribute_if_needed"),
                deviceUuid=device_uuid,
                imageUuidList=[image_id]
            )]

            activation_params = dict(
                schedule_validate=activation_details.get("scehdule_validate"),
                payload=payload
            )
            self.log("Activation Params: " + str(activation_params))

            response = self.dnac._exec(
                family="software_image_management_swim",
                function='trigger_software_image_activation',
                op_modifies=True,
                params=activation_params,
            )
            if response:
                task_details = {}
                task_id = response.get("response").get("taskId")

                while (True):
                    task_details = self.get_task_details(task_id)

                    if not task_details.get("isError") and \
                            ("completed successfully" in task_details.get("progress")):
                        self.result['changed'] = True
                        self.status = "success"
                        self.result['msg'] = "Image with Id {0} Activated Successfully".format(image_id)
                        device_activation_count += 1
                        break

                    if task_details.get("isError"):
                        error_msg = "Image with Id {0} Activation Failed".format(image_id)
                        self.result['response'] = task_details
                        device_ips_list.append(device_management_ip)
                        break

        if device_activation_count == 0:
            self.status = "failed"
            msg = "Image with Id {0} Activation Failed for all devices".format(image_id)
        elif device_activation_count == len(device_uuid_list):
            self.result['changed'] = True
            self.status = "success"
            msg = "Image with Id {0} Activated Successfully for all devices".format(image_id)
        else:
            self.result['changed'] = True
            self.status = "success"
            msg = "Image with Id {0} Activated and partially Successfull".format(image_id)
            self.log("For Devices {0} Image Activation gets Failed".format(str(device_ips_list)), "CRITICAL")

        self.result['msg'] = msg
        self.log(msg)

        return self

    def get_diff_merged(self, config):
        """
        Get tagging details and then trigger distribution followed by activation if specified in the playbook.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            config (dict): The configuration dictionary containing tagging, distribution, and activation details.
        Returns:
            self: The current instance of the class with updated 'result' and 'have' attributes.
        Description:
            This function checks the provided playbook configuration for tagging, distribution, and activation details. It
            then triggers these operations in sequence if the corresponding details are found in the configuration.The
            function monitors the progress of each task and updates the 'result' dictionary accordingly. If any of the
            operations are successful, 'changed' is set to True.
        """

        if config.get("tagging_details"):
            self.get_diff_tagging().check_return_status()

        if config.get("image_distribution_details"):
            self.get_diff_distribution().check_return_status()

        if config.get("image_activation_details"):
            self.get_diff_activation().check_return_status()

        return self


def main():
    """ main entry point for module execution
    """

    element_spec = {'dnac_host': {'required': True, 'type': 'str'},
                    'dnac_port': {'type': 'str', 'default': '443'},
                    'dnac_username': {'type': 'str', 'default': 'admin', 'aliases': ['user']},
                    'dnac_password': {'type': 'str', 'no_log': True},
                    'dnac_verify': {'type': 'bool', 'default': 'True'},
                    'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
                    'dnac_debug': {'type': 'bool', 'default': False},
                    'dnac_log_level': {'type': 'str', 'default': 'INFO'},
                    'dnac_log': {'type': 'bool', 'default': False},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged']}
                    }

    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    dnac_swims = DnacSwims(module)
    state = dnac_swims.params.get("state")

    if state not in dnac_swims.supported_states:
        dnac_swims.status = "invalid"
        dnac_swims.msg = "State {0} is invalid".format(state)
        dnac_swims.check_return_status()

    dnac_swims.validate_input().check_return_status()
    for config in dnac_swims.validated_config:
        dnac_swims.reset_values()
        dnac_swims.get_want(config).check_return_status()
        dnac_swims.get_diff_import().check_return_status()
        dnac_swims.get_have().check_return_status()
        dnac_swims.get_diff_state_apply[state](config).check_return_status()

    module.exit_json(**dnac_swims.result)


if __name__ == '__main__':
    main()
