#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ["A Mohamed Rafeek, Madhan Sankaranarayanan"]

import time
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase
)


class NetworkProfileFunctions(DnacBase):
    """Class containing member attributes for network profile workflow manager module"""

    def __init__(self, module):
        super().__init__(module)

    def check_site_template(self, each_profile, profile_info):
        """
        Extend get have for site, and template related validate information
        for the given profile config from Cisco Catalyst Center

        Parameters:
            self (object): An instance of a class used for interacting with
                           Cisco Catalyst Center.
            each_profile (dict) - Playbook details containing network profile
            profile_info (dict) - Validate and add the site and template info
                to the existing profile information.

        Returns:
            self - The current object with template, validate site id
            information collection for profile update.
        """
        onboarding_templates = each_profile.get("onboarding_templates")
        day_n_templates = each_profile.get("day_n_templates")
        self.log("Check given template exist in the Catalyst Center for {0}, {1}".
                 format(onboarding_templates, day_n_templates), "INFO")

        if onboarding_templates and isinstance(onboarding_templates, list) and len(onboarding_templates) > 0:
            profile_info["onboarding_templates"] = self.get_templates_details(
                onboarding_templates)

        if day_n_templates and isinstance(day_n_templates, list) and len(day_n_templates) > 0:
            profile_info["day_n_templates"] = self.get_templates_details(day_n_templates)

        site_names = each_profile.get("site_names")
        if site_names:
            site_response = []
            for site in site_names:
                if site:
                    each_site_response = {}
                    each_site_response["site_exist"], each_site_response["site_id"] =\
                        self.get_site_id(site)
                    each_site_response["site_names"] = site
                    site_response.append(each_site_response)

                    child_sites = self.get_child_sites(site)
                    if child_sites:
                        site_response.extend(child_sites)

                    if not each_site_response["site_exist"]:
                        self.msg = 'Given site {0} not exist in Catalyst Center'.format(site)
                        self.log(self.msg, "ERROR")
                        self.set_operation_result("failed", False, self.msg,
                                                  "ERROR").check_return_status()

            if len(site_response) > 0:
                # Filter duplicate site ids from site response
                site_response = [dict(final_site)
                                 for final_site in {frozenset(site.items())
                                                    for site in site_response}]
                self.log("Found Site ID(s) list: {0}".format(self.pprint(site_response)), "INFO")
                profile_info["site_response"] = site_response

    def get_child_sites(self, site_name_hierarchy):
        """
        Get all child site mapped for the given site hierarchy

        Parameters:
            self (object): An instance of a class used for interacting with
                           Cisco Catalyst Center.
            site_name_hierarchy (str) - Site name with complete hierarchy

        Returns:
            child_site_response or None - Any child sites found add the child site id
            with status and complete hierarchy unless return None.
        """
        get_sites_params = {"name_hierarchy": site_name_hierarchy + "/.*"}
        self.log("Parameters for get_sites request: {}".format(get_sites_params), "DEBUG")

        try:
            response = self.execute_get_request("site_design", "get_sites", get_sites_params)
            self.log("Response from get_sites request: {}".format(response), "DEBUG")

            if response and isinstance(response, dict):
                child_sites = response.get("response", [])
                self.log("Found {0} child sites for site area: '{1}'".format(
                    len(child_sites), site_name_hierarchy), "DEBUG")

                if child_sites:
                    child_site_response = []
                    for child in child_sites:
                        child_site_id = child.get("id")
                        child_site_name_hierarchy = child.get("nameHierarchy")
                        self.log("Received child site: '{0}' with ID: '{1}'".
                                 format(child_site_name_hierarchy, child_site_id), "DEBUG")

                        if child_site_id:
                            each_site_response = {}
                            each_site_response["site_exist"], each_site_response["site_id"] =\
                                True, child_site_id
                            each_site_response["site_names"] = child_site_name_hierarchy
                            child_site_response.append(each_site_response)

                    self.log("All child sites for site area: '{0}': {1}".format(
                        site_name_hierarchy, self.pprint(child_site_response)), "DEBUG")
                    return child_site_response
                else:
                    return None

        except Exception as e:
            self.msg = 'An error occurred during get child sites: {0}'.format(str(e))
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return None

    def get_templates_details(self, template_list):
        """
        This Function used to get the list of templates from Cisco Catalyst Center
        and validate the template_list exist in the Catalyst Center.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            template_list (list): list of string contains template name to validate.

        Returns:
            list: A list of dict contain the Template details of the given list from
            template_list.

        Description:
            This function used to get the templates details from Cisco Catalyst Center and
            compare with given template_list from play book and retrun with list of
            template details.
        """
        self.log("Get templates details for : {0}".format(template_list), "INFO")

        try:
            response = self.dnac._exec(
                family="configuration_templates",
                function="gets_the_templates_available_v1",
                params={}
            )
            self.log("Response from gets_the_templates_available_v1 API: {0}".
                     format(self.pprint(response)), "DEBUG")

            if response and isinstance(response, list):
                template_info_list = []
                if len(response) > 0:
                    for input_template in template_list:
                        template_info = {}
                        for each_template in response:
                            if each_template.get("name") == input_template:
                                template_info = {
                                    "template_name": each_template.get("name"),
                                    "template_exist": True,
                                    "template_id": each_template.get("templateId"),
                                    "template_info": each_template
                                }
                                template_info_list.append(template_info)

                        if not template_info:
                            self.msg = 'Given template {0} not exist in Catalyst Center'.format(
                                input_template)
                            self.log(self.msg, "ERROR")
                            self.set_operation_result("failed", False, self.msg,
                                                      "ERROR").check_return_status()

                if len(template_info_list) > 0:
                    return template_info_list
                else:
                    return None

        except Exception as e:
            self.msg = 'An error occurred during get templates details: {0}'.format(str(e))
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return None

    def get_network_profile(self, profile_type, offset, limit):
        """
        Get network profile list from Cisco Catalyst Center based on the profile type
        given in the playbook and response with network profile information.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            profile_type (str): A string containing Wireless, Switch or Assurance.
            offset (int): Offset value start from 1
            limit (int): Limit value start from 1 to 500

        Returns:
            list: A list of dict contains network profile information.

        Description:
            This function used to get the network profile based on input config.
        """

        param = {"type": profile_type,
                 "offset": offset,
                 "limit": limit}
        self.log("Getting all network profile", "INFO")
        try:
            response = self.dnac._exec(
                family="site_design",
                function="retrieves_the_list_of_network_profiles_for_sites_v1",
                params=param
            )
            self.log("Response from retrieves_the_list_of_network_profiles_for_sites_v1 API: {0}".
                     format(self.pprint(response)), "DEBUG")
            if response and isinstance(response, dict):
                self.log("Received the network profile response: {0}".
                         format(self.pprint(response["response"])), "INFO")
                return response.get("response")
            else:
                return None

        except Exception as e:
            self.msg = 'An error occurred during get network profile: {0}'.format(str(e))
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return None

    def get_templates_for_profile(self, profile_id):
        """
        Get the CLI template for the specific profile id
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            profile_id (str): A string containing profile id to fetch template assigned to
                the profile.

        Returns:
            list: A list of dict contains network template id and name.

        Description:
            This function is used to get cli template for the specific profile id
        """
        self.log("Profile id for the template: {0}".format(profile_id), "INFO")
        param = {
            "profile_id": profile_id
        }

        try:
            response = self.dnac._exec(
                family="network_settings",
                function="retrieve_cli_templates_attached_to_a_network_profile_v1",
                params=param
            )
            self.log("Response from retrieve_cli_templates_attached_to_a_network_profile_v1 " +
                     "API: {0}".format(self.pprint(response)), "DEBUG")

            if response and isinstance(response, dict):
                return response.get("response")
            else:
                return None

        except Exception as e:
            self.msg = "An error occurred during retrieve cli templates " +\
                "for profile: {0}".format(str(e))
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

    def assign_site_to_network_profile(self, profile_id, site_id):
        """
        Assign a site to a network profile.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            profile_id (str): A string containing profile id used to assign to site.
            site_id (str): A string containing site id used to assign the profile to this site id.

        Returns:
            dict: A dict contains Task details of the profile assigned status.

        Description:
            This function is used to assign the Profile id to the Site.
        """
        self.log("Assigning site {0} to profile {1}.".format(
            profile_id, site_id), "INFO")
        params = {
            "profile_id": profile_id,
            "id": site_id
        }

        return self.execute_process_task_data(
            "site_design", "assign_a_network_profile_for_sites_to_the_given_site_v1",
            params
        )

    def unassign_site_to_network_profile(self, profile_id, site_id):
        """
        Un assign a site from the network profile.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            profile_id (str): A string containing profile id used to un assign from site.
            site_id (str): A string containing site id used to un assign from the profile.

        Returns:
            dict: A dict contains Task details of the profile unassigned status.

        Description:
            This function is used to un assign the Profile id from the Site.
        """
        param = {
            "profile_id": profile_id,
            "site_id": site_id
        }
        self.log("Unassign site to network profile for: {0}".format(str(param)), "INFO")

        return self.execute_process_task_data(
            "site_design", "unassigns_a_network_profile_for_sites_from_multiple_sites_v1",
            param
        )

    def delete_network_profiles(self, profile_id):
        """
        Delete network profiles from the Catalyst Center and response with
        the task details.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            profile_id (str): Contains profile to be deleted.

        Returns:
            dict: A dict contains task details of the deleted status.

        Description:
            This function is used to delete network profiles from Catalyst Center.
        """

        self.log("Delete network profiles for: {0}".format(profile_id), "INFO")
        param = {
            "id": profile_id,
        }

        return self.execute_process_task_data(
            "site_design", "deletes_a_network_profile_for_sites_v1", param
        )

    def execute_process_task_data(self, profile_family, profile_function_name,
                                  payload_data, task_id=None):
        """
        This function used to execute the payload data based on the family and function
        and get the task id, aslo pass the taskid and get details of the task as a output.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            profile_family (str): A string containing family name of the API.
            profile_function_name (str): A string containing function name of the API.
            payload_data (dict): Contains dict of payload for the API.
            task_id (str): Optional param if task id is available profile_family,
                        profile_function_name, payload_data can be dummy data
        Returns:
            dict: A dict contains Task details as output.

        Description:
            This function is used to process the API call and show the task details
            as the response.
        """
        try:
            if profile_family and profile_function_name and payload_data:
                if not task_id:
                    task_id = self.get_taskid_post_api_call(profile_family,
                                                            profile_function_name,
                                                            payload_data)
                resync_retry_count = int(self.payload.get("dnac_api_task_timeout"))
                resync_retry_interval = int(self.payload.get("dnac_task_poll_interval"))
                while resync_retry_count:
                    task_details_response = self.get_tasks_by_id(task_id)
                    self.log("Status of the task: {0} .".format(self.status), "INFO")

                    if task_details_response.get("endTime") is not None:
                        if task_details_response.get("status") == "SUCCESS":
                            self.result['changed'] = True
                            self.result['response'] = self.get_task_details_by_id(task_id)
                            return self.result['response']
                        if task_details_response.get("status") == "FAILURE":
                            self.result['changed'] = False
                            self.result['response'] = self.get_task_details_by_id(task_id)
                            return self.result['response']

                    time.sleep(resync_retry_interval)
                    resync_retry_count = resync_retry_count - 1
            else:
                return None

        except Exception as e:
            self.msg = 'An error occurred during get task details: {0}'.format(str(e))
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

    def value_exists(self, data, target_key, target_value):
        """
        This function used check specifice key, value pair exist in the data of dict or
        list of dict and return the True or False as a response.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            data (dict): Contains dict or list of dict data when need to find
            target_key (str): A string containing key of the dict in the data.
            target_value (str): A string containing value to find in the data.

        Returns:
            bool: return True or False based the key, value matches.

        Description:
            This function is used to check the given key, value exist in the data
            and return the true or false..
        """
        if isinstance(data, dict):
            for value in data.values():
                if data.get(target_key) == target_value or self.value_exists(value, target_key,
                                                                             target_value):
                    return True
        elif isinstance(data, list):
            for item in data:
                if self.value_exists(item, target_key, target_value):
                    return True
        return False
