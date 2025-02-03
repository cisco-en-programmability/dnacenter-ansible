#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform operations on create and delete network profile details 
in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ["A Mohamed Rafeek, Madhan Sankaranarayanan"]

DOCUMENTATION = r"""
---
module: network_profile_workflow_manager
short_description: Resource module for managing network profile in Cisco Catalyst Center
description: This module allows to create/delete the network profile in Cisco Catalyst Center. 
    - It supports creating and deleting switch/wireless/assurance profile. 
    - This module interacts with Cisco Catalyst Center's to create profile name, SSID details,
      additinal interface details destination port and protcol.
    version_added: '6.27.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - A Mohamed Rafeek (@mabdulk2)
  - Madhan Sankaranarayanan (@madhansansel)
  - Sonali Deepthi (@skesali)

options:
  config_verify:
    description: Set to `True` to enable configuration verification on Cisco DNA Center after applying the playbook config. This will ensure that the system validates the configuration state after the change is applied.
    type: bool
    default: False
  state:
    description: Specifies the desired state for the configuration. If `merged`, the module will create or update the configuration, adding new settings or modifying existing ones. If `deleted`, it will remove the specified settings.
    type: str
    choices: ["merged", "deleted"]
    default: merged
 config:
    description: A list containing the details for network profile creation. 
    type: list
    elements: dict
    required: true
    suboptions:
      switch_profile:
        description: Configures and creates a network profile for switching.
        type: list
        elements: dict
        suboptions:
          profile_name:
            description: Name of the switch profile to be created.
            type: str
            required: true
          site_name:
            description: |
              Site name contains assign the site to profile. For example, ["Global/USA/New York/BLDNYC"].
            type: list
            elements: str
            required: false
          onboarding_template:
            description: Name of the onboarding template to assign with the profile.
            type: str
            required: false
          day_n_template:
            description: Name of the Day-N template to assign with the profile.
            type: str
            required: false

requirements:
- dnacentersdk >= 2.9.3
- python >= 3.9
notes:
 - SDK Method used are

    site_design.assign_sites,

 - Paths used are
    GET dna/intent/api/v1/wirelessProfiles
    POST dna/intent/api/v1/wirelessProfiles/{
    GET /dna/intent/api/v1/app-policy-intent
    DELETE /dna/intent/api/v1/app-policy-intent
"""

EXAMPLES = r"""
---
- hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: no
  connection: local
  tasks:
    - name: Create network profile for switch
      cisco.dnac.path_trace_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_port: "{{ dnac_port }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_version: "{{ dnac_version }}"
        dnac_log_level: DEBUG
        dnac_log: true
        state: deleted
        config_verify: true
        config: 
          - switch_profile:
              profile_name: "Test_switch"
              onboarding_template: [test_template]
              day_n_template: [test_template1]
              site_name: ["global/chennai/LTTS/FLOOR1", "global/chennai/LTTS/FLOOR2"]

"""

RETURN = r"""

#Case 1: Successful creation/updatation of wireless profile
Response: Create
{
    "msg": "Switch Profile created/updated successfully for '[{'profile_name': 'APISample3', 'status': 'Network Profile [ff0003b4-adab-4de4-af0e-0cf07d6df07f] Successfully created'}]'.",
    "response": [
        {
            "profile_name": "APISample3",
            "status": "Network Profile [ff0003b4-adab-4de4-af0e-0cf07d6df07f] created Successfully"
        }
    ],
    "status": "success"
}

#Case 2: Successfully deletion of wireless profile
Response: Delete
{
    "msg": "Switch Profile deleted successfully for '[{'profile_name': 'APISample3', 'status': 'Network Profile [ff0003b4-adab-4de4-af0e-0cf07d6df07f] Successfully Deleted'}]'.",
    "response": [
        {
            "profile_name": "APISample3",
            "status": "Network Profile [ff0003b4-adab-4de4-af0e-0cf07d6df07f] Successfully Deleted"
        }
    ],
    "status": "success"
}
"""

import requests
import re
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    validate_str,
)

