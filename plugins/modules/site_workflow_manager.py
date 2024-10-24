#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = (
    "Madhan Sankaranarayanan, Rishita Chowdhary, Abhishek Maheshwari, Megha Kandari, Sonali Deepthi Kesali")

DOCUMENTATION = r"""
---
module: site_workflow_manager
short_description: Resource module for Site operations
description:
- Manage operation create, bulk create, update and delete of the resource Sites.
- Creates site with area/building/floor with specified hierarchy.
- Create multiple sites (area, building, or floor) with specified hierarchies in bulk.
- Updates site with area/building/floor with specified hierarchy.
- Deletes site with area/building/floor with specified hierarchy.
version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Madhan Sankaranarayanan (@madhansansel)
        Rishita Chowdhary (@rishitachowdhary)
        Abhishek Maheshwari (@abhishekmaheshwari)
        Megha Kandari (@kandarimegha)
        Sonali Deepthi Kesali (@skesali)
options:
  config_verify:
    description: Set to true to verify the Cisco Catalyst Center config after applying the playbook config.
    type: bool
    default: false
  state:
    description: The state of Catalyst Center after module completion.
    type: str
    choices: [ merged, deleted ]
    default: merged
  config:
    description: It represents a list of details for creating/managing/deleting sites, including areas, buildings, and floors.
    type: list
    elements: dict
    required: True
    suboptions:
      site_type:
        description: Type of site to create/update/delete (eg area, building, floor).
        type: str
      site:
        description: Contains details about the site being managed including areas, buildings and floors.
        type: dict
        suboptions:
          area:
            description: Configuration details for creating or managing an area within a site.
            type: dict
            suboptions:
              name:
                description: Name of the area to be created or managed (e.g., "Area1").
                type: str
              parent_name:
                description: The full name of the parent under which the area will be created/managed/deleted (e.g., "Global/USA").
                type: str
          building:
            description: Configuration details required for creating or managing a building within a site.
            type: dict
            suboptions:
              address:
                description: Physical address of the building that is to be created or managed.
                type: str
              latitude:
                description: Geographical latitude coordinate of the building. For example, use 37.338 for a location in San Jose, California.
                    Valid values range from -90.0 to +90.0 degrees.
                type: float
              longitude:
                description: Geographical longitude coordinate of the building. For example, use -121.832 for a location in San Jose, California.
                    Valid values range from -180.0 to +180.0 degrees.
                type: float
              name:
                description: Name of the building (e.g., "Building1").
                type: str
              parent_name:
                description: Hierarchical parent path of the building, indicating its location within the site (e.g., "Global/USA/San Francisco").
                type: str
          floor:
            description: Configuration details required for creating or managing a floor within a site.
            type: dict
            suboptions:
              height:
                description: Height of the floor in feet (e.g., 15.23).
                type: float
              length:
                description: Length of the floor in feet (e.g., 100.11).
                type: float
              name:
                description: Name of the floor (e.g., "Floor-1").
                type: str
              parent_name:
                description: Hierarchical parent path of the floor, indicating its location within the site (e.g.,
                    "Global/USA/San Francisco/BGL_18").
                type: str
              rf_model:
                description: The RF (Radio Frequency) model type for the floor, which is essential for simulating and optimizing wireless
                    network coverage. Select from the following allowed values, which describe different environmental signal propagation
                    characteristics.
                    Type of floor (allowed values are 'Cubes And Walled Offices', 'Drywall Office Only', 'Indoor High Ceiling',
                    'Outdoor Open Space').
                    Cubes And Walled Offices - This RF model typically represents indoor areas with cubicles or walled offices, where
                        radio signals may experience attenuation due to walls and obstacles.
                    Drywall Office Only - This RF model indicates an environment with drywall partitions, commonly found in office spaces,
                        which may have moderate signal attenuation.
                    Indoor High Ceiling - This RF model is suitable for indoor spaces with high ceilings, such as auditoriums or atriums,
                        where signal propagation may differ due to the height of the ceiling.
                    Outdoor Open Space - This RF model is used for outdoor areas with open spaces, where signal propagation is less obstructed
                        and may follow different patterns compared to indoor environments.
                type: str
              width:
                description: Width of the floor in feet (e.g., 100.22).
                type: float
              floor_number:
                description: Floor number within the building site (e.g., 5). This value can only be specified during the creation of the
                    floor and cannot be modified afterward.
                type: int
              bulk_operation:
                description: Set to 'true' or 'false' to enable bulk operations for site creation and management.
                type: bool
                default: false

requirements:
- dnacentersdk == 2.4.5
- python >= 3.9
notes:
  - SDK Method used are
    sites.Sites.create_site,
    sites.Sites.update_site,
    sites.Sites.delete_site
    site.Sites.create_sites
    site.Sites.update_a_floor
    site.Sites.update_a_building
    site.Sites.update_an_area
    site.Sites.delete_a_floor
    site.Sites.delete_a_building
    site.Sites.delete_an_area
    site.Sites.get_site_assigned_network_devices

  - Paths used are
    POST /dna/intent/api/v1/site,
    PUT dna/intent/api/v1/site/{siteId},
    DELETE dna/intent/api/v1/site/{siteId}
    DELETE/dna/intent/api/v2/buildings/{id}
    DELETE/dna/intent/api/v1/areas/{id}
    DELETE/dna/intent/api/v2/floors/{id}
    PUT/dna/intent/api/v2/floors/{id}
    PUT/dna/intent/api/v1/areas/{id}
    PUT/dna/intent/api/v2/buildings/{id}
    GET/dna/intent/api/v1/sites
    POST/dna/intent/api/v1/sites/bulk
    GET/dna/intent/api/v1/networkDevices/assignedToSite
"""

EXAMPLES = r"""
- name: Create a new area site
  cisco.dnac.site_workflow_manager:
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
          name: Test
          parent_name: Global/India
      site_type: area

- name: Create a new building site
  cisco.dnac.site_workflow_manager:
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
          name: Building_1
          parent_name: Global/India
          address: Bengaluru, Karnataka, India
          latitude: 24.12
          longitude: 23.45
      site_type: building

- name: Create a Floor site under the building
  cisco.dnac.site_workflow_manager:
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
          name: Floor_1
          parent_name: Global/India/Building_1
          length: 75.76
          width: 35.54
          height: 30.12
          rf_model: Cubes And Walled Offices
          floor_number: 2
      site_type: floor

- name: Updating the Floor details under the building
  cisco.dnac.site_workflow_manager:
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
          name: Floor_1
          parent_name: Global/India/Building_1
          length: 75.76
          width: 35.54
          height: 30.12
      site_type: floor

- name: Deleting any site you need site name and parent name
  cisco.dnac.site_workflow_manager:
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
          name: Floor_1
          parent_name: Global/India/Building_1
      site_type: floor

- name: Create bulk sites and upload floor map
  cisco.dnac.site_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: DEBUG
    config_verify: True
    state: merged
    config:
    - site:
        area:
            - name: japan
              parent_name_hierarchy: 'Global'
            - name: Abc2
              parent_name_hierarchy: 'Global'
        building:
            - name: blossom
              address: '1234 Elm Street'
              parent_name_hierarchy: 'Global/japan'
              latitude: 37.387
              longitude: -121.845
              country: India
        floor:
            - name: cherry
              parent_name_hierarchy: 'Global/japan/blossom'
              length: 103.23
              width: 75.1
              height: 50.23
              rf_model: 'Cubes And Walled Offices'
              floor_number: 3
              units_of_measure: 'feet'
              upload_floor_image_path: "/Users/skesali/Downloads/pngegg.png"
        bulk_operation: true
"""

