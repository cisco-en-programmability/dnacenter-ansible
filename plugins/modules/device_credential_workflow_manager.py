#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform operations on device credentials in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ['Muthu Rakesh, Madhan Sankaranarayanan, Megha Kandari']

DOCUMENTATION = r"""
---
module: device_credential_workflow_manager
short_description: Resource module for Global Device Credentials and Assigning Credentials to sites.
description:
- Manage operations on Global Device Credentials, Assigning Credentials to sites and Sync Credentials to site device.
- API to create global device credentials.
- API to update global device credentials.
- API to delete global device credentials.
- API to assign the device credential to the site.
- API to sync the device credential to the site. Sync functionality will be applicable for DNAC version 2.3.7.6 onwards.
version_added: '6.7.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Muthu Rakesh (@MUTHU-RAKESH-27)
        Madhan Sankaranarayanan (@madhansansel)
        Megha Kandari (@kandarimegha)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center after applying the playbook config.
    type: bool
    default: False
  state:
    description: The state of Cisco Catalyst Center after module completion.
    type: str
    choices: [ merged, deleted ]
    default: merged
  config:
    description:
    - List of details of global device credentials and site names.
    type: list
    elements: dict
    required: true
    suboptions:
      global_credential_details:
        description: Manages global device credentials
        type: dict
        suboptions:
          cli_credential:
            description: Global Credential V2's cliCredential.
            type: list
            elements: dict
            suboptions:
              description:
                description: Description. Required for creating the credential.
                type: str
              enable_password:
                description:
                - cli_credential credential Enable Password.
                - Password cannot contain spaces or angle brackets (< >)
                type: str
              id:
                description: Credential Id. Use this for updating the device credential.
                type: str
              password:
                description:
                - cli_credential credential Password.
                - Required for creating/updating the credential.
                - Password cannot contain spaces or angle brackets (< >).
                type: str
              username:
                description:
                - cli_credential credential Username.
                - Username cannot contain spaces or angle brackets (< >).
                type: str
              old_description:
                description: Old Description. Use this for updating the description/Username.
                type: str
              old_username:
                description: Old Username. Use this for updating the description/Username.
                type: str
          https_read:
            description: Global Credential V2's httpsRead.
            type: list
            elements: dict
            suboptions:
              id:
                description: Credential Id. Use this for updating the device credential.
                type: str
              name:
                description: Name. Required for creating the credential.
                type: str
              password:
                description:
                - https_read credential Password.
                - Required for creating/updating the credential.
                - Password cannot contain spaces or angle brackets (< >).
                type: str
              port:
                description: Port. Default port is 443.
                type: int
              username:
                description:
                - https_read credential Username.
                - Username cannot contain spaces or angle brackets (< >).
                type: str
              old_description:
                description: Old Description. Use this for updating the description/Username.
                type: str
              old_username:
                description: Old Username. Use this for updating the description/Username.
                type: str
          https_write:
            description: Global Credential V2's httpsWrite.
            type: list
            elements: dict
            suboptions:
              id:
                description: Credential Id. Use this for updating the device credential.
                type: str
              name:
                description: Name. Required for creating the credential.
                type: str
              password:
                description:
                - https_write credential Password.
                - Required for creating/updating the credential.
                - Password cannot contain spaces or angle brackets (< >).
                type: str
              port:
                description: Port. Default port is 443.
                type: int
              username:
                description:
                - https_write credential Username.
                - Username cannot contain spaces or angle brackets (< >).
                type: str
              old_description:
                description: Old Description. Use this for updating the description/Username.
                type: str
              old_username:
                description: Old Username. Use this for updating the description/Username.
                type: str
          snmp_v2c_read:
            description: Global Credential V2's snmpV2cRead.
            type: list
            elements: dict
            suboptions:
              description:
                description: Description. Required for creating the credential.
                type: str
              id:
                description: Credential Id. Use this for updating the device credential.
                type: str
              read_community:
                description:
                - snmp_v2c_read Read Community.
                - Password cannot contain spaces or angle brackets (< >).
                type: str
              old_description:
                description: Old Description. Use this for updating the description.
                type: str
          snmp_v2c_write:
            description: Global Credential V2's snmpV2cWrite.
            type: list
            elements: dict
            suboptions:
              description:
                description: Description. Required for creating the credential.
                type: str
              id:
                description: Credential Id. Use this for updating the device credential.
                type: str
              write_community:
                description:
                - snmp_v2c_write Write Community.
                - Password cannot contain spaces or angle brackets (< >).
                type: str
              old_description:
                description: Old Description. Use this for updating the description.
                type: str
          snmp_v3:
            description: Global Credential V2's snmpV3.
            type: list
            elements: dict
            suboptions:
              auth_password:
                description:
                - snmp_v3 Auth Password.
                - Password must contain minimum 8 characters.
                - Password cannot contain spaces or angle brackets (< >).
                type: str
              auth_type:
                description: Auth Type. ["SHA", "MD5"].
                type: str
              description:
                description:
                - snmp_v3 Description.
                - Should be unique from other snmp_v3 credentials.
                type: str
              id:
                description: Credential Id. Use this for updating the device credential.
                type: str
              privacy_password:
                description:
                - snmp_v3 Privacy Password.
                - Password must contain minimum 8 characters.
                - Password cannot contain spaces or angle brackets (< >).
                type: str
              privacy_type:
                description: Privacy Type. ["AES128", "AES192", "AES256"].
                type: str
              snmp_mode:
                description: Snmp Mode. ["AUTHPRIV", "AUTHNOPRIV", "NOAUTHNOPRIV"].
                type: str
              username:
                description:
                - snmp_v3 credential Username.
                - Username cannot contain spaces or angle brackets (< >).
                type: str
              old_description:
                description: Old Description. Use this for updating the description.
                type: str
      assign_credentials_to_site:
        description: Assign Device Credentials to Site.
        type: dict
        suboptions:
          cli_credential:
            description: CLI Credential.
            type: dict
            suboptions:
              description:
                description: CLI Credential Description.
                type: str
              username:
                description: CLI Credential Username.
                type: str
              id:
                description: CLI Credential Id. Use (Description, Username) or Id.
                type: str
          https_read:
            description: HTTP(S) Read Credential
            type: dict
            suboptions:
              description:
                description: HTTP(S) Read Credential Description.
                type: str
              username:
                description: HTTP(S) Read Credential Username.
                type: str
              id:
                description: HTTP(S) Read Credential Id. Use (Description, Username) or Id.
                type: str
          https_write:
            description: HTTP(S) Write Credential
            type: dict
            suboptions:
              description:
                description: HTTP(S) Write Credential Description.
                type: str
              username:
                description: HTTP(S) Write Credential Username.
                type: str
              id:
                description: HTTP(S) Write Credential Id. Use (Description, Username) or Id.
                type: str
          site_name:
            description: Site Name to assign credential.
            type: list
            elements: str
          snmp_v2c_read:
            description: SNMPv2c Read Credential
            type: dict
            suboptions:
              description:
                description: SNMPv2c Read Credential Description.
                type: str
              id:
                description: SNMPv2c Read Credential Id. Use Description or Id.
                type: str
          snmp_v2c_write:
            description: SNMPv2c Write Credential
            type: dict
            suboptions:
              description:
                description: SNMPv2c Write Credential Description.
                type: str
              id:
                description: SNMPv2c Write Credential Id. Use Description or Id.
                type: str
          snmp_v3:
            description: snmp_v3 Credential
            type: dict
            suboptions:
              description:
                description: snmp_v3 Credential Description.
                type: str
              id:
                description: snmp_v3 Credential Id. Use Description or Id.
                type: str
      apply_credentials_to_site:
        description: Apply Device Credentials to Site.
        type: dict
        suboptions:
          cli_credential:
            description: CLI Credential.
            type: dict
            suboptions:
              description:
                description: CLI Credential Description.
                type: str
              username:
                description: CLI Credential Username.
                type: str
              id:
                description: CLI Credential Id. Use (Description, Username) or Id.
                type: str
          site_name:
            description: Site Name to apply credential.
            type: list
            elements: str
          snmp_v2c_read:
            description: SNMPv2c Read Credential
            type: dict
            suboptions:
              description:
                description: SNMPv2c Read Credential Description.
                type: str
              id:
                description: SNMPv2c Read Credential Id. Use Description or Id.
                type: str
          snmp_v2c_write:
            description: SNMPv2c Write Credential
            type: dict
            suboptions:
              description:
                description: SNMPv2c Write Credential Description.
                type: str
              id:
                description: SNMPv2c Write Credential Id. Use Description or Id.
                type: str
          snmp_v3:
            description: snmp_v3 Credential
            type: dict
            suboptions:
              description:
                description: snmp_v3 Credential Description.
                type: str
              id:
                description: snmp_v3 Credential Id. Use Description or Id.
                type: str
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.9
seealso:
- name: Cisco Catalyst Center documentation for Discovery CreateGlobalCredentialsV2
  description: Complete reference of the CreateGlobalCredentialsV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!create-global-credentials-v-2
- name: Cisco Catalyst Center documentation for Discovery DeleteGlobalCredentialV2
  description: Complete reference of the DeleteGlobalCredentialV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-global-credential-v-2
- name: Cisco Catalyst Center documentation for Discovery UpdateGlobalCredentialsV2
  description: Complete reference of the UpdateGlobalCredentialsV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-global-credentials-v-2
- name: Cisco Catalyst Center documentation for Network Settings AssignDeviceCredentialToSiteV2
  description: Complete reference of the AssignDeviceCredentialToSiteV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!assign-device-credential-to-site-v-2
- name: Cisco Catalyst Center documentation for Network Settings updateDeviceCredentialSettingsForASite_
  description: Complete reference of the updateDeviceCredentialSettingsForASite API.
  link: https://developer.cisco.com/docs/dna-center/update-device-credential-settings-for-a-site
- name: Cisco Catalyst Center documentation for Network Settings syncNetworkDevicesCredential
  description: Complete reference of the syncNetworkDevicesCredential API.
  link: https://developer.cisco.com/docs/dna-center/sync-network-devices-credential

notes:
  - SDK Method used are
    discovery.Discovery.create_global_credentials_v2,
    discovery.Discovery.delete_global_credential_v2,
    discovery.Discovery.update_global_credentials_v2,
    network_settings.NetworkSettings.assign_device_credential_to_site_v2,
    network_settings.NetworkSettings.get_device_credential_settings_for_a_site,
    network_settings.NetworkSettings.update_device_credential_settings_for_a_site,
    network_settings.NetworkSettings.sync_network_devices_credential,
    network_settings.NetworkSettings.get_network_devices_credentials_sync_status,
    site.Sites.get_site_assigned_network_devices,
    site.Sites.get_sites

  - Paths used are
    post /dna/intent/api/v2/global-credential,
    delete /dna/intent/api/v2/global-credential/{id},
    put /dna/intent/api/v2/global-credential,
    post /dna/intent/api/v2/credential-to-site/{siteId},
    get /dna/intent/api/v1/sites/${id}/deviceCredentials,
    post /dna/intent/api/v1/sites/deviceCredentials/apply,
    post /dna/intent/api/v1/sites/${id}/deviceCredentials,
    get /dna/intent/api/v1/sites/${id}/deviceCredentials/status,
    get /dna/intent/api/v1/networkDevices/assignedToSite,
    get /dna/intent/api/v1/sites,
"""