class NetworkSwitchProfile(DnacBase):
    """Class containing member attributes for network profile workflow manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]
        self.switch, self.assurance = [], []
        self.switch_delete, self.assurance_delete = [], []
        self.common_delete = []
        self.not_processed = []

        self.keymap = dict(
            sites = "sites"
        )

        host_name = self.params["dnac_host"]
        self.dnac_url = "https://{0}".format(str(host_name))
        self.token_str = self.dnac.api.access_token
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Auth-Token": str(self.token_str)
        }

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.

        Parameters:
            self: The instance of the class containing the 'config' attribute to be validated.

        Returns:
            The method updates these attributes of the instance:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation ('success' or 'failed').
                - self.validated_config: If successful, a validated version of the 'config' parameter.
        """
        temp_spec = {
            'switch_profile': {
                'type': 'list',
                'elements': 'dict',
                'profile_name': {'type': 'str', 'required': True},
                'site_name': {'type': 'list', 'elements': 'str', 'required': False},
                'onboarding_template': {'type': 'list', 'elements': 'str', 'required': False},
                'day_n_template': {'type': 'list', 'elements': 'str', 'required': False}
            }
        }

        if not self.config:
            self.msg = "The playbook configuration is empty or missing."
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        # Validate configuration against the specification
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            self.msg = "The playbook contains invalid parameters: {0}".format(
                invalid_params)
            self.result['response'] = self.msg
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validate_input': {0}".format(
            str(valid_temp))
        self.log(self.msg, "INFO")

        return self

    def input_data_validation(self, config):
        """
        Additional validation to check if the provided input switch profile is correct
        and as per the UI Cisco Catalyst Center.

        Parameters:
            self (object): An instance of a class for interacting with Cisco Catalyst Center.
            config (dict): Dictionary containing the switch profile details.

        Returns:
            list: List of invalid profile data with details.

        Description:
            Iterates through available profile details and Returns the list of invalid
            data for further action or validation.
        """
        errormsg = []

        switch_profile = config.get("switch_profile")
        if switch_profile and len(switch_profile) > 0:
            for each_profile in switch_profile:
                profile_name = each_profile.get("profile_name")
                if profile_name:
                    param_spec = dict(type="str", length_max=200)
                    validate_str(profile_name, param_spec, "profile_name", errormsg)
                else:
                    errormsg.append("profile_name: Profile Name is missing in playbook.")

                if self.payload.get("state") == "deleted":
                    continue

                site_name = each_profile.get("site_name")
                if site_name and len(site_name) > 0:
                    for sites in site_name:
                        param_spec = dict(type="str", length_max=200)
                        validate_str(sites, param_spec, "site_name", errormsg)
                else:
                    errormsg.append("site_name: Site Name(s) are missing in playbook.")

                onboarding_template_name = each_profile.get("onboarding_template")
                if onboarding_template_name and len(onboarding_template_name) > 0:
                    for template in onboarding_template_name:
                        param_spec = dict(type="str", length_max=200)
                        validate_str(template, param_spec, "onboarding_template", errormsg)

                day_n_template_name = each_profile.get("day_n_template")
                if day_n_template_name and len(day_n_template_name) > 0:
                    for template in day_n_template_name:
                        param_spec = dict(type="str", length_max=200)
                        validate_str(template, param_spec, "day_n_template", errormsg)

        if len(errormsg) > 0:
            self.msg = "Invalid parameters in playbook config: '{0}' ".format(errormsg)
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

        self.msg = "Successfully validated config params: {0}".format(str(config))
        self.log(self.msg, "INFO")
        return self

    def get_want(self, config):
        """
        Retrieve network profile or delete profile from playbook configuration.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing network switch profile details.
        Returns:
            self: The current instance of the class with updated 'want' attributes.
        Raises:
            AnsibleFailJson: If an incorrect import type is specified.
        Description:
            This function parses the playbook configuration to extract information related to network
            profile. It stores these details in the 'want' dictionary
            for later use in the Ansible module.
        """
        want = {}
        if config:
            want["switch_profile"] = config.get("switch_profile")
        self.want = want
        self.log("Desired State (want): {0}".format(self.pprint(self.want)), "INFO")

        return self

    def get_have(self, config):
        """
        Get required details for the given profile config from Cisco Catalyst Center

        Parameters:
            config (dict) - Playbook details containing network switch profile

        Returns:
            self - The current object with templates and site details
            information collection for profile create and update.
        """
        if config:
            switch_list = config.get("switch_profile")
            if switch_list:
                self.have["switch_profile"] = []

                all_profile = self.get_network_profile("Switching", 1, 500)
                if all_profile:
                    if len(all_profile) == 500:
                        offset = 1
                        while True:
                            offset += 1
                            all_profile.extend(self.get_network_profile(
                                "Switching", offset, 500))
                    self.have["switch_profile_list"] = all_profile

                for each_profile in switch_list:
                    profile_info = {}
                    profile_info["profile_name"] = each_profile.get("profile_name")
                    self.check_site_template(each_profile, profile_info)

                    if self.value_exists(self.have["switch_profile_list"],
                                         "name", profile_info["profile_name"]):

                        index_no = next((indexno for indexno, data in enumerate(
                            self.have["switch_profile_list"])
                            if data.get("name") == each_profile.get("profile_name")), -1)
                        profile_id = self.have["switch_profile_list"][index_no]["id"]
                        profile_info["profile_id"] = profile_id

                        self.log("Getting templates for the profile: {0}".format(
                            profile_info["profile_name"]), "INFO")
                        template_detail = self.get_templates_for_profile(profile_id)
                        profile_info["previous_templates"] = template_detail
                        temp_status, unmatch = self.compare_config_with_sites_templates(
                            each_profile, template_detail, "template")
                        profile_info["template_compare_stat"] = True
                        profile_info["template_compare_unmatched"] = unmatch
                        if not temp_status:
                            profile_info["template_compare_stat"] = False
                            profile_info["template_compare_unmatched"] = unmatch

                        self.log("Getting site list for the profile: {0}".format(
                            profile_info["profile_name"]), "INFO")
                        site_list = self.get_site_lists_for_profile(profile_id)
                        profile_info["previous_sites"] = site_list
                        site_status, unmatch = self.compare_config_with_sites_templates(
                            profile_info["site_response"], site_list, "sites")
                        profile_info["site_compare_stat"] = True
                        profile_info["site_compare_unmatched"] = unmatch
                        if not site_status:
                            profile_info["site_compare_stat"] = False
                            profile_info["site_compare_unmatched"] = unmatch

                        if temp_status and site_status:
                            profile_info["profile_compare_stat"] = True
                            profile_info["profile_compare_unmatched"] = None
                    else:
                        profile_info["profile_compare_stat"] = False
                        profile_info["profile_compare_unmatched"] = each_profile

                    self.have["switch_profile"].append(profile_info)

                if len(self.have["switch_profile"]) < 1:
                    self.msg = "No data found for switching profile for the " +\
                        "given config: {0}".format(config)

        self.log("Current State (have): {0}".format(self.pprint(self.have)), "INFO")
        self.msg = "Successfully retrieved the details from the system"
        self.status = "success"
        return self

    def compare_config_with_sites_templates(self, each_config, data_list, config_type):
        """
        Function used to compare each input switch config templates data with
        existing assign profile template
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            each_config (dict): A dict containing profile name, template name to compare existing
                                template assigned profile template.
            data_list (list): List of dict contains template id and name assigned to the profile.

        Returns:
            status : A bool contains matches true or false.
            unmatch: A list of unmatched template names

        Description:
            This function is used to compare the template names and return status and unmatched
            template names as response.
        """
        if config_type == "template":
            un_match_template = []
            matched_template = []
            for template_type in ["onboarding_template", "day_n_template"]:
                tempaltes = each_config.get(template_type)
                if tempaltes:
                    for template in tempaltes:
                        if not self.value_exists(data_list, "name", template):
                            un_match_template.append(template)
                        else:
                            matched_template.append(template)

            if len(un_match_template) > 0:
                return False, un_match_template
            else:
                if len(matched_template) == len(data_list):
                    return True, None
                else:
                    return False, matched_template

        if config_type == "sites":
            un_match_site_ids = []
            matched_site_ids = []
            if each_config:
                for site in each_config:
                    if not self.value_exists(data_list, "id", site["site_id"]):
                        un_match_site_ids.append(site["site_name"])
                    else:
                        matched_site_ids.append(site["site_name"])

            if len(un_match_site_ids) > 0:
                return False, un_match_site_ids
            else:
                if len(matched_site_ids) == len(data_list):
                    return True, None
                else:
                    return False, matched_site_ids

    def get_site_lists_for_profile(self, profile_id):
        """
        Get the Site ID list for the specific profile id
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            profile_id (str): A string containing profile id to fetch Sites assigned to
                the profile.

        Returns:
            list: A list of dict contains site id was assigned for the profile.

        Description:
            This function is used to get site id list for the specific profile id
        """
        self.log("Profile id for the sites: {0}".format(profile_id), "INFO")
        param = {
            "profile_id": profile_id
        }
        func_name = "retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1"
        try:
            response = self.dnac._exec(
                family="site_design",
                function=func_name,
                params=param
            )
            self.log("Response from get site lists for profile API: {0}".
                     format(self.pprint(response)), "DEBUG")
            if response and isinstance(response, dict):
                return response.get("response")
            else:
                return None

        except Exception as e:
            self.msg = 'An error occurred during retrieve sites for profile: {0}'.format(str(e))
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

    def create_switch_profile(self, each_config, profile_id=None):
        """
        This function used to create or update the switch profile based on the given playbook
        configuration based on profile ID create/update the profile.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (list of dict) - Playbook details containing switch profile information.
            profile_id (str): A string containing profile id to update the switch profile.
        Returns:
            dict: A dict contains Task details of the profile assigned status.
            self - The current object with message and created/updated response information.

        Description:
            This function is used to Create profile or update the Profile template and retrun 
            response as a task details.
        """
        target_url = f"{self.dnac_url}/api/v1/siteprofile"
        response = {}
        for each_have in self.have["switch_profile"]:
            if each_have.get("profile_name") == each_config["profile_name"]:
                ob_template_ids, dn_template_ids = [], []
                profile_attributes = []

                if each_have.get("onboarding_template"):
                    for template in each_have.get("onboarding_template"):
                        ob_template_ids.append(dict(
                        key="template.id",
                        value=template.get("template_id")
                        ))

                if each_have.get("day_n_template"):
                    for template in each_have.get("day_n_template"):
                        dn_template_ids.append(dict(
                        key="template.id",
                        value=template.get("template_id")
                        ))

                if len(ob_template_ids) > 0:
                    profile_attributes.append(dict(
                        key="day0.templates",
                        attribs=ob_template_ids
                    ))
                if len(dn_template_ids) > 0:
                    profile_attributes.append(dict(
                        key="cli.templates",
                        attribs=dn_template_ids
                    ))

                payload = {
                        "name": each_config["profile_name"],
                        "namespace": "switching",
                        "profileAttributes": profile_attributes
                    }

                self.log("Creating switch profile with parameters: {0}".format(
                            self.pprint(payload)), "INFO")
                try:
                    response = None
                    if profile_id:
                        target_url = target_url + "/" + profile_id
                        response = requests.put(
                        target_url, headers=self.headers, json=payload,
                        verify=False, timeout=10
                    )
                    else:
                        response = requests.post(
                            target_url, headers=self.headers, json=payload,
                            verify=False, timeout=10
                        )

                    if response.status_code in [200, 202]:
                        response_json = response.json()
                        self.log("Switch profile created successfully: {0}".format(
                            self.pprint(response_json)), "INFO")
                        task_id = response_json.get("response", {}).get("taskId")
                        return self.execute_process_task_data("profile", target_url,
                                                       payload, task_id)
                    else:
                        self.log("Failed to create switch profile: {0} - {1}".
                                format(response.status_code, str(response.text)), "ERROR")

                except Exception as e:
                    self.msg = 'An error occurred during create Switch profile: {0}'.format(
                        str(e))
                    self.log(self.msg, "ERROR")
                    self.fail_and_exit(self.msg)
        return None

    def process_delete_profiles(self, profile_list, type_list_name):
        """
        This function used unassign the sites and delete the swith profile based on the delete
        state .
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            profile_list (list of dict): Profile list containing input playbook switch 
                                         profile information.
            type_list_name (str): A string key top identify the profile from get have.

        Returns:
            self - The current object with message and delete response information.

        Description:
            This function is used to delete the switch profile and return the object.
        """
        deleted_count = 0
        for each_profile in profile_list:
            if not self.value_exists(self.have[type_list_name], "name",
                                        each_profile["profile_name"]):
                deleted_count += 1

        if deleted_count == len(profile_list):
            self.msg = "No changes required, profile(s) are already deleted"
            self.log(self.msg, "INFO")
            self.set_operation_result("success", False, self.msg, "INFO").check_return_status()
            return self

        for each_profile in profile_list:
            have_list = self.have[type_list_name]
            if have_list and len(have_list) > 0:
                for each_have in have_list:
                    if each_have.get("name") == each_profile["profile_name"]:
                        profile_id = each_have.get("id")
                        sites = each_profile.get("site_name")
                        if sites and len(sites) > 0:
                            unassign_site = []
                            for each_site in sites:
                                site_exist, site_id = self.get_site_id(each_site)
                                unassign_response = self.unassign_site_to_network_profile(
                                    profile_id, site_id)
                                unassign_site.append(unassign_response)

                            if len(unassign_site) == len(sites):
                                self.log("Sites unassigned successfully {0}".format(
                                    sites), "INFO")

                        task_details = self.delete_network_profiles(profile_id)
                        if task_details:
                            if self.result['changed']:
                                profile_response = dict(profile_name=each_profile["profile_name"],
                                                        status=task_details["progress"])
                                self.common_delete.append(profile_response)
                            else:
                                profile_response = dict(profile_name=each_profile["profile_name"],
                                                        status=task_details)
                                self.not_processed.append(profile_response)
                        else:
                            self.not_processed.append(each_profile)
                            self.msg = self.msg + "Unable to delete profile: '{0}'.".format(
                                str(self.not_processed))

        if len(self.common_delete) > 0:
            self.msg = "Network Profile deleted successfully for '{0}'.".format(
                str(self.common_delete))
            self.changed = True
            self.status = "success"

        if len(self.not_processed) > 0:
            self.msg = "Unable to delete the profile '{0}'.".format(
                self.not_processed)
        return self

    def get_diff_merged(self, config):
        """
        Update or create network switch profile in Cisco Catalyst Center based on the
        playbook details

        Parameters:
            config (list of dict) - Playbook details containing switch profile information.

        Returns:
            self - The current object with message and created/updated response information.
        """
        self.msg = ""
        self.changed = False
        self.status = "failed"

        switch_profile = config.get("switch_profile")
        if switch_profile is not None and len(switch_profile) > 0:
            profile_no = 0
            match_count = 0
            for each_profile in switch_profile:
                unmatch_stat = self.have["switch_profile"][profile_no].get("profile_compare_stat")
                if any(profile["name"] == each_profile["profile_name"]
                       for profile in self.have["switch_profile_list"]) and unmatch_stat:
                    match_count += 1

            if match_count == len(switch_profile):
                self.msg = "No changes required, Switch profile(s) are already created"
                self.log(self.msg, "INFO")
                self.set_operation_result("success", False, self.msg, "INFO").check_return_status()
                return self

            profile_no = 0
            for each_profile in switch_profile:
                unmatch_stat = self.have["switch_profile"][profile_no].get("profile_compare_stat")
                unmatch_template_stat = self.have["switch_profile"][profile_no].get("template_compare_stat")
                unmatch_site_stat = self.have["switch_profile"][profile_no].get("site_compare_stat")
                task_details = {}
                # Below if condition for creating the switch profile
                if not unmatch_stat and not unmatch_template_stat and not unmatch_site_stat:
                    task_details = self.create_switch_profile(each_profile)

                    if task_details:
                        profile_response = dict(profile_name=each_profile["profile_name"],
                                                status=task_details["progress"])
                        uuid_pattern = \
                            r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b"
                        match = re.search(uuid_pattern, task_details["progress"])
                        if match:
                            profile_id = match.group()
                            have_site = self.have["switch_profile"][profile_no].get("site_response")
                            site_id_list = []

                            if have_site and isinstance(have_site, list) and len(have_site) > 0:
                                for each_site in have_site:
                                    if each_site["site_exist"]:
                                        site_id_list.append(each_site["site_id"])

                            if len(site_id_list) > 0:
                                assign_response = []
                                for site in site_id_list:
                                    assign_response.append(self.assign_site_to_network_profile(
                                        profile_id, site))

                        profile_no += 1
                        self.switch.append(profile_response)
                    else:
                        self.not_processed.append(config)
                        self.msg = self.msg + "Unable to create profile: '{0}'.".format(
                            str(self.not_processed))
                # Below else part for updating the switch profile
                else:
                    unassign_site_task, assign_site_task, update_temp_status = [], [], []
                    if not unmatch_template_stat:
                        for each_have in self.have["switch_profile"]:
                            if each_have.get("profile_name") == each_profile["profile_name"]:
                                task_details = self.create_switch_profile(each_profile,
                                    each_have.get("profile_id"))

                                if task_details:
                                    profile_response = dict(
                                        profile_name=each_profile["profile_name"],
                                        status=task_details["progress"])
                                    update_temp_status.append(profile_response)
                                else:
                                    self.msg = self.msg +\
                                        "Unable to update profile with template: '{0}'.".format(
                                            str(each_profile["profile_name"]))

                    if not unmatch_site_stat:
                        for each_have in self.have["switch_profile"]:
                            if each_have.get("profile_name") == each_profile["profile_name"]:

                                sites = each_have.get("previous_sites")
                                if sites and len(sites) > 0:
                                    for each_site in sites:
                                        unassign_response = self.unassign_site_to_network_profile(
                                            each_have.get("profile_id"), each_site.get("id"))
                                        unassign_site_task.append(unassign_response)

                                    if len(unassign_site_task) == len(sites):
                                        self.log("Sites unassigned successfully {0}".format(
                                            sites), "INFO")

                                have_site = each_have.get("site_response")
                                site_id_list = []
                                if have_site and isinstance(have_site, list) and len(have_site) > 0:
                                    for each_site in have_site:
                                        if each_site["site_exist"]:
                                            site_id_list.append(each_site["site_id"])

                                if len(site_id_list) > 0:
                                    for site in site_id_list:
                                        assign_site_task.append(self.assign_site_to_network_profile(
                                            each_have.get("profile_id"), site))

                    self.msg = "Network profile '" +\
                        each_profile["profile_name"] + "' updated successfully"
                    profile_response = dict(profile_name=each_profile["profile_name"],
                                            status= self.msg)
                    if len(update_temp_status) > 0 or len(unassign_site_task) > 0 or\
                        len(assign_site_task) > 0:
                        self.switch.append(profile_response)
                    else:
                        self.not_processed.append(config)

            if len(self.switch) > 0:
                self.msg = "Switch Profile created/updated successfully for '{0}'.".format(
                    str(self.switch))
                self.changed = True
                self.status = "success"

            if len(self.not_processed) > 0:
                self.msg = self.msg + "Unable to create Switch profile '{0}'.".format(
                    str(self.not_processed))

            self.log(self.msg, "INFO")
            self.set_operation_result(self.status, self.changed, self.msg, "INFO",
                                    self.switch).check_return_status()

        return self

    def verify_diff_merged(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is merged (Create/Update).

        Parameters:
            config (dict) - Playbook details containing network switch profile
                            releated information.

        Returns:
            self - The current object with message and response information.
        """
        self.msg = ""
        success_profile = []
        self.changed = False
        self.status = "failed"
        switch_profile = config.get("switch_profile")

        if switch_profile:
            for each_profile in switch_profile:
                if len(self.switch) > 0:
                    for each_created in self.switch:
                        if each_created.get("profile_name") == each_profile["profile_name"]:
                            success_profile.append(each_created["profile_name"])
                else:
                    self.msg = "No changes required, Switch profile(s) are already created and verified"
                    self.log(self.msg, "INFO")
                    self.set_operation_result("success", False, self.msg, "INFO").check_return_status()
                    return self

        if len(success_profile) > 0:
            self.msg = "Profile created/updated are verified successfully for '{0}'.".format(
                str(success_profile))
            self.changed = True
            self.status = "success"

        if len(self.not_processed) > 0:
            self.msg = self.msg + "\n Unable to create profile '{0}'.".format(
                str(self.not_processed))

        self.log(self.msg, "INFO")
        self.set_operation_result(self.status, self.changed, self.msg, "INFO",
                            self.switch).check_return_status()
        return self

    def get_diff_deleted(self, config):
        """
        Delete Network switch profile in Cisco Catalyst Center based on playbook details.

        Parameters:
            config (list of dict) - Playbook details

        Returns:
            self - The current object with profile deletion message and response information.
        """
        self.changed = False
        self.status = "failed"

        switch_profile = config.get("switch_profile")
        if switch_profile is not None and len(switch_profile) > 0:
            self.process_delete_profiles(switch_profile, "switch_profile_list")

        self.log(self.msg, "INFO")
        self.set_operation_result(self.status, self.changed, self.msg, "INFO",
                                  self.common_delete).check_return_status()
        return self

    def verify_diff_deleted(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is deleted (delete).

        Parameters:
            config (dict) - Playbook details containing Network profile switch information.

        Returns:
            self - The current object with message and response.
        """
        switch_profile = config.get("switch_profile")
        if switch_profile is not None:
            self.msg = ""
            success_profile = []
            self.changed = False
            self.status = "failed"
            self.get_have(config)

            for each_profile in switch_profile:
                if len(self.common_delete) < 1:
                    self.msg = "No changes required, profile(s) are already deleted"
                    self.log(self.msg, "INFO")
                    self.set_operation_result("success", False, self.msg, "INFO").check_return_status()
                    return self

                if not self.value_exists(self.have["switch_profile_list"],
                                         "name", each_profile["profile_name"]):
                    success_profile.append(each_profile["profile_name"])

        if len(success_profile) > 0:
            self.msg = "Switch profile(s) deleted and verified successfully for '{0}'.".format(
                str(success_profile))
            self.changed = True
            self.status = "success"

        if len(self.not_processed) > 0:
            self.msg = self.msg + "Unable to delete below Switch profile '{0}'.".format(
                    config)

        self.log(self.msg, "INFO")
        self.set_operation_result(self.status, self.changed, self.msg, "INFO",
                                  self.common_delete).check_return_status()
        return self


def main():
    """main entry point for module execution"""

    # Define the specification for module arguments
    element_spec = {
        "dnac_host": {"type": 'str', "required": True},
        "dnac_port": {"type": 'str', "default": '443'},
        "dnac_username": {"type": 'str', "default": 'admin', "aliases": ['user']},
        "dnac_password": {"type": 'str', "no_log": True},
        "dnac_verify": {"type": 'bool', "default": 'True'},
        "dnac_version": {"type": 'str', "default": '2.3.7.6'},
        "dnac_debug": {"type": 'bool', "default": False},
        "dnac_log": {"type": 'bool', "default": False},
        "dnac_log_level": {"type": 'str', "default": 'WARNING'},
        "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
        "dnac_log_append": {"type": 'bool', "default": True},
        "config_verify": {"type": 'bool', "default": False},
        "dnac_api_task_timeout": {"type": 'int', "default": 1200},
        "dnac_task_poll_interval": {"type": 'int', "default": 2},
        "config": {"type": 'list', "required": True, "elements": 'dict'},
        "state": {"default": 'merged', "choices": ['merged', 'deleted']},
        "validate_response_schema": {"type": 'bool', "default": True},
    }

    # Create an AnsibleModule object with argument specifications
    module = AnsibleModule(argument_spec=element_spec,
                            supports_check_mode=False)
    ccc_network_profile = NetworkSwitchProfile(module)
    state = ccc_network_profile.params.get("state")

    if ccc_network_profile.compare_dnac_versions(
        ccc_network_profile.get_ccc_version(), "2.3.7.6") < 0:
        ccc_network_profile.status = "failed"
        ccc_network_profile.msg = (
            "The specified version '{0}' does not support the network profile workflow feature."
            "Supported version(s) start from '2.3.7.6' onwards.".
            format(ccc_network_profile.get_ccc_version())
        )
        ccc_network_profile.log(ccc_network_profile.msg, "ERROR")
        ccc_network_profile.check_return_status()

    if state not in ccc_network_profile.supported_states:
        ccc_network_profile.status = "invalid"
        ccc_network_profile.msg = "State {0} is invalid".format(state)
        ccc_network_profile.check_return_status()

    ccc_network_profile.validate_input().check_return_status()
    config_verify = ccc_network_profile.params.get("config_verify")

    for config in ccc_network_profile.validated_config:
        ccc_network_profile.reset_values()
        ccc_network_profile.input_data_validation(config).check_return_status()
        ccc_network_profile.get_want(config).check_return_status()
        ccc_network_profile.get_have(config).check_return_status()
        ccc_network_profile.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_network_profile.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_network_profile.result)

if __name__ == "__main__":
    main()
