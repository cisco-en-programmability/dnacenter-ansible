#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2022, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Madhan Sankaranarayanan, Rishita Chowdhary, Abhishek Maheshwari")

DOCUMENTATION = r"""
---
module: site_intent
short_description: Resource module for Site operations
description:
- Manage operation create, update and delete of the resource Sites.
- Creates site with area/building/floor with specified hierarchy.
- Updates site with area/building/floor with specified hierarchy.
- Deletes site with area/building/floor with specified hierarchy.
version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.intent_params
author: Madhan Sankaranarayanan (@madhansansel)
        Rishita Chowdhary (@rishitachowdhary)
        Abhishek Maheshwari (@abhishekmaheshwari)
options:
  config_verify:
    description: Set to True to verify the Cisco DNA Center config after applying the playbook config.
    type: bool
    default: False
  dnac_log_level:
    description: Specifies the log level for Cisco Catalyst Center logging, categorizing logs by severity.
        Options- [CRITICAL, ERROR, WARNING, INFO, DEBUG]
    type: str
    default: INFO
  state:
    description: The state of DNAC after module completion.
    type: str
    choices: [ merged, deleted ]
    default: merged
  config:
    description:
    - List of details of site being managed.
    type: list
    elements: dict
    required: true
    suboptions:
      type:
        description: Type of site to create/update/delete (eg area, building, floor).
        type: str
      site:
        description: Site Details.
        type: dict
        suboptions:
          area:
            description: Site Create's area.
            type: dict
            suboptions:
              name:
                description: Name of the area (eg Area1).
                type: str
              parentName:
                description: Complete Parent name of the Area to be created/deleted(eg Global/).
                type: str
          building:
            description: Building Details.
            type: dict
            suboptions:
              address:
                description: Address of the building to be created.
                type: str
              latitude:
                description: Latitude coordinate of the building (eg 37.338).Values between -90 to +90.
                type: int
              longitude:
                description: Longitude coordinate of the building (eg -121.832).Values between -180 to +180.
                type: int
              name:
                description: Name of the building (eg building1).
                type: str
              parent_name:
                description: Complete Parent name of the Building to be created/deleted(eg Global/USA/San Francisco).
                type: str
          floor:
            description: Site Create's floor.
            type: dict
            suboptions:
              height:
                description: Height of the floor units is ft. (eg 15).
                type: int
              length:
                description: Length of the floor units is ft. (eg 100).
                type: int
              name:
                description: Name of the floor (eg floor-1).
                type: str
              parentName:
                description: Complete Parent name of the floor to be created(eg Global/USA/San Francisco/BGL_18).
                type: str
              rf_model:
                description: Type of floor. Allowed values are 'Cubes And Walled Offices',
                  'Drywall Office Only', 'Indoor High Ceiling', 'Outdoor Open Space'.
                type: str
              width:
                description: Width of the floor units is ft. (eg 100).
                type: int
              floor_number:
                description: Floor number in the building/site (eg 5).once created, it can't be modified.
                type: int

requirements:
- dnacentersdk == 2.4.5
- python >= 3.5
notes:
  - SDK Method used are
    sites.Sites.create_site,
    sites.Sites.update_site,
    sites.Sites.delete_site

  - Paths used are
    post /dna/intent/api/v1/site,
    put dna/intent/api/v1/site/{siteId},
    delete dna/intent/api/v1/site/{siteId}
"""

EXAMPLES = r"""
- name: Create a new area site
  cisco.dnac.site_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: "{{dnac_log}}"
    state: merged
    config:
    - site:
        area:
          name: string
          parentName: string
      type: string

- name: Create a new building site
  cisco.dnac.site_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: "{{dnac_log}}"
    state: merged
    config:
    - site:
        building:
          address: string
          latitude: 0
          longitude: 0
          name: string
          parentName: string
      type: string

- name: Create a Floor site under the building
  cisco.dnac.site_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: "{{dnac_log}}"
    state: merged
    config:
    - site:
        floor:
          name: string
          parent_name: string
          length: int
          width: int
          height: int
          rf_model: string
          floor_number: int
      type: string

- name: Updating the Floor details under the building
  cisco.dnac.site_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: "{{dnac_log}}"
    state: merged
    config:
    - site:
        floor:
          name: string
          parent_name: string
          length: int
          width: int
          height: int
      type: string

- name: Deleting any site you need site name and parentName
  cisco.dnac.site_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: "{{dnac_log}}"
    state: deleted
    config:
    - site:
        floor:
          name: string
          parent_name: string
      type: string
"""