EXAMPLES = r"""
---
  - name: Create Credentials and assign it to a site.
    cisco.dnac.device_credential_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - global_credential_details:
        cli_credential:
        - description: string
          username: string
          password: string
          enable_password: string
        snmp_v2c_read:
        - description: string
          read_community: string
        snmp_v2c_write:
        - description: string
          write_community: string
        snmp_v3:
        - auth_password: string
          auth_type: SHA
          snmp_mode: AUTHPRIV
          privacy_password: string
          privacy_type: AES128
          username: string
          description: string
        https_read:
        - description: string
          username: string
          password: string
          port: 443
        https_write:
        - description: string
          username: string
          password: string
          port: 443
      assign_credentials_to_site:
        cli_credential:
          id: string
        snmp_v2c_read:
          id: string
        snmp_v2c_write:
          id: string
        snmp_v3:
          id: string
        https_read:
          id: string
        https_write:
           id: string
        site_name:
        - string

  - name: Create Multiple Credentials.
    cisco.dnac.device_credential_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - global_credential_details:
        cli_credential:
        - description: string
          username: string
          password: string
          enable_password: string
        - description: string
          username: string
          password: string
          enable_password: string
        snmp_v2c_read:
        - description: string
          read_community: string
        - description: string
          read_community: string
        snmp_v2c_write:
        - description: string
          write_community: string
        - description: string
          write_community: string
        snmp_v3:
        - auth_password: string
          auth_type: SHA
          snmp_mode: AUTHPRIV
          privacy_password: string
          privacy_type: AES128
          username: string
          description: string
        - auth_password: string
          auth_type: SHA
          snmp_mode: AUTHPRIV
          privacy_password: string
          privacy_type: AES128
          username: string
          description: string
        https_read:
        - description: string
          username: string
          password: string
          port: 443
        - description: string
          username: string
          password: string
          port: 443
        https_write:
        - description: string
          username: string
          password: string
          port: 443
        - description: string
          username: string
          password: string
          port: 443

  - name: Update global device credentials using id
    cisco.dnac.device_credential_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - global_credential_details:
        cli_credential:
        - description: string
          username: string
          password: string
          enable_password: string
          id: string
        snmp_v2c_read:
        - description: string
          read_community: string
          id: string
        snmp_v2c_write:
        - description: string
          write_community: string
          id: string
        snmp_v3:
        - auth_password: string
          auth_type: SHA
          snmp_mode: AUTHPRIV
          privacy_password: string
          privacy_type: AES128
          username: string
          description: string
          id: string
        https_read:
        - description: string
          username: string
          password: string
          port: 443
          id: string
        https_write:
        - description: string
          username: string
          password: string
          port: 443
          id: string

  - name: Update multiple global device credentials using id
    cisco.dnac.device_credential_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - global_credential_details:
        cli_credential:
        - description: string
          username: string
          password: string
          enable_password: string
          id: string
        - description: string
          username: string
          password: string
          enable_password: string
          id: string
        snmp_v2c_read:
        - description: string
          read_community: string
          id: string
        - description: string
          read_community: string
          id: string
        snmp_v2c_write:
        - description: string
          write_community: string
          id: string
        - description: string
          write_community: string
          id: string
        snmp_v3:
        - auth_password: string
          auth_type: SHA
          snmp_mode: AUTHPRIV
          privacy_password: string
          privacy_type: AES128
          username: string
          description: string
          id: string
        - auth_password: string
          auth_type: SHA
          snmp_mode: AUTHPRIV
          privacy_password: string
          privacy_type: AES128
          username: string
          description: string
          id: string
        https_read:
        - description: string
          username: string
          password: string
          port: 443
          id: string
        - description: string
          username: string
          password: string
          port: 443
          id: string
        https_write:
        - description: string
          username: string
          password: string
          port: 443
          id: string
        - description: string
          username: string
          password: string
          port: 443
          id: string

  - name: Update global device credential name/description using old name and description.
    cisco.dnac.device_credential_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - global_credential_details:
        cli_credential:
        - description: string
          username: string
          password: string
          enable_password: string
          old_description: string
          old_username: string
        snmp_v2c_read:
        - description: string
          read_community: string
          old_description: string
        snmp_v2c_write:
        - description: string
          write_community: string
          old_description: string
        snmp_v3:
        - auth_password: string
          auth_type: string
          snmp_mode: string
          privacy_password: string
          privacy_type: string
          username: string
          description: string
        https_read:
        - description: string
          username: string
          password: string
          port: string
          old_description: string
          old_username: string
        https_write:
        - description: string
          username: string
          password: string
          port: string
          old_description: string
          old_username: string

  - name: Assign Credentials to sites using old description and username.
    cisco.dnac.device_credential_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - assign_credentials_to_site:
        cli_credential:
          description: string
          username: string
        snmp_v2c_read:
          description: string
        snmp_v2c_write:
          description: string
        snmp_v3:
          description: string
        https_read:
          description: string
          username: string
        https_write:
          description: string
          username: string
        site_name:
        - string
        - string

  - name: Sync global device credentials to a site.
    cisco.dnac.device_credential_workflow_manager:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log_level: "{{ dnac_log_level }}"
    dnac_log: True
    state: merged
    config_verify: True
    config:
      - apply_credentials_to_site:
        cli_credential:
          description: string
          username: string
        snmp_v2c_read:
          description: string
        snmp_v2c_write:
          description: string
        snmp_v3:
          description: string
        site_name:
        - string

"""

RETURN = r"""
# Case_1: Successful creation/updation/deletion of global device credentials
dnac_response1:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }

# Case_2: Successful assignment/sync of global device credentials to a site.
dnac_response2:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }

"""

import copy
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    get_dict_result,
)


