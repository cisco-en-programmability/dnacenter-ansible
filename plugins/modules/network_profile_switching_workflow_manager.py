#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to create, update, or delete network switch profiles
in Cisco Catalyst Center, and manage associated sites and CLI templates."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ["A Mohamed Rafeek, Madhan Sankaranarayanan"]

DOCUMENTATION = r"""
---
module: network_profile_switching_workflow_manager
short_description: Resource module for managing switch
  profiles in Cisco Catalyst Center
description: >
  This module allows the creation and deletion of network
  switch profiles in Cisco Catalyst Center. - Supports
  creating and deleting switch profiles. - Allows assignment
  of profiles to sites, onboarding templates, and Day-N
  templates.
version_added: '6.31.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - A Mohamed Rafeek (@mabdulk2)
  - Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: >
      Set to `True` to enable configuration verification
      on Cisco Catalyst Center after applying the playbook
      configuration. This ensures that the system validates
      the configuration state after the change is applied.
    type: bool
    default: false
  state:
    description: >
      Specifies the desired state for the configuration.
      If `merged`, the module will create or update
      the configuration, adding new settings or modifying
      existing ones. If `deleted`, it will remove the
      specified settings.
    type: str
    choices: ["merged", "deleted"]
    default: merged
  config:
    description: A list containing the details for network
      switch profile creation.
    type: list
    elements: dict
    required: true
    suboptions:
      profile_name:
        description: Name of the switch profile to be
          created.
        type: str
        required: true
      site_names:
        description: >
          Site names must be specified in the full site
          hierarchy format for example 'Global/Country/City/Building'.
        type: list
        elements: str
        required: false
      onboarding_templates:
        description: >
          List of onboarding template names assigned
          to the profile. Note: Onboarding templates
          are currently unavailable due to SDK/API constraints.
        type: list
        elements: str
        required: false
      day_n_templates:
        description: List of Day-N template names assigned
          to the profile.
        type: list
        elements: str
        required: false
requirements:
  - dnacentersdk >= 2.8.6
  - python >= 3.9
notes:
  - This module uses the following SDK methods site_design.retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1
    site_design.assign_sites site_design.retrieves_the_list_of_network_profiles_for_sites_v1
    site_design.assign_a_network_profile_for_sites_to_the_given_site_v1
    site_design.unassigns_a_network_profile_for_sites_from_multiple_sites_v1
    site_design.deletes_a_network_profile_for_sites_v1
    configuration_templates.gets_the_templates_available_v1
    network_settings.retrieve_cli_templates_attached_to_a_network_profile_v1
  - Paths used are
    GET /dna/intent/api/v1/networkProfilesForSites
    GET /dna/intent/api/v1/template-programmer/template
    GET /dna/intent/api/v1/networkProfilesForSites/{profileId}/templates
    POST /dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments
    POST /dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments/bulk
    POST /api/v1/siteprofile
"""

EXAMPLES = r"""
---
- hosts: dnac_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  connection: local
  tasks:
    - name: Create network profile for switch
      cisco.dnac.network_profile_switching_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: true
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: merged
        config:
          - profile_name: "Campus_Switching_Profile"
            day_n_templates:
              - "Campus_Switch_Config_Update"
            site_names:
              - "Global/Chennai"
              - "Global/Abc"
    - name: Update network profile for switch
      cisco.dnac.network_profile_switching_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: true
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: merged
        config:
          - profile_name: "Enterprise_Switching_Profile"
            day_n_templates:
              - "Periodic_Config_Audit"
            site_names:
              - "Global/India/Chennai/Main_Office"
              - "Global/India/Madurai/Branch_Office"
              - "Global/USA/San Francisco/Regional_HQ"
    - name: Delete switching profile for devices from
        specified sites
      cisco.dnac.network_profile_switching_workflow_manager:
        dnac_host: "{{ dnac_host }}"
        dnac_username: "{{ dnac_username }}"
        dnac_password: "{{ dnac_password }}"
        dnac_verify: "{{ dnac_verify }}"
        dnac_port: "{{ dnac_port }}"
        dnac_version: "{{ dnac_version }}"
        dnac_debug: "{{ dnac_debug }}"
        dnac_log: true
        dnac_log_level: DEBUG
        config_verify: true
        dnac_api_task_timeout: 1000
        dnac_task_poll_interval: 1
        state: deleted
        config:
          - profile_name: "Enterprise_Switching_Profile"
            site_names:
              - "Global/India/Chennai/Main_Office"
              - "Global/India/Madurai/Branch_Office"
              - "Global/USA/San Francisco/Regional_HQ"
"""

