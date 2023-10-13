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
options:
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
                description: Parent name of the area to be created.
                type: str
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
          floor:
            description: Site Create's floor.
            type: dict
            suboptions:
              height:
                description: Height of the floor (eg 15).
                type: int
              length:
                description: Length of the floor (eg 100).
                type: int
              name:
                description: Name of the floor (eg floor-1).
                type: str
              parentName:
                description: Parent name of the floor to be created.
                type: str
              rfModel:
                description: Type of floor. Allowed values are 'Cubes And Walled Offices',
                  'Drywall Office Only', 'Indoor High Ceiling', 'Outdoor Open Space'.
                type: str
              width:
                description: Width of the floor (eg 100).
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
- name: Create a new building site
  cisco.dnac.site_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: "{{dnac_log}}"
    config:
    - site:
        building:
          address: string
          latitude: 0
          longitude: 0
          name: string
          parentName: string
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
    dnac_compare_equality,
)

floor_plan = {
    '57057': 'CUBES AND WALLED OFFICES',
    '57058': 'DRYWELL OFFICE ONLY',
    '41541500': 'FREE SPACE',
    '57060': 'INDOOR HIGH CEILING',
    '57059': 'OUTDOOR OPEN SPACE'
}


class DnacSite(DnacBase):
    """Class containing member attributes for site intent module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]

    def validate_input(self):
        """Validate the fields provided in the playbook"""

        if not self.config:
            self.msg = "config not available in playbook for validattion"
            self.status = "success"
            return self

        temp_spec = dict(
            type=dict(required=False, type='str'),
            site=dict(required=True, type='dict'),
        )

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
        """Get the current site info"""

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
                    address=location.get("attributes").get("address", ""),
                    latitude=location.get("attributes").get("latitude"),
                    longitude=location.get("attributes").get("longitude"),
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
                    rfModel=floor_plan.get(rf_model),
                    width=map_geometry.get("attributes").get("width"),
                    length=map_geometry.get("attributes").get("length"),
                    height=map_geometry.get("attributes").get("height")
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
        """Check if the site exists"""

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
            log("The input site is not valid or site is not present.")

        if response:
            log(str(response))

            response = response.get("response")
            current_site = self.get_current_site(response)
            site_exists = True

        log(str(self.validated_config))

        return (site_exists, current_site)

    def get_site_params(self, params):
        """Store the site related parameters"""

        site = params.get("site")
        typeinfo = params.get("type")

        if typeinfo == "floor":
            site["floor"]["rfModel"] = site.get("floor").get("rfModel").upper()

        site_params = dict(
            type=typeinfo,
            site=site,
        )

        return site_params

    def get_site_name(self, site):
        """Get and Return the site name"""

        site_type = site.get("type")
        parent_name = site.get("site").get(site_type).get("parentName")
        name = site.get("site").get(site_type).get("name")
        site_name = '/'.join([parent_name, name])

        log(site_name)

        return site_name

    def site_requires_update(self):
        """Check if the site requires updates"""

        requested_site = self.want.get("site_params")
        current_site = self.have.get("current_site")

        log("Current Site: " + str(current_site))
        log("Requested Site: " + str(requested_site))

        obj_params = [
            ("type", "type"),
            ("site", "site")
        ]

        return any(not dnac_compare_equality(current_site.get(dnac_param),
                                             requested_site.get(ansible_param))
                   for (dnac_param, ansible_param) in obj_params)

    def get_execution_details(self, execid):
        response = None
        response = self.dnac._exec(
            family="task",
            function='get_business_api_execution_details',
            params={"execution_id": execid}
        )

        log(str(response))

        if response and isinstance(response, dict):
            return response

    def get_have(self, config):
        """Get the site details from DNAC"""

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
        """Get all the site related information from playbook
        that is needed to be created in DNAC"""

        want = {}

        want = dict(
            site_params=self.get_site_params(config),
            site_name=self.get_site_name(config),
        )

        self.want = want

        return self

    def get_diff_merged(self, config):
        """Update/Create site info in DNAC with fields provided in DNAC"""

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
                self.result['msg'] = "Site does not need update"
                self.module.exit_json(**self.result)

        else:
            # Creating New Site
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
                    log("Site Updated Successfully")
                    self.result['msg'] = "Site Updated Successfully"
                    self.result['response'].update({"siteId": self.have.get("site_id")})

                else:
                    # Get the site id of the newly created site.
                    (site_exists, current_site) = self.site_exists()

                    if site_exists:
                        log("Site Created Successfully")
                        log("Current site:" + str(current_site))
                        self.result['msg'] = "Site Created Successfully"
                        self.result['response'].update({"siteId": current_site.get('site_id')})

        return self

    def get_diff_deleted(self, config):
        """Call DNAC API to delete sites with provided inputs"""

        site_exists = self.have.get("site_exists")

        if site_exists:
            response = self.dnac._exec(
                family="sites",
                function="delete_site",
                params={"site_id": self.have.get("site_id")},
            )

            if response and isinstance(response, dict):
                executionid = response.get("executionId")
                while True:
                    execution_details = self.get_execution_details(executionid)
                    if execution_details.get("status") == "SUCCESS":
                        self.result['changed'] = True
                        self.result['response'] = execution_details
                        self.result['response'].update({"siteId": self.have.get("site_id")})
                        self.result['msg'] = "Site deleted successfully"
                        break

                    elif execution_details.get("bapiError"):
                        self.module.fail_json(msg=execution_details.get("bapiError"),
                                              response=execution_details)
                        break

        else:
            self.module.fail_json(msg="Site Not Found", response=[])

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
                    'dnac_log': {'type': 'bool', 'default': False},
                    'validate_response_schema': {'type': 'bool', 'default': True},
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

    for config in dnac_site.validated_config:
        dnac_site.reset_values()
        dnac_site.get_want(config).check_return_status()
        dnac_site.get_have(config).check_return_status()
        dnac_site.get_diff_state_apply[state](config).check_return_status()

    module.exit_json(**dnac_site.result)


if __name__ == '__main__':
    main()