class DeviceCredential(DnacBase):
    """Class containing member attributes for device_credential_workflow_manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.result["response"] = [
            {
                "globalCredential": {},
                "assignCredential": {},
                "applyCredential": {}
            }
        ]
        self.payload = module.params
        self.dnac_version = int(self.payload.get(
            "dnac_version").replace(".", ""))
        self.version_2_3_5_3, self.version_2_3_7_6 = 2353, 2376

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.
        Parameters:
            self: The instance of the class containing the 'config' attribute to be validated.
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
            self.msg = "config not available in playbook for validation"
            self.status = "success"
            return self

        # temp_spec is the specification for the expected structure of configuration parameters
        temp_spec = {
            "global_credential_details": {
                "type": 'dict',
                "cli_credential": {
                    "type": 'list',
                    "description": {"type": 'string'},
                    "username": {"type": 'string'},
                    "password": {"type": 'string'},
                    "enable_password": {"type": 'string'},
                    "old_description": {"type": 'string'},
                    "old_username": {"type": 'string'},
                    "id": {"type": 'string'},
                },
                "snmp_v2c_read": {
                    "type": 'list',
                    "description": {"type": 'string'},
                    "read_community": {"type": 'string'},
                    "old_description": {"type": 'string'},
                    "id": {"type": 'string'},
                },
                "snmp_v2c_write": {
                    "type": 'list',
                    "description": {"type": 'string'},
                    "write_community": {"type": 'string'},
                    "old_description": {"type": 'string'},
                    "id": {"type": 'string'},
                },
                "snmp_v3": {
                    "type": 'list',
                    "description": {"type": 'string'},
                    "username": {"type": 'string'},
                    "snmp_mode": {"type": 'string'},
                    "auth_type": {"type": 'string'},
                    "auth_password": {"type": 'string'},
                    "privacy_type": {"type": 'string'},
                    "privacy_password": {"type": 'string'},
                    "old_description": {"type": 'string'},
                    "id": {"type": 'string'},
                },
                "https_read": {
                    "type": 'list',
                    "description": {"type": 'string'},
                    "username": {"type": 'string'},
                    "password": {"type": 'string'},
                    "port": {"type": 'integer'},
                    "old_description": {"type": 'string'},
                    "old_username": {"type": 'string'},
                    "id": {"type": 'string'},
                },
                "https_write": {
                    "type": 'list',
                    "description": {"type": 'string'},
                    "username": {"type": 'string'},
                    "password": {"type": 'string'},
                    "port": {"type": 'integer'},
                    "old_description": {"type": 'string'},
                    "old_username": {"type": 'string'},
                    "id": {"type": 'string'},
                }
            },
            "assign_credentials_to_site": {
                "type": 'dict',
                "cli_credential": {
                    "type": 'dict',
                    "description": {"type: 'string'"},
                    "username": {"type": 'string'},
                    "id": {"type": 'string'},
                },
                "snmp_v2c_read": {
                    "type": 'dict',
                    "description": {"type: 'string'"},
                    "username": {"type": 'string'},
                    "id": {"type": 'string'},
                },
                "snmp_v2c_write": {
                    "type": 'dict',
                    "description": {"type: 'string'"},
                    "id": {"type": 'string'},
                },
                "snmp_v3": {
                    "type": 'dict',
                    "description": {"type: 'string'"},
                    "id": {"type": 'string'},
                },
                "https_read": {
                    "type": 'dict',
                    "description": {"type: 'string'"},
                    "username": {"type": 'string'},
                    "id": {"type": 'string'},
                },
                "https_write": {
                    "type": 'dict',
                    "description": {"type: 'string'"},
                    "username": {"type": 'string'},
                    "id": {"type": 'string'},
                },
                "site_name": {
                    "type": 'list',
                    "elements": 'string'
                }
            }
        }

        # Validate playbook params against the specification (temp_spec)
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format("\n".join(invalid_params))
            self.status = "failed"
            return self

        self.validated_config = valid_temp
        self.log("Successfully validated playbook config params: {0}".format(valid_temp), "INFO")
        self.msg = "Successfully validated input from the playbook"
        self.status = "success"
        return self

    def get_site_id(self, site_name):
        """
        Get the site id from the site name.
        Use check_return_status() to check for failure

        Parameters:
            site_name (str) - Site name

        Returns:
            str or None - The Site Id if found, or None if not found or error
        """

        try:
            if self.dnac_version <= self.version_2_3_5_3:
                response = self.dnac._exec(
                    family="sites",
                    function='get_site',
                    op_modifies=True,
                    params={"name": site_name},
                )
                self.log("Received API response from 'get_site': {0}".format(response), "DEBUG")
            else:
                response = self.dnac._exec(
                    family="site_design",
                    function='get_sites',
                    op_modifies=True,
                    params={"name_hierarchy": site_name},
                )
                self.log("Received API response from 'get_sites': {0}".format(response), "DEBUG")

            if not response:
                self.log("Failed to retrieve the site ID for the site name: {0}"
                         .format(site_name), "ERROR")
                return None

            response = response.get("response")
            if not response:
                self.log("The site with the name '{0}' is not valid".format(site_name), "ERROR")
                return None

            _id = response[0].get("id")
            self.log("Site ID for the site name {0}: {1}".format(site_name, _id), "INFO")
        except Exception as e:
            self.log("Exception occurred while getting site_id from the site_name: {0}"
                     .format(e), "CRITICAL")
            return None

        return _id

    def get_global_credentials_params(self):
        """
        Get the current Global Device Credentials from Cisco Catalyst Center.

        Parameters:
            self - The current object details.

        Returns:
            global_credentials (dict) - All global device credentials details.
        """

        try:
            global_credentials = self.dnac._exec(
                family="discovery",
                function='get_all_global_credentials_v2',
            )
            global_credentials = global_credentials.get("response")
            self.log("All global device credentials details: {0}"
                     .format(global_credentials), "DEBUG")
        except Exception as msg:
            self.msg = (
                "Exception occurred while getting global device credentials: {0}".format(msg)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        return global_credentials

    def get_cli_params(self, cliDetails):
        """
        Format the CLI parameters for the CLI credential configuration in Cisco Catalyst Center.

        Parameters:
            cliDetails (list of dict) - Cisco Catalyst Center details containing CLI Credentials.

        Returns:
            cliCredential (list of dict) - Processed CLI credential data
            in the format suitable for the Cisco Catalyst Center config.
        """

        cliCredential = []
        for item in cliDetails:
            if item is None:
                cliCredential.append(None)
            else:
                value = {
                    "username": item.get("username"),
                    "description": item.get("description"),
                    "id": item.get("id")
                }
                cliCredential.append(value)
        return cliCredential

    def get_snmpV2cRead_params(self, snmpV2cReadDetails):
        """
        Format the snmp_v2c_read parameters for the snmp_v2c_read
        credential configuration in Cisco Catalyst Center.

        Parameters:
            snmpV2cReadDetails (list of dict) - Cisco Catalyst Center
            Details containing snmp_v2c_read Credentials.

        Returns:
            snmpV2cRead (list of dict) - Processed snmp_v2c_read credential
            data in the format suitable for the Cisco Catalyst Center config.
        """

        snmpV2cRead = []
        for item in snmpV2cReadDetails:
            if item is None:
                snmpV2cRead.append(None)
            else:
                value = {
                    "description": item.get("description"),
                    "id": item.get("id")
                }
                snmpV2cRead.append(value)
        return snmpV2cRead

    def get_snmpV2cWrite_params(self, snmpV2cWriteDetails):
        """
        Format the snmp_v2c_write parameters for the snmp_v2c_write
        credential configuration in Cisco Catalyst Center.

        Parameters:
            snmpV2cWriteDetails (list of dict) - Cisco Catalyst Center
            Details containing snmp_v2c_write Credentials.

        Returns:
            snmpV2cWrite (list of dict) - Processed snmp_v2c_write credential
            data in the format suitable for the Cisco Catalyst Center config.
        """

        snmpV2cWrite = []
        for item in snmpV2cWriteDetails:
            if item is None:
                snmpV2cWrite.append(None)
            else:
                value = {
                    "description": item.get("description"),
                    "id": item.get("id")
                }
                snmpV2cWrite.append(value)
        return snmpV2cWrite

    def get_httpsRead_params(self, httpsReadDetails):
        """
        Format the https_read parameters for the https_read
        credential configuration in Cisco Catalyst Center.

        Parameters:
            httpsReadDetails (list of dict) - Cisco Catalyst Center
            Details containing https_read Credentials.

        Returns:
            httpsRead (list of dict) - Processed https_read credential
            data in the format suitable for the Cisco Catalyst Center config.
        """

        httpsRead = []
        for item in httpsReadDetails:
            if item is None:
                httpsRead.append(None)
            else:
                value = {
                    "description": item.get("description"),
                    "username": item.get("username"),
                    "port": item.get("port"),
                    "id": item.get("id")
                }
                httpsRead.append(value)
        return httpsRead

    def get_httpsWrite_params(self, httpsWriteDetails):
        """
        Format the https_write parameters for the https_write
        credential configuration in Cisco Catalyst Center.

        Parameters:
            httpsWriteDetails (list of dict) - Cisco Catalyst Center
            Details containing https_write Credentials.

        Returns:
            httpsWrite (list of dict) - Processed https_write credential
            data in the format suitable for the Cisco Catalyst Center config.
        """

        httpsWrite = []
        for item in httpsWriteDetails:
            if item is None:
                httpsWrite.append(None)
            else:
                value = {
                    "description": item.get("description"),
                    "username": item.get("username"),
                    "port": item.get("port"),
                    "id": item.get("id")
                }
                httpsWrite.append(value)
        return httpsWrite

    def get_snmpV3_params(self, snmpV3Details):
        """
        Format the snmp_v3 parameters for the snmp_v3 credential configuration in Cisco Catalyst Center.

        Parameters:
            snmpV3Details (list of dict) - Cisco Catalyst Center details containing snmp_v3 Credentials.

        Returns:
            snmpV3 (list of dict) - Processed snmp_v3 credential
            data in the format suitable for the Cisco Catalyst Center config.
        """

        snmpV3 = []
        for item in snmpV3Details:
            if item is None:
                snmpV3.append(None)
            else:
                value = {
                    "username": item.get("username"),
                    "description": item.get("description"),
                    "snmpMode": item.get("snmpMode"),
                    "id": item.get("id"),
                }
                if value.get("snmpMode") == "AUTHNOPRIV":
                    value["authType"] = item.get("authType")
                elif value.get("snmpMode") == "AUTHPRIV":
                    value.update({
                        "authType": item.get("authType"),
                        "privacyType": item.get("privacyType")
                    })
                snmpV3.append(value)
        return snmpV3

    def get_cli_credentials(self, CredentialDetails, global_credentials):
        """
        Get the current CLI Credential from
        Cisco Catalyst Center based on the provided playbook details.
        Check this API using the check_return_status.

        Parameters:
            CredentialDetails (dict) - Playbook details containing Global Device Credentials.
            global_credentials (dict) - All global device credentials details.

        Returns:
            cliDetails (List) - The current CLI credentials.
        """

        # playbook CLI Credential details
        all_CLI = CredentialDetails.get("cli_credential")
        # All CLI details from Cisco Catalyst Center
        cli_details = global_credentials.get("cliCredential")
        # Cisco Catalyst Center details for the CLI Credential given in the playbook
        cliDetails = []
        if all_CLI and cli_details:
            for cliCredential in all_CLI:
                cliDetail = None
                cliId = cliCredential.get("id")
                if cliId:
                    cliDetail = get_dict_result(cli_details, "id", cliId)
                    if not cliDetail:
                        self.msg = "CLI credential ID is invalid"
                        self.status = "failed"
                        return self

                cliOldDescription = cliCredential.get("old_description")
                cliOldUsername = cliCredential.get("old_username")
                if cliOldDescription and cliOldUsername and (not cliDetail):
                    for item in cli_details:
                        if item.get("description") == cliOldDescription \
                                and item.get("username") == cliOldUsername:
                            if cliDetail:
                                self.msg = "There are multiple CLI credentials with the same old_description and old_username. " + \
                                           "Kindly provide the ID for the global device credentials."
                                self.status = "failed"
                                return self
                            cliDetail = item
                    if not cliDetail:
                        self.msg = "CLI credential old_description or old_username is invalid"
                        self.status = "failed"
                        return self

                cliDescription = cliCredential.get("description")
                cliUsername = cliCredential.get("username")
                if cliDescription and cliUsername and (not cliDetail):
                    for item in cli_details:
                        if item.get("description") == cliDescription \
                                and item.get("username") == cliUsername:
                            if cliDetail:
                                self.msg = "There are multiple CLI credentials with the same description and username. " + \
                                           "Kindly provide the ID for the global device credentials."
                                self.status = "failed"
                                return self
                            cliDetail = item
                cliDetails.append(cliDetail)
        return cliDetails

    def get_snmpV2cRead_credentials(self, CredentialDetails, global_credentials):
        """
        Get the current snmp_v2c_read Credential from
        Cisco Catalyst Center based on the provided playbook details.
        Check this API using the check_return_status.

        Parameters:
            CredentialDetails (dict) - Playbook details containing Global Device Credentials.
            global_credentials (dict) - All global device credentials details.

        Returns:
            snmpV2cReadDetails (List) - The current snmp_v2c_read.
        """

        # Playbook snmp_v2c_read Credential details
        all_snmpV2cRead = CredentialDetails.get("snmp_v2c_read")

        # All snmp_v2c_read details from the Cisco Catalyst Center
        snmpV2cRead_details = global_credentials.get("snmpV2cRead")

        # Cisco Catalyst Center details for the snmp_v2c_read Credential given in the playbook
        snmpV2cReadDetails = []
        if all_snmpV2cRead and snmpV2cRead_details:
            for snmpV2cReadCredential in all_snmpV2cRead:
                snmpV2cReadDetail = None
                snmpV2cReadId = snmpV2cReadCredential.get("id")
                if snmpV2cReadId:
                    snmpV2cReadDetail = get_dict_result(snmpV2cRead_details, "id", snmpV2cReadId)
                    if not snmpV2cReadDetail:
                        self.msg = "snmp_v2c_read credential ID is invalid"
                        self.status = "failed"
                        return self

                snmpV2cReadOldDescription = snmpV2cReadCredential.get("old_description")
                if snmpV2cReadOldDescription and (not snmpV2cReadDetail):
                    snmpV2cReadDetail = get_dict_result(
                        snmpV2cRead_details,
                        "description",
                        snmpV2cReadOldDescription
                    )
                    if not snmpV2cReadDetail:
                        self.msg = "snmp_v2c_read credential old_description is invalid"
                        self.status = "failed"
                        return self

                snmpV2cReadDescription = snmpV2cReadCredential.get("description")
                if snmpV2cReadDescription and (not snmpV2cReadDetail):
                    snmpV2cReadDetail = get_dict_result(
                        snmpV2cRead_details,
                        "description",
                        snmpV2cReadDescription
                    )
                snmpV2cReadDetails.append(snmpV2cReadDetail)
        return snmpV2cReadDetails

    def get_snmpV2cWrite_credentials(self, CredentialDetails, global_credentials):
        """
        Get the current snmp_v2c_write Credential from
        Cisco Catalyst Center based on the provided playbook details.
        Check this API using the check_return_status.

        Parameters:
            CredentialDetails (dict) - Playbook details containing Global Device Credentials.
            global_credentials (dict) - All global device credentials details.

        Returns:
            snmpV2cWriteDetails (List) - The current snmp_v2c_write.
        """

        # Playbook snmp_v2c_write Credential details
        all_snmpV2cWrite = CredentialDetails.get("snmp_v2c_write")

        # All snmp_v2c_write details from the Cisco Catalyst Center
        snmpV2cWrite_details = global_credentials.get("snmpV2cWrite")

        # Cisco Catalyst Center details for the snmp_v2c_write Credential given in the playbook
        snmpV2cWriteDetails = []
        if all_snmpV2cWrite and snmpV2cWrite_details:
            for snmpV2cWriteCredential in all_snmpV2cWrite:
                snmpV2cWriteDetail = None
                snmpV2cWriteId = snmpV2cWriteCredential.get("id")
                if snmpV2cWriteId:
                    snmpV2cWriteDetail = get_dict_result(snmpV2cWrite_details, "id", snmpV2cWriteId)
                    if not snmpV2cWriteDetail:
                        self.msg = "snmp_v2c_write credential ID is invalid"
                        self.status = "failed"
                        return self

                snmpV2cWriteOldDescription = snmpV2cWriteCredential.get("old_description")
                if snmpV2cWriteOldDescription and (not snmpV2cWriteDetail):
                    snmpV2cWriteDetail = get_dict_result(
                        snmpV2cWrite_details,
                        "description",
                        snmpV2cWriteOldDescription
                    )
                    if not snmpV2cWriteDetail:
                        self.msg = "snmp_v2c_write credential old_description is invalid "
                        self.status = "failed"
                        return self

                snmpV2cWriteDescription = snmpV2cWriteCredential.get("description")
                if snmpV2cWriteDescription and (not snmpV2cWriteDetail):
                    snmpV2cWriteDetail = get_dict_result(
                        snmpV2cWrite_details,
                        "description",
                        snmpV2cWriteDescription
                    )
                snmpV2cWriteDetails.append(snmpV2cWriteDetail)
        return snmpV2cWriteDetails

    def get_httpsRead_credentials(self, CredentialDetails, global_credentials):
        """
        Get the current https_read Credential from
        Cisco Catalyst Center based on the provided playbook details.
        Check this API using the check_return_status.

        Parameters:
            CredentialDetails (dict) - Playbook details containing Global Device Credentials.
            global_credentials (dict) - All global device credentials details.

        Returns:
            httpsReadDetails (List) - The current https_read.
        """

        # Playbook https_read Credential details
        all_httpsRead = CredentialDetails.get("https_read")

        # All https_read details from the Cisco Catalyst Center
        httpsRead_details = global_credentials.get("httpsRead")

        # Cisco Catalyst Center details for the https_read Credential given in the playbook
        httpsReadDetails = []
        if all_httpsRead and httpsRead_details:
            for httpsReadCredential in all_httpsRead:
                httpsReadDetail = None
                httpsReadId = httpsReadCredential.get("id")
                if httpsReadId:
                    httpsReadDetail = get_dict_result(httpsRead_details, "id", httpsReadId)
                    if not httpsReadDetail:
                        self.msg = "https_read credential Id is invalid"
                        self.status = "failed"
                        return self

                httpsReadOldDescription = httpsReadCredential.get("old_description")
                httpsReadOldUsername = httpsReadCredential.get("old_username")
                if httpsReadOldDescription and httpsReadOldUsername and (not httpsReadDetail):
                    for item in httpsRead_details:
                        if item.get("description") == httpsReadOldDescription \
                                and item.get("username") == httpsReadOldUsername:
                            if httpsReadDetail:
                                self.msg = "There are multiple https_read credentials with the same old_description and old_username. " + \
                                           "Kindly provide the ID for the global device credentials."
                                self.status = "failed"
                                return self
                            httpsReadDetail = item
                    if not httpsReadDetail:
                        self.msg = "https_read credential old_description or old_username is invalid"
                        self.status = "failed"
                        return self

                httpsReadDescription = httpsReadCredential.get("description")
                httpsReadUsername = httpsReadCredential.get("username")
                if httpsReadDescription and httpsReadUsername and (not httpsReadDetail):
                    for item in httpsRead_details:
                        if item.get("description") == httpsReadDescription \
                                and item.get("username") == httpsReadUsername:
                            if httpsReadDetail:
                                self.msg = "There are multiple https_read credentials with the same description and username. " + \
                                           "Kindly provide the ID for the global device credentials."
                                self.status = "failed"
                                return self
                            httpsReadDetail = item
                httpsReadDetails.append(httpsReadDetail)
        return httpsReadDetails

    def get_httpsWrite_credentials(self, CredentialDetails, global_credentials):
        """
        Get the current https_write Credential from
        Cisco Catalyst Center based on the provided playbook details.
        Check this API using the check_return_status.

        Parameters:
            CredentialDetails (dict) - Playbook details containing Global Device Credentials.
            global_credentials (dict) - All global device credentials details.

        Returns:
            httpsWriteDetails (List) - The current https_write.
        """

        # Playbook https_write Credential details
        all_httpsWrite = CredentialDetails.get("https_write")

        # All https_write details from the Cisco Catalyst Center
        httpsWrite_details = global_credentials.get("httpsWrite")

        # Cisco Catalyst Center details for the https_write Credential given in the playbook
        httpsWriteDetails = []
        if all_httpsWrite and httpsWrite_details:
            for httpsWriteCredential in all_httpsWrite:
                httpsWriteDetail = None
                httpsWriteId = httpsWriteCredential.get("id")
                if httpsWriteId:
                    httpsWriteDetail = get_dict_result(httpsWrite_details, "id", httpsWriteId)
                    if not httpsWriteDetail:
                        self.msg = "https_write credential Id is invalid"
                        self.status = "failed"
                        return self

                httpsWriteOldDescription = httpsWriteCredential.get("old_description")
                httpsWriteOldUsername = httpsWriteCredential.get("old_username")
                if httpsWriteOldDescription and httpsWriteOldUsername and (not httpsWriteDetail):
                    for item in httpsWrite_details:
                        if item.get("description") == httpsWriteOldDescription \
                                and item.get("username") == httpsWriteOldUsername:
                            if httpsWriteDetail:
                                self.msg = "There are multiple https_write credentials with the same old_description and old_username. " + \
                                           "Kindly provide the ID for the global device credentials."
                                self.status = "failed"
                                return self
                            httpsWriteDetail = item
                    if not httpsWriteDetail:
                        self.msg = "https_write credential old_description or " + \
                                   "old_username is invalid"
                        self.status = "failed"
                        return self

                httpsWriteDescription = httpsWriteCredential.get("description")
                httpsWriteUsername = httpsWriteCredential.get("username")
                if httpsWriteDescription and httpsWriteUsername and (not httpsWriteDetail):
                    for item in httpsWrite_details:
                        if item.get("description") == httpsWriteDescription \
                                and item.get("username") == httpsWriteUsername:
                            if httpsWriteDetail:
                                self.msg = "There are multiple https_write credentials with the same description and username. " + \
                                           "Kindly provide the ID for the global device credentials."
                                self.status = "failed"
                                return self
                            httpsWriteDetail = item
                httpsWriteDetails.append(httpsWriteDetail)
        return httpsWriteDetails

    def get_snmpV3_credentials(self, CredentialDetails, global_credentials):
        """
        Get the current snmp_v3 Credential from
        Cisco Catalyst Center based on the provided playbook details.
        Check this API using the check_return_status.

        Parameters:
            CredentialDetails (dict) - Playbook details containing Global Device Credentials.
            global_credentials (dict) - All global device credentials details.

        Returns:
            snmpV3Details (List) - The current snmp_v3.
        """

        # Playbook snmp_v3 Credential details
        all_snmpV3 = CredentialDetails.get("snmp_v3")

        # All snmp_v3 details from the Cisco Catalyst Center
        snmpV3_details = global_credentials.get("snmpV3")

        # Cisco Catalyst Center details for the snmp_v3 Credential given in the playbook
        snmpV3Details = []
        if all_snmpV3 and snmpV3_details:
            for snmpV3Credential in all_snmpV3:
                snmpV3Detail = None
                snmpV3Id = snmpV3Credential.get("id")
                if snmpV3Id:
                    snmpV3Detail = get_dict_result(snmpV3_details, "id", snmpV3Id)
                    if not snmpV3Detail:
                        self.msg = "snmp_v3 credential id is invalid"
                        self.status = "failed"
                        return self

                snmpV3OldDescription = snmpV3Credential.get("old_description")
                if snmpV3OldDescription and (not snmpV3Detail):
                    snmpV3Detail = get_dict_result(snmpV3_details, "description", snmpV3OldDescription)
                    if not snmpV3Detail:
                        self.msg = "snmp_v3 credential old_description is invalid"
                        self.status = "failed"
                        return self

                snmpV3Description = snmpV3Credential.get("description")
                if snmpV3Description and (not snmpV3Detail):
                    snmpV3Detail = get_dict_result(
                        snmpV3_details, "description", snmpV3Description)
                snmpV3Details.append(snmpV3Detail)
        return snmpV3Details

    def get_have_device_credentials(self, CredentialDetails):
        """
        Get the current Global Device Credentials from
        Cisco Catalyst Center based on the provided playbook details.
        Check this API using the check_return_status.

        Parameters:
            CredentialDetails (dict) - Playbook details containing Global Device Credentials.

        Returns:
            self - The current object with updated information.
        """

        global_credentials = self.get_global_credentials_params()
        cliDetails = self.get_cli_credentials(CredentialDetails, global_credentials)
        snmpV2cReadDetails = self.get_snmpV2cRead_credentials(CredentialDetails, global_credentials)
        snmpV2cWriteDetails = self.get_snmpV2cWrite_credentials(CredentialDetails,
                                                                global_credentials)
        httpsReadDetails = self.get_httpsRead_credentials(CredentialDetails, global_credentials)
        httpsWriteDetails = self.get_httpsWrite_credentials(CredentialDetails, global_credentials)
        snmpV3Details = self.get_snmpV3_credentials(CredentialDetails, global_credentials)
        self.have.update({"globalCredential": {}})
        if cliDetails:
            cliCredential = self.get_cli_params(cliDetails)
            self.have.get("globalCredential").update({"cliCredential": cliCredential})
        if snmpV2cReadDetails:
            snmpV2cRead = self.get_snmpV2cRead_params(snmpV2cReadDetails)
            self.have.get("globalCredential").update({"snmpV2cRead": snmpV2cRead})
        if snmpV2cWriteDetails:
            snmpV2cWrite = self.get_snmpV2cWrite_params(snmpV2cWriteDetails)
            self.have.get("globalCredential").update({"snmpV2cWrite": snmpV2cWrite})
        if httpsReadDetails:
            httpsRead = self.get_httpsRead_params(httpsReadDetails)
            self.have.get("globalCredential").update({"httpsRead": httpsRead})
        if httpsWriteDetails:
            httpsWrite = self.get_httpsWrite_params(httpsWriteDetails)
            self.have.get("globalCredential").update({"httpsWrite": httpsWrite})
        if snmpV3Details:
            snmpV3 = self.get_snmpV3_params(snmpV3Details)
            self.have.get("globalCredential").update({"snmpV3": snmpV3})

        self.log("Global device credential details: {0}"
                 .format(self.have.get("globalCredential")), "DEBUG")
        self.msg = "Collected the Global Device Credential Details from the Cisco Catalyst Center"
        self.status = "success"
        return self

    def get_have(self, config):
        """
        Get the current Global Device Credentials and
        Device Credentials assigned to a site in Cisco Catalyst Center.

        Parameters:
            config (dict) - Playbook details containing Global Device
            Credentials configurations and Device Credentials should
            be assigned to a site.

        Returns:
            self - The current object with updated information of Global
            Device Credentials and Device Credentials assigned to a site.
        """

        if config.get("global_credential_details") is not None:
            CredentialDetails = config.get("global_credential_details")
            self.get_have_device_credentials(CredentialDetails).check_return_status()

        self.log("Current State (have): {0}".format(self.have), "INFO")
        self.msg = "Successfully retrieved the details from the Cisco Catalyst Center"
        self.status = "success"
        return self

    def get_want_device_credentials(self, CredentialDetails):
        """
        Get the Global Device Credentials from the playbook.
        Check this API using the check_return_status.

        Parameters:
            CredentialDetails (dict) - Playbook details containing Global Device Credentials.

        Returns:
            self - The current object with updated information of
            Global Device Credentials from the playbook.
        """

        want = {
            "want_create": {},
            "want_update": {}
        }
        if CredentialDetails.get("cli_credential"):
            cli = CredentialDetails.get("cli_credential")
            have_cli_ptr = 0
            create_cli_ptr = 0
            update_cli_ptr = 0
            values = ["password", "description", "username", "id"]
            have_cliCredential = self.have.get("globalCredential").get("cliCredential")
            for item in cli:
                if not have_cliCredential or have_cliCredential[have_cli_ptr] is None:
                    if want.get("want_create").get("cliCredential") is None:
                        want.get("want_create").update({"cliCredential": []})
                    create_credential = want.get("want_create").get("cliCredential")
                    create_credential.append({})
                    for i in range(0, 3):
                        if item.get(values[i]):
                            create_credential[create_cli_ptr] \
                                .update({values[i]: item.get(values[i])})
                        else:
                            self.msg = values[i] + " is mandatory for creating cli_credential " + str(
                                have_cli_ptr)
                            self.status = "failed"
                            return self

                    if item.get("enable_password"):
                        create_credential[create_cli_ptr] \
                            .update({"enablePassword": item.get("enable_password")})
                    create_cli_ptr = create_cli_ptr + 1
                else:
                    if want.get("want_update").get("cliCredential") is None:
                        want.get("want_update").update({"cliCredential": []})
                    update_credential = want.get(
                        "want_update").get("cliCredential")
                    update_credential.append({})
                    if item.get("password"):
                        update_credential[update_cli_ptr] \
                            .update({"password": item.get("password")})
                    else:
                        self.msg = "password is mandatory for updating cli_credential " + str(have_cli_ptr)
                        self.status = "failed"
                        return self

                    for i in range(1, 4):
                        if item.get(values[i]):
                            update_credential[update_cli_ptr] \
                                .update({values[i]: item.get(values[i])})
                        else:
                            update_credential[update_cli_ptr].update({
                                values[i]: self.have.get("globalCredential")
                                .get("cliCredential")[have_cli_ptr].get(values[i])
                            })

                    if item.get("enable_password"):
                        update_credential[update_cli_ptr].update({
                            "enablePassword": item.get("enable_password")
                        })
                    update_cli_ptr = update_cli_ptr + 1
                have_cli_ptr = have_cli_ptr + 1

        if CredentialDetails.get("snmp_v2c_read"):
            snmpV2cRead = CredentialDetails.get("snmp_v2c_read")
            have_snmpv2cread_ptr = 0
            create_snmpv2cread_ptr = 0
            update_snmpv2cread_ptr = 0
            values = ["read_community", "description", "id"]
            keys = ["readCommunity", "description", "id"]
            have_snmpV2cRead = self.have.get("globalCredential").get("snmpV2cRead")
            for item in snmpV2cRead:
                if not have_snmpV2cRead or have_snmpV2cRead[have_snmpv2cread_ptr] is None:
                    if want.get("want_create").get("snmpV2cRead") is None:
                        want.get("want_create").update({"snmpV2cRead": []})
                    create_credential = want.get("want_create").get("snmpV2cRead")
                    create_credential.append({})
                    for i in range(0, 2):
                        if item.get(values[i]):
                            create_credential[create_snmpv2cread_ptr] \
                                .update({keys[i]: item.get(values[i])})
                        else:
                            self.msg = values[i] + " is mandatory for creating snmp_v2c_read " + str(have_snmpv2cread_ptr)
                            self.status = "failed"
                            return self
                    create_snmpv2cread_ptr = create_snmpv2cread_ptr + 1
                else:
                    if want.get("want_update").get("snmpV2cRead") is None:
                        want.get("want_update").update({"snmpV2cRead": []})
                    update_credential = want.get("want_update").get("snmpV2cRead")
                    update_credential.append({})
                    if item.get("read_community"):
                        update_credential[update_snmpv2cread_ptr] \
                            .update({"readCommunity": item.get("read_community")})
                    else:
                        self.msg = "read_community is mandatory for updating snmp_v2c_read " + str(have_snmpv2cread_ptr)
                        self.status = "failed"
                        return self
                    for i in range(1, 3):
                        if item.get(values[i]):
                            update_credential[update_snmpv2cread_ptr] \
                                .update({values[i]: item.get(values[i])})
                        else:
                            update_credential[update_snmpv2cread_ptr].update({
                                values[i]: self.have.get("globalCredential")
                                .get("snmpV2cRead")[have_snmpv2cread_ptr].get(values[i])
                            })
                    update_snmpv2cread_ptr = update_snmpv2cread_ptr + 1
                have_snmpv2cread_ptr = have_snmpv2cread_ptr + 1

        if CredentialDetails.get("snmp_v2c_write"):
            snmpV2cWrite = CredentialDetails.get("snmp_v2c_write")
            have_snmpv2cwrite_ptr = 0
            create_snmpv2cwrite_ptr = 0
            update_snmpv2cwrite_ptr = 0
            values = ["write_community", "description", "id"]
            keys = ["writeCommunity", "description", "id"]
            have_snmpV2cWrite = self.have.get("globalCredential").get("snmpV2cWrite")
            for item in snmpV2cWrite:
                if not have_snmpV2cWrite or have_snmpV2cWrite[have_snmpv2cwrite_ptr] is None:
                    if want.get("want_create").get("snmpV2cWrite") is None:
                        want.get("want_create").update({"snmpV2cWrite": []})
                    create_credential = want.get(
                        "want_create").get("snmpV2cWrite")
                    create_credential.append({})
                    for i in range(0, 2):
                        if item.get(values[i]):
                            create_credential[create_snmpv2cwrite_ptr] \
                                .update({keys[i]: item.get(values[i])})
                        else:
                            self.msg = values[i] + " is mandatory for creating snmp_v2c_write " + str(have_snmpv2cwrite_ptr)
                            self.status = "failed"
                            return self
                    create_snmpv2cwrite_ptr = create_snmpv2cwrite_ptr + 1
                else:
                    if want.get("want_update").get("snmpV2cWrite") is None:
                        want.get("want_update").update({"snmpV2cWrite": []})
                    update_credential = want.get("want_update").get("snmpV2cWrite")
                    update_credential.append({})
                    if item.get("write_community"):
                        update_credential[update_snmpv2cwrite_ptr] \
                            .update({"writeCommunity": item.get("write_community")})
                    else:
                        self.msg = "write_community is mandatory for updating snmp_v2c_write " + str(have_snmpv2cwrite_ptr)
                        self.status = "failed"
                        return self
                    for i in range(1, 3):
                        if item.get(values[i]):
                            update_credential[update_snmpv2cwrite_ptr] \
                                .update({values[i]: item.get(values[i])})
                        else:
                            update_credential[update_snmpv2cwrite_ptr].update({
                                values[i]: self.have.get("globalCredential")
                                .get("snmpV2cWrite")[have_snmpv2cwrite_ptr].get(values[i])
                            })
                    update_snmpv2cwrite_ptr = update_snmpv2cwrite_ptr + 1
                have_snmpv2cwrite_ptr = have_snmpv2cwrite_ptr + 1

        if CredentialDetails.get("https_read"):
            httpsRead = CredentialDetails.get("https_read")
            have_httpsread_ptr = 0
            create_httpsread_ptr = 0
            update_httpsread_ptr = 0
            values = ["password", "description", "username", "id", "port"]
            have_httpsRead = self.have.get("globalCredential").get("httpsRead")
            for item in httpsRead:
                self.log("Global credentials details: {0}"
                         .format(self.have.get("globalCredential")), "DEBUG")
                if not have_httpsRead or have_httpsRead[have_httpsread_ptr] is None:
                    if want.get("want_create").get("httpsRead") is None:
                        want.get("want_create").update({"httpsRead": []})
                    create_credential = want.get("want_create").get("httpsRead")
                    create_credential.append({})
                    for i in range(0, 3):
                        if item.get(values[i]):
                            create_credential[create_httpsread_ptr] \
                                .update({values[i]: item.get(values[i])})
                        else:
                            self.msg = values[i] + " is mandatory for creating https_read " + str(have_httpsread_ptr)
                            self.status = "failed"
                            return self
                    if item.get("port"):
                        create_credential[create_httpsread_ptr] \
                            .update({"port": item.get("port")})
                    else:
                        create_credential[create_httpsread_ptr] \
                            .update({"port": "443"})
                    create_httpsread_ptr = create_httpsread_ptr + 1
                else:
                    if want.get("want_update").get("httpsRead") is None:
                        want.get("want_update").update({"httpsRead": []})
                    update_credential = want.get("want_update").get("httpsRead")
                    update_credential.append({})
                    if item.get("password"):
                        update_credential[update_httpsread_ptr] \
                            .update({"password": item.get("password")})
                    else:
                        self.msg = "The password is mandatory for updating https_read " + str(have_httpsread_ptr)
                        self.status = "failed"
                        return self
                    for i in range(1, 5):
                        if item.get(values[i]):
                            update_credential[update_httpsread_ptr] \
                                .update({values[i]: item.get(values[i])})
                        else:
                            update_credential[update_httpsread_ptr].update({
                                values[i]: self.have.get("globalCredential")
                                .get("httpsRead")[have_httpsread_ptr].get(values[i])
                            })
                    update_httpsread_ptr = update_httpsread_ptr + 1
                have_httpsread_ptr = have_httpsread_ptr + 1

        if CredentialDetails.get("https_write"):
            httpsWrite = CredentialDetails.get("https_write")
            have_httpswrite_ptr = 0
            create_httpswrite_ptr = 0
            update_httpswrite_ptr = 0
            values = ["password", "description", "username", "id", "port"]
            have_httpsWrite = self.have.get("globalCredential").get("httpsWrite")
            for item in httpsWrite:
                if not have_httpsWrite or have_httpsWrite[have_httpswrite_ptr] is None:
                    if want.get("want_create").get("httpsWrite") is None:
                        want.get("want_create").update({"httpsWrite": []})
                    create_credential = want.get("want_create").get("httpsWrite")
                    create_credential.append({})
                    for i in range(0, 3):
                        if item.get(values[i]):
                            create_credential[create_httpswrite_ptr] \
                                .update({values[i]: item.get(values[i])})
                        else:
                            self.msg = values[i] + " is mandatory for creating https_write " + str(have_httpswrite_ptr)
                            self.status = "failed"
                            return self
                    if item.get("port"):
                        create_credential[create_httpswrite_ptr] \
                            .update({"port": item.get("port")})
                    else:
                        create_credential[create_httpswrite_ptr] \
                            .update({"port": "443"})
                    create_httpswrite_ptr = create_httpswrite_ptr + 1
                else:
                    if want.get("want_update").get("httpsWrite") is None:
                        want.get("want_update").update({"httpsWrite": []})
                    update_credential = want.get(
                        "want_update").get("httpsWrite")
                    update_credential.append({})
                    if item.get("password"):
                        update_credential[update_httpswrite_ptr] \
                            .update({"password": item.get("password")})
                    else:
                        self.msg = "The password is mandatory for updating https_write " + str(have_httpswrite_ptr)
                        self.status = "failed"
                        return self
                    for i in range(1, 5):
                        if item.get(values[i]):
                            update_credential[update_httpswrite_ptr] \
                                .update({values[i]: item.get(values[i])})
                        else:
                            update_credential[update_httpswrite_ptr].update({
                                values[i]: self.have.get("globalCredential")
                                .get("httpsWrite")[have_httpswrite_ptr].get(values[i])
                            })
                    update_httpswrite_ptr = update_httpswrite_ptr + 1
                have_httpswrite_ptr = have_httpswrite_ptr + 1

        if CredentialDetails.get("snmp_v3"):
            snmpV3 = CredentialDetails.get("snmp_v3")
            have_snmpv3_ptr = 0
            create_snmpv3_ptr = 0
            update_snmpv3_ptr = 0
            values = ["description", "username", "id"]
            have_snmpV3 = self.have.get("globalCredential").get("snmpV3")
            for item in snmpV3:
                if not have_snmpV3 or have_snmpV3[have_snmpv3_ptr] is None:
                    if want.get("want_create").get("snmpV3") is None:
                        want.get("want_create").update({"snmpV3": []})
                    create_credential = want.get("want_create").get("snmpV3")
                    create_credential.append({})
                    for i in range(0, 2):
                        if item.get(values[i]):
                            create_credential[create_snmpv3_ptr] \
                                .update({values[i]: item.get(values[i])})
                        else:
                            self.msg = values[i] + " is mandatory for creating snmp_v3 " + str(have_snmpv3_ptr)
                            self.status = "failed"
                            return self
                    if item.get("snmp_mode"):
                        create_credential[create_snmpv3_ptr] \
                            .update({"snmpMode": item.get("snmp_mode")})
                    else:
                        create_credential[create_snmpv3_ptr] \
                            .update({"snmpMode": "AUTHPRIV"})
                    if create_credential[create_snmpv3_ptr].get("snmpMode") == "AUTHNOPRIV" or \
                            create_credential[create_snmpv3_ptr].get("snmpMode") == "AUTHPRIV":
                        auths = ["auth_password", "auth_type"]
                        keys = {
                            "auth_password": "authPassword",
                            "auth_type": "authType"
                        }
                        for auth in auths:
                            if item.get(auth):
                                create_credential[create_snmpv3_ptr] \
                                    .update({keys[auth]: item.get(auth)})
                            else:
                                self.msg = auth + " is mandatory for creating snmp_v3 " + str(have_snmpv3_ptr)
                                self.status = "failed"
                                return self
                        if len(item.get("auth_password")) < 8:
                            self.msg = "auth_password length should be greater than 8"
                            self.status = "failed"
                            return self
                        self.log("snmp_mode: {0}".format(create_credential[create_snmpv3_ptr]
                                 .get("snmpMode")), "DEBUG")
                    if create_credential[create_snmpv3_ptr].get("snmpMode") == "AUTHPRIV":
                        privs = ["privacy_password", "privacy_type"]
                        key = {
                            "privacy_password": "privacyPassword",
                            "privacy_type": "privacyType"
                        }
                        for priv in privs:
                            if item.get(priv):
                                create_credential[create_snmpv3_ptr] \
                                    .update({key[priv]: item.get(priv)})
                            else:
                                self.msg = priv + " is mandatory for creating snmp_v3 " + str(have_snmpv3_ptr)
                                self.status = "failed"
                                return self
                        if len(item.get("privacy_password")) < 8:
                            self.msg = "privacy_password should be greater than 8"
                            self.status = "failed"
                            return self
                    elif create_credential[create_snmpv3_ptr].get("snmpMode") != "NOAUTHNOPRIV":
                        self.msg = "snmp_mode in snmpV3 is not ['AUTHPRIV', 'AUTHNOPRIV', 'NOAUTHNOPRIV']"
                        self.status = "failed"
                        return self
                    create_snmpv3_ptr = create_snmpv3_ptr + 1
                else:
                    if want.get("want_update").get("snmpV3") is None:
                        want.get("want_update").update({"snmpV3": []})
                    update_credential = want.get("want_update").get("snmpV3")
                    update_credential.append({})
                    for value in values:
                        if item.get(value):
                            update_credential[update_snmpv3_ptr] \
                                .update({value: item.get(value)})
                        else:
                            update_credential[update_snmpv3_ptr].update({
                                value: self.have.get("globalCredential")
                                .get("snmpV3")[have_snmpv3_ptr].get(value)
                            })
                    if item.get("snmp_mode"):
                        update_credential[update_snmpv3_ptr] \
                            .update({"snmpMode": item.get("snmp_mode")})
                    if update_credential[update_snmpv3_ptr].get("snmpMode") == "AUTHNOPRIV" or \
                            update_credential[update_snmpv3_ptr].get("snmpMode") == "AUTHPRIV":
                        if item.get("auth_type"):
                            update_credential[update_snmpv3_ptr] \
                                .update({"authType": item.get("auth_type")})
                        elif self.have.get("globalCredential") \
                                .get("snmpMode")[have_snmpv3_ptr].get("authType"):
                            update_credential[update_snmpv3_ptr].update({
                                "authType": self.have.get("globalCredential")
                                .get("snmpMode")[have_snmpv3_ptr].get("authType")
                            })
                        else:
                            self.msg = "auth_type is required for updating snmp_v3 " + \
                                       str(have_snmpv3_ptr)
                            self.status = "failed"
                            return self
                        if item.get("auth_password"):
                            update_credential[update_snmpv3_ptr] \
                                .update({"authPassword": item.get("auth_password")})
                        else:
                            self.msg = "auth_password is required for updating snmp_v3 " + \
                                       str(have_snmpv3_ptr)
                            self.status = "failed"
                            return self
                        if len(item.get("auth_password")) < 8:
                            self.msg = "auth_password length should be greater than 8"
                            self.status = "failed"
                            return self
                    elif update_credential[update_snmpv3_ptr].get("snmpMode") == "AUTHPRIV":
                        if item.get("privacy_type"):
                            update_credential[update_snmpv3_ptr] \
                                .update({"privacyType": item.get("privacy_type")})
                        elif self.have.get("globalCredential") \
                                .get("snmpMode")[have_snmpv3_ptr].get("privacyType"):
                            update_credential[update_snmpv3_ptr].update({
                                "privacyType": self.have.get("globalCredential")
                                .get("snmpMode")[have_snmpv3_ptr].get("privacyType")
                            })
                        else:
                            self.msg = "privacy_type is required for updating snmp_v3 " + \
                                       str(have_snmpv3_ptr)
                            self.status = "failed"
                            return self
                        if item.get("privacy_password"):
                            update_credential[update_snmpv3_ptr] \
                                .update({"privacyPassword": item.get("privacy_password")})
                        else:
                            self.msg = "privacy_password is required for updating snmp_v3 " + \
                                       str(have_snmpv3_ptr)
                            self.status = "failed"
                            return self
                        if len(item.get("privacy_password")) < 8:
                            self.msg = "privacy_password length should be greater than 8"
                            self.status = "failed"
                            return self
                    update_snmpv3_ptr = update_snmpv3_ptr + 1
                have_snmpv3_ptr = have_snmpv3_ptr + 1
        self.want.update(want)
        self.msg = "Collected the Global Credentials from the Cisco Catalyst Center"
        self.status = "success"
        return self

    def get_want_assign_credentials(self, AssignCredentials):
        """
        Get the Credentials to be assigned to a site from the playbook.
        Check this API using the check_return_status.

        Parameters:
            AssignCredentials (dict) - Playbook details containing
            credentials that need to be assigned to a site.

        Returns:
            self - The current object with updated information of credentials
            that need to be assigned to a site from the playbook.
        """
        want = {
            "assign_credentials": {}
        }
        site_names = AssignCredentials.get("site_name")
        if not site_names:
            self.msg = "The 'site_name' is required parameter for 'assign_credentials_to_site'"
            self.status = "failed"
            return self

        site_ids = []
        for site_name in site_names:
            current_site_id = self.get_site_id(site_name)
            if not current_site_id:
                self.msg = "The site_name '{0}' is invalid in 'assign_credentials_to_site'".format(site_name)
                self.status = "failed"
                return self
            site_ids.append(current_site_id)

        want.update({"site_id": site_ids})
        global_credentials = self.get_global_credentials_params()
        cli_credential = AssignCredentials.get("cli_credential")
        if cli_credential:
            cliId = cli_credential.get("id")
            cliDescription = cli_credential.get("description")
            cliUsername = cli_credential.get("username")

            if cliId or cliDescription and cliUsername:
                # All CLI details from the Cisco Catalyst Center
                cli_details = global_credentials.get("cliCredential")
                if not cli_details:
                    self.msg = "Global CLI credential is not available"
                    self.status = "failed"
                    return self
                cliDetail = None
                if cliId:
                    cliDetail = get_dict_result(cli_details, "id", cliId)
                    if not cliDetail:
                        self.msg = "The ID for the CLI credential is not valid."
                        self.status = "failed"
                        return self
                elif cliDescription and cliUsername:
                    for item in cli_details:
                        if item.get("description") == cliDescription and \
                                item.get("username") == cliUsername:
                            cliDetail = item
                    if not cliDetail:
                        self.msg = "The username and description of the CLI credential are invalid"
                        self.status = "failed"
                        return self
                if self.dnac_version <= self.version_2_3_5_3:
                    want.get("assign_credentials").update({"cliId": cliDetail.get("id")})
                else:
                    want.get("assign_credentials").update({
                        "cliCredentialsId": {"credentialsId": cliDetail.get("id")}
                    })

        snmp_v2c_read = AssignCredentials.get("snmp_v2c_read")
        if snmp_v2c_read:
            snmpV2cReadId = snmp_v2c_read.get("id")
            snmpV2cReadDescription = snmp_v2c_read.get("description")
            if snmpV2cReadId or snmpV2cReadDescription:

                # All snmp_v2c_read details from the Cisco Catalyst Center
                snmpV2cRead_details = global_credentials.get("snmpV2cRead")
                if not snmpV2cRead_details:
                    self.msg = "Global snmp_v2c_read credential is not available"
                    self.status = "failed"
                    return self
                snmpV2cReadDetail = None
                if snmpV2cReadId:
                    snmpV2cReadDetail = get_dict_result(snmpV2cRead_details, "id", snmpV2cReadId)
                    if not snmpV2cReadDetail:
                        self.msg = "The ID of the snmp_v2c_read credential is not valid."
                        self.status = "failed"
                        return self
                elif snmpV2cReadDescription:
                    for item in snmpV2cRead_details:
                        if item.get("description") == snmpV2cReadDescription:
                            snmpV2cReadDetail = item
                    if not snmpV2cReadDetail:
                        self.msg = "The username and description for the snmp_v2c_read credential are invalid."
                        self.status = "failed"
                        return self
                if self.dnac_version <= self.version_2_3_5_3:
                    want.get("assign_credentials").update({"snmpV2ReadId": snmpV2cReadDetail.get("id")})
                else:
                    want.get("assign_credentials").update({
                        "snmpv2cReadCredentialsId": {"credentialsId": snmpV2cReadDetail.get("id")}
                    })

        snmp_v2c_write = AssignCredentials.get("snmp_v2c_write")
        if snmp_v2c_write:
            snmpV2cWriteId = snmp_v2c_write.get("id")
            snmpV2cWriteDescription = snmp_v2c_write.get("description")
            if snmpV2cWriteId or snmpV2cWriteDescription:

                # All snmp_v2c_write details from the Cisco Catalyst Center
                snmpV2cWrite_details = global_credentials.get("snmpV2cWrite")
                if not snmpV2cWrite_details:
                    self.msg = "Global snmp_v2c_write Credential is not available"
                    self.status = "failed"
                    return self
                snmpV2cWriteDetail = None
                if snmpV2cWriteId:
                    snmpV2cWriteDetail = get_dict_result(snmpV2cWrite_details, "id", snmpV2cWriteId)
                    if not snmpV2cWriteDetail:
                        self.msg = "The ID of the snmp_v2c_write credential is invalid."
                        self.status = "failed"
                        return self
                elif snmpV2cWriteDescription:
                    for item in snmpV2cWrite_details:
                        if item.get("description") == snmpV2cWriteDescription:
                            snmpV2cWriteDetail = item
                    if not snmpV2cWriteDetail:
                        self.msg = "The username and description of the snmp_v2c_write credential are invalid."
                        self.status = "failed"
                        return self
                if self.dnac_version <= self.version_2_3_5_3:
                    want.get("assign_credentials").update({"snmpV2WriteId": snmpV2cWriteDetail.get("id")})
                else:
                    want.get("assign_credentials").update({
                        "snmpv2cWriteCredentialsId": {"credentialsId": snmpV2cWriteDetail.get("id")}
                    })

        https_read = AssignCredentials.get("https_read")
        if https_read:
            httpReadId = https_read.get("id")
            httpReadDescription = https_read.get("description")
            httpReadUsername = https_read.get("username")
            if httpReadId or httpReadDescription and httpReadUsername:

                # All httpRead details from the Cisco Catalyst Center
                httpRead_details = global_credentials.get("httpsRead")
                if not httpRead_details:
                    self.msg = "Global httpRead Credential is not available."
                    self.status = "failed"
                    return self
                httpReadDetail = None
                if httpReadId:
                    httpReadDetail = get_dict_result(httpRead_details, "id", httpReadId)
                    if not httpReadDetail:
                        self.msg = "The ID of the httpRead credential is not valid."
                        self.status = "failed"
                        return self
                elif httpReadDescription and httpReadUsername:
                    for item in httpRead_details:
                        if item.get("description") == httpReadDescription and \
                                item.get("username") == httpReadUsername:
                            httpReadDetail = item
                    if not httpReadDetail:
                        self.msg = "The description and username for the httpRead credential are invalid."
                        self.status = "failed"
                        return self
                if self.dnac_version <= self.version_2_3_5_3:
                    want.get("assign_credentials").update({"httpRead": httpReadDetail.get("id")})
                else:
                    want.get("assign_credentials").update({
                        "httpReadCredentialsId": {"credentialsId": httpReadDetail.get("id")}
                    })

        https_write = AssignCredentials.get("https_write")
        if https_write:
            httpWriteId = https_write.get("id")
            httpWriteDescription = https_write.get("description")
            httpWriteUsername = https_write.get("username")
            if httpWriteId or httpWriteDescription and httpWriteUsername:

                # All httpWrite details from the Cisco Catalyst Center
                httpWrite_details = global_credentials.get("httpsWrite")
                if not httpWrite_details:
                    self.msg = "Global httpWrite credential is not available."
                    self.status = "failed"
                    return self
                httpWriteDetail = None
                if httpWriteId:
                    httpWriteDetail = get_dict_result(httpWrite_details, "id", httpWriteId)
                    if not httpWriteDetail:
                        self.msg = "The ID of the httpWrite credential is not valid."
                        self.status = "failed"
                        return self
                elif httpWriteDescription and httpWriteUsername:
                    for item in httpWrite_details:
                        if item.get("description") == httpWriteDescription and \
                                item.get("username") == httpWriteUsername:
                            httpWriteDetail = item
                    if not httpWriteDetail:
                        self.msg = "The description and username for the httpWrite credential are invalid."
                        self.status = "failed"
                        return self
                if self.dnac_version <= self.version_2_3_5_3:
                    want.get("assign_credentials").update({"httpWrite": httpWriteDetail.get("id")})
                else:
                    want.get("assign_credentials").update({
                        "httpWriteCredentialsId": {"credentialsId": httpWriteDetail.get("id")}
                    })

        snmp_v3 = AssignCredentials.get("snmp_v3")
        if snmp_v3:
            snmpV3Id = snmp_v3.get("id")
            snmpV3Description = snmp_v3.get("description")
            if snmpV3Id or snmpV3Description:

                # All snmp_v3 details from the Cisco Catalyst Center
                snmpV3_details = global_credentials.get("snmpV3")
                if not snmpV3_details:
                    self.msg = "Global snmp_v3 Credential is not available."
                    self.status = "failed"
                    return self
                snmpV3Detail = None
                if snmpV3Id:
                    snmpV3Detail = get_dict_result(snmpV3_details, "id", snmpV3Id)
                    if not snmpV3Detail:
                        self.msg = "The ID of the snmp_v3 credential is not valid."
                        self.status = "failed"
                        return self
                elif snmpV3Description:
                    for item in snmpV3_details:
                        if item.get("description") == snmpV3Description:
                            snmpV3Detail = item
                    if not snmpV3Detail:
                        self.msg = "The username and description for the snmp_v2c_write credential are invalid."
                        self.status = "failed"
                        return self
                if self.dnac_version <= self.version_2_3_5_3:
                    want.get("assign_credentials").update({"snmpV3Id": snmpV3Detail.get("id")})
                else:
                    want.get("assign_credentials").update({
                        "snmpv3CredentialsId": {"credentialsId": snmpV3Detail.get("id")}
                    })

        self.log("Desired State (want): {0}".format(want), "INFO")
        self.want.update(want)
        self.msg = "Collected the Credentials needed to be assigned from the Cisco Catalyst Center"
        self.status = "success"
        return self

    def get_want_apply_credentials(self, ApplyCredentials):
        """
        Get the Credentials to be applied to a site from the playbook.
        Check this API using the check_return_status.

        Parameters:
            ApplyCredentials (dict) - Playbook details containing
            credentials that need to be applied to a site.

        Returns:
            self - The current object with updated information of credentials
            that need to be applied to a site from the playbook.
        """
        want = {
            "apply_credentials": {}
        }
        site_name = ApplyCredentials.get("site_name")
        if not site_name:
            self.msg = "The 'site_name' is required parameter for 'apply_credentials_to_site'"
            self.status = "failed"
            return self
        want["apply_credentials"]["site_id"] = self.get_site_id(site_name[0])
        global_credentials = self.get_global_credentials_params()
        cli_credential = ApplyCredentials.get("cli_credential")
        if cli_credential:
            cliId = cli_credential.get("id")
            cliDescription = cli_credential.get("description")
            cliUsername = cli_credential.get("username")

            if cliId or cliDescription and cliUsername:
                # All CLI details from the Cisco Catalyst Center
                cli_details = global_credentials.get("cliCredential")
                if not cli_details:
                    self.msg = "Global CLI credential is not available"
                    self.status = "failed"
                    return self
                cliDetail = None
                if cliId:
                    cliDetail = get_dict_result(cli_details, "id", cliId)
                    if not cliDetail:
                        self.msg = "The ID for the CLI credential is not valid."
                        self.status = "failed"
                        return self
                elif cliDescription and cliUsername:
                    for item in cli_details:
                        if item.get("description") == cliDescription and \
                                item.get("username") == cliUsername:
                            cliDetail = item
                    if not cliDetail:
                        self.msg = "The username and description of the CLI credential are invalid"
                        self.status = "failed"
                        return self
                want["apply_credentials"]["cliId"] = cliDetail.get("id")

        snmp_v2c_read = ApplyCredentials.get("snmp_v2c_read")
        if snmp_v2c_read:
            snmpV2cReadId = snmp_v2c_read.get("id")
            snmpV2cReadDescription = snmp_v2c_read.get("description")
            if snmpV2cReadId or snmpV2cReadDescription:

                # All snmp_v2c_read details from the Cisco Catalyst Center
                snmpV2cRead_details = global_credentials.get("snmpV2cRead")
                if not snmpV2cRead_details:
                    self.msg = "Global snmp_v2c_read credential is not available"
                    self.status = "failed"
                    return self
                snmpV2cReadDetail = None
                if snmpV2cReadId:
                    snmpV2cReadDetail = get_dict_result(
                        snmpV2cRead_details, "id", snmpV2cReadId)
                    if not snmpV2cReadDetail:
                        self.msg = "The ID of the snmp_v2c_read credential is not valid."
                        self.status = "failed"
                        return self
                elif snmpV2cReadDescription:
                    for item in snmpV2cRead_details:
                        if item.get("description") == snmpV2cReadDescription:
                            snmpV2cReadDetail = item
                    if not snmpV2cReadDetail:
                        self.msg = "The username and description for the snmp_v2c_read credential are invalid."
                        self.status = "failed"
                        return self
                want["apply_credentials"]["snmpV2ReadId"] = snmpV2cReadDetail.get(
                    "id")

        snmp_v2c_write = ApplyCredentials.get("snmp_v2c_write")
        if snmp_v2c_write:
            snmpV2cWriteId = snmp_v2c_write.get("id")
            snmpV2cWriteDescription = snmp_v2c_write.get("description")
            if snmpV2cWriteId or snmpV2cWriteDescription:

                # All snmp_v2c_write details from the Cisco Catalyst Center
                snmpV2cWrite_details = global_credentials.get("snmpV2cWrite")
                if not snmpV2cWrite_details:
                    self.msg = "Global snmp_v2c_write Credential is not available"
                    self.status = "failed"
                    return self
                snmpV2cWriteDetail = None
                if snmpV2cWriteId:
                    snmpV2cWriteDetail = get_dict_result(
                        snmpV2cWrite_details, "id", snmpV2cWriteId)
                    if not snmpV2cWriteDetail:
                        self.msg = "The ID of the snmp_v2c_write credential is invalid."
                        self.status = "failed"
                        return self
                elif snmpV2cWriteDescription:
                    for item in snmpV2cWrite_details:
                        if item.get("description") == snmpV2cWriteDescription:
                            snmpV2cWriteDetail = item
                    if not snmpV2cWriteDetail:
                        self.msg = "The username and description of the snmp_v2c_write credential are invalid."
                        self.status = "failed"
                        return self
                want["apply_credentials"]["snmpV2WriteId"] = snmpV2cWriteDetail.get(
                    "id")

        snmp_v3 = ApplyCredentials.get("snmp_v3")
        if snmp_v3:
            snmpV3Id = snmp_v3.get("id")
            snmpV3Description = snmp_v3.get("description")
            if snmpV3Id or snmpV3Description:

                # All snmp_v3 details from the Cisco Catalyst Center
                snmpV3_details = global_credentials.get("snmpV3")
                if not snmpV3_details:
                    self.msg = "Global snmp_v3 Credential is not available."
                    self.status = "failed"
                    return self
                snmpV3Detail = None
                if snmpV3Id:
                    snmpV3Detail = get_dict_result(
                        snmpV3_details, "id", snmpV3Id)
                    if not snmpV3Detail:
                        self.msg = "The ID of the snmp_v3 credential is not valid."
                        self.status = "failed"
                        return self
                elif snmpV3Description:
                    for item in snmpV3_details:
                        if item.get("description") == snmpV3Description:
                            snmpV3Detail = item
                    if not snmpV3Detail:
                        self.msg = "The username and description for the snmp_v2c_write credential are invalid."
                        self.status = "failed"
                        return self
                want["apply_credentials"]["snmpV3Id"] = snmpV3Detail.get("id")

        self.log("Desired State (want): {0}".format(want), "INFO")
        self.want.update(want)
        self.msg = "Collected the Credentials needed to be applied from the Cisco Catalyst Center"
        self.status = "success"
        return self

    def get_want(self, config):
        """
        Get the current Global Device Credentials and Device
        Credentials assigned to a site form the playbook.

        Parameters:
            config (dict) - Playbook details containing Global Device
            Credentials configurations and Device Credentials should
            be assigned to a site.

        Returns:
            self - The current object with updated information of Global
            Device Credentials and Device Credentials assigned to a site.
        """

        if config.get("global_credential_details"):
            CredentialDetails = config.get("global_credential_details")
            self.get_want_device_credentials(CredentialDetails).check_return_status()

        if config.get("assign_credentials_to_site"):
            AssignCredentials = config.get("assign_credentials_to_site")
            self.get_want_assign_credentials(AssignCredentials).check_return_status()

        if config.get("apply_credentials_to_site"):
            ApplyCredentials = config.get("apply_credentials_to_site")
            self.get_want_apply_credentials(ApplyCredentials).check_return_status()

        self.log("Desired State (want): {0}".format(self.want), "INFO")
        self.msg = "Successfully retrieved details from the playbook"
        self.status = "success"
        return self

    def create_device_credentials(self):
        """
        Create Global Device Credential to the Cisco Catalyst
        Center based on the provided playbook details.
        Check the return value of the API with check_return_status().

        Parameters:
            self

        Returns:
            self
        """

        result_global_credential = self.result.get("response")[0].get("globalCredential")
        want_create = self.want.get("want_create")
        if not want_create:
            result_global_credential.update({
                "No Creation": {
                    "response": "No Response",
                    "msg": "No Creation is available"
                }
            })
            return self

        credential_params = want_create
        self.log("Creating global credential API input parameters: {0}"
                 .format(credential_params), "DEBUG")
        response = self.dnac._exec(
            family="discovery",
            function='create_global_credentials_v2',
            op_modifies=True,
            params=credential_params,
        )
        self.log("Received API response from 'create_global_credentials_v2': {0}"
                 .format(response), "DEBUG")
        validation_string = "global credential addition performed"
        self.check_task_response_status(response, validation_string, "create_global_credentials_v2").check_return_status()
        self.log("Global credential created successfully", "INFO")
        result_global_credential.update({
            "Creation": {
                "response": credential_params,
                "msg": "Global Credential Created Successfully"
            }
        })
        self.msg = "Global Device Credential Created Successfully"
        self.status = "success"
        return self

    def update_device_credentials(self):
        """
        Update Device Credential to the Cisco Catalyst Center based on the provided playbook details.
        Check the return value of the API with check_return_status().

        Parameters:
            self

        Returns:
            self
        """

        result_global_credential = self.result.get("response")[0].get("globalCredential")

        # Get the result global credential and want_update from the current object
        want_update = self.want.get("want_update")
        # If no credentials to update, update the result and return
        if not want_update:
            result_global_credential.update({
                "No Updation": {
                    "response": "No Response",
                    "msg": "No Updation is available"
                }
            })
            self.msg = "No Updation is available"
            self.status = "success"
            return self
        i = 0
        flag = True
        values = ["cliCredential", "snmpV2cRead", "snmpV2cWrite",
                  "httpsRead", "httpsWrite", "snmpV3"]
        final_response = []
        self.log("Desired State for global device credentials updation: {0}"
                 .format(want_update), "DEBUG")
        while flag:
            flag = False
            credential_params = {}
            for value in values:
                if want_update.get(value) and i < len(want_update.get(value)):
                    flag = True
                    credential_params.update({value: want_update.get(value)[i]})
            i = i + 1
            if credential_params:
                final_response.append(credential_params)
                response = self.dnac._exec(
                    family="discovery",
                    function='update_global_credentials_v2',
                    op_modifies=True,
                    params=credential_params,
                )
                self.log("Received API response for 'update_global_credentials_v2': {0}"
                         .format(response), "DEBUG")
                validation_string = "global credential update performed"
                self.check_task_response_status(response, validation_string, "update_global_credentials_v2").check_return_status()
        self.log("Updating device credential API input parameters: {0}"
                 .format(final_response), "DEBUG")
        self.log("Global device credential updated successfully", "INFO")
        result_global_credential.update({
            "Updation": {
                "response": final_response,
                "msg": "Global Device Credential Updated Successfully"
            }
        })
        self.msg = "Global Device Credential Updated Successfully"
        self.status = "success"
        return self

    def assign_credentials_to_site(self):
        """
        Assign Global Device Credential to the Cisco Catalyst
        Center based on the provided playbook details.
        Check the return value of the API with check_return_status().

        Parameters:
            self

        Returns:
            self
        """

        result_assign_credential = self.result.get("response")[0].get("assignCredential")
        credential_params = self.want.get("assign_credentials")
        final_response = []
        self.log("Assigning device credential to site API input parameters: {0}"
                 .format(credential_params), "DEBUG")
        if not credential_params:
            result_assign_credential.update({
                "No Assign Credentials": {
                    "response": "No Response",
                    "msg": "No Assignment is available"
                }
            })
            self.msg = "No Assignment is available"
            self.status = "success"
            return self

        site_ids = self.want.get("site_id")
        for site_id in site_ids:

            if self.dnac_version <= self.version_2_3_5_3:
                credential_params.update({"site_id": site_id})
                final_response.append(copy.deepcopy(credential_params))
                response = self.dnac._exec(
                    family="network_settings",
                    function='assign_device_credential_to_site_v2',
                    op_modifies=True,
                    params=credential_params,
                )
                self.log("Received API response for 'assign_device_credential_to_site_v2': {0}"
                         .format(response), "DEBUG")
                validation_string = "desired common settings operation successful"
                self.check_task_response_status(
                    response, validation_string, "assign_device_credential_to_site_v2").check_return_status()
            else:
                credential_params.update({"id": site_id})
                final_response.append(copy.deepcopy(credential_params))
                response = self.dnac._exec(
                    family="network_settings",
                    function='update_device_credential_settings_for_a_site',
                    op_modifies=True,
                    params=credential_params
                )
                self.log("Received API response for 'update_device_credential_settings_for_a_site': {0}"
                         .format(response), "DEBUG")
                validation_string = "desired common settings operation successful"
                self.check_task_response_status(
                    response, validation_string, "update_device_credential_settings_for_a_site").check_return_status()

        self.log("Device credential assigned to site {0} is successfully."
                 .format(site_ids), "INFO")
        self.log("Desired State for assign credentials to a site: {0}"
                 .format(final_response), "DEBUG")
        result_assign_credential.update({
            "Assign Credentials": {
                "response": final_response,
                "msg": "Device Credential Assigned to a site is Successfully"
            }
        })
        self.msg = "Global Credential is assigned Successfully"
        self.status = "success"
        return self

    def get_network_devices_credentials_sync_status(self):
        """
        Get network devices credentials sync status from Cisco Catalyst Center.

        Parameters:
            self - The current object with updated Global Device Credential information.

        Returns:
            sync_status - Response for all network devices credential's sync status.
        """
        site_id = self.want.get("apply_credentials").get("site_id")
        try:
            sync_status = self.dnac._exec(
                family="network_settings",
                function='get_network_devices_credentials_sync_status',
                params={"id": site_id}
            )
            sync_status = sync_status.get("response")
            self.log("All global device credentials sync details: {0}"
                     .format(sync_status), "DEBUG")
        except Exception as msg:
            self.msg = (
                "Exception occurred while getting global device credentials sync status: {0}".format(
                    msg)
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        return sync_status

    def check_device_assigned_to_site(self, site_id):
        """
        Check if any devices are assigned to a given site in Cisco Catalyst Center.

        Parameters:
            self - The current object with updated Global Device Credential information.
            site_id - The ID of the site to check for assigned devices.

        Returns:
            site_response - The response from the API call.
        """
        self.log(
            "Checking assigned devices for site with ID: {0}".format(site_id), "DEBUG")
        site_assigned_network_devices_response = self.dnac._exec(
            family="site_design",
            function="get_site_assigned_network_devices",
            op_modifies=True,
            params={"site_id": site_id},
        )
        self.log("Received API response from 'get_site_assigned_network_devices': {0}"
                 .format(str(site_assigned_network_devices_response)), "DEBUG")
        site_response = site_assigned_network_devices_response.get(
            "response", [])

        return site_response

    def get_assigned_device_credential(self, site_id):
        """
        Get device credential settings for a site from Cisco Catalyst Center.

        Parameters:
            self - The current object with updated Global Device Credential information.

        Returns:
            site_credential_response - The device credential settings for the specified site.
        """
        self.log(
            "Retrieving device credential settings for site ID: {0}".format(site_id), "DEBUG")
        credential_settings = self.dnac._exec(
            family="network_settings",
            function='get_device_credential_settings_for_a_site',
            params={"id": site_id}
        )

        self.log("Received API response: {0}".format(credential_settings), "DEBUG")
        site_credential_response = credential_settings.get("response")
        self.log("Device credential settings details: {0}".format(
            site_credential_response), "DEBUG")

        return site_credential_response

    def apply_credentials_to_site(self):
        """
        Apply Global Device Credential to the Cisco Catalyst
        Center based on the provided playbook details.
        Check the return value of the API with check_return_status().

        Parameters:
            self - The current object with updated Global Device Credential information.

        Returns:
            self - The current object with updated Global Device Credential information.

        """
        if self.dnac_version >= self.version_2_3_7_6:
            result_apply_credential = self.result.get(
                "response")[0].get("applyCredential")
            credential_params = self.want.get("apply_credentials")
            final_response = []
            self.log("Applying device credential to site API input parameters: {0}"
                     .format(credential_params), "DEBUG")

            if not credential_params:
                result_apply_credential.update({
                    "No Apply Credentials": {
                        "response": "No Response",
                        "msg": "No device credential id is available"
                    }
                })
                self.msg = "No device credential id is available"
                self.status = "success"
                return self

            site_id = self.want.get("apply_credentials").get("site_id")
            site_response = self.check_device_assigned_to_site(site_id)
            if not site_response:
                result_apply_credential.update({
                    "No Apply Credentials": {
                        "response": "No Response",
                        "msg": "No device available in the site"
                    }
                })
                self.msg = "No device available in the site: {0}".format(site_id)
                self.log(self.msg, "WARNING")
                self.status = "skipped"
                return self

            cred_sync_status = self.get_network_devices_credentials_sync_status()
            credential_mapping = {
                "cli": "cliId",
                "snmpV2Read": "snmpV2ReadId",
                "snmpV2Write": "snmpV2WriteId",
                "snmpV3": "snmpV3Id"
            }

            not_synced_ids, assigned_site_ids = [], []

            for status_key, param_key in credential_mapping.items():
                if param_key in credential_params:
                    status_list = cred_sync_status.get(status_key, [])
                    for status in status_list:
                        if status.get('status') != 'Synced':
                            if credential_params.get(param_key):
                                not_synced_ids.append(credential_params[param_key])
            assigned_device_credential = self.get_assigned_device_credential(site_id)

            for value in assigned_device_credential.values():
                if isinstance(value, dict) and "credentialsId" in value:
                    assigned_site_ids.append(value.get("credentialsId"))

            valid_sync_cred_ids, invalid_sync_cred_ids = [], []

            for id in not_synced_ids:
                if id in assigned_site_ids:
                    valid_sync_cred_ids.append(id)
                else:
                    invalid_sync_cred_ids.append(id)

            self.log("Credential IDs {} not assigned to site, so Sync not possible." .format(
                invalid_sync_cred_ids), "INFO")

            if not valid_sync_cred_ids:
                result_apply_credential.update({
                    "Applied Credentials": {
                        "response": final_response,
                        "msg": "Provided credentials category is/are already synced."
                    }
                })
                self.msg = (
                    "Provided credentials category is/are already synced: {0}".format(
                        credential_params)
                )
                self.log(self.msg, "WARNING")
                self.status = "skipped"
                return self

            for credential_id in valid_sync_cred_ids:
                param = {"deviceCredentialId": credential_id,
                         "siteId": site_id}
                self.log("Credential {0} to be synced with {1} site id." .format(credential_id, site_id), "INFO")
                final_response.append(copy.deepcopy(param))
                response = self.dnac._exec(
                    family="network_settings",
                    function="sync_network_devices_credential",
                    op_modifies=True,
                    params=param
                )

                self.log("Received API response for 'sync_network_devices_credential': {0}"
                         .format(response), "DEBUG")
                validation_string = "successfully applied credential."
                self.check_task_response_status(response, validation_string,
                                                "sync_network_devices_credential").check_return_status()

                self.log("Device credential applied to site {0} successfully."
                         .format(site_id), "INFO")
                self.log("Desired State for applying credentials to a site: {0}"
                         .format(final_response), "DEBUG")
                result_apply_credential.update({
                    "Applied Credentials": {
                        "response": final_response,
                        "msg": "Successfully applied credential."
                    }
                })
            self.msg = "Global Credential is applied Successfully"
            self.status = "success"
        else:
            self.msg = (
                "Cisco Catalyst Center version '{0}' doesn't support apply credentials to site feature.".format(
                    self.payload.get("dnac_version")), "ERROR"
            )
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self.check_return_status()

        return self

    def get_diff_merged(self, config):
        """
        Update or Create Global Device Credential and assign device
        credential to a site in Cisco Catalyst Center based on the playbook provided.

        Parameters:
            config (list of dict) - Playbook details containing Global
            Device Credential and assign credentials to a site information.

        Returns:
            self
        """

        if config.get("global_credential_details") is not None:
            self.create_device_credentials().check_return_status()

        if config.get("global_credential_details") is not None:
            self.update_device_credentials().check_return_status()

        if config.get("assign_credentials_to_site") is not None:
            self.assign_credentials_to_site().check_return_status()

        if config.get("apply_credentials_to_site") is not None:
            self.apply_credentials_to_site().check_return_status()

        return self

    def delete_device_credential(self, config):
        """
        Delete Global Device Credential in Cisco Catalyst Center based on the playbook details.
        Check the return value of the API with check_return_status().

        Parameters:
            config (dict) - Playbook details containing Global Device Credential information.
            self - The current object details.

        Returns:
            self
        """

        result_global_credential = self.result.get(
            "response")[0].get("globalCredential")
        have_values = self.have.get("globalCredential")
        final_response = {}
        self.log("Global device credentials to be deleted: {0}".format(
            have_values), "DEBUG")
        credential_mapping = {
            "cliCredential": "cli_credential",
            "snmpV2cRead": "snmp_v2c_read",
            "snmpV2cWrite": "snmp_v2c_write",
            "snmpV3": "snmp_v3",
            "httpsRead": "https_read",
            "httpsWrite": "https_write"
        }
        failed_status = False
        changed_status = False
        for item in have_values:
            config_itr = -1
            final_response.update({item: []})
            for value in have_values.get(item):
                config_itr = config_itr + 1
                description = config.get("global_credential_details") \
                                    .get(credential_mapping.get(item))[config_itr].get("description")
                if value is None:
                    self.log("Credential Name: {0}".format(item), "DEBUG")
                    self.log("Credential Item: {0}".format(config.get("global_credential_details")
                             .get(credential_mapping.get(item))), "DEBUG")
                    final_response.get(item).append({
                        "description": description,
                        "response": "Global credential not found"
                    })
                    continue

                _id = have_values.get(item)[config_itr].get("id")
                changed_status = True
                response = self.dnac._exec(
                    family="discovery",
                    function="delete_global_credential_v2",
                    op_modifies=True,
                    params={"id": _id},
                )
                self.log("Received API response for 'delete_global_credential_v2': {0}"
                         .format(response), "DEBUG")
                validation_string = "global credential deleted successfully"
                response = response.get("response")
                if response.get("errorcode") is not None:
                    self.msg = response.get("response").get("detail")
                    self.status = "failed"
                    return self

                task_id = response.get("taskId")
                while True:
                    task_details = self.get_task_details(task_id)
                    self.log('Getting task details from task ID {0}: {1}'.format(
                        task_id, task_details), "DEBUG")

                    if task_details.get("isError") is True:
                        if task_details.get("failureReason"):
                            failure_msg = str(
                                task_details.get("failureReason"))
                        else:
                            failure_msg = str(task_details.get("progress"))
                        self.status = "failed"
                        break

                    if validation_string in task_details.get("progress").lower():
                        self.status = "success"
                        break

                    self.log("progress set to {0} for taskid: {1}".format(
                        task_details.get('progress'), task_id), "DEBUG")

                if self.status == "failed":
                    failed_status = True
                    final_response.get(item).append({
                        "description": description,
                        "failure_response": failure_msg
                    })
                else:
                    final_response.get(item).append({
                        "description": description,
                        "response": "Global credential deleted successfully"
                    })

        self.log("Deleting device credential API input parameters: {0}"
                 .format(final_response), "DEBUG")
        result_global_credential.update({
            "Deletion": {
                "response": final_response,
            }
        })
        if failed_status is True:
            self.msg = "Global device credentials are not deleted."
            self.module.fail_json(msg=self.msg, response=final_response)
        else:
            self.result['changed'] = changed_status
            self.msg = "Global Device Credentials Deleted Successfully"
            result_global_credential.get("Deletion").update({"msg": self.msg})
            self.log(str(self.msg), "INFO")
            self.status = "success"

        return self

    def get_diff_deleted(self, config):
        """
        Delete Global Device Credential in Cisco Catalyst Center based on the playbook details.

        Parameters:
            config (dict) - Playbook details containing Global Device Credential information.
            self - The current object details.

        Returns:
            self
        """

        if config.get("global_credential_details") is not None:
            self.delete_device_credential(config).check_return_status()

        return self

    def verify_diff_merged(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is merged (Create/Update).

        Parameters:
            config (dict) - Playbook details containing Global Pool,
            Reserved Pool, and Network Management configuration.

        Returns:
            self
        """

        self.get_have(config)
        self.get_want(config)
        self.log("Current State (have): {0}".format(self.have), "INFO")
        self.log("Desired State (want): {0}".format(self.want), "INFO")

        if config.get("global_credential_details") is not None:
            if self.want.get("want_create"):
                self.msg = "Global Device Credentials config is not applied to the Cisco Catalyst Center"
                self.status = "failed"
                return self

            if self.want.get("want_update"):
                credential_types = ["cliCredential", "snmpV2cRead", "snmpV2cWrite",
                                    "httpsRead", "httpsWrite", "snmpV3"]
                value_mapping = {
                    "cliCredential": ["username", "description", "id"],
                    "snmpV2cRead": ["description", "id"],
                    "snmpV2cWrite": ["description", "id"],
                    "httpsRead": ["description", "username", "port", "id"],
                    "httpsWrite": ["description", "username", "port", "id"],
                    "snmpV3": ["username", "description", "snmpMode", "id"]
                }
                for credential_type in credential_types:
                    if self.want.get(credential_type):
                        want_credential = self.want.get(credential_type)
                        if self.have.get(credential_type):
                            have_credential = self.have.get(credential_type)
                        values = value_mapping.get(credential_type)
                        for value in values:
                            equality = have_credential.get(
                                value) is want_credential.get(value)
                            if not have_credential or not equality:
                                self.msg = "{0} config is not applied ot the Cisco Catalyst Center".format(
                                    credential_type)
                                self.status = "failed"
                                return self

            self.log("Successfully validated global device credential", "INFO")
            self.result.get("response")[0].get(
                "globalCredential").update({"Validation": "Success"})

        if config.get("assign_credentials_to_site") is not None:
            self.log(
                "Successfully validated the assign device credential to site", "INFO")
            self.result.get("response")[0].get(
                "assignCredential").update({"Validation": "Success"})

        if config.get("apply_credentials_to_site") is not None:
            self.log(
                "Successfully validated the assign device credential to site", "INFO")
            self.result.get("response")[0].get(
                "applyCredential").update({"Validation": "Success"})

        self.msg = "Successfully validated the global device credential, assigned and applied device credential to site."
        self.status = "success"
        return self

    def verify_diff_deleted(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is deleted (delete).

        Parameters:
            config (dict) - Playbook details containing Global Pool,
            Reserved Pool, and Network Management configuration.

        Returns:
            self
        """

        self.get_have(config)
        self.log("Current State (have): {0}".format(self.have), "INFO")
        self.log("Desired State (want): {0}".format(self.want), "INFO")

        if config.get("global_credential_details") is not None:
            have_global_credential = self.have.get("globalCredential")
            credential_types = ["cliCredential", "snmpV2cRead", "snmpV2cWrite",
                                "httpsRead", "httpsWrite", "snmpV3"]
            for credential_type in credential_types:
                have_global_credential_type = have_global_credential.get(
                    credential_type)
                if have_global_credential_type is not None:
                    for item in have_global_credential_type:
                        if item is not None:
                            self.msg = "The configuration for deleting the global device credentials " + \
                                       "is not being applied to the current configuration"
                            self.status = "failed"
                            return self

            self.log(
                "Successfully validated absence of global device credential.", "INFO")
            self.result.get("response")[0].get(
                "globalCredential").update({"Validation": "Success"})

        self.msg = "Successfully validated the absence of Global Device Credential."
        self.status = "success"
        return self

    def reset_values(self):
        """
        Reset all neccessary attributes to default values

        Parameters:
            self

        Returns:
            self
        """

        self.have.clear()
        self.want.clear()
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
        "dnac_version": {"type": 'str', "default": '2.2.3.3'},
        "dnac_debug": {"type": 'bool', "default": False},
        "dnac_log": {"type": 'bool', "default": False},
        "dnac_log_level": {"type": 'str', "default": 'WARNING'},
        "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
        "dnac_log_append": {"type": 'bool', "default": True},
        "config_verify": {"type": 'bool', "default": False},
        'dnac_api_task_timeout': {'type': 'int', "default": 1200},
        'dnac_task_poll_interval': {'type': 'int', "default": 2},
        "config": {"type": 'list', "required": True, "elements": 'dict'},
        "state": {"default": 'merged', "choices": ['merged', 'deleted']},
        "validate_response_schema": {"type": 'bool', "default": True},
    }

    # Create an AnsibleModule object with argument specifications
    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)
    ccc_credential = DeviceCredential(module)
    state = ccc_credential.params.get("state")
    config_verify = ccc_credential.params.get("config_verify")
    if state not in ccc_credential.supported_states:
        ccc_credential.status = "invalid"
        ccc_credential.msg = "State {0} is invalid".format(state)
        ccc_credential.check_return_status()

    ccc_credential.validate_input().check_return_status()

    for config in ccc_credential.config:
        ccc_credential.reset_values()
        ccc_credential.get_have(config).check_return_status()
        if state != "deleted":
            ccc_credential.get_want(config).check_return_status()
        ccc_credential.get_diff_state_apply[state](
            config).check_return_status()
        if config_verify:
            ccc_credential.verify_diff_state_apply[state](
                config).check_return_status()

    module.exit_json(**ccc_credential.result)


if __name__ == "__main__":
    main()