RETURN = r"""
#Case 1: Successful creation of Switch profile
response_create:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
        "msg": "Profile created/updated are verified successfully for '['Enterprise_Access_Switch']'.",
        "response": [
            {
                "profile_name": "Enterprise_Access_Switch",
                "status": "Network Profile [487bf1e8-b014-4cc7-9e33-1ea7c2805b4c] Successfully Created"
            }
        ],
        "status": "success"
    }
#Case 2: Successful updatation of Switch profile
response_update:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
        "msg": "Profile created/updated are verified successfully for '['Campus_Core_Switch_Profile']'.",
        "response": [
                {
                    "profile_name": "Campus_Core_Switch_Profile",
                    "status": "Network profile 'Campus_Core_Switch_Profile' updated successfully"
                }
            ],
        "status": "success"
    }
#Case 3: Successful deletion of Switch profile
response_delete:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
        "msg": "Switch Profile deleted successfully for '[{'profile_name': 'Branch_Site_Switching',",
        "response": [
            {
                "profile_name": "Branch_Site_Switching",
                "status": "Network Profile [ff0003b4-adab-4de4-af0e-0cf07d6df07f] Successfully Deleted"
            }],
        "status": "success"
    }
"""


try:
    import requests

    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
    requests = None
import re
import time
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    validate_list_of_dicts,
    validate_str,
)
from ansible_collections.cisco.dnac.plugins.module_utils.network_profiles import (
    NetworkProfileFunctions,
)