RETURN = r"""
#Case_1: Site is successfully created/updated/deleted
response_1:
  description: A dictionary with API execution details as returned by the Cisco Catalyst Center Python SDK
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
  description: A dictionary with API execution details as returned by the Cisco Catalyst Center Python SDK
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
  description: A list with the response returned by the Cisco Catalyst Center Python
  returned: always
  type: list
  sample: >
    {
       "response": [],
       "msg": String
    }

#Case_5: Bulk site created successfully
response_5:
  description: A dictionary with API task details as returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
        "response": {
            "startTime": 1725427091204,
            "version": 1725427091204,
            "progress": "{\"TOTAL\":0,\"VALIDATION_FAILURE_COUNT\":0,\"VALIDATION_SUCCESS_COUNT\":0,\
            "VALIDATION_PENDING_COUNT\":0,\"CRAETION_SUCCESS_COUNT\":0,\"message\":\
            "Group import is in progress.Count will be updated shortly.\"}",
            "serviceType": "Grouping Service",
            "operationIdList": [
            "3e7f1f73-b6f8-4ac6-b925-22e372e72510"
            ],
            "isError": False,
            "instanceTenantId": "6663114d388b29001399e46a",
            "id": "0191bb78-0704-767c-94c6-95a6e5a511d1"
        },
        "version": "1.0"
    }

"""

floor_plan = {
    '101101': 'Cubes And Walled Offices',
    '101102': 'Drywall Office Only',
    '101105': 'Free Space',
    '101104': 'Indoor High Ceiling',
    '101103': 'Outdoor Open Space'
}
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    get_dict_result,
)

import os