RETURN = r"""
#Case_1: Site is successfully created/updated/deleted
response_1:
  description: A dictionary with API execution details as returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response":
        {
             "bapiExecutionId": String,
             "bapiKey": String,
             "bapiName": String,
             "endTime": String,
             "endTimeEpoch": 0,
             "runtimeInstanceId": String,
             "siteId": String,
             "startTime": String,
             "startTimeEpoch": 0,
             "status": String,
             "timeDuration": 0

        },
      "msg": "string"
    }

#Case_2: Site exits and does not need an update
response_2:
  description: A dictionary with existing site details.
  returned: always
  type: dict
  sample: >
    {
      "response":
      {
            "site": {},
            "siteId": String,
            "type": String
      },
      "msg": String
    }

#Case_3: Error while creating/updating/deleting site
response_3:
  description: A dictionary with API execution details as returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response":
        {
             "bapiError": String,
             "bapiExecutionId": String,
             "bapiKey": String,
             "bapiName": String,
             "endTime": String,
             "endTimeEpoch": 0,
             "runtimeInstanceId": String,
             "startTime": String,
             "startTimeEpoch": 0,
             "status": String,
             "timeDuration": 0

        },
      "msg": "string"
    }

#Case_4: Site not found when atempting to delete site
response_4:
  description: A list with the response returned by the Cisco DNAC Python
  returned: always
  type: list
  sample: >
    {
       "response": [],
       "msg": String
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    log,
    get_dict_result,
)

floor_plan = {
    '101101': 'Cubes And Walled Offices',
    '101102': 'Drywall Office Only',
    '101105': 'Free Space',
    '101104': 'Indoor High Ceiling',
    '101103': 'Outdoor Open Space'
}


class DnacSite(DnacBase):
    """Class containing member attributes for site intent module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Returns:
            The method returns an instance of the class with updated attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either 'success' or 'failed').
                - self.validated_config: If successful, a validated version of the 'config' parameter.
        Example:
            To use this method, create an instance of the class and call 'validate_input' on it.
            If the validation succeeds, 'self.status' will be 'success' and 'self.validated_config'
            will contain the validated configuration. If it fails, 'self.status' will be 'failed', and
            'self.msg' will describe the validation issues.
        """

        if not self.config:
            self.msg = "config not available in playbook for validattion"
            self.status = "success"
            return self

        temp_spec = dict(
            type=dict(required=False, type='str'),
            site=dict(required=True, type='dict'),
        )
        self.config = self.camel_to_snake_case(self.config)
        # Validate site params
        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(
                "\n".join(invalid_params)
            )
            self.status = "failed"
            return self

        self.validated_config = valid_temp
        log(str(valid_temp))
        self.msg = "Successfully validated input"
        self.status = "success"
        return self

    def get_current_site(self, site):
        """
        Get the current site information.
        Parameters:
          self (object): An instance of a class used for interacting with Cisco DNA Center.
          - site (list): A list containing information about the site.
        Returns:
          - dict: A dictionary containing the extracted site information.
        Description:
            This method extracts information about the current site based on
          the provided 'site' list. It determines the type of the site
          (area, building, or floor) and retrieves specific details
          accordingly. The resulting dictionary includes the type, site
          details, and the site ID.
        """

        site_info = {}

        location = get_dict_result(site[0].get("additionalInfo"), 'nameSpace', "Location")
        typeinfo = location.get("attributes").get("type")

        if typeinfo == "area":
            site_info = dict(
                area=dict(
                    name=site[0].get("name"),
                    parentName=site[0].get("siteNameHierarchy").split("/" + site[0].get("name"))[0]
                )
            )

        elif typeinfo == "building":
            site_info = dict(
                building=dict(
                    name=site[0].get("name"),
                    parentName=site[0].get("siteNameHierarchy").split("/" + site[0].get("name"))[0],
                    address=location.get("attributes").get("address"),
                    latitude=location.get("attributes").get("latitude"),
                    longitude=location.get("attributes").get("longitude"),
                    country=location.get("attributes").get("country"),
                )
            )

        elif typeinfo == "floor":
            map_geometry = get_dict_result(site[0].get("additionalInfo"), 'nameSpace', "mapGeometry")
            map_summary = get_dict_result(site[0].get("additionalInfo"), 'nameSpace', "mapsSummary")
            rf_model = map_summary.get("attributes").get("rfModel")

            site_info = dict(
                floor=dict(
                    name=site[0].get("name"),
                    parentName=site[0].get("siteNameHierarchy").split("/" + site[0].get("name"))[0],
                    rf_model=floor_plan.get(rf_model),
                    width=map_geometry.get("attributes").get("width"),
                    length=map_geometry.get("attributes").get("length"),
                    height=map_geometry.get("attributes").get("height"),
                    floorNumber=map_geometry.get("attributes").get("floor_number", "")
                )
            )

        current_site = dict(
            type=typeinfo,
            site=site_info,
            siteId=site[0].get("id")
        )

        log(str(current_site))

        return current_site

    def site_exists(self):
        """
        Check if the site exists in Cisco DNA Center.

        Parameters:
          - self (object): An instance of the class containing the method.
        Returns:
          - tuple: A tuple containing a boolean indicating whether the site exists and
                   a dictionary containing information about the existing site.
                   The returned tuple includes two elements:
                   - site_exists (bool): Indicates whether the site exists.
                   - dict: Contains information about the existing site. If the
                           site doesn't exist, this dictionary is empty.
        Description:
            Checks the existence of a site in Cisco DNA Center by querying the
          'get_site' function in the 'sites' family. It utilizes the
          'site_name' parameter from the 'want' attribute to identify the site.
        """

        site_exists = False
        current_site = {}
        response = None
        try:
            response = self.dnac._exec(
                family="sites",
                function='get_site',
                params={"name": self.want.get("site_name")},
            )

        except Exception as e:
            self.log("The input site {0} is not valid or site is not present.".format(self.want.get("site_name")))

        if response:
            self.log(str(response))

            response = response.get("response")
            current_site = self.get_current_site(response)
            site_exists = True

        log(str(self.validated_config))

        return (site_exists, current_site)

    def get_site_params(self, params):
        """
        Store the site-related parameters.

        Parameters:
          self (object): An instance of a class used for interacting with Cisco DNA Center.
          - params (dict): Dictionary containing site-related parameters.
        Returns:
          - dict: Dictionary containing the stored site-related parameters.
                  The returned dictionary includes the following keys:
                  - 'type' (str): The type of the site.
                  - 'site' (dict): Dictionary containing site-related info.
        Description:
            This method takes a dictionary 'params' containing site-related
          information and stores the relevant parameters based on the site
          type. If the site type is 'floor', it ensures that the 'rfModel'
          parameter is stored in uppercase.
        """
        typeinfo = params.get("type")
        site_info = {}

        if typeinfo == 'area':
            area_details = params.get('site').get('area')
            site_info['area'] = {
                'name': area_details.get('name'),
                'parentName': area_details.get('parent_name')
            }
        elif typeinfo == 'building':
            building_details = params.get('site').get('building')
            site_info['building'] = {
                'name': building_details.get('name'),
                'address': building_details.get('address'),
                'parentName': building_details.get('parent_name'),
                'latitude': building_details.get('latitude'),
                'longitude': building_details.get('longitude'),
                'country': building_details.get('country')
            }
        else:
            floor_details = params.get('site').get('floor')
            site_info['floor'] = {
                'name': floor_details.get('name'),
                'parentName': floor_details.get('parent_name'),
                'length': floor_details.get('length'),
                'width': floor_details.get('width'),
                'height': floor_details.get('height'),
                'floorNumber': floor_details.get('floor_number', '')
            }
            try:
                site_info["floor"]["rfModel"] = floor_details.get("rf_model")
            except Exception as e:
                self.log("Floor doesnot have rfModel attribute")

        site_params = dict(
            type=typeinfo,
            site=site_info,
        )

        return site_params

    def get_site_name(self, site):
        """
        Get and Return the site name.
        Parameters:
          - self (object): An instance of a class used for interacting with Cisco DNA Center.
          - site (dict): A dictionary containing information about the site.
        Returns:
          - str: The constructed site name.
        Description:
            This method takes a dictionary 'site' containing information about
          the site and constructs the site name by combining the parent name
          and site name.
        """

        site_type = site.get("type")
        parent_name = site.get("site").get(site_type).get("parent_name")
        name = site.get("site").get(site_type).get("name")
        site_name = '/'.join([parent_name, name])
        self.log(site_name)

        return site_name

    def compare_float_values(self, ele1, ele2, precision=2):
        """
        Compare two floating-point values with a specified precision.
        Args:
            - self (object): An instance of a class used for interacting with Cisco DNA Center.
            - ele1 (float): The first floating-point value to be compared.
            - ele2 (float): The second floating-point value to be compared.
            - precision (int, optional): The number of decimal places to consider in the comparison, Defaults to 2.
        Return:
            bool: True if the rounded values are equal within the specified precision, False otherwise.
        Description:
            This method compares two floating-point values, ele1 and ele2, by rounding them
            to the specified precision and checking if the rounded values are equal. It returns
            True if the rounded values are equal within the specified precision, and False otherwise.
        """

        return round(float(ele1), precision) == round(float(ele2), precision)

    def is_area_updated(self, updated_site, requested_site):
        """
        Check if the area site details have been updated.
        Args:
            - self (object): An instance of a class used for interacting with Cisco DNA Center.
            - updated_site (dict): The site details after the update.
            - requested_site (dict): The site details as requested for the update.
        Return:
            bool: True if the area details (name and parentName) have been updated, False otherwise.
        Description:
            This method compares the area details (name and parentName) of the updated site
            with the requested site and returns True if they are equal, indicating that the area
            details have been updated. Returns False if there is a mismatch in the area site details.
        """

        return (
            updated_site['name'] == requested_site['name'] and
            updated_site['parentName'] == requested_site['parentName']
        )

    def is_building_updated(self, updated_site, requested_site):
        """
        Check if the building details in a site have been updated.
        Args:
            - self (object): An instance of a class used for interacting with Cisco DNA Center.
            - updated_site (dict): The site details after the update.
            - requested_site (dict): The site details as requested for the update.
        Return:
            bool: True if the building details have been updated, False otherwise.
        Description:
            This method compares the building details of the updated site with the requested site.
            It checks if the name, parentName, latitude, longitude, and address (if provided) are
            equal, indicating that the building details have been updated. Returns True if the
            details match, and False otherwise.
        """

        return (
            updated_site['name'] == requested_site['name'] and
            updated_site['parentName'] == requested_site['parentName'] and
            self.compare_float_values(updated_site['latitude'], requested_site['latitude']) and
            self.compare_float_values(updated_site['longitude'], requested_site['longitude']) and
            (requested_site['address'] is None or updated_site['address'] == requested_site['address'])
        )

    def is_floor_updated(self, updated_site, requested_site):
        """
        Check if the floor details in a site have been updated.

        Args:
            - self (object): An instance of a class used for interacting with Cisco DNA Center.
            - updated_site (dict): The site details after the update.
            - requested_site (dict): The site details as requested for the update.
        Return:
            bool: True if the floor details have been updated, False otherwise.
        Description:
            This method compares the floor details of the updated site with the requested site.
            It checks if the name, rf_model, length, width, and height are equal, indicating
            that the floor details have been updated. Returns True if the details match, and False otherwise.
        """

        keys_to_compare = ['length', 'width', 'height']
        if updated_site['name'] != requested_site['name'] or updated_site['rf_model'] != requested_site['rfModel']:
            return False

        for key in keys_to_compare:
            if not self.compare_float_values(updated_site[key], requested_site[key]):
                return False

        return True

    def site_requires_update(self):
        """
        Check if the site requires updates.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Returns:
            bool: True if the site requires updates, False otherwise.
        Description:
            This method compares the site parameters of the current site
            ('current_site') and the requested site parameters ('requested_site')
            stored in the 'want' attribute. It checks for differences in
            specified parameters, such as the site type and site details.
        """

        type = self.have['current_site']['type']
        updated_site = self.have['current_site']['site'][type]
        requested_site = self.want['site_params']['site'][type]
        self.log("Current Site: " + str(updated_site))
        self.log("Requested Site: " + str(requested_site))

        if type == "building":
            return not self.is_building_updated(updated_site, requested_site)

        elif type == "floor":
            return not self.is_floor_updated(updated_site, requested_site)

        return not self.is_area_updated(updated_site, requested_site)

    def get_have(self, config):
        """
        Get the site details from DNAC
        Parameters:
          - self (object): An instance of a class used for interacting with Cisco DNA Center.
          - config (dict): A dictionary containing the configuration details.
        Returns:
          - self (object): An instance of a class used for interacting with  Cisco DNA Center.
        Description:
            This method queries Cisco DNA Center to check if a specified site
            exists. If the site exists, it retrieves details about the current
            site, including the site ID and other relevant information. The
            results are stored in the 'have' attribute for later reference.
        """

        site_exists = False
        current_site = None
        have = {}

        # check if given site exits, if exists store current site info
        (site_exists, current_site) = self.site_exists()

        log("Site Exists: " + str(site_exists) + "\n Current Site:" + str(current_site))

        if site_exists:
            have["site_id"] = current_site.get("siteId")
            have["site_exists"] = site_exists
            have["current_site"] = current_site

        self.have = have

        return self

    def get_want(self, config):
        """
        Get all site-related information from the playbook needed for creation/updation/deletion of site in Cisco DNA Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            config (dict): A dictionary containing configuration information.
        Returns:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Description:
            Retrieves all site-related information from playbook that is
            required for creating a site in Cisco DNA Center. It includes
            parameters such as 'site_params' and 'site_name.' The gathered
            information is stored in the 'want' attribute for later reference.
        """

        want = {}
        want = dict(
            site_params=self.get_site_params(config),
            site_name=self.get_site_name(config),
        )

        self.want = want

        return self

    def get_diff_merged(self, config):
        """
        Update/Create site information in Cisco DNA Center with fields
        provided in the playbook.
        Parameters:
          self (object): An instance of a class used for interacting with Cisco DNA Center.
          config (dict): A dictionary containing configuration information.
        Returns:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Description:
            This method determines whether to update or create a site in Cisco DNA Center based on the provided
            configuration information. If the specified site exists, the method checks if it requires an update
            by calling the 'site_requires_update' method. If an update is required, it calls the 'update_site'
            function from the 'sites' family of the Cisco DNA Center API. If the site does not require an update,
            the method exits, indicating that the site is up to date.
        """

        site_updated = False
        site_created = False

        # check if the given site exists and/or needs to be updated/created.
        if self.have.get("site_exists"):
            if self.site_requires_update():
                # Existing Site requires update
                site_params = self.want.get("site_params")
                site_params["site_id"] = self.have.get("site_id")

                response = self.dnac._exec(
                    family="sites",
                    function='update_site',
                    op_modifies=True,
                    params=site_params,
                )
                site_updated = True

            else:
                # Site does not neet update
                self.result['response'] = self.have.get("current_site")
                self.msg = "Site - {0} does not need any update".format(self.have.get("current_site"))
                self.log(self.msg)
                self.result['msg'] = self.msg
                return self

        else:
            # Creating New Site
            site_params = self.want.get("site_params")
            response = self.dnac._exec(
                family="sites",
                function='create_site',
                op_modifies=True,
                params=self.want.get("site_params"),
            )

            log(str(response))
            site_created = True

        if site_created or site_updated:
            if response and isinstance(response, dict):
                executionid = response.get("executionId")
                while True:
                    execution_details = self.get_execution_details(executionid)
                    if execution_details.get("status") == "SUCCESS":
                        self.result['changed'] = True
                        self.result['response'] = execution_details
                        break

                    elif execution_details.get("bapiError"):
                        self.module.fail_json(msg=execution_details.get("bapiError"),
                                              response=execution_details)
                        break

                if site_updated:
                    log_msg = "Site - {0} Updated Successfully".format(self.want.get("site_name"))
                    self.log(log_msg)
                    self.result['msg'] = log_msg
                    self.result['response'].update({"siteId": self.have.get("site_id")})

                else:
                    # Get the site id of the newly created site.
                    (site_exists, current_site) = self.site_exists()

                    if site_exists:
                        log_msg = "Site - {0} Created Successfully".format(current_site)
                        self.log(log_msg)
                        self.log("Current site:" + str(current_site))
                        self.result['msg'] = log_msg
                        self.result['response'].update({"siteId": current_site.get('site_id')})

        return self

    def delete_single_site(self, site_id, site_name):
        """"
        Delete a single site in the Cisco DNA Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
            site_id (str): The ID of the site to be deleted.
            site_name (str): The name of the site to be deleted.
        Returns:
            self (object): An instance of a class used for interacting with Cisco DNA Center.
        Description:
            This function initiates the deletion of a site in the Cisco DNA Center by calling the delete API.
            If the deletion is successful, the result is marked as changed, and the status is set to "success."
            If an error occurs during the deletion process, the status is set to "failed," and the log contains
            details about the error.
        """

        try:
            response = self.dnac._exec(
                family="sites",
                function="delete_site",
                params={"site_id": site_id},
            )

            if response and isinstance(response, dict):
                executionid = response.get("executionId")
                while True:
                    execution_details = self.get_execution_details(executionid)
                    if execution_details.get("status") == "SUCCESS":
                        msg = "Site - {0} deleted successfully".format(site_name)
                        self.result['changed'] = True
                        self.result['response'] = msg
                        self.status = "success"
                        self.log(msg)
                        break
                    elif execution_details.get("bapiError"):
                        self.module.fail_json(msg=execution_details.get("bapiError"), response=execution_details)
                        break

        except Exception as e:
            msg = "Cannot Delete device from Inventory because of {0}".format(str(e))
            self.log(msg)
            self.status = "failed"
            self.msg = msg

        return self

    def get_diff_deleted(self, config):
        """
        Call Cisco DNA Center API to delete sites with provided inputs.
        Parameters:
          - self (object): An instance of a class used for interacting with Cisco DNA Center.
          - config (dict): Dictionary containing information for site deletion.
        Returns:
          - self: The result dictionary includes the following keys:
              - 'changed' (bool): Indicates whether changes were made
                 during the deletion process.
              - 'response' (dict): Contains details about the execution
                 and the deleted site ID.
              - 'msg' (str): A message indicating the status of the deletion operation.
        Description:
            This method initiates the deletion of a site by calling the 'delete_site' function in the 'sites' family
            of the Cisco DNA Center API. It uses the site ID obtained from the 'have' attribute.
        """

        site_exists = self.have.get("site_exists")
        if not site_exists:
            msg = msg = "Cannot delete Site - {0} as it's not found in Cisco DNA Center".format(self.want.get("site_name"))
            self.result.update({'changed': False,
                                'response': msg,
                                'msg': msg})
            self.log(msg)
            self.status = "success"
            return self

        # Check here if the site have the childs then fetch it using get membership API and then sort it
        # in reverse order and start deleting from bottom to top
        site_id = self.have.get("site_id")
        mem_response = self.dnac._exec(
            family="sites",
            function="get_membership",
            params={"site_id": site_id},
        )
        site_response = mem_response.get("site").get("response")

        if len(site_response) == 0:
            self.delete_single_site(site_id, self.want.get("site_name"))
            return self

        # Sorting the response in reverse order based on hierarchy levels
        sorted_site_resp = sorted(site_response, key=lambda x: x.get("groupHierarchy"), reverse=True)

        # Deleting each level in reverse order till topmost parent site
        for item in sorted_site_resp:
            self.delete_single_site(item['id'], item['name'])

        # Delete the final parent site
        self.delete_single_site(site_id, self.want.get("site_name"))
        msg = "Site - {0} and it's child sites deleted successfully".format(self.want.get("site_name"))
        self.result['response'] = msg
        self.log(msg)

        return self

    def verify_diff_merged(self, config):
        """
        Verify the merged status(Creation/Updation) of site configuration in Cisco DNA Center.
        Args:
            - self (object): An instance of a class used for interacting with Cisco DNA Center.
            - config (dict): The configuration details to be verified.
        Return:
            - self (object): An instance of a class used for interacting with Cisco DNA Center.
        Description:
            This method checks the merged status of a configuration in Cisco DNA Center by retrieving the current state
            (have) and desired state (want) of the configuration, logs the states, and validates whether the specified
            site exists in the DNA Center configuration.
        """

        self.get_have(config)
        self.log(str(self.have))
        self.log(str(self.want))
        # Code to validate dnac config for merged state
        site_exist = self.have.get("site_exists")

        if site_exist:
            self.status = "success"
            msg = "Requested Site - {0} present in Cisco DNA Center and creation verified.".format(self.want.get("site_name"))
            self.log(msg)

        require_update = self.site_requires_update()

        if not require_update:
            self.log("Site - {0} Updation Verified Successfully.".format(self.want.get("site_name")))
            self. status = "success"
            return self

        self.log("Playbook paramater doesnot match with the Cisco DNA Center means Merged task not executed successfully.")

        return self

    def verify_diff_deleted(self, config):
        """
        Verify the deletion status of site configuration in Cisco DNA Center.
        Args:
            - self (object): An instance of a class used for interacting with Cisco DNA Center.
            - config (dict): The configuration details to be verified.
        Return:
            - self (object): An instance of a class used for interacting with Cisco DNA Center.
        Description:
            This method checks the deletion status of a configuration in Cisco DNA Center.
            It validates whether the specified site exists in the DNA Center configuration.
        """

        self.get_have(config)
        self.log(str(self.have))
        self.log(str(self.want))
        # Code to validate dnac config for delete state
        site_exist = self.have.get("site_exists")

        if not site_exist:
            self.status = "success"
            msg = "Requested Site - {0} already deleted from Cisco DNA Center and verified successfully.".format(self.want.get("site_name"))
            self.log(msg)
            return self

        self.log("Playbook paramater doesnot match with the Cisco DNA Center means Deletion not executed successfully.")

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
                    'config_verify': {'type': 'bool', "default": False},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged', 'deleted']}
                    }

    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    dnac_site = DnacSite(module)
    state = dnac_site.params.get("state")

    if state not in dnac_site.supported_states:
        dnac_site.status = "invalid"
        dnac_site.msg = "State {0} is invalid".format(state)
        dnac_site.check_return_status()

    dnac_site.validate_input().check_return_status()
    config_verify = dnac_site.params.get("config_verify")

    for config in dnac_site.validated_config:
        dnac_site.reset_values()
        dnac_site.get_want(config).check_return_status()
        dnac_site.get_have(config).check_return_status()
        dnac_site.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            dnac_site.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**dnac_site.result)


if __name__ == '__main__':
    main()