class NetworkSwitchProfile(NetworkProfileFunctions):
    """Class containing member attributes for network profile workflow manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]
        self.switch, self.assurance = [], []
        self.switch_delete, self.assurance_delete = [], []
        self.common_delete = []
        self.not_processed = []

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.

        Parameters:
            self: The instance of the class containing the 'config' attribute to be validated.

        Returns:
            The method updates these attributes of the instance:
                - msg: A message describing the validation result.
                - self.status: The status of the validation ('success' or 'failed').
                - self.validated_config: If successful, a validated version of the 'config' parameter.
        """
        temp_spec = {
            "profile_name": {"type": "str", "required": True},
            "site_names": {"type": "list", "elements": "str", "required": False},
            "onboarding_templates": {
                "type": "list",
                "elements": "str",
                "required": False,
            },
            "day_n_templates": {"type": "list", "elements": "str", "required": False},
        }

        if not self.config:
            msg = "The playbook configuration is empty or missing."
            self.set_operation_result("failed", False, msg, "ERROR")
            return self

        # Validate configuration against the specification
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)

        if invalid_params:
            msg = "The playbook contains invalid parameters: {0}".format(invalid_params)
            self.result["response"] = msg
            self.set_operation_result("failed", False, msg, "ERROR")
            return self

        self.validated_config = valid_temp
        msg = "Successfully validated playbook configuration parameters using 'validate_input': {0}".format(
            str(valid_temp)
        )
        self.log(msg, "INFO")

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
        self.log(
            "Validating input data from Playbook config: {0}".format(config), "INFO"
        )
        errormsg = []

        duplicate_profile = self.find_duplicate_value(config, "profile_name")
        if duplicate_profile:
            errormsg.append(
                "profile_name: Duplicate Profile Name(s) '{0}' found in playbook.".format(
                    duplicate_profile
                )
            )

        for each_profile in config:
            profile_name = each_profile.get("profile_name")
            if profile_name:
                param_spec = dict(type="str", length_max=255)
                validate_str(profile_name, param_spec, "profile_name", errormsg)
            else:
                errormsg.append("profile_name: Profile Name is missing in playbook.")

            site_names = each_profile.get("site_names")
            if site_names:
                for sites in site_names:
                    param_spec = dict(type="str", length_max=200)
                    validate_str(sites, param_spec, "site_names", errormsg)
                    duplicate_sites = list(
                        set([site for site in site_names if site_names.count(site) > 1])
                    )
                    if duplicate_sites:
                        errormsg.append(
                            "Duplicate site(s) '{0}' found in site_names".format(
                                duplicate_sites
                            )
                        )
                        break

            onboarding_template_name = each_profile.get("onboarding_templates")
            day_n_template_name = each_profile.get("day_n_templates")
            if onboarding_template_name:
                errormsg.append(
                    "onboarding_templates: Onboarding templates are currently unavailable due to SDK/API upgrade. "
                    "This feature will be available in an upcoming release"
                )
                for template in onboarding_template_name:
                    param_spec = dict(type="str", length_max=200)
                    validate_str(template, param_spec, "onboarding_templates", errormsg)
                    duplicate_template = list(
                        set(
                            [
                                item
                                for item in onboarding_template_name
                                if onboarding_template_name.count(item) > 1
                            ]
                        )
                    )
                    if duplicate_template:
                        errormsg.append(
                            "Duplicate template(s) '{0}' found in onboarding_templates".format(
                                duplicate_template
                            )
                        )
                        break

                    if day_n_template_name and template in day_n_template_name:
                        errormsg.append(
                            "Onboarding_templates: Duplicate template "
                            + "'{0}' found in day_n_templates".format(template)
                        )
                        break

            if day_n_template_name:
                duplicate_template = []
                for template in day_n_template_name:
                    param_spec = dict(type="str", length_max=200)
                    validate_str(template, param_spec, "day_n_templates", errormsg)
                    duplicate_template = list(
                        set(
                            [
                                item
                                for item in day_n_template_name
                                if day_n_template_name.count(item) > 1
                            ]
                        )
                    )
                if duplicate_template:
                    errormsg.append(
                        "Duplicate template(s) '{0}' found in day_n_template_name".format(
                            duplicate_template
                        )
                    )

        if errormsg:
            self.msg = "Invalid parameters in playbook config: '{0}' ".format(errormsg)
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

        msg = "Successfully validated config params: {0}".format(str(config))
        self.log(msg, "INFO")
        return self

    def get_want(self, config):
        """
        Retrieve network profile or delete profile from playbook configuration.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing network switch profile details.
        Returns:
            self: The current instance of the class with updated 'want' attributes.

        Description:
            This function parses the playbook configuration to extract information related to network
            profile. It stores these details in the 'want' dictionary
            for later use in the Ansible module.
        """
        self.log(
            "Validating input data and update to want for: {0}".format(config), "INFO"
        )

        self.input_data_validation(config).check_return_status()
        want = {}
        if config:
            want["switch_profile"] = config

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
        self.log(
            "Collecting template and swith profile related information for: {0}".format(
                config
            ),
            "INFO",
        )
        self.have["switch_profile"], self.have["switch_profile_list"] = [], []
        offset = 1
        limit = 500

        resync_retry_count = int(self.payload.get("dnac_api_task_timeout"))
        resync_retry_interval = int(self.payload.get("dnac_task_poll_interval"))
        while resync_retry_count > 0:
            profiles = self.get_network_profile("Switching", offset, limit)
            if not profiles:
                self.log(
                    "No data received from API (Offset={0}). Exiting pagination.".format(
                        offset
                    ),
                    "DEBUG",
                )
                break

            self.log(
                "Received {0} profile(s) from API (Offset={1}).".format(
                    len(profiles), offset
                ),
                "DEBUG",
            )
            self.have["switch_profile_list"].extend(profiles)

            if len(profiles) < limit:
                self.log(
                    "Received less than limit ({0}) results, assuming last page. Exiting pagination.".format(
                        limit
                    ),
                    "DEBUG",
                )
                break

            offset += limit  # Increment offset for pagination
            self.log(
                "Incrementing offset to {0} for next API request.".format(offset),
                "DEBUG",
            )

            self.log(
                "Pauses execution for {0} seconds.".format(resync_retry_interval),
                "INFO",
            )
            time.sleep(resync_retry_interval)
            resync_retry_count = resync_retry_count - resync_retry_interval

        if self.have["switch_profile_list"]:
            self.log(
                "Total {0} profile(s) retrieved for 'switch': {1}.".format(
                    len(self.have["switch_profile_list"]),
                    self.pprint(self.have["switch_profile_list"]),
                ),
                "DEBUG",
            )
        else:
            self.log("No existing switch profile(s) found.", "WARNING")

        for each_profile in config:
            profile_info = {"profile_name": each_profile.get("profile_name")}
            self.check_site_template(each_profile, profile_info)

            if self.value_exists(
                self.have["switch_profile_list"], "name", profile_info["profile_name"]
            ):

                index_no = next(
                    (
                        indexno
                        for indexno, data in enumerate(self.have["switch_profile_list"])
                        if data.get("name") == each_profile.get("profile_name")
                    ),
                    -1,
                )
                profile_id = self.have["switch_profile_list"][index_no]["id"]
                profile_info["profile_id"] = profile_id

                self.log(
                    "Getting templates for the profile: {0}".format(
                        profile_info["profile_name"]
                    ),
                    "INFO",
                )
                template_detail = self.get_templates_for_profile(profile_id)
                if template_detail:
                    profile_info["previous_templates"] = template_detail

                temp_status, unmatch = self.compare_config_with_sites_templates(
                    each_profile, template_detail, "template"
                )
                profile_info["template_compare_stat"] = True
                profile_info["template_compare_unmatched"] = None
                if not temp_status:
                    profile_info["template_compare_stat"] = False
                    profile_info["template_compare_unmatched"] = unmatch

                self.log(
                    "Getting site list for the profile: {0}".format(
                        profile_info["profile_name"]
                    ),
                    "INFO",
                )
                site_status = None
                site_list = self.get_site_lists_for_profile(
                    each_profile.get("profile_name"), profile_id
                )
                if site_list:
                    self.log(
                        "Received Site List: {0} for config: {1}.".format(
                            site_list, each_profile
                        ),
                        "INFO",
                    )
                    profile_info["previous_sites"] = site_list

                if site_list and profile_info.get("site_response"):
                    site_status, unmatch = self.compare_config_with_sites_templates(
                        profile_info["site_response"], site_list, "sites"
                    )
                    profile_info["site_compare_stat"] = True
                    profile_info["site_compare_unmatched"] = None
                    if not site_status:
                        profile_info["site_compare_stat"] = False
                        profile_info["site_compare_unmatched"] = unmatch

                if not site_list and not profile_info.get("site_response"):
                    profile_info["site_compare_stat"] = True
                    profile_info["site_compare_unmatched"] = None
                    site_status = True

                if temp_status and site_status:
                    profile_info["profile_compare_stat"] = True
                    profile_info["profile_compare_unmatched"] = None
                else:
                    profile_info["profile_compare_stat"] = False
                    profile_info["profile_compare_unmatched"] = each_profile

            self.have["switch_profile"].append(profile_info)

        if not self.have["switch_profile"]:
            msg = (
                "No data found for switching profile for the "
                + "given config: {0}".format(config)
            )
            self.log(msg, "DEBUG")

        self.log("Current State (have): {0}".format(self.pprint(self.have)), "INFO")
        self.msg = "Successfully retrieved the details from the system"
        return self

    def create_switch_profile(self, each_config, profile_id=None):
        """
        Create or update a switch profile based on the given configuration.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (list of dict) - Playbook details containing switch profile information.
            profile_id (str): A string containing profile id to update the switch profile.

        Returns:
            dict or None: Task details if the profile is created/updated, otherwise None.

        Description:
            This function is used to Create profile or update the Profile template and retrun
            response as a task details.

        Note: Once API and SDK are ready this function will be replaced
        """
        self.log("Starting switch profile creation/update process.", "INFO")
        host_name = self.params["dnac_host"]
        if not host_name:
            msg = "Cisco Catalyst Center host information is missing."
            self.log(msg, "ERROR")
            self.fail_and_exit(msg)

        # Direct API call as SDK is not available yet
        dnac_url = "https://{0}".format(str(host_name))

        token_str = self.dnac.api.access_token
        if not token_str:
            msg = "Failed to retrieve access token from Cisco Catalyst Center."
            self.log(msg, "ERROR")
            self.fail_and_exit(msg)

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Auth-Token": str(token_str),
        }
        target_url = str(dnac_url) + "/api/v1/siteprofile"
        response = None

        for existing_profile in self.have.get("switch_profile", []):
            if existing_profile.get("profile_name") == each_config["profile_name"]:

                profile_attributes = []
                payload = {
                    "name": each_config["profile_name"],
                    "namespace": "switching",
                    "profileAttributes": profile_attributes,
                }

                self.log(
                    "Creating switch profile with parameters: {0}".format(
                        self.pprint(payload)
                    ),
                    "INFO",
                )
                try:
                    response = None
                    if profile_id:
                        target_url = target_url + "/" + profile_id
                        self.log(
                            "Updating existing switch profile (Profile ID: {0}). Target URL: {1}".format(
                                profile_id, target_url
                            ),
                            "INFO",
                        )
                        response = requests.put(
                            target_url,
                            headers=headers,
                            json=payload,
                            verify=False,
                            timeout=10,
                        )
                    else:
                        self.log(
                            "Creating new switch profile. Target URL: {0}".format(
                                target_url
                            ),
                            "INFO",
                        )
                        response = requests.post(
                            target_url,
                            headers=headers,
                            json=payload,
                            verify=False,
                            timeout=10,
                        )

                    if response.status_code in [200, 202]:
                        response_json = response.json()
                        self.log(
                            "Switch profile created successfully: {0}".format(
                                self.pprint(response_json)
                            ),
                            "INFO",
                        )
                        task_id = response_json.get("response", {}).get("taskId")
                        return self.execute_process_task_data(
                            "profile", target_url, payload, task_id
                        )
                    else:
                        self.log(
                            "Failed to create switch profile: {0} - {1}".format(
                                response.status_code, str(response.text)
                            ),
                            "ERROR",
                        )

                except Exception as e:
                    msg = "Error on creating Network Profile: Unable to get the success response creating profile '{0}'. ".format(
                        each_config["profile_name"]
                    )
                    self.log(msg + str(e), "ERROR")
                    self.fail_and_exit(msg)

        self.log("No matching switch profile found. Skipping profile creation.", "INFO")
        return None

    def process_delete_profiles(self, profile_list, type_list_name):
        """
        Unassigns sites and deletes the switch profile if it exists in the delete state.

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
        self.log("Starting process to delete network profiles.", "INFO")
        deleted_count = 0
        for each_profile in profile_list:
            if not self.value_exists(
                self.have[type_list_name], "name", each_profile["profile_name"]
            ):
                self.log(
                    "Profile '{0}' not found. Skipping deletion.".format(
                        each_profile["profile_name"]
                    ),
                    "INFO",
                )
                deleted_count += 1

        if deleted_count == len(profile_list):
            self.msg = "No changes required, profile(s) are already deleted"
            self.log(self.msg, "INFO")
            self.set_operation_result(
                "success", False, self.msg, "INFO"
            ).check_return_status()
            return self

        for each_profile in profile_list:
            exist_profile_list = self.have[type_list_name]
            if exist_profile_list:
                for each_have in exist_profile_list:
                    if each_have.get("name") == each_profile["profile_name"]:
                        profile_id = each_have.get("id")
                        sites = each_profile.get("site_names")
                        unassign_site = []

                        if sites:
                            self.log(
                                "Unassigning sites {0} from profile '{1}'.".format(
                                    sites, each_profile["profile_name"]
                                ),
                                "INFO",
                            )

                            for each_site in sites:
                                site_exist, site_id = self.get_site_id(each_site)
                                unassign_response = (
                                    self.unassign_site_to_network_profile(
                                        each_profile["profile_name"],
                                        profile_id,
                                        each_site,
                                        site_id,
                                    )
                                )
                                unassign_site.append(unassign_response)

                            if len(unassign_site) == len(sites):
                                self.log(
                                    "Sites unassigned successfully {0}".format(sites),
                                    "INFO",
                                )
                            else:
                                self.log(
                                    "Some sites could not be unassigned for profile '{0}'.".format(
                                        each_profile["profile_name"]
                                    ),
                                    "WARNING",
                                )

                        self.log(
                            "Initiating deletion of profile '{0}'.".format(
                                each_profile["profile_name"]
                            ),
                            "INFO",
                        )
                        task_details = self.delete_network_profiles(
                            each_profile["profile_name"], profile_id
                        )
                        if task_details:
                            if self.result["changed"]:
                                profile_response = dict(
                                    profile_name=each_profile["profile_name"],
                                    status=task_details["progress"],
                                )
                                if unassign_site:
                                    profile_response["site_unassign_status"] = (
                                        "Site(s) '{0}' unassigned Successfully.".format(
                                            sites
                                        )
                                    )
                                self.common_delete.append(profile_response)
                                self.log(
                                    "Profile '{0}' deleted successfully.".format(
                                        each_profile["profile_name"]
                                    ),
                                    "INFO",
                                )
                            else:
                                profile_response = dict(
                                    profile_name=each_profile["profile_name"],
                                    status=task_details,
                                )
                                self.not_processed.append(profile_response)
                                self.log(
                                    "Profile '{0}' deletion not processed.".format(
                                        each_profile["profile_name"]
                                    ),
                                    "WARNING",
                                )
                        else:
                            self.not_processed.append(each_profile)
                            self.msg = (
                                self.msg
                                + "Unable to delete profile: '{0}'.".format(
                                    str(self.not_processed)
                                )
                            )
                            self.log(
                                "Unable to delete profile '{0}'.".format(
                                    each_profile["profile_name"]
                                ),
                                "ERROR",
                            )
                        break

        if self.common_delete:
            self.msg = "Network Profile deleted successfully for '{0}'.".format(
                str(self.common_delete)
            )

        if self.not_processed:
            self.msg = "Unable to delete the profile '{0}'.".format(self.not_processed)
            self.set_operation_result(
                "failed", False, self.msg, "ERROR", self.not_processed
            ).check_return_status()
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
        self.log(
            "Starting to create/update switch profile for: {0}".format(config), "INFO"
        )

        profile_no = 0
        match_count = 0
        self.changed = False
        self.msg = ""
        for each_profile in config:
            unmatch_stat = self.have["switch_profile"][profile_no].get(
                "profile_compare_stat"
            )
            if (
                any(
                    profile["name"] == each_profile["profile_name"]
                    for profile in self.have["switch_profile_list"]
                )
                and unmatch_stat
            ):
                self.msg = "Profile {0} already exist.".format(
                    each_profile["profile_name"]
                )
                self.log(self.msg, "INFO")
                match_count += 1
            profile_no += 1

        if match_count == len(config):
            self.msg = "No changes required, Switch profile(s) are already created"
            self.log(self.msg, "INFO")
            self.set_operation_result(
                "success", False, self.msg, "INFO"
            ).check_return_status()
            return self

        profile_no = 0
        for each_profile in config:
            unmatch_stat = self.have["switch_profile"][profile_no].get(
                "profile_compare_stat"
            )
            profile_id = self.have["switch_profile"][profile_no].get("profile_id")
            profile_name = self.have["switch_profile"][profile_no].get("profile_name")

            unmatch_template_stat = self.have["switch_profile"][profile_no].get(
                "template_compare_stat"
            )
            ob_template = self.have["switch_profile"][profile_no].get(
                "onboarding_templates"
            )
            dn_template = self.have["switch_profile"][profile_no].get("day_n_templates")
            previous_templates = self.have["switch_profile"][profile_no].get(
                "previous_templates"
            )

            have_site = self.have["switch_profile"][profile_no].get("site_response")
            previous_sites = self.have["switch_profile"][profile_no].get(
                "previous_sites"
            )
            unmatch_site_stat = self.have["switch_profile"][profile_no].get(
                "site_compare_stat"
            )
            task_details = {}

            # Below if condition for creating the switch profile
            if not profile_id:
                self.log(
                    "Found unmatch in the profile: {0}".format(
                        self.pprint(each_profile)
                    ),
                    "DEBUG",
                )
                task_details = self.create_switch_profile(each_profile)

                if task_details:
                    self.log(
                        "Profile created find the task details: {0}".format(
                            self.pprint(task_details)
                        ),
                        "DEBUG",
                    )
                    profile_response = dict(
                        profile_name=each_profile["profile_name"],
                        status=task_details["progress"],
                    )
                    uuid_pattern = r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b"
                    match = re.search(uuid_pattern, task_details["progress"])

                    if match:
                        profile_id = match.group()
                else:
                    self.msg = self.msg + "Unable to create profile: '{0}'.".format(
                        str(self.not_processed)
                    )

            assign_site_task, update_temp_status = [], []
            if not unmatch_template_stat:
                self.log(
                    "Started attaching template(s) for the profile: {0}".format(
                        profile_name
                    ),
                    "INFO",
                )

                if ob_template and profile_id:
                    update_temp_status.append(
                        self.process_templates(
                            ob_template, previous_templates, profile_name, profile_id
                        )
                    )
                    self.log(
                        "Template Response (ob_template): {0}".format(
                            self.pprint(update_temp_status)
                        ),
                        "DEBUG",
                    )

                if dn_template and profile_id:
                    update_temp_status.append(
                        self.process_templates(
                            dn_template, previous_templates, profile_name, profile_id
                        )
                    )
                    self.log(
                        "Template Response (dn_template): {0}".format(
                            self.pprint(update_temp_status)
                        ),
                        "DEBUG",
                    )

            if not unmatch_site_stat:
                self.log(
                    "Found unmatched site in profile: {0}".format(profile_name), "DEBUG"
                )
                if have_site and isinstance(have_site, list):
                    for each_site in have_site:
                        if not self.value_exists(
                            previous_sites, "id", each_site["site_id"]
                        ):
                            assign_site_task.append(
                                self.assign_site_to_network_profile(
                                    profile_id,
                                    each_site["site_id"],
                                    profile_name,
                                    each_site["site_names"],
                                )
                            )

            have_profile_id = self.have["switch_profile"][profile_no].get("profile_id")
            if have_profile_id:
                if update_temp_status or assign_site_task:
                    self.msg = "Network profile '{0}' updated successfully.".format(
                        each_profile["profile_name"]
                    )
                    self.log(self.msg, "INFO")
                    profile_response = dict(
                        profile_name=each_profile["profile_name"], status=self.msg
                    )
                    self.switch.append(profile_response)
                else:
                    self.not_processed.append(each_profile["profile_name"])
            else:
                if profile_id or update_temp_status or assign_site_task:
                    self.msg = "Network profile '{0}' created successfully.".format(
                        each_profile["profile_name"]
                    )
                    self.log(self.msg, "INFO")
                    profile_response = dict(
                        profile_name=each_profile["profile_name"], status=self.msg
                    )
                    self.switch.append(profile_response)
                else:
                    self.not_processed.append(each_profile["profile_name"])

            profile_no += 1

        if self.switch:
            self.msg = "Switch Profile created/updated successfully for '{0}'.".format(
                str(self.switch)
            )
            self.log(self.msg, "INFO")
            self.changed = True

        if self.not_processed:
            self.msg += " Unable to process the following Switch Profile(s): '{0}'. They may not have been created or already exist.".format(
                ", ".join(map(str, self.not_processed))
            )
            self.log(self.msg, "DEBUG")

        self.log(self.msg, "INFO")
        self.set_operation_result(
            self.status, self.changed, self.msg, "INFO", self.switch
        ).check_return_status()

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
        self.log(
            "Starting to verify created/updated switch profile for: {0}".format(config),
            "INFO",
        )
        success_profile = []

        if not self.switch and not self.not_processed:
            msg = "No changes required, Switch profile(s) are already created and verified"
            self.log(msg, "INFO")
            self.set_operation_result(
                "success", False, msg, "INFO"
            ).check_return_status()
            return self

        for each_profile in config:
            for each_created in self.switch:
                if each_created.get("profile_name") == each_profile["profile_name"]:
                    success_profile.append(each_created["profile_name"])

        if not success_profile:
            msg = "Unable to create the profile for '{0}'.".format(config)
            self.log(msg, "INFO")
            self.fail_and_exit(msg)

        msg = "Profile created/updated are verified successfully for '{0}'.".format(
            str(success_profile)
        )
        self.log(msg, "INFO")
        self.set_operation_result(
            "success", True, msg, "INFO", self.switch
        ).check_return_status()
        return self

    def get_diff_deleted(self, config):
        """
        Delete Network switch profile in Cisco Catalyst Center based on playbook details.

        Parameters:
            config (list of dict) - Playbook details

        Returns:
            self - The current object with profile deletion message and response information.
        """
        self.log("Starting to delete switch profile(s) for: {0}".format(config), "INFO")

        self.process_delete_profiles(
            config, "switch_profile_list"
        ).check_return_status()

        return self

    def verify_diff_deleted(self, config):
        """
        Validates that the switch profile(s) in Cisco Catalyst Center have been deleted
        based on the playbook details.

        Parameters:
            config (dict) - Playbook details containing Network profile switch information.

        Returns:
            self - The current object with message and response.
        """
        self.log(
            "Starting to verify the deleted switch profile for: {0}".format(config),
            "INFO",
        )
        success_profile = []
        self.get_have(config)

        for each_profile in config:
            if not self.common_delete:
                msg = "No changes required, profile(s) are already deleted"
                self.log(msg, "INFO")
                self.set_operation_result(
                    "success", False, msg, "INFO"
                ).check_return_status()
                return self

            if not self.value_exists(
                self.have["switch_profile_list"], "name", each_profile["profile_name"]
            ):
                success_profile.append(each_profile["profile_name"])

        if len(success_profile) > 0:
            msg = (
                "Switch profile(s) deleted and verified successfully for '{0}'.".format(
                    str(success_profile)
                )
            )
            self.changed = True

        if len(self.not_processed) > 0:
            msg = msg + "Unable to delete below Switch profile '{0}'.".format(config)
            self.changed = False
            self.status = "failed"

        self.log(msg, "INFO")
        self.set_operation_result(
            self.status, self.changed, msg, "INFO", self.common_delete
        ).check_return_status()
        return self


def main():
    """main entry point for module execution"""

    # Define the specification for module arguments
    element_spec = {
        "dnac_host": {"type": "str", "required": True},
        "dnac_port": {"type": "str", "default": "443"},
        "dnac_username": {"type": "str", "default": "admin", "aliases": ["user"]},
        "dnac_password": {"type": "str", "no_log": True},
        "dnac_verify": {"type": "bool", "default": True},
        "dnac_version": {"type": "str", "default": "2.2.3.3"},
        "dnac_debug": {"type": "bool", "default": False},
        "dnac_log": {"type": "bool", "default": False},
        "dnac_log_level": {"type": "str", "default": "WARNING"},
        "dnac_log_file_path": {"type": "str", "default": "dnac.log"},
        "dnac_log_append": {"type": "bool", "default": True},
        "config_verify": {"type": "bool", "default": False},
        "dnac_api_task_timeout": {"type": "int", "default": 1200},
        "dnac_task_poll_interval": {"type": "int", "default": 2},
        "config": {"type": "list", "required": True, "elements": "dict"},
        "state": {"default": "merged", "choices": ["merged", "deleted"]},
        "validate_response_schema": {"type": "bool", "default": True},
    }

    # Create an AnsibleModule object with argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=False)
    ccc_network_profile = NetworkSwitchProfile(module)
    state = ccc_network_profile.params.get("state")

    if (
        ccc_network_profile.compare_dnac_versions(
            ccc_network_profile.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_network_profile.status = "failed"
        ccc_network_profile.msg = (
            "The specified version '{0}' does not support the network profile workflow feature."
            "Supported version(s) start from '2.3.7.9' onwards.".format(
                ccc_network_profile.get_ccc_version()
            )
        )
        ccc_network_profile.log(ccc_network_profile.msg, "ERROR")
        ccc_network_profile.check_return_status()

    if state not in ccc_network_profile.supported_states:
        ccc_network_profile.status = "invalid"
        ccc_network_profile.msg = "State {0} is invalid".format(state)
        ccc_network_profile.check_return_status()

    ccc_network_profile.validate_input().check_return_status()
    config_verify = ccc_network_profile.params.get("config_verify")

    config = ccc_network_profile.validated_config
    if not config:
        ccc_network_profile.msg = "Playbook configuration is missing."
        ccc_network_profile.log(ccc_network_profile.msg, "ERROR")
        ccc_network_profile.fail_and_exit(ccc_network_profile.msg)

    ccc_network_profile.reset_values()
    ccc_network_profile.get_want(config).check_return_status()
    ccc_network_profile.get_have(config).check_return_status()
    ccc_network_profile.get_diff_state_apply[state](config).check_return_status()
    if config_verify:
        ccc_network_profile.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_network_profile.result)


if __name__ == "__main__":
    main()