class Site(DnacBase):
    """Class containing member attributes for Site workflow_manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]
        self.created_site_list, self.updated_site_list, self.update_not_needed_sites = [], [], []
        self.deleted_site_list, self.site_absent_list = [], []
        self.keymap = {}

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
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
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log("Error: {0}".format(self.msg), "ERROR")
            return self
        self.log("Configuration details found in the playbook: {0}".format(self.config), "INFO")
        temp_spec = dict(
            type=dict(required=False, type='str'),
            site=dict(required=True, type='dict'),
        )
        self.config = self.update_site_type_key(self.config)
        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(
                "\n".join(invalid_params)
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook config params: {0}".format(
            str(valid_temp))
        self.log(self.msg, "INFO")
        self.status = "success"

        return self

    def get_current_site(self, site):
        """
        Get the current site information.
        Parameters:
          self (object): An instance of a class used for interacting with Cisco Catalyst Center.
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
        location = get_dict_result(site[0].get(
            "additionalInfo"), 'nameSpace', "Location")
        typeinfo = location.get("attributes").get("type")

        if typeinfo == "area":
            site_info = dict(
                area=dict(
                    name=site[0].get("name"),
                    parentName=site[0].get("siteNameHierarchy").split(
                        "/" + site[0].get("name"))[0]
                )
            )

        elif typeinfo == "building":
            site_info = dict(
                building=dict(
                    name=site[0].get("name"),
                    parentName=site[0].get("siteNameHierarchy").split(
                        "/" + site[0].get("name"))[0],
                    address=location.get("attributes").get("address"),
                    latitude=location.get("attributes").get("latitude"),
                    longitude=location.get("attributes").get("longitude"),
                    country=location.get("attributes").get("country"),
                )
            )

        elif typeinfo == "floor":
            map_geometry = get_dict_result(site[0].get(
                "additionalInfo"), 'nameSpace', "mapGeometry")
            map_summary = get_dict_result(site[0].get(
                "additionalInfo"), 'nameSpace', "mapsSummary")
            rf_model = map_summary.get("attributes").get("rfModel")
            site_info = dict(
                floor=dict(
                    name=site[0].get("name"),
                    parentName=site[0].get("siteNameHierarchy").split(
                        "/" + site[0].get("name"))[0],
                    rfmodel=rf_model,
                    width=map_geometry.get("attributes").get("width"),
                    length=map_geometry.get("attributes").get("length"),
                    height=map_geometry.get("attributes").get("height"),
                    floorNumber=map_summary.get('attributes').get('floorIndex')
                )
            )
        current_site = dict(
            type=typeinfo,
            site=site_info,
            siteId=site[0].get("id")
        )

        self.log("Current site details: {0}".format(str(current_site)), "INFO")
        return current_site

    def site_exists(self):
        """
        Check if the site exists in Cisco Catalyst Center.
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
            Checks the existence of a site in Cisco Catalyst Center by querying the
          'get_site' function in the 'sites' family. It utilizes the
          'site_name' parameter from the 'want' attribute to identify the site.
        """
        site_exists = False
        current_site = {}
        response = None

        if self.compare_dnac_versions(self.get_ccc_version(), "2.3.5.3") <= 0:
            site_name = self.want.get("site_name")
            response = self.get_site(site_name)
            if not response:
                self.log("No response received from 'get_site' API for site: {0}".format(site_name), "ERROR")
                return (site_exists, current_site)

            response = response.get("response")
            self.log("Received API response from 'get_site': {0}".format(str(response)), "DEBUG")

            current_site = self.get_current_site(response)
            if current_site:
                site_exists = True
                self.log("Site '{0}' exists in Cisco Catalyst Center".format(site_name), "INFO")
            else:
                self.log("No valid site details found for '{0}'".format(site_name), "WARNING")

            return (site_exists, current_site)

        else:
            try:
                response = {}
                if self.config[0].get('site', {}).get('bulk_operation', False):
                    bulk_operation = self.config[0].get('site', {}).get('bulk_operation', False)
                else:
                    bulk_operation = self.config[0]['site']['type']

                self.log("Bulk operation mode: {}".format(bulk_operation), "INFO")
                if bulk_operation:
                    name_list = [site["name"] for site in self.want if "name" in site]
                    all_sites_info = []
                    for name in name_list:
                        try:
                            response = self.get_site(name)
                            response_data = response.get("response", [])
                            site_exists = True
                            if not response_data:
                                self.log("No site information found for name: {0}".format(name), "WARNING")
                                return (site_exists, current_site)

                            for site in response_data:
                                if isinstance(site, dict):
                                    current_site = dict(site.items())
                                    if site.get('nameHierarchy'):
                                        current_site['parentName'] = site['nameHierarchy'].rsplit('/', 1)[0]
                                    else:
                                        current_site['parentName'] = None

                                    all_sites_info.append(current_site)
                                    site_exists = True
                        except Exception as e:
                            self.log("Error fetching site for name '{0}': {1}".format(name, str(e)))

                    return (site_exists, all_sites_info)

            except Exception as e:
                self.log("Bulk operation is not available due to : {0}".format(str(e)), "WARNING")
                name_hierarchy = self.want.get("site_name")
                try:
                    response = self.get_site(name_hierarchy)
                except Exception as e:
                    self.log("Error fetching site for {0}: {1}".format(name_hierarchy, str(e)))
                response = response.get("response")
                if not response:
                    self.log("No site information found for name hierarchy: {0}".format(name_hierarchy), "WARNING")
                    return (site_exists, current_site)

                if response:
                    self.log("Received API response from 'get_sites': {0}".format(
                        str(response)), "DEBUG")
                    all_sites_info = []
                    for site in response:
                        if isinstance(site, dict):
                            current_site = dict(site.items())
                            name_hierarchy = site.get('nameHierarchy', '')
                            if name_hierarchy:
                                current_site['parentName'] = name_hierarchy.rsplit('/', 1)[0]
                            else:
                                current_site['parentName'] = None

                            all_sites_info.append(current_site)
                            site_exists = True

            return (site_exists, current_site)

    def get_parent_id(self, parent_name):
        """
        Retrieve the ID of the parent site in Cisco Catalyst Center.

        Parameters:
        - parent_name (str): The name of the parent site for which the ID is to be retrieved.

        Returns:
        - str: The ID of the parent site if it exists. If the site is not found or an error occurs,
            it returns None.

        Description:
        This method checks whether the specified parent site exists in Cisco Catalyst Center by
        querying the 'get_site' function within the 'sites' family. If the site is found, its
        corresponding ID is returned. If the site does not exist, or if an error occurs during
        the query, the method logs the appropriate message and returns None.
        """
        parent_id = None
        self.log("Starting retrieval of parent site ID for site name: '{}'".format(parent_name), "DEBUG")

        try:
            parent_response = self.get_site(parent_name)
            parent_response = parent_response.get("response")
            if not parent_response:
                self.log("No data found for site '{}'. Site does not exist.".format(parent_name), "INFO")
                return None
            parent_id = parent_response[0].get("id")
            if parent_id:
                self.log("Parent site ID for site '{}' successfully retrieved: {}".format(parent_name, parent_id), "DEBUG")
            else:
                self.log("Parent site ID for site '{}' could not be retrieved from response.".format(parent_name), "WARNING")
        except Exception as e:
            self.log("An error occurred while retrieving site '{}': {}".format(parent_name, str(e)), "ERROR")
        return parent_id

    def get_site_params(self, params):
        """
        Store the site-related parameters.

        Parameters:
          self (object): An instance of a class used for interacting with Cisco Catalyst Center.
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

        if typeinfo not in ["area", "building", "floor"]:
            self.msg = "Given bulk site create playbook is only applicable to DNAC version 2.3.7.6"
            self.set_operation_result("failed", False, self.msg, "ERROR")

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

            if isinstance(floor_details, dict):
                rf_model = floor_details.get("rf_model")
                if not rf_model:
                    self.log("The attribute 'rf_model' is missing or has a falsy value in floor '{0}'.".format(
                        floor_details.get('name')), "WARNING")
                else:
                    site_info["floor"]["rfModel"] = rf_model

        site_params = dict(
            type=typeinfo,
            site=site_info,
        )
        self.log("Site parameters: {0}".format(str(site_params)), "DEBUG")
        return site_params

    def get_site_name(self, site):
        """
        Get and Return the site name.
        Parameters:
        - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        - site (dict): A dictionary containing information about the site.
        Returns:
        - str: The constructed site name.
        Description:
            This method takes a dictionary 'site' containing information about
        the site and constructs the site name by combining the parent name
        and site name.
        """
        try:
            self.log("Retrieving site name for site data: {}".format(site), "DEBUG")
            site_type = site.get("type")
            parent_name = site.get("site", {}).get(site_type, {}).get("parent_name")
            self.log("Identified site type: {}".format(site_type), "DEBUG")
            self.log("Retrieved parent name: {}".format(parent_name), "DEBUG")
            if not parent_name:
                self.msg = "Parent name is missing for site type '{}' in the playbook.".format(site_type)
                self.result["response"] = self.msg
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return None

            name = site.get("site", {}).get(site_type, {}).get("name")
            self.log("Retrieved site name: {}".format(name), "DEBUG")

            if not name:
                self.msg = "Site name is missing for site type '{}' in the playbook.".format(site_type)
                self.result["response"] = self.msg
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return None

            site_name = '/'.join([parent_name, name])
            self.log("Constructed site name: {}".format(site_name), "INFO")
            return site_name

        except Exception as e:
            error_message = "An error occurred while getting site name: {0}".format(str(e))
            self.log(error_message, "ERROR")

    def compare_float_values(self, ele1, ele2, precision=2):
        """
        Compare two floating-point values with a specified precision.
        Args:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
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
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - updated_site (dict): The site details after the update.
            - requested_site (dict): The site details as requested for the update.
        Return:
            bool: True if the area details (name and parent name) have been updated, False otherwise.
        Description:
            This method compares the area details (name and parent name) of the updated site
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
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - updated_site (dict): The site details after the update.
            - requested_site (dict): The site details as requested for the update.
        Return:
            bool: True if the building details have been updated, False otherwise.
        Description:
            This method compares the building details of the updated site with the requested site.
            It checks if the name, parent_name, latitude, longitude, and address (if provided) are
            equal, indicating that the building details have been updated. Returns True if the
            details match, and False otherwise.
        """
        return (
            updated_site['name'] == requested_site['name'] and
            updated_site['parentName'] == requested_site['parentName'] and
            self.compare_float_values(updated_site['latitude'], requested_site['latitude']) and
            self.compare_float_values(updated_site['longitude'], requested_site['longitude']) and
            ('address' in requested_site and (requested_site['address'] is None or updated_site.get(
                'address') == requested_site['address']))
        )

    def is_floor_updated(self, updated_site, requested_site):
        """
        Check if the floor details in a site have been updated.

        Args:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
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
        if updated_site['name'] != requested_site['name'] or updated_site.get('rf_model') != requested_site.get('rfModel'):
            return False
        if requested_site.get('floorNumber') and int(requested_site.get('floorNumber')) != int(updated_site.get('floorNumber')):
            return False

        for key in keys_to_compare:
            if not self.compare_float_values(updated_site[key], requested_site[key]):
                return False

        return True

    def site_requires_update(self):
        """
        Check if the site requires updates.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
            bool: True if the site requires updates, False otherwise.
        Description:
            This method compares the site parameters of the current site
            ('current_site') and the requested site parameters ('requested_site')
            stored in the 'want' attribute. It checks for differences in
            specified parameters, such as the site type and site details.
        """
        if self.compare_dnac_versions(self.get_ccc_version(), "2.3.5.3") <= 0:
            current_site = self.have.get('current_site', {})
            site_type = current_site.get('type')
            updated_site = current_site.get('site', {}).get(site_type)
            requested_site = self.want['site_params']['site'].get(site_type)
        else:
            current_site = self.have.get('current_site', {})
            site_type = current_site.get('type')
            self.log("Current site details: {}".format(current_site), "INFO")
            updated_site = current_site
            requested_site = self.want.get('site_params', {}).get('site', {}).get(site_type)

        self.log("Updated Site details: {}".format(updated_site), "INFO")
        self.log("Requested Site details: {}".format(requested_site), "INFO")

        if site_type == "building":
            needs_update = not self.is_building_updated(updated_site, requested_site)
            self.log("Building site requires update: {}".format(needs_update), "DEBUG")
            return needs_update

        if site_type == "floor":
            needs_update = not self.is_floor_updated(updated_site, requested_site)
            self.log("Floor site requires update: {}".format(needs_update), "DEBUG")
            return needs_update

        if site_type == "area":
            needs_update = not self.is_area_updated(updated_site, requested_site)
            self.log("Area site requires update: {}".format(needs_update), "DEBUG")
            return needs_update

        self.msg = "Unsupported site type '{0}' given in the playbook.".format(site_type)
        self.set_operation_result("failed", False, self.msg, "ERROR")
        return False

    def get_have(self, config):
        """
        Get the site details from Cisco Catalyst Center.

        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): A dictionary containing the configuration details.
        Returns:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method queries Cisco Catalyst Center to check if a specified site
            exists. If the site exists, it retrieves details about the current
            site, including the site ID and other relevant information. The
            results are stored in the 'have' attribute for later reference.
        """
        site_exists = False
        current_site = None
        have = {}

        try:
            if self.compare_dnac_versions(self.get_ccc_version(), "2.3.7.6") >= 0:
                if self.config[0].get('site', {}).get('bulk_operation', False):
                    site_exists, current_site = self.site_exists()
                    self.log("Bulk operation: Site exists: {}".format(site_exists), "DEBUG")
                    self.log("Current site details: {}".format(current_site), "DEBUG")

                    if site_exists:
                        have["site_exists"] = site_exists
                        have["current_site"] = current_site
                        self.log("Site details found in Cisco Catalyst Center: {}".format(current_site), "DEBUG")
                    else:
                        self.log("No site found in Cisco Catalyst Center.", "WARNING")
            site_exists, current_site = self.site_exists()
            self.log("Regular operation: Retrieved site existence: {}".format(site_exists), "DEBUG")

            if site_exists:
                if self.compare_dnac_versions(self.get_ccc_version(), "2.3.5.3") <= 0:
                    have["site_id"] = current_site.get("siteId")
                    self.log("Using legacy siteId for site version <= 2.3.5.3: {}".format(have["site_id"]), "DEBUG")
                else:
                    have["site_id"] = current_site.get("id")
                    self.log("Using updated site ID for newer version: {}".format(have["site_id"]), "DEBUG")

                have["site_exists"] = site_exists
                have["current_site"] = current_site

            self.have = have
            self.log("Final 'have' state updated: {}".format(self.have), "INFO")

            return self

        except Exception as e:
            self.msg = "An unexpected error occurred while retrieving site details: {}".format(e)
            self.set_operation_result("failed", False, self.msg, "ERROR")

    def get_want(self, config):
        """
        Get all site-related information from the playbook needed for creation/updation/deletion of site in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A dictionary containing configuration information.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            Retrieves all site-related information from playbook that is
            required for creating a site in Cisco Catalyst Center. It includes
            parameters such as 'site_params' and 'site_name.' The gathered
            information is stored in the 'want' attribute for later reference.
        """
        try:
            if self.compare_dnac_versions(self.get_ccc_version(), "2.3.7.6") >= 0:
                want_list = []
                if 'site' in self.config[0]:
                    self.keymap = {}
                    self.keymap = self.map_config_key_to_api_param(self.keymap, config)
                    self.keymap.update({
                        "floor_number": "floorNumber",
                        "rf_model": "rfModel",
                        "parent_name_hierarchy": "parentNameHierarchy",
                        "units_of_measure": "unitsOfMeasure"
                    })
                    self.log("Processing keymap: {}".format(self.keymap), "INFO")

                    if 'area' in self.config[0]['site']:
                        for area in self.config[0]['site']['area']:
                            self.log("Processing area: {0}".format(area['name']), "INFO")
                            want = {}
                            for key, value in area.items():
                                if value is not None:
                                    mapped_key = self.keymap.get(key, key)
                                    want[mapped_key] = value
                            want["type"] = "area"
                            want_list.append(want)
                            self.log("Constructed area entry: {}".format(want), "DEBUG")

                    if 'building' in self.config[0]['site']:
                        for building in self.config[0]['site']['building']:
                            self.log("Processing building: {0}".format(building['name']), "INFO")
                            want = {}
                            for key, value in building.items():
                                if value is not None:
                                    mapped_key = self.keymap.get(key, key)
                                    want[mapped_key] = value
                            want["type"] = "building"
                            want_list.append(want)
                            self.log("Constructed building entry: {}".format(want), "DEBUG")

                    if 'floor' in self.config[0]['site']:
                        for floor in self.config[0]['site']['floor']:
                            self.log("Processing floor: {0}".format(floor['name']), "INFO")
                            want = {}
                            for key, value in floor.items():
                                if value is not None:
                                    mapped_key = self.keymap.get(key, key)
                                    want[mapped_key] = value
                            want["type"] = "floor"
                            want_list.append(want)
                            self.log("Constructed floor entry: {}".format(want), "DEBUG")

                    self.want = want_list
                    self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
                    return self

        except Exception as e:
            self.log("An unexpected error occurred: {0}".format(e), "ERROR")

        want = dict(
            site_params=self.get_site_params(config),
            site_name=self.get_site_name(config),
        )
        self.want = want
        self.log("Desired State (want): {0}".format(self.pprint(self.want)), "INFO")
        return self

    def update_floor(self, site_params):
        """
        Updates a floor in the site hierarchy using the provided site parameters.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            site_params (dict): Dictionary containing parameters required for the floor update, including the site_id.

        Returns:
            dict: The API response from the 'updates_a_floor' operation or None if an exception occurs.
        """
        response = None
        units_of_measure = "feet"
        try:
            self.log("Updating floor with parameters: {0}".format(site_params), "INFO")
            parent_name = site_params.get("site", {}).get("floor", {}).get("parentName")
            parent_id = self.get_parent_id(parent_name)
            site_params['site']['floor']['parentId'] = parent_id
            site_params['site']['floor']['unitsOfMeasure'] = units_of_measure
            self.log("Updated site_params with parent_id: {0}".format(site_params), "INFO")
            floor_param = site_params.get('site', {}).get('floor')
            site_id = self.have.get("site_id")
            floor_param['id'] = site_id

            response = self.dnac._exec(
                family="site_design",
                function='updates_a_floor',
                op_modifies=True,
                params=floor_param
            )

            if response and isinstance(response, dict):
                self.log("Initial API response from 'updates_a_floor': {0}".format(response), "DEBUG")
                execution_id = response.get("executionId")

                if execution_id:
                    while True:
                        execution_details = self.get_execution_details(execution_id)
                        if execution_details.get("status") == "SUCCESS":
                            self.log("Floor update completed successfully.", "INFO")
                            break
                        elif execution_details.get("bapiError"):
                            self.status = "failed"
                            self.msg = "Error during floor update execution: {0}".format(execution_details.get("bapiError")), "ERROR"
                            self.result['response'] = self.msg
                            self.log(self.msg, "ERROR")
                            break

        except Exception as e:
            error_msg = "Exception occurred while updating floor with site_id '{0}' due to: {1}".format(
                site_params.get('site_id'), str(e)
            )
            self.log(error_msg, "ERROR")

        return response

    def update_building(self, site_params):
        """
        Updates a building in the site hierarchy using the provided site id.

        Args:
            site_params (dict): Dictionary containing parameters required for the building update, including the site_id.

        Returns:
            dict: The API response from the 'update_a_building' operation.
        """
        response = None
        try:
            self.log("Updating building with parameters: {0}".format(site_params), "INFO")
            parent_name = site_params.get("site", {}).get("building", {}).get("parentName")
            parent_id = self.get_parent_id(parent_name)
            site_params['site']['building']['parentId'] = parent_id
            self.log("Updated site_params with parent_id: {0}".format(site_params), "INFO")
            building_param = site_params.get('site', {}).get('building')
            site_id = self.have.get("site_id")
            building_param['id'] = site_id
            response = self.dnac._exec(
                family="site_design",
                function='updates_a_building',
                op_modifies=True,
                params=building_param,
            )
            self.log("Building update successful. API response: {0}".format(response), "DEBUG")

            return response

        except Exception as e:
            self.msg = "Exception occurred while updating building '{0}' due to: {1}".format(site_params.get('site_name'), str(e))
            self.result['response'] = self.msg
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def update_area(self, site_params):
        """
        Updates an area in the site hierarchy using the provided site id.

        Args:
            site_params (dict): Dictionary containing parameters required for the area update, including the site_id.

        Returns:
            dict: The API response from the 'update_an_area' operation.
        """
        response = None
        try:
            self.log("Updating area with parameters: {0}".format(
                site_params), "INFO")
            parent_id = self.have.get("parent_id")
            site_params['site']['area']['parentId'] = parent_id
            area_param = site_params.get('site', {}).get('area')
            site_id = self.have.get("site_id")
            area_param['id'] = site_id

            response = self.dnac._exec(
                family="site_design",
                function='updates_an_area',
                op_modifies=True,
                params=area_param,
            )
            self.log("Area update successful. API response: {0}".format(
                response), "DEBUG")

            return response

        except Exception as e:
            self.msg = "Exception occurred while updating area'{0}' due to: {1}".format(site_params.get('site_name'), str(e))
            self.result['response'] = self.msg
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def creating_bulk_site(self):
        """
        Creates a site (area, building, or floor) in the site hierarchy using the provided site parameters.

        Args:
            site_params (dict): Dictionary containing parameters required for the site creation.

        Returns:
            dict: The API response from the 'create_sites' operation.
        """
        params = self.want
        self.log("Before executing create site: {0}".format(params), "INFO")
        try:
            response = self.dnac._exec(
                family="site_design",
                function='create_sites',
                op_modifies=True,
                params={"payload": params}
            )

            if not response:
                self.log("Site creation failed: No response from the API.", "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                return None

            self.log("Site creation successful. Response: {0}".format(response), "INFO")
            return response

        except Exception as e:
            error_msg = "Exception occurred while creating site due to: {}".format(str(e))
            self.log(error_msg, "ERROR")
            self.status = "failed"
            self.check_return_status()

    def get_diff_merged(self, config):
        """
        Update/Create site information in Cisco Catalyst Center with fields
        provided in the playbook.
        Parameters:
          self (object): An instance of a class used for interacting with Cisco Catalyst Center.
          config (dict): A dictionary containing configuration information.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method determines whether to update or create a site in Cisco Catalyst Center based on the provided
            configuration information. If the specified site exists, the method checks if it requires an update
            by calling the 'site_requires_update' method. If an update is required, it calls the 'update_site'
            function from the 'sites' family of the Cisco Catalyst Center API. If the site does not require an update,
            the method exits, indicating that the site is up to date.
        """
        site_updated = False
        site_created = False

        if self.compare_dnac_versions(self.get_ccc_version(), "2.3.7.6") >= 0:
            try:
                bulk_operation = self.config[0].get('site', {}).get('bulk_operation', False)
                self.log("Bulk operation status retrieved: {}".format(bulk_operation))
                if bulk_operation:
                    response = self.creating_bulk_site()
                    self.log("Response from creating_bulk_site: {}".format(response))
                    if response and isinstance(response, dict) and "response" in response:
                        task_id = response["response"].get("taskId")
                        if task_id:
                            self.log("Task Id for the 'site_creation' task is {}".format(task_id), "INFO")

                            task_name = "create_sites"
                            success_msg = "Site created successfully."
                            self.get_task_status_from_tasks_by_id(task_id, task_name, success_msg)
                            self.result['changed'] = True

                            name_list = [site.get("name") for site in self.want if "name" in site]
                            self.created_site_list.append(name_list)
                            self.log("Site '{}' created successfully".format(name_list), "INFO")
                            return self
                        self.log("No valid task ID received from the 'creating_bulk_site' response.", "WARNING")
                        return None
                    self.log("No response received from the 'creating_bulk_site' API call.", "WARNING")
                    return None
            except Exception as e:
                self.log("Yaml is not available for bulk: {}".format(e), "ERROR")

        if self.have.get("site_exists"):
            site_name = self.want.get("site_name")

            if self.compare_dnac_versions(self.get_ccc_version(), "2.3.5.3") <= 0 and self.site_requires_update():
                try:
                    site_params = self.want.get("site_params")
                    site_params["site_id"] = self.have.get("site_id")
                    self.log("Site parameters prepared for update: {}".format(site_params))
                    self.log("Site update process started.", "INFO")

                    response = self.dnac._exec(
                        family="sites",
                        function='update_site',
                        op_modifies=True,
                        params=site_params,
                    )
                    self.log("Received API response from 'update_site': {0}".format(str(response)), "DEBUG")
                    site_updated = True
                except Exception as e:
                    self.log("Unexpected error occurred: {0}".format(str(e)), "ERROR")
                    error_message = "Site - {0} does not need any update".format(site_name)
                    return {"error_message": error_message}

            if not self.site_requires_update():
                self.update_not_needed_sites.append(site_name)
                self.log("Site - {0} does not need any update".format(site_name), "INFO")

                return self

            if site_updated and response and isinstance(response, dict):
                execution_id = response.get("executionId")
                while True:
                    execution_details = self.get_execution_details(execution_id)
                    if execution_details.get("status") == "SUCCESS":
                        self.result['changed'] = True
                        break
                    elif execution_details.get("bapiError"):
                        self.module.fail_json(msg=execution_details.get(
                            "bapiError"), response=execution_details)
                        break

                if site_updated:
                    self.updated_site_list.append(site_name)
                    self.log("Site - {0} Updated Successfully".format(site_name), "INFO")

                else:
                    site_exists = self.site_exists()
                    if site_exists:
                        self.created_site_list.append(site_name)
                        self.log("Site '{0}' created successfully".format(site_name), "INFO")

            elif self.compare_dnac_versions(self.get_ccc_version(), "2.3.7.6") >= 0 and self.site_requires_update():
                site_params = self.want.get("site_params")
                site_params["site_id"] = self.have.get("site_id")
                site_type = site_params.get("type")

                response = (self.update_floor(site_params) if site_type == "floor"
                            else self.update_area(site_params) if site_type == "area"
                            else self.update_building(site_params) if site_type == "building"
                            else self.log("Unknown site type: {0}".format(site_type), "ERROR"))

                if response:
                    self.log("Received API response from 'update_site': {0}".format(str(response)), "DEBUG")
                    site_updated = True

                if site_updated and response and isinstance(response, dict):
                    taskid = response["response"]["taskId"]
                    task_details = self.get_task_details(taskid)

                    while True:
                        if site_type != "floor":
                            if task_details.get("progress") == "Group is updated successfully":
                                self.result['changed'] = True
                                self.result['response'] = task_details
                                break
                        else:
                            if task_details.get("progress") == "Service domain is updated successfully.":
                                self.result['changed'] = True
                                self.result['response'] = task_details
                                break

                        if task_details.get("bapiError"):
                            self.module.fail_json(msg=task_details.get("bapiError"), response=task_details)
                            break
                else:
                    self.update_not_needed_sites.append(site_name)
                    self.log("Site - {0} does not need any update".format(site_name), "INFO")
                    return self

        else:
            self.log(site_updated)

            if self.compare_dnac_versions(self.get_ccc_version(), "2.3.5.3") <= 0:
                try:
                    site_params = self.want.get("site_params")
                    try:
                        if site_params['site'].get('building'):
                            building_details = {}
                            for key, value in site_params['site']['building'].items():
                                if value is not None:
                                    building_details[key] = value

                            site_params['site']['building'] = building_details

                    except Exception as e:
                        site_type = site_params['type']
                        name = site_params['site'][site_type]['name']
                        self.log(
                            "The site '{0}' is not categorized as a building; no need to filter 'None' values.".format(name), "INFO")

                    response = self.dnac._exec(
                        family="sites",
                        function='create_site',
                        op_modifies=True,
                        params=site_params,
                    )
                    self.log("Received API response from 'create_site': {0}".format(str(response)), "DEBUG")
                    site_created = True
                except Exception as e:
                    self.log("Unexpected error occurred: {0}".format(str(e)), "ERROR")
                    error_message = "Failed to create site '{0}': {1}".format(site_name, str(e))
                    return {"error_message": error_message}

                if (site_created or site_updated) and response and isinstance(response, dict):
                    executionid = response.get("executionId")
                    while True:
                        execution_details = self.get_execution_details(executionid)
                        if execution_details.get("status") == "SUCCESS":
                            self.result['changed'] = True
                            break
                        elif execution_details.get("bapiError"):
                            self.module.fail_json(msg=execution_details.get(
                                "bapiError"), response=execution_details)
                            break

                    site_exists, current_site = self.site_exists()
                    if site_exists:
                        site_name = self.want.get("site_name")
                        self.created_site_list.append(site_name)
                        self.log("Site '{0}' created successfully".format(site_name), "INFO")
                    return self
            else:
                self.msg = "This version : '{0}' given yaml format is not applicable to create a site' ".format(
                    self.payload.get("dnac_version"))
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        if site_updated:
            self.updated_site_list.append(site_name)
            self.log("Site - {0} Updated Successfully".format(site_name), "INFO")
        else:
            site_exists, current_site = self.site_exists()
            if site_exists:
                self.created_site_list.append(site_name)
                self.log("Site '{0}' created successfully".format(site_name), "INFO")

        return self

    def delete_single_site(self, site_id, site_name):
        """"
        Delete a single site in the Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            site_id (str): The ID of the site to be deleted.
            site_name (str): The name of the site to be deleted.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This function initiates the deletion of a site in the Cisco Catalyst Center by calling the delete API.
            If the deletion is successful, the result is marked as changed, and the status is set to "success."
            If an error occurs during the deletion process, the status is set to "failed," and the log contains
            details about the error.
        """
        try:
            response = self.dnac._exec(
                family="sites",
                function="delete_site",
                op_modifies=True,
                params={"site_id": site_id},
            )
            if response and isinstance(response, dict):
                self.log("Received API response from 'delete_site': {0}".format(str(response)), "DEBUG")
                executionid = response.get("executionId")

                while True:
                    execution_details = self.get_execution_details(executionid)
                    if execution_details.get("status") == "SUCCESS":
                        self.status = "success"
                        self.deleted_site_list.append(site_name)
                        self.log("Site '{0}' deleted successfully".format(site_name), "INFO")
                        break
                    elif execution_details.get("bapiError"):
                        self.log("Error response for 'delete_site' execution: {0}".format(
                            execution_details.get("bapiError")), "ERROR")
                        self.module.fail_json(msg=execution_details.get(
                            "bapiError"), response=execution_details)
                        break

        except Exception as e:
            self.msg = "Exception occurred while deleting site '{0}' due to: {1}".format(site_name, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")

        return self

    def delete_floor(self, site_name):
        """
        Deletes a floor site by ID.

        Parameters:
            site_id (str): The ID of the floor site to be deleted.
            site_name (str): The name of the floor site to be deleted.

        Returns:
            dict: The API response from the 'deletes_a_floor' operation.
        """
        site_id = self.have.get("site_id")
        try:
            self.log(
                "Deleting floor site: {0} with ID: {1}".format(site_name, site_id), "INFO")
            response = self.dnac._exec(
                family="site_design",
                function="deletes_a_floor",
                op_modifies=True,
                params={'id': site_id},
            )
            self.log("Successfully deleted floor site: {0}. API response: {1}".format(site_name, response), "DEBUG")
            return response
        except Exception as e:
            self.msg = "Exception occurred while deleting floor site '{0}' with site_id '{1}' due to: {2}".format(site_name, site_id, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def delete_building(self, site_name):
        """
        Deletes a building site by ID.

        Parameters:
            site_id (str): The ID of the building site to be deleted.
            site_name (str): The name of the building site to be deleted.

        Returns:
            dict: The API response from the 'deletes_a_building' operation.
        """
        site_id = self.have.get("site_id")
        try:

            self.log("Deleting building site: {0} with ID: {1}".format(site_name, site_id), "INFO")

            response = self.dnac._exec(
                family="site_design",
                function="deletes_a_building",
                op_modifies=True,
                params={'id': site_id},
            )
            self.log("Successfully deleted building site: {0}. API response: {1}".format(site_name, response), "DEBUG")
            return response

        except Exception as e:
            self.msg = "Exception occurred while deleting building site '{0}' with site_id '{1}' due to: {2}".format(site_name, site_id, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def delete_area(self, site_name):
        """
        Deletes an area site by ID.

        Parameters:
            site_id (str): The ID of the site to be deleted.
            site_name (str): The name of the site to be deleted.

        Returns:
            self: An instance of the class used for interacting with Cisco Catalyst Center.
        """
        site_id = self.have.get("site_id")
        try:
            self.log("Deleting area site: {0} with ID: {1}".format(site_name, site_id), "INFO")
            response = self.dnac._exec(
                family="site_design",
                function="deletes_an_area",
                op_modifies=True,
                params={'id': site_id},
            )
            self.log("Successfully deleted farea site: {0}. API response: {1}".format(site_name, response), "DEBUG")
            return response

        except Exception as e:
            self.msg = "Exception occurred while deleting area site '{0}' with site_id '{1}' due to: {2}".format(site_name, site_id, str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def get_diff_deleted(self, config):
        """
        Call Cisco Catalyst Center API to delete sites with provided inputs.
        Parameters:
          - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
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
            of the Cisco Catalyst Center API. It uses the site ID obtained from the 'have' attribute.
        """
        site_exists = self.have.get("site_exists")
        site_name = self.want.get("site_name")

        if not site_exists:
            self.status = "success"
            self.log(
                "Unable to delete site '{0}' as it's not found in Cisco Catalyst Center".format(self.want.get("site_name")), "INFO")
            return self

        if self.compare_dnac_versions(self.get_ccc_version(), "2.3.5.3") <= 0:
            site_id = self.have.get("site_id")
            api_response, response = self.get_device_ids_from_site(site_name, site_id)

            self.log(
                "Received API response from 'get_membership': {0}".format(str(api_response)), "DEBUG")

            site_response = api_response.get("site", {}).get("response", [])
            self.log(
                "Site '{0}' response along with its child sites: {1}".format(site_name, str(site_response)), "DEBUG")

            if not site_response:
                self.delete_single_site(site_id, site_name)
                return self

            sorted_site_resp = sorted(
                site_response, key=lambda x: x.get("groupHierarchy"), reverse=True)

            for item in sorted_site_resp:
                self.delete_single_site(item['id'], item['name'])

            self.delete_single_site(site_id, site_name)
            self.log(
                "The site '{0}' and its child sites have been deleted successfully".format(site_name), "INFO")

        elif self.compare_dnac_versions(self.get_ccc_version(), "2.3.7.6") >= 0:
            site_params = self.want.get("site_params")
            site_params["site_id"] = self.have.get("site_id")
            site_type = site_params.get("type")
            site_id = self.have.get("site_id")

            response = self.get_site(site_id)
            self.log("Received API response from 'get_site_assigned_network_devices': {0}".format(str(response)), "DEBUG")
            site_response = response.get("response", [])

            if site_response:
                self.module.fail_json(
                    msg=(
                        "Site '{0}' cannot be deleted because it has assigned devices. "
                        "Please delete devices first then delete the site.".format(site_name)
                    )
                )

                return self

            response = None
            if site_type == "floor":
                response = self.delete_floor(site_name)
            elif site_type == "area":
                response = self.delete_area(site_name)
                self.log(
                    "Manual test response for deleting area: {0}".format(str(response)), "DEBUG")
            elif site_type == "building":
                response = self.delete_building(site_name)

            self.log(
                "Received API response from 'deleted': {0}".format(str(response)), "DEBUG")
            site_deleted = response is not None

            if site_deleted and isinstance(response, dict):
                taskid = response.get("response", {}).get("taskId")

                if taskid:
                    task_details = self.get_task_details(taskid)
                    while True:
                        if site_type != "floor":
                            if task_details.get("progress") == "Group is deleted successfully":
                                self.log(
                                    "Area site '{0}' deleted successfully.".format(site_name), "INFO")
                                self.result['changed'] = True
                                self.result['response'] = task_details
                                self.deleted_site_list.append(site_name)
                                break
                            elif task_details.get("failureReason"):
                                self.log(
                                    "Error response for 'deletes_an_area' task: {0}".format(task_details.get('failureReason')), "ERROR")
                                self.module.fail_json(msg=task_details.get(
                                    "failureReason"), response=task_details)
                                break
                        else:
                            if task_details.get("progress") == "NCMP00150: Service domain is deleted successfully":
                                self.log("Area site '{0}' deleted successfully.".format(site_name), "INFO")
                                self.result['changed'] = True
                                self.result['response'] = task_details
                                self.deleted_site_list.append(site_name)
                                break
                            elif task_details.get("failureReason"):
                                self.log("Error response for 'deletes_an_area' task: {0}".format(task_details.get('failureReason')), "ERROR")
                                self.module.fail_json(msg=task_details.get(
                                    "failureReason"), response=task_details)
                                break

        return self

    def verify_diff_merged(self, config):
        """
        Verify the merged status (Creation/Updation) of site configuration in Cisco Catalyst Center.
        Args:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified.
        Return:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the merged status of a configuration in Cisco Catalyst Center by retrieving the current state
            (have) and desired state (want) of the configuration, logs the states, and validates whether the specified
            site exists in the Catalyst Center configuration.
        """
        try:
            if self.compare_dnac_versions(self.get_ccc_version(), "2.3.7.6") >= 0 and self.config[0].get('site', {}).get('bulk_operation', False):
                name_list = [site["name"] for site in self.want if "name" in site]
                self.get_have(config)
                site_exist = self.have.get("site_exists")

                if site_exist:
                    self.status = "success"
                    self.msg = "The requested site '{0}' is present in the Cisco Catalyst Center and its creation has been verified.".format(name_list)
                    self.log(self.msg, "INFO")
                return self

        except Exception as e:
            self.log("An unexpected error occurred: {0}".format(e), "ERROR")
            return self

        self.get_have(config)
        site_exist = self.have.get("site_exists")
        site_name = self.want.get("site_name")

        self.log("Current State (have): {0}".format(str(self.have)), "INFO")
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        if site_exist:
            self.status = "success"
            self.msg = "The requested site '{0}' is present in the Cisco Catalyst Center and its creation has been verified.".format(site_name)
            self.log(self.msg, "INFO")

        require_update = self.site_requires_update()

        if not require_update:
            self.log("The update for site '{0}' has been successfully verified.".format(site_name), "INFO")
            self.status = "success"
            return self

        self.log("""The playbook input for site '{0}' does not align with the Cisco Catalyst Center, indicating that the merge task
                may not have executed successfully.""".format(site_name), "INFO")

        return self

    def verify_diff_deleted(self, config):
        """
        Verify the deletion status of site configuration in Cisco Catalyst Center.
        Args:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified.
        Return:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the deletion status of a configuration in Cisco Catalyst Center.
            It validates whether the specified site exists in the Catalyst Center configuration.
        """
        self.get_have(config)
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        site_exist = self.have.get("site_exists")

        if not site_exist:
            self.status = "success"
            msg = """The requested site '{0}' has already been deleted from the Cisco Catalyst Center and this has been
                successfully verified.""".format(self.want.get("site_name"))
            self.log(msg, "INFO")
            return self

        self.log("""Mismatch between the playbook input for site '{0}' and the Cisco Catalyst Center indicates that
                 the deletion was not executed successfully.""".format(self.want.get("site_name")), "INFO")
        return self

    def upload_floor_image(self, config):
        map_details = None
        map_status = None
        response = None
        success_message = None

        try:
            self.log("Starting upload_floor_image function", "DEBUG")

            self.get_want(config)
            self.get_have(config)

            file_path = config['site']['floor'][0]['upload_floor_image_path']
            self.log("File path extracted from config: {}".format(file_path), "DEBUG")

            if not os.path.exists(file_path):
                raise ValueError("File path does not exist: {}".format(file_path))
            self.log("File path exists: {}".format(file_path), "DEBUG")

            if file_path.lower().endswith('.png'):
                content_type = 'image/png'
            elif file_path.lower().endswith('.jpg') or file_path.lower().endswith('.jpeg'):
                content_type = 'image/jpeg'
            elif file_path.lower().endswith('.pdf'):
                content_type = 'application/pdf'
            else:
                raise ValueError("Unsupported file format.")
            self.log("Determined content type: {}".format(content_type), "DEBUG")

            try:
                with open(file_path, "rb") as image_file:
                    file_content = image_file.read()
            except IOError as e:
                raise IOError("Failed to read file at {}: {}".format(file_path, str(e)))

            site_id = self.have.get("site_id")
            if not site_id:
                raise ValueError("No valid site_id found in 'self.have'.")
            multipart_fields = {
                'image': (os.path.basename(file_path), file_content, content_type)
            }

            if self.compare_dnac_versions(self.get_ccc_version(), "2.3.7.6") >= 0:
                try:
                    response = self.dnac._exec(
                        family="site_design",
                        function="uploads_floor_image",
                        op_modifies=True,
                        params={
                            "id": site_id,
                            "multipart_fields": multipart_fields,
                            "multipart_monitor_callback": None
                        }
                    )
                    if response is None:
                        self.log("No response received from the API.", "ERROR")
                    else:
                        self.log("API response: {}".format(response), "DEBUG")
                except Exception as e:
                    self.msg = "An exception occurred during API execution: {}".format(str(e))
                    self.log(self.msg, "ERROR")
                    self.module.fail_json(msg=self.msg)
                    return None, None, None

            else:
                raise ValueError("DNAC version is below the required version for this function.")

        except Exception as e:
            self.msg = "An exception occurred: {}".format(str(e))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return None, None, None

        if not response:
            self.msg = "Failed to upload floor image: No response from the API."
            self.set_operation_result("failed", False, self.msg, "ERROR")
        if isinstance(response, dict) and "id" in response:
            self.log("Received valid API response: {}".format(response), "DEBUG")
            map_details = True
            map_status = response
            success_message = "Floor image uploaded successfully."
            self.log(success_message, "INFO")
        else:
            self.log("Invalid response received from API. Response: {}".format(response), "ERROR")

        return map_details, map_status, success_message

    def update_site_messages(self):
        """
        Update site messages based on the status of created, updated, and deleted sites.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
            self (object): An instance of a class representing the status of the operation, including whether it was
                successful or failed, any error messages encountered during operation.
        Description:
            This method updates the messages related to site creation, updating, and deletion in the Cisco Catalyst Center.
            It evaluates the status of created sites, updated sites, and sites that are no longer needed for update to
            determine the appropriate message to be set. The messages are then stored in the 'msg' attribute of the object.
        """
        if self.created_site_list and self.updated_site_list:
            self.result['changed'] = True
            if self.update_not_needed_sites:
                msg = """Site(s) '{0}' created successfully as well as Site(s) '{1}' updated successully and the some site(s)
                        '{2}' needs no update in Cisco Catalyst Center"""
                self.msg = msg.format(str(self.created_site_list), str(
                    self.updated_site_list), str(self.update_not_needed_sites))
            else:
                self.msg = """Site(s) '{0}' created successfully in Cisco Catalyst Center as well as Site(s) '{1}' updated successully in
                        Cisco Catalyst Center""".format(str(self.created_site_list), str(self.updated_site_list))
        elif self.created_site_list:
            self.result['changed'] = True
            if self.update_not_needed_sites:
                self.msg = """Site(s) '{0}' created successfully and some site(s) '{1}' not needs any update in Cisco Catalyst
                                Center.""".format(str(self.created_site_list), str(self.update_not_needed_sites))
            else:
                self.msg = "Site(s) '{0}' created successfully in Cisco Catalyst Center.".format(
                    str(self.created_site_list))
        elif self.updated_site_list:
            self.result['changed'] = True
            if self.update_not_needed_sites:
                self.msg = """Site(s) '{0}' updated successfully and some site(s) '{1}' not needs any update in Cisco Catalyst
                                Center.""".format(str(self.updated_site_list), str(self.update_not_needed_sites))
            else:
                self.msg = "Site(s) '{0}' updated successfully in Cisco Catalyst Center.".format(
                    str(self.updated_site_list))
        elif self.update_not_needed_sites:
            self.result['changed'] = False
            self.msg = "Site(s) '{0}' not needs any update in Cisco Catalyst Center.".format(
                str(self.update_not_needed_sites))
        elif self.deleted_site_list and self.site_absent_list:
            self.result['changed'] = True
            self.msg = """Given site(s) '{0}' deleted successfully from Cisco Catalyst Center and unable to deleted some site(s) '{1}' as they
                    are not found in Cisco Catalyst Center.""".format(str(self.deleted_site_list), str(self.site_absent_list))
        elif self.deleted_site_list:
            self.result['changed'] = True
            self.msg = "Given site(s) '{0}' deleted successfully from Cisco Catalyst Center".format(
                str(self.deleted_site_list))
        else:
            self.result['changed'] = False
            self.msg = "Unable to delete site(s) '{0}' as it's not found in Cisco Catalyst Center.".format(
                str(self.site_absent_list))

        self.status = "success"
        self.result['response'] = self.msg
        self.result['msg'] = self.msg

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
                    'dnac_log_level': {'type': 'str', 'default': 'WARNING'},
                    "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
                    "dnac_log_append": {"type": 'bool', "default": True},
                    'dnac_log': {'type': 'bool', 'default': False},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'config_verify': {'type': 'bool', "default": False},
                    'dnac_api_task_timeout': {'type': 'int', "default": 1200},
                    'dnac_task_poll_interval': {'type': 'int', "default": 2},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged', 'deleted']}
                    }

    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    ccc_site = Site(module)
    state = ccc_site.params.get("state")

    if ccc_site.compare_dnac_versions(ccc_site.get_ccc_version(), "2.3.5.3") < 0:
        ccc_site.msg = (
            "The specified version '{0}' does not support the site workflow feature. Supported versions start from '2.3.5.3' onwards. "
            "Version '2.3.5.3' introduces APIs for creating, updating, and deleting sites. "
            "Version '2.3.7.6' expands support to include APIs for bulk site creating, updating, and deleting sites.".format(
                ccc_site.get_ccc_version())
        )

        ccc_site.status = "failed"
        ccc_site.check_return_status()

    if state not in ccc_site.supported_states:
        ccc_site.status = "invalid"
        ccc_site.msg = "State {0} is invalid".format(state)
        ccc_site.check_return_status()

    ccc_site.validate_input().check_return_status()
    config_verify = ccc_site.params.get("config_verify")

    for config in ccc_site.validated_config:
        ccc_site.reset_values()
        ccc_site.get_want(config).check_return_status()
        ccc_site.get_have(config).check_return_status()
        ccc_site.upload_floor_image(config)
        ccc_site.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_site.verify_diff_state_apply[state](
                config).check_return_status()

    ccc_site.update_site_messages().check_return_status()

    module.exit_json(**ccc_site.result)


if __name__ == '__main__':
    main()
