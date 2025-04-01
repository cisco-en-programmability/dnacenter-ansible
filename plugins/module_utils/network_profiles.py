#!/usr/bin/env python
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
        Validate and retrieve site and template details for the given profile.

        Parameters:
            self (object): An instance of a class used for interacting with
                           Cisco Catalyst Center.
            each_profile (dict) - Playbook details containing network profile
            profile_info (dict) - Validate and add the site and template info
                to the existing profile information.

        Returns:
            self: Updated object with validated site and template information.
        """
        onboarding_templates = each_profile.get("onboarding_templates")
        day_n_templates = each_profile.get("day_n_templates")
        self.log("Check given template exist in the Catalyst Center for {0}, {1}".
                 format(onboarding_templates, day_n_templates), "INFO")

        self.log("Fetching onboarding template details for: {0}".format(onboarding_templates),
                 "DEBUG")
        if onboarding_templates and isinstance(onboarding_templates, list):
            profile_info["onboarding_templates"] = self.get_templates_details(
                onboarding_templates)

        self.log("Fetching day-N template details for: {0}".format(day_n_templates), "DEBUG")
        if day_n_templates and isinstance(day_n_templates, list):
            profile_info["day_n_templates"] = self.get_templates_details(day_n_templates)

        site_names = each_profile.get("site_names")
        if site_names:
            validated_sites = []
            for site in site_names:
                if site:
                    site_data = {}
                    site_data["site_exist"], site_data["site_id"] =\
                        self.get_site_id(site)
                    site_data["site_names"] = site
                    validated_sites.append(site_data)
                    self.log("Site '{0}' existence: {1}, Site ID: {2}".format(
                        site, site_data["site_exist"], site_data["site_id"]), "INFO")

                    child_sites = self.get_child_sites(site)
                    if child_sites:
                        self.log("Child sites found for '{0}': {1}".format(site, child_sites), "DEBUG")
                        validated_sites.extend(child_sites)

                    if not site_data["site_exist"]:
                        self.msg = 'Given site {0} not exist in Catalyst Center'.format(site)
                        self.log(self.msg, "ERROR")
                        self.set_operation_result("failed", False, self.msg,
                                                  "ERROR").check_return_status()

            if len(validated_sites) > 0:
                # Filter duplicate site ids from site response
                unique_sites = [dict(final_site)
                                for final_site in {frozenset(site.items())
                                                   for site in validated_sites}]
                self.log("Found Site ID(s) list: {0}".format(self.pprint(unique_sites)), "INFO")
                profile_info["site_response"] = unique_sites

            return self

    def get_child_sites(self, site_name_hierarchy):
        """
        Retrieve child sites mapped to the given site hierarchy.

        Parameters:
            self (object): An instance of a class used for interacting with
                           Cisco Catalyst Center.
            site_name_hierarchy (str) - Site name with complete hierarchy

        Returns:
            list or None: List of child site details if found, otherwise None.
        """
        get_sites_params = {"name_hierarchy": site_name_hierarchy + "/.*"}
        self.log("Fetching child sites for '{}'. Request parameters: {}".format(
            site_name_hierarchy, get_sites_params), "DEBUG")

        try:
            response = self.execute_get_request("site_design", "get_sites", get_sites_params)
            self.log("Response from get_sites request: {}".format(response), "DEBUG")

            if response and isinstance(response, dict):
                child_sites = response.get("response", [])
                self.log("Found {0} child sites for site area: '{1}'".format(
                    len(child_sites), site_name_hierarchy), "DEBUG")

                if not child_sites:
                    self.log("No child sites found for '{0}'. Returning None.".format(
                        site_name_hierarchy), "DEBUG")
                    return None

                child_site_response = []
                for child in child_sites:
                    child_site_id = child.get("id")
                    child_site_name_hierarchy = child.get("nameHierarchy")
                    self.log("Received child site: '{0}' with ID: '{1}'".
                             format(child_site_name_hierarchy, child_site_id), "DEBUG")

                    if child_site_id and child_site_name_hierarchy:
                        self.log("Processing child site: '{0}' (ID: '{1}')".format(
                            child_site_name_hierarchy, child_site_id), "DEBUG")
                        child_site_response.append({
                            "site_exist": True,
                            "site_id": child_site_id,
                            "site_names": child_site_name_hierarchy
                        })

                self.log("All child sites for site area: '{0}': {1}".format(
                    site_name_hierarchy, self.pprint(child_site_response)), "DEBUG")
                return child_site_response

        except Exception as e:
            self.msg = 'An error occurred during get child sites: {0}'.format(str(e))
            self.log(self.msg, "ERROR")
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return None

    def get_templates_details(self, template_list):
        """
        Retrieve and validate the given list of templates from Cisco Catalyst Center.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            template_list (list): List of template names to validate.

        Returns:
            list or None: List of dictionaries containing template details if found, otherwise None.

        Description:
            This function used to get the templates details from Cisco Catalyst Center and
            compare with given template_list from play book and retrun with list of
            template details.
        """
        self.log("Fetching details for templates: {}".format(template_list), "INFO")

        try:
            response = self.dnac._exec(
                family="configuration_templates",
                function="gets_the_templates_available_v1",
                params={}
            )
            self.log("Response from gets_the_templates_available_v1 API: {0}".
                     format(self.pprint(response)), "DEBUG")

            if not response or not isinstance(response, list):
                self.log("Invalid or empty response received. No templates found.", "WARNING")
                return None

            template_info_list = []
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
                        self.log("Template '{0}' found with ID '{1}'.".format(
                            input_template, each_template.get("templateId")), "DEBUG")
                        break

                if not template_info:
                    self.msg = "Given template '{0}' does not exist in Catalyst Center".format(
                        input_template)
                    self.log(self.msg, "ERROR")
                    self.fail_and_exit(self.msg)

            if len(template_info_list) > 0:
                self.log("Final validated template details: {0}".format(
                    self.pprint(template_info_list)), "INFO")
                return template_info_list
            else:
                self.log("No valid templates found in the given list.", "WARNING")
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
        self.log("Fetching network profiles for profile type: {0}".format(profile_type), "INFO")

        try:
            response = self.execute_get_request(
                "site_design", "retrieves_the_list_of_network_profiles_for_sites_v1", param)
            self.log("Response from retrieves_the_list_of_network_profiles_for_sites_v1 API: {0}".
                     format(self.pprint(response)), "DEBUG")

            profiles = response.get("response")
            if not profiles or not isinstance(profiles, list):
                self.log("Invalid or missing network profile response, expected dict but got {0}".
                         format(type(profiles).__name__), "ERROR")
                return None

            self.log("Received network profile response: {0}".format(self.pprint(profiles)), "INFO")
            return profiles

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
            list: A list of dict contains network template ids and names.

        Description:
            This function is used to get cli template for the specific profile id
        """
        self.log("Fetching CLI templates for profile ID: {0}".format(profile_id), "INFO")
        param = {
            "profile_id": profile_id
        }

        try:
            response = self.execute_get_request(
                "network_settings", "retrieve_cli_templates_attached_to_a_network_profile_v1",
                param)
            self.log("Response from retrieve_cli_templates_attached_to_a_network_profile_v1 " +
                     "API: {0}".format(self.pprint(response)), "DEBUG")

            templates = response.get("response")
            if not templates or not isinstance(templates, list):
                self.log("Invalid or missing template response, expected list but got {0}".
                         format(type(templates).__name__), "ERROR")
                return None

            self.log("CLI templates retrieved: {0}".format(self.pprint(templates)), "INFO")
            return templates

        except Exception as e:
            self.msg = "An error occurred during retrieve cli templates " +\
                "for profile: {0}".format(str(e))
            self.log(self.msg, "ERROR")
            return None

    def attach_networkprofile_cli_template(self, profile_name, profile_id, template_name,
                                           template_id):
        """
        Attaches a network profile to a CLI template using the given profile and template details.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            profile_name (str): Name of the network profile.
            profile_id (str): Unique identifier of the network profile.
            template_name (str): Name of the CLI template.
            template_id (str): Unique identifier of the CLI template.

        Returns:
            dict: Contains network profile information if successful.
            None: If the operation fails.

        Description:
            Attaches a given network profile to a CLI template by sending the necessary
            request payload.
        """
        self.log("Attaching CLI template '{0}' (ID: {1}) to profile '{2}' (ID: {3})".format(
            template_name, template_id, profile_name, profile_id), "INFO")
        function_name = "attach_network_profile_to_a_day_n_cli_template_v1"
        profile_payload = {
            "profileId": profile_id,
            "template_id": template_id
        }

        try:
            return self.execute_process_task_data("configuration_templates",
                                                  function_name, profile_payload)

        except Exception as e:
            error_msg = "Failed to attach profile '{0}' to CLI template '{1}': {2}".format(
                profile_name, template_name, str(e))
            self.log(error_msg, "ERROR")
            self.set_operation_result("failed", False, error_msg, "ERROR")
            return None

    def detach_networkprofile_cli_template(self, profile_name, profile_id, template_name,
                                           template_id):
        """
        Detaches a network profile from a CLI template using the provided profile and template IDs.

        Parameters:
            profile_name (str): Name of the network profile.
            profile_id (str): Unique identifier of the network profile.
            template_name (str): Name of the CLI template.
            template_id (str): Unique identifier of the CLI template.

        Returns:
            dict: Contains network profile information if successful.
            None: If the operation fails.

        Description:
            Detaches the specified network profile from a CLI template by sending
            the necessary request payload.
        """

        self.log("Detaching CLI template '{0}' (ID: {1}) from network profile '{2}' (ID: {3})".
                 format(template_name, template_id, profile_name, profile_id), "INFO")
        function_name = "detach_a_list_of_network_profiles_from_a_day_n_cli_template_v1"
        profile_payload = {
            "profileId": profile_id,
            "template_id": template_id
        }
        try:
            return self.execute_process_task_data("configuration_templates",
                                                  function_name, profile_payload)

        except Exception as e:
            error_msg = "Failed to detach network profile '{0}' (ID: {1}) from CLI template '{2}' (ID: {3}): {4}".format(
                profile_name, profile_id, template_name, template_id, str(e))
            self.log(error_msg, "ERROR")
            self.set_operation_result("failed", False, error_msg, "ERROR")
            return None

    def assign_site_to_network_profile(self, profile_id, site_id, profile_name, site_name):
        """
        Assign a site to a network profile.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            profile_id (str): A string containing profile id used to assign to site.
            site_id (str): A string containing site id used to assign the site id to profile.
            profile_name (str): A string containing profile name used to assign site to profile.
            site_name (str): A string containing site name used to assign the site to profile.

        Returns:
            dict: A dict contains Task details of the profile assigned status.

        Description:
            This function is used to assign the Profile id to the Site.
        """
        self.log("Assigning site {0}: {1} to profile {2}:{3}.".format(
            site_name, site_id, profile_name, profile_id), "INFO")
        params = {
            "profile_id": profile_id,
            "id": site_id
        }

        return self.execute_process_task_data(
            "site_design", "assign_a_network_profile_for_sites_to_the_given_site_v1",
            params
        )

    def unassign_site_to_network_profile(self, profile_name, profile_id, site_name, site_id):
        """
        Un assign a site from the network profile.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            profile_name (str): A string containing profile name used to unassign from site.
            profile_id (str): A string containing profile id used to unassign from site.
            site_name (str): A string containing site name used to un assign from the profile.
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
        self.log("Unassigning site {0}: {1} from network profile {2}: {3}.".
                 format(site_name, site_id, profile_name, profile_id), "INFO")

        return self.execute_process_task_data(
            "site_design", "unassigns_a_network_profile_for_sites_from_multiple_sites_v1",
            param
        )

    def delete_network_profiles(self, profile_name, profile_id):
        """
        Delete network profiles from the Catalyst Center and response with
        the task details.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            profile_name (str): Contains profile_name to be deleted.
            profile_id (str): Contains profile ID to be deleted.

        Returns:
            dict: A dict contains task details of the deleted status.

        Description:
            This function is used to delete network profiles from Catalyst Center.
        """

        self.log("Delete network profiles for {0}: {1}".format(profile_name, profile_id), "INFO")
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
            if not profile_family or not profile_function_name or not payload_data:
                self.log("Invalid API parameters provided.", "ERROR")
                return None

            if not task_id:
                task_id = self.get_taskid_post_api_call(profile_family,
                                                        profile_function_name,
                                                        payload_data)
                if not task_id:
                    self.log("Failed to retrieve task ID.", "ERROR")
                    return None

            if not isinstance(self.payload, dict):
                self.log("self.payload is not a valid dictionary.", "ERROR")
                return None

            resync_retry_count = int(self.payload.get("dnac_api_task_timeout", 10))
            resync_retry_interval = int(self.payload.get("dnac_task_poll_interval", 5))
            while resync_retry_count > 0:
                task_details_response = self.get_tasks_by_id(task_id)

                if not task_details_response:  # Ensure the response is valid
                    self.log("Failed to retrieve task details for task ID: {0}".
                             format(task_id), "ERROR")
                    return None

                task_status = task_details_response.get("status")
                self.log("Task ID: {0}, Status: {1}, Attempts remaining: {2}".format(
                    task_id, task_status, resync_retry_count), "INFO")

                if task_details_response.get("endTime") is not None:
                    if task_status == "SUCCESS":
                        self.result['changed'] = True
                        self.result['response'] = self.get_task_details_by_id(task_id)
                        return self.result['response']

                    if task_status == "FAILURE":
                        self.result['changed'] = False
                        self.result['response'] = self.get_task_details_by_id(task_id)
                        return self.result['response']

                self.log("Pauses execution for {0} seconds.".format(resync_retry_interval), "INFO")
                time.sleep(resync_retry_interval)
                resync_retry_count = resync_retry_count - 1

            self.log("Task {0} did not complete within the timeout.".format(task_id), "ERROR")
            return None

        except Exception as e:
            self.msg = 'An error occurred during get task details: {0}'.format(str(e))
            self.log(self.msg, "ERROR")
            self.fail_and_exit(self.msg)

    def value_exists(self, data, target_key, target_value):
        """
        Check if a specific key-value pair exists in a dictionary or a list of dictionaries.

        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            data (dict | list): The dictionary or list of dictionaries to search in.
            target_key (str): A string containing key of the dict in the data.
            target_value (str): A string containing value to find in the data.

        Returns:
            bool: True if the key-value pair exists, otherwise False.

        Description:
            This function recursively searches for the key-value pair in nested
            dictionaries and lists.
        """
        if isinstance(data, dict):
            # First, check if the key exists in the dictionary at the top level
            if data.get(target_key) == target_value:
                return True

            # Then, recursively check values (nested dictionaries/lists)
            for value in data.values():
                if self.value_exists(value, target_key, target_value):
                    return True
        elif isinstance(data, list):
            for item in data:
                if self.value_exists(item, target_key, target_value):
                    return True
        return False

    def find_duplicate_value(self, config_list, key_name):
        """
        Identifies duplicate values for a given key in a list of dictionaries.

        Parameters:
            config_list (list of dict): A list where each dictionary contains key-value pairs.
            key_name (str): The key whose values need to be checked for duplicates.

        Returns:
            list: A list of duplicate key_name values found in the input list.
        """
        seen = set()
        duplicates = set()

        for item in config_list:  # Ensure the item is a dictionary
            value = item.get(key_name)
            if value:
                if value in seen:
                    duplicates.add(value)
                else:
                    seen.add(value)

        return list(duplicates)
