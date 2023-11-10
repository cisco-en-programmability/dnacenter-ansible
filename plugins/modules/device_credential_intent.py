#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2023, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform operations on device credentials in Cisco DNA Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ['Muthu Rakesh, Madhan Sankaranarayanan']

DOCUMENTATION = r"""
---
module: device_credential_intent
short_description: Resource module for Global Device Credentials and Assigning Credentials to sites.
description:
- Manage operations on Global Device Credentials and Assigning Credentials to sites.
- API to create global device credentials.
- API to update global device credentials.
- API to delete global device credentials.
- API to assign the device credential to the site.
version_added: '6.8.0'
extends_documentation_fragment:
  - cisco.dnac.intent_params
author: Muthu Rakesh (@MUTHU-RAKESH-27)
        Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description: The state of Cisco DNA Center after module completion.
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
      GlobalCredentialDetails:
        description: Manages global device credentials
        type: dict
        suboptions:
          cliCredential:
            description: Global Credential V2's cliCredential.
            type: list
            elements: dict
            suboptions:
              description:
                description: Description. Required for creating the credential.
                type: str
              enablePassword:
                description:
                - cliCredential credential Enable Password.
                - Password cannot contain spaces or angle brackets (< >)
                type: str
              id:
                description: Credential Id. Use this for updating the device credential.
                type: str
              password:
                description:
                - cliCredential credential Password.
                - Required for creating/updating the credential.
                - Password cannot contain spaces or angle brackets (< >).
                type: str
              username:
                description:
                - cliCredential credential Username.
                - Username cannot contain spaces or angle brackets (< >).
                type: str
              old_description:
                description: Old Description. Use this for updating the description/Username.
                type: str
              old_username:
                description: Old Username. Use this for updating the description/Username.
                type: str
          httpsRead:
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
                - httpsRead credential Password.
                - Required for creating/updating the credential.
                - Password cannot contain spaces or angle brackets (< >).
                type: str
              port:
                description: Port. Default port is 443.
                type: int
              username:
                description:
                - httpsRead credential Username.
                - Username cannot contain spaces or angle brackets (< >).
                type: str
              old_description:
                description: Old Description. Use this for updating the description/Username.
                type: str
              old_username:
                description: Old Username. Use this for updating the description/Username.
                type: str
          httpsWrite:
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
                - httpsWrite credential Password.
                - Required for creating/updating the credential.
                - Password cannot contain spaces or angle brackets (< >).
                type: str
              port:
                description: Port. Default port is 443.
                type: int
              username:
                description:
                - httpsWrite credential Username.
                - Username cannot contain spaces or angle brackets (< >).
                type: str
              old_description:
                description: Old Description. Use this for updating the description/Username.
                type: str
              old_username:
                description: Old Username. Use this for updating the description/Username.
                type: str
          snmpV2cRead:
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
              readCommunity:
                description:
                - snmpV2cRead Read Community.
                - Password cannot contain spaces or angle brackets (< >).
                type: str
              old_description:
                description: Old Description. Use this for updating the description.
                type: str
          snmpV2cWrite:
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
              writeCommunity:
                description:
                - snmpV2cWrite Write Community.
                - Password cannot contain spaces or angle brackets (< >).
                type: str
              old_description:
                description: Old Description. Use this for updating the description.
                type: str
          snmpV3:
            description: Global Credential V2's snmpV3.
            type: list
            elements: dict
            suboptions:
              authPassword:
                description:
                - snmpV3 Auth Password.
                - Password must contain minimum 8 characters.
                - Password cannot contain spaces or angle brackets (< >).
                type: str
              authType:
                description: Auth Type. ["SHA", "MD5"].
                type: str
              description:
                description:
                - snmpV3 Description.
                - Should be unique from other snmpV3 credentials.
                type: str
              id:
                description: Credential Id. Use this for updating the device credential.
                type: str
              privacyPassword:
                description:
                - snmpV3 Privacy Password.
                - Password must contain minimum 8 characters.
                - Password cannot contain spaces or angle brackets (< >).
                type: str
              privacyType:
                description: Privacy Type. ["AES128", "AES192", "AES256"].
                type: str
              snmpMode:
                description: Snmp Mode. ["AUTHPRIV", "AUTHNOPRIV", "NOAUTHNOPRIV"].
                type: str
              username:
                description:
                - snmpV3 credential Username.
                - Username cannot contain spaces or angle brackets (< >).
                type: str
              old_description:
                description: Old Description. Use this for updating the description.
                type: str
      AssignCredentialsToSite:
        description: Assign Device Credentials to Site.
        type: dict
        suboptions:
          cliDescription:
            description: CLI Credential Description.
            type: str
          cliUsername:
            description: CLI Credential Username.
            type: str
          cliId:
            description: CLI Credential Id. Use (Description, Username) or Id.
            type: str
          httpReadDescription:
            description: HTTP(S) Read Credential Description.
            type: str
          httpReadUsername:
            description: HTTP(S) Read Credential Username.
            type: str
          httpRead:
            description: HTTP(S) Read Credential Id. Use (Description, Username) or Id.
            type: str
          httpWriteDescription:
            description: HTTP(S) Write Credential Description.
            type: str
          httpWriteUsername:
            description: HTTP(S) Write Credential Username.
            type: str
          httpWrite:
            description: HTTP(S) Write Credential Id. Use (Description, Username) or Id.
            type: str
          siteName:
            description: Site Name to assign credential.
            type: list
            elements: str
          snmpV2ReadDescription:
            description: SNMPv2c Read Credential Description.
            type: str
          snmpV2ReadId:
            description: SNMPv2c Read Credential Id. Use Description or Id.
            type: str
          snmpV2WriteDescription:
            description: SNMPv2c Write Credential Description.
            type: str
          snmpV2WriteId:
            description: SNMPv2c Write Credential Id. Use Description or Id.
            type: str
          snmpV3Description:
            description: SNMPv3 Credential Description.
            type: str
          snmpV3Id:
            description: SNMPv3 Credential Id. Use Description or Id.
            type: str
requirements:
- dnacentersdk >= 2.5.5
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Discovery CreateGlobalCredentialsV2
  description: Complete reference of the CreateGlobalCredentialsV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!create-global-credentials-v-2
- name: Cisco DNA Center documentation for Discovery DeleteGlobalCredentialV2
  description: Complete reference of the DeleteGlobalCredentialV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-global-credential-v-2
- name: Cisco DNA Center documentation for Discovery UpdateGlobalCredentialsV2
  description: Complete reference of the UpdateGlobalCredentialsV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-global-credentials-v-2
- name: Cisco DNA Center documentation for Network Settings AssignDeviceCredentialToSiteV2
  description: Complete reference of the AssignDeviceCredentialToSiteV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!assign-device-credential-to-site-v-2
notes:
  - SDK Method used are
    discovery.Discovery.create_global_credentials_v2,
    discovery.Discovery.delete_global_credential_v2,
    discovery.Discovery.update_global_credentials_v2,
    network_settings.NetworkSettings.assign_device_credential_to_site_v2,

  - Paths used are
    post /dna/intent/api/v2/global-credential,
    delete /dna/intent/api/v2/global-credential/{id},
    put /dna/intent/api/v2/global-credential,
    post /dna/intent/api/v2/credential-to-site/{siteId},
"""

EXAMPLES = r"""
---
  - name: Create Credentials and assign it to a site.
    cisco.dnac.device_credential_intent:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    state: merged
    config:
    - GlobalCredentialDetails:
        cliCredential:
        - description: string
          username: string
          password: string
          enablePassword: string
        snmpV2cRead:
        - description: string
          readCommunity: string
        snmpV2cWrite:
        - description: string
          writeCommunity: string
        snmpV3:
        - authPassword: string
          authType: SHA
          snmpMode: AUTHPRIV
          privacyPassword: string
          privacyType: AES128
          username: string
          description: string
        httpsRead:
        - description: string
          username: string
          password: string
          port: 443
        httpsWrite:
        - description: string
          username: string
          password: string
          port: 443
      AssignCredentialsToSite:
        cliId: string
        snmpV2ReadId: string
        snmpV2WriteId: string
        snmpV3Id: string
        httpRead: string
        httpWrite: string
        siteName:
        - string

  - name: Create Multiple Credentials.
    cisco.dnac.device_credential_intent:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    state: merged
    config:
    - GlobalCredentialDetails:
        cliCredential:
        - description: string
          username: string
          password: string
          enablePassword: string
        - description: string
          username: string
          password: string
          enablePassword: string
        snmpV2cRead:
        - description: string
          readCommunity: string
        - description: string
          readCommunity: string
        snmpV2cWrite:
        - description: string
          writeCommunity: string
        - description: string
          writeCommunity: string
        snmpV3:
        - authPassword: string
          authType: SHA
          snmpMode: AUTHPRIV
          privacyPassword: string
          privacyType: AES128
          username: string
          description: string
        - authPassword: string
          authType: SHA
          snmpMode: AUTHPRIV
          privacyPassword: string
          privacyType: AES128
          username: string
          description: string
        httpsRead:
        - description: string
          username: string
          password: string
          port: 443
        - description: string
          username: string
          password: string
          port: 443
        httpsWrite:
        - description: string
          username: string
          password: string
          port: 443
        - description: string
          username: string
          password: string
          port: 443

  - name: Update global device credentials using id
    cisco.dnac.device_credential_intent:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    state: merged
    config:
    - GlobalCredentialDetails:
        cliCredential:
        - description: string
          username: string
          password: string
          enablePassword: string
          id: string
        snmpV2cRead:
        - description: string
          readCommunity: string
          id: string
        snmpV2cWrite:
        - description: string
          writeCommunity: string
          id: string
        snmpV3:
        - authPassword: string
          authType: SHA
          snmpMode: AUTHPRIV
          privacyPassword: string
          privacyType: AES128
          username: string
          description: string
          id: string
        httpsRead:
        - description: string
          username: string
          password: string
          port: 443
          id: string
        httpsWrite:
        - description: string
          username: string
          password: string
          port: 443
          id: string

  - name: Update multiple global device credentials using id
    cisco.dnac.device_credential_intent:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    state: merged
    config:
    - GlobalCredentialDetails:
        cliCredential:
        - description: string
          username: string
          password: string
          enablePassword: string
          id: string
        - description: string
          username: string
          password: string
          enablePassword: string
          id: string
        snmpV2cRead:
        - description: string
          readCommunity: string
          id: string
        - description: string
          readCommunity: string
          id: string
        snmpV2cWrite:
        - description: string
          writeCommunity: string
          id: string
        - description: string
          writeCommunity: string
          id: string
        snmpV3:
        - authPassword: string
          authType: SHA
          snmpMode: AUTHPRIV
          privacyPassword: string
          privacyType: AES128
          username: string
          description: string
          id: string
        - authPassword: string
          authType: SHA
          snmpMode: AUTHPRIV
          privacyPassword: string
          privacyType: AES128
          username: string
          description: string
          id: string
        httpsRead:
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
        httpsWrite:
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
    cisco.dnac.device_credential_intent:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    state: merged
    config:
    - GlobalCredentialDetails:
        cliCredential:
        - description: string
          username: string
          password: string
          enablePassword: string
          old_description: string
          old_username: string
        snmpV2cRead:
        - description: string
          readCommunity: string
          old_description: string
        snmpV2cWrite:
        - description: string
          writeCommunity: string
          old_description: string
        snmpV3:
        - authPassword: string
          authType: string
          snmpMode: string
          privacyPassword: string
          privacyType: string
          username: string
          description: string
        httpsRead:
        - description: string
          username: string
          password: string
          port: string
          old_description: string
          old_username: string
        httpsWrite:
        - description: string
          username: string
          password: string
          port: string
          old_description: string
          old_username: string

  - name: Assign Credentials to sites using old description and username.
    cisco.dnac.device_credential_intent:
    dnac_host: "{{ dnac_host }}"
    dnac_port: "{{ dnac_port }}"
    dnac_username: "{{ dnac_username }}"
    dnac_password: "{{ dnac_password }}"
    dnac_verify: "{{ dnac_verify }}"
    dnac_debug: "{{ dnac_debug }}"
    dnac_log: True
    state: merged
    config:
    - AssignCredentialsToSite:
        cliDescription: string
        cliUsername: string
        snmpV2ReadDescription: string
        snmpV2WriteDescription: string
        snmpV3Description: string
        httpReadDescription: string
        httpReadUsername: string
        httpWriteUsername: string
        httpWriteDescription: string
        siteName:
        - string
        - string

"""

RETURN = r"""
# Case_1: Successful creation/updation/deletion of global device credentials
dnac_response1:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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

# Case_2: Successful assignment of global device credentials to a site.
dnac_response2:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    get_dict_result,
)


class DnacCredential(DnacBase):
    """Class containing member attributes for device credential intent module"""

    def __init__(self, module):
        super().__init__(module)
        self.result["response"] = [
            {
                "globalCredential": {},
                "assignCredential": {}
            }
        ]

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
            "GlobalCredentialDetails": {
                "type": 'dict',
                "cliCredential": {
                    "type": 'list',
                    "description": {"type": 'string'},
                    "username": {"type": 'string'},
                    "password": {"type": 'string'},
                    "enablePassword": {"type": 'string'},
                    "old_description": {"type": 'string'},
                    "old_username": {"type": 'string'},
                    "id": {"type": 'string'},
                },
                "snmpV2cRead": {
                    "type": 'list',
                    "description": {"type": 'string'},
                    "readCommunity": {"type": 'string'},
                    "old_description": {"type": 'string'},
                    "id": {"type": 'string'},
                },
                "snmpV2cWrite": {
                    "type": 'list',
                    "description": {"type": 'string'},
                    "writeCommunity": {"type": 'string'},
                    "old_description": {"type": 'string'},
                    "id": {"type": 'string'},
                },
                "snmpV3": {
                    "type": 'list',
                    "description": {"type": 'string'},
                    "username": {"type": 'string'},
                    "snmpMode": {"type": 'string'},
                    "authType": {"type": 'string'},
                    "authPassword": {"type": 'string'},
                    "privacyType": {"type": 'string'},
                    "privacyPassword": {"type": 'string'},
                    "old_description": {"type": 'string'},
                    "id": {"type": 'string'},
                },
                "httpsRead": {
                    "type": 'list',
                    "description": {"type": 'string'},
                    "username": {"type": 'string'},
                    "password": {"type": 'string'},
                    "port": {"type": 'integer'},
                    "old_description": {"type": 'string'},
                    "old_username": {"type": 'string'},
                    "id": {"type": 'string'},
                },
                "httpsWrite": {
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
            "AssignCredentialsToSite": {
                "type": 'dict',
                "cliDescription": {"type": 'string'},
                "cliUsername": {"type": 'string'},
                "cliId": {"type": 'string'},
                "snmpV2ReadDescription": {"type": 'string'},
                "snmpV2ReadId": {"type": 'string'},
                "snmpV2WriteDescription": {"type": 'string'},
                "snmpV2WriteId": {"type": 'string'},
                "snmpV3Description": {"type": 'string'},
                "snmpV3Id": {"type": 'string'},
                "httpReadDescription": {"type": 'string'},
                "httpReadUsername": {"type": 'string'},
                "httpRead": {"type": 'string'},
                "httpWriteDescription": {"type": 'string'},
                "httpWriteUsername": {"type": 'string'},
                "httpWrite": {"type": 'string'},
                "siteName": {"type": 'list'}
            }
        }

        # Validate playbook params against the specification (temp_spec)
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format("\n".join(invalid_params))
            self.status = "failed"
            return self

        self.validated_config = valid_temp
        self.log(str(valid_temp))
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
            response = self.dnac._exec(
                family="sites",
                function='get_site',
                params={"name": site_name},
            )
            self.log(str(response))
            if not response:
                self.log("Failed to get the site id from site name {0}".format(site_name))
                return None

            _id = response.get("response")[0].get("id")
            self.log("Site ID for the site name {0}".format(site_name) + str(_id))
        except Exception as exec:
            self.log("Error while getting site_id from the site_name" + str(exec))
            return None

        return _id

    def get_global_credentials_params(self):
        """
        Get the current Global Device Credentials from Cisco DNA Center.

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
            self.log("All Global Device Credentials Details " + str(global_credentials))
        except Exception as exec:
            self.log("Error while getting global device credentials: " + str(exec))
            return None

        return global_credentials

    def get_cli_params(self, cliDetails):
        """
        Format the CLI parameters for the CLI credential configuration in Cisco DNA Center.

        Parameters:
            cliDetails (list of dict) - Cisco DNA Center details containing CLI Credentials.

        Returns:
            cliCredential (list of dict) - Processed CLI credential data
            in the format suitable for the Cisco DNA Center config.
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
        Format the snmpV2cRead parameters for the snmpV2cRead
        credential configuration in Cisco DNA Center.

        Parameters:
            snmpV2cReadDetails (list of dict) - Cisco DNA Center
            Details containing snmpV2cRead Credentials.

        Returns:
            snmpV2cRead (list of dict) - Processed snmpV2cRead credential
            data in the format suitable for the Cisco DNA Center config.
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
        Format the snmpV2cWrite parameters for the snmpV2cWrite
        credential configuration in Cisco DNA Center.

        Parameters:
            snmpV2cWriteDetails (list of dict) - Cisco DNA Center
            Details containing snmpV2cWrite Credentials.

        Returns:
            snmpV2cWrite (list of dict) - Processed snmpV2cWrite credential
            data in the format suitable for the Cisco DNA Center config.
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
        Format the httpsRead parameters for the httpsRead
        credential configuration in Cisco DNA Center.

        Parameters:
            httpsReadDetails (list of dict) - Cisco DNA Center
            Details containing httpsRead Credentials.

        Returns:
            httpsRead (list of dict) - Processed httpsRead credential
            data in the format suitable for the Cisco DNA Center config.
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
        Format the httpsWrite parameters for the httpsWrite
        credential configuration in Cisco DNA Center.

        Parameters:
            httpsWriteDetails (list of dict) - Cisco DNA Center
            Details containing httpsWrite Credentials.

        Returns:
            httpsWrite (list of dict) - Processed httpsWrite credential
            data in the format suitable for the Cisco DNA Center config.
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
        Format the snmpV3 parameters for the snmpV3 credential configuration in Cisco DNA Center.

        Parameters:
            snmpV3Details (list of dict) - Cisco DNA Center details containing snmpV3 Credentials.

        Returns:
            snmpV3 (list of dict) - Processed snmpV3 credential
            data in the format suitable for the Cisco DNA Center config.
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
        Cisco DNA Center based on the provided playbook details.
        Check this API using the check_return_status.

        Parameters:
            CredentialDetails (dict) - Playbook details containing Global Device Credentials.
            global_credentials (dict) - All global device credentials details.

        Returns:
            cliDetails (List) - The current CLI credentials.
        """

        # playbook CLI Credential details
        all_CLI = CredentialDetails.get("cliCredential")
        # All CLI details from Cisco DNA Center
        cli_details = global_credentials.get("cliCredential")
        # Cisco DNA Center details for the CLI Credential given in the playbook
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
                                self.msg = "More than one CLI credential with same \
                                            old_description and old_username. Pass ID."
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
                                self.msg = "More than one CLI Credential with same \
                                            description and username. Pass ID."
                                self.status = "failed"
                                return self
                            cliDetail = item
                cliDetails.append(cliDetail)
        return cliDetails

    def get_snmpV2cRead_credentials(self, CredentialDetails, global_credentials):
        """
        Get the current snmpV2cRead Credential from
        Cisco DNA Center based on the provided playbook details.
        Check this API using the check_return_status.

        Parameters:
            CredentialDetails (dict) - Playbook details containing Global Device Credentials.
            global_credentials (dict) - All global device credentials details.

        Returns:
            snmpV2cReadDetails (List) - The current snmpV2cRead.
        """

        # Playbook snmpV2cRead Credential details
        all_snmpV2cRead = CredentialDetails.get("snmpV2cRead")
        # All snmpV2cRead details from the Cisco DNA Center
        snmpV2cRead_details = global_credentials.get("snmpV2cRead")
        # Cisco DNA Center details for the snmpV2cRead Credential given in the playbook
        snmpV2cReadDetails = []
        if all_snmpV2cRead and snmpV2cRead_details:
            for snmpV2cReadCredential in all_snmpV2cRead:
                snmpV2cReadDetail = None
                snmpV2cReadId = snmpV2cReadCredential.get("id")
                if snmpV2cReadId:
                    snmpV2cReadDetail = get_dict_result(snmpV2cRead_details, "id", snmpV2cReadId)
                    if not snmpV2cReadDetail:
                        self.msg = "snmpV2cRead credential ID is invalid"
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
                        self.msg = "snmpV2cRead credential old_description is invalid"
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
        Get the current snmpV2cWrite Credential from
        Cisco DNA Center based on the provided playbook details.
        Check this API using the check_return_status.

        Parameters:
            CredentialDetails (dict) - Playbook details containing Global Device Credentials.
            global_credentials (dict) - All global device credentials details.

        Returns:
            snmpV2cWriteDetails (List) - The current snmpV2cWrite.
        """

        # Playbook snmpV2cWrite Credential details
        all_snmpV2cWrite = CredentialDetails.get("snmpV2cWrite")
        # All snmpV2cWrite details from the Cisco DNA Center
        snmpV2cWrite_details = global_credentials.get("snmpV2cWrite")
        # Cisco DNA Center details for the snmpV2cWrite Credential given in the playbook
        snmpV2cWriteDetails = []
        if all_snmpV2cWrite and snmpV2cWrite_details:
            for snmpV2cWriteCredential in all_snmpV2cWrite:
                snmpV2cWriteDetail = None
                snmpV2cWriteId = snmpV2cWriteCredential.get("id")
                if snmpV2cWriteId:
                    snmpV2cWriteDetail = get_dict_result(snmpV2cWrite_details, "id", snmpV2cWriteId)
                    if not snmpV2cWriteDetail:
                        self.msg = "snmpV2cWrite credential ID is invalid"
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
                        self.msg = "snmpV2cWrite credential old_description is invalid "
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
        Get the current httpsRead Credential from
        Cisco DNA Center based on the provided playbook details.
        Check this API using the check_return_status.

        Parameters:
            CredentialDetails (dict) - Playbook details containing Global Device Credentials.
            global_credentials (dict) - All global device credentials details.

        Returns:
            httpsReadDetails (List) - The current httpsRead.
        """

        # Playbook httpsRead Credential details
        all_httpsRead = CredentialDetails.get("httpsRead")
        # All httpsRead details from the Cisco DNA Center
        httpsRead_details = global_credentials.get("httpsRead")
        # Cisco DNA Center details for the httpsRead Credential given in the playbook
        httpsReadDetails = []
        if all_httpsRead and httpsRead_details:
            for httpsReadCredential in all_httpsRead:
                httpsReadDetail = None
                httpsReadId = httpsReadCredential.get("id")
                if httpsReadId:
                    httpsReadDetail = get_dict_result(httpsRead_details, "id", httpsReadId)
                    if not httpsReadDetail:
                        self.msg = "httpsRead credential Id is invalid"
                        self.status = "failed"
                        return self

                httpsReadOldDescription = httpsReadCredential.get("old_description")
                httpsReadOldUsername = httpsReadCredential.get("old_username")
                if httpsReadOldDescription and httpsReadOldUsername and (not httpsReadDetail):
                    for item in httpsRead_details:
                        if item.get("description") == httpsReadOldDescription \
                                and item.get("username") == httpsReadOldUsername:
                            if httpsReadDetail:
                                self.msg = "More than one httpsRead credential with same \
                                            old_description and old_username. Pass ID."
                                self.status = "failed"
                                return self
                            httpsReadDetail = item
                    if not httpsReadDetail:
                        self.msg = "httpsRead credential old_description or old_username is invalid"
                        self.status = "failed"
                        return self

                httpsReadDescription = httpsReadCredential.get("description")
                httpsReadUsername = httpsReadCredential.get("username")
                if httpsReadDescription and httpsReadUsername and (not httpsReadDetail):
                    for item in httpsRead_details:
                        if item.get("description") == httpsReadDescription \
                                and item.get("username") == httpsReadUsername:
                            if httpsReadDetail:
                                self.msg = "More than one httpsRead credential with same \
                                            description and username. Pass ID."
                                self.status = "failed"
                                return self
                            httpsReadDetail = item
                httpsReadDetails.append(httpsReadDetail)
        return httpsReadDetails

    def get_httpsWrite_credentials(self, CredentialDetails, global_credentials):
        """
        Get the current httpsWrite Credential from
        Cisco DNA Center based on the provided playbook details.
        Check this API using the check_return_status.

        Parameters:
            CredentialDetails (dict) - Playbook details containing Global Device Credentials.
            global_credentials (dict) - All global device credentials details.

        Returns:
            httpsWriteDetails (List) - The current httpsWrite.
        """

        # Playbook httpsWrite Credential details
        all_httpsWrite = CredentialDetails.get("httpsWrite")
        # All httpsWrite details from the Cisco DNA Center
        httpsWrite_details = global_credentials.get("httpsWrite")
        # Cisco DNA Center details for the httpsWrite Credential given in the playbook
        httpsWriteDetails = []
        if all_httpsWrite and httpsWrite_details:
            for httpsWriteCredential in all_httpsWrite:
                httpsWriteDetail = None
                httpsWriteId = httpsWriteCredential.get("id")
                if httpsWriteId:
                    httpsWriteDetail = get_dict_result(httpsWrite_details, "id", httpsWriteId)
                    if not httpsWriteDetail:
                        self.msg = "httpsWrite credential Id is invalid"
                        self.status = "failed"
                        return self

                httpsWriteOldDescription = httpsWriteCredential.get("old_description")
                httpsWriteOldUsername = httpsWriteCredential.get("old_username")
                if httpsWriteOldDescription and httpsWriteOldUsername and (not httpsWriteDetail):
                    for item in httpsWrite_details:
                        if item.get("description") == httpsWriteOldDescription \
                                and item.get("username") == httpsWriteOldUsername:
                            if httpsWriteDetail:
                                self.msg = "More than one httpsWrite credential with same \
                                            old_description and old_username. Pass ID"
                                self.status = "failed"
                                return self
                            httpsWriteDetail = item
                    if not httpsWriteDetail:
                        self.msg = "httpsWrite credential old_description or \
                                    old_username is invalid"
                        self.status = "failed"
                        return self

                httpsWriteDescription = httpsWriteCredential.get("description")
                httpsWriteUsername = httpsWriteCredential.get("username")
                if httpsWriteDescription and httpsWriteUsername and (not httpsWriteDetail):
                    for item in httpsWrite_details:
                        if item.get("description") == httpsWriteDescription \
                                and item.get("username") == httpsWriteUsername:
                            httpsWriteDetail = item
                httpsWriteDetails.append(httpsWriteDetail)
        return httpsWriteDetails

    def get_snmpV3_credentials(self, CredentialDetails, global_credentials):
        """
        Get the current snmpV3 Credential from
        Cisco DNA Center based on the provided playbook details.
        Check this API using the check_return_status.

        Parameters:
            CredentialDetails (dict) - Playbook details containing Global Device Credentials.
            global_credentials (dict) - All global device credentials details.

        Returns:
            snmpV3Details (List) - The current snmpV3.
        """

        # Playbook snmpV3 Credential details
        all_snmpV3 = CredentialDetails.get("snmpV3")
        # All snmpV3 details from the Cisco DNA Center
        snmpV3_details = global_credentials.get("snmpV3")
        # Cisco DNA Center details for the snmpV3 Credential given in the playbook
        snmpV3Details = []
        if all_snmpV3 and snmpV3_details:
            for snmpV3Credential in all_snmpV3:
                snmpV3Detail = None
                snmpV3Id = snmpV3Credential.get("id")
                if snmpV3Id:
                    snmpV3Detail = get_dict_result(snmpV3_details, "id", snmpV3Id)
                    if not snmpV3Detail:
                        self.msg = "snmpV3 credential id is invalid"
                        self.status = "failed"
                        return self

                snmpV3OldDescription = snmpV3Credential.get("old_description")
                if snmpV3OldDescription and (not snmpV3Detail):
                    snmpV3Detail = get_dict_result(snmpV3_details,
                                                   "description", snmpV3OldDescription)
                    if not snmpV3Detail:
                        self.msg = "snmpV3 credential old_description is invalid"
                        self.status = "failed"
                        return self

                snmpV3Description = snmpV3Credential.get("description")
                if snmpV3Description and (not snmpV3Detail):
                    snmpV3Detail = get_dict_result(snmpV3_details, "description", snmpV3Description)
                snmpV3Details.append(snmpV3Detail)
        return snmpV3Details

    def get_have_device_credentials(self, CredentialDetails):
        """
        Get the current Global Device Credentials from
        Cisco DNA Center based on the provided playbook details.
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

        self.log("Global Device Credential Details " + str(self.have.get("globalCredential")))
        self.msg = "Collected the Global Device Credential Details from the Cisco DNA Center"
        self.status = "success"
        return self

    def get_have(self, config):
        """
        Get the current Global Device Credentials and
        Device Credentials assigned to a site in Cisco DNA Center.

        Parameters:
            config (dict) - Playbook details containing Global Device
            Credentials configurations and Device Credentials should
            be assigned to a site.

        Returns:
            self - The current object with updated information of Global
            Device Credentials and Device Credentials assigned to a site.
        """

        if config.get("GlobalCredentialDetails") is not None:
            CredentialDetails = config.get("GlobalCredentialDetails")
            self.get_have_device_credentials(CredentialDetails).check_return_status()

        self.log("Credentials and Credentials Assigned to Site Details in Cisco DNA Center " +
                 str(self.have))
        self.msg = "Successfully retrieved the details from the Cisco DNA Center"
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
        if CredentialDetails.get("cliCredential"):
            cli = CredentialDetails.get("cliCredential")
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
                            self.msg = values[i] + " is mandatory for creating \
                                       cliCredential " + str(have_cli_ptr)
                            self.status = "failed"
                            return self

                    if item.get("enablePassword"):
                        create_credential[create_cli_ptr] \
                            .update({"enablePassword": item.get("enablePassword")})
                    create_cli_ptr = create_cli_ptr + 1
                else:
                    if want.get("want_update").get("cliCredential") is None:
                        want.get("want_update").update({"cliCredential": []})
                    update_credential = want.get("want_update").get("cliCredential")
                    update_credential.append({})
                    if item.get("password"):
                        update_credential[update_cli_ptr] \
                            .update({"password": item.get("password")})
                    else:
                        self.msg = "password is mandatory for udpating \
                                   cliCredential " + str(have_cli_ptr)
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

                    if item.get("enablePassword"):
                        update_credential[update_cli_ptr].update({
                            "enablePassword": item.get("enablePassword")
                        })
                    update_cli_ptr = update_cli_ptr + 1
                have_cli_ptr = have_cli_ptr + 1

        if CredentialDetails.get("snmpV2cRead"):
            snmpV2cRead = CredentialDetails.get("snmpV2cRead")
            have_snmpv2cread_ptr = 0
            create_snmpv2cread_ptr = 0
            update_snmpv2cread_ptr = 0
            values = ["readCommunity", "description", "id"]
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
                                .update({values[i]: item.get(values[i])})
                        else:
                            self.msg = values[i] + " is mandatory for creating \
                                       snmpV2cRead " + str(have_snmpv2cread_ptr)
                            self.status = "failed"
                            return self
                    create_snmpv2cread_ptr = create_snmpv2cread_ptr + 1
                else:
                    if want.get("want_update").get("snmpV2cRead") is None:
                        want.get("want_update").update({"snmpV2cRead": []})
                    update_credential = want.get("want_update").get("snmpV2cRead")
                    update_credential.append({})
                    if item.get("readCommunity"):
                        update_credential[update_snmpv2cread_ptr] \
                            .update({"readCommunity": item.get("readCommunity")})
                    else:
                        self.msg = "readCommunity is mandatory for updating \
                                   snmpV2cRead " + str(have_snmpv2cread_ptr)
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

        if CredentialDetails.get("snmpV2cWrite"):
            snmpV2cWrite = CredentialDetails.get("snmpV2cWrite")
            have_snmpv2cwrite_ptr = 0
            create_snmpv2cwrite_ptr = 0
            update_snmpv2cwrite_ptr = 0
            values = ["writeCommunity", "description", "id"]
            have_snmpV2cWrite = self.have.get("globalCredential").get("snmpV2cWrite")
            for item in snmpV2cWrite:
                if not have_snmpV2cWrite or have_snmpV2cWrite[have_snmpv2cwrite_ptr] is None:
                    if want.get("want_create").get("snmpV2cWrite") is None:
                        want.get("want_create").update({"snmpV2cWrite": []})
                    create_credential = want.get("want_create").get("snmpV2cWrite")
                    create_credential.append({})
                    for i in range(0, 2):
                        if item.get(values[i]):
                            create_credential[create_snmpv2cwrite_ptr] \
                                .update({values[i]: item.get(values[i])})
                        else:
                            self.msg = values[i] + " is mandatory for creating \
                                       snmpV2cWrite " + str(have_snmpv2cwrite_ptr)
                            self.status = "failed"
                            return self
                    create_snmpv2cwrite_ptr = create_snmpv2cwrite_ptr + 1
                else:
                    if want.get("want_update").get("snmpV2cWrite") is None:
                        want.get("want_update").update({"snmpV2cWrite": []})
                    update_credential = want.get("want_update").get("snmpV2cWrite")
                    update_credential.append({})
                    if item.get("writeCommunity"):
                        update_credential[update_snmpv2cwrite_ptr] \
                            .update({"writeCommunity": item.get("writeCommunity")})
                    else:
                        self.msg = "writeCommunity is mandatory for updating \
                                   snmpV2cWrite " + str(have_snmpv2cwrite_ptr)
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

        if CredentialDetails.get("httpsRead"):
            httpsRead = CredentialDetails.get("httpsRead")
            have_httpsread_ptr = 0
            create_httpsread_ptr = 0
            update_httpsread_ptr = 0
            values = ["password", "description", "username", "id", "port"]
            have_httpsRead = self.have.get("globalCredential").get("httpsRead")
            for item in httpsRead:
                self.log(str(self.have.get("globalCredential")))
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
                            self.msg = values[i] + " is mandatory for creating \
                                       httpsRead " + str(have_httpsread_ptr)
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
                        self.msg = "password is mandatory for updating \
                                   httpsRead " + str(have_httpsread_ptr)
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

        if CredentialDetails.get("httpsWrite"):
            httpsWrite = CredentialDetails.get("httpsWrite")
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
                            self.msg = values[i] + " is mandatory for creating \
                                       httpsWrite " + str(have_httpswrite_ptr)
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
                    update_credential = want.get("want_update").get("httpsWrite")
                    update_credential.append({})
                    if item.get("password"):
                        update_credential[update_httpswrite_ptr] \
                            .update({"password": item.get("password")})
                    else:
                        self.msg = "password is mandatory for updating \
                                   httpsRead " + str(have_httpswrite_ptr)
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

        if CredentialDetails.get("snmpV3"):
            snmpV3 = CredentialDetails.get("snmpV3")
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
                            self.msg = values[i] + " is mandatory for creating \
                                       snmpV3 " + str(have_snmpv3_ptr)
                            self.status = "failed"
                            return self
                    if item.get("snmpMode"):
                        create_credential[create_snmpv3_ptr] \
                            .update({"snmpMode": item.get("snmpMode")})
                    else:
                        create_credential[create_snmpv3_ptr] \
                            .update({"snmpMode": "AUTHPRIV"})
                    if create_credential[create_snmpv3_ptr].get("snmpMode") == "AUTHNOPRIV" or \
                            create_credential[create_snmpv3_ptr].get("snmpMode") == "AUTHPRIV":
                        auths = ["authPassword", "authType"]
                        for auth in auths:
                            if item.get(auth):
                                create_credential[create_snmpv3_ptr] \
                                    .update({auth: item.get(auth)})
                            else:
                                self.msg = auth + " is mandatory for creating \
                                           snmpV3 " + str(have_snmpv3_ptr)
                                self.status = "failed"
                                return self
                        if len(item.get("authPassword")) < 8:
                            self.msg = "authPassword length should be greater than 8"
                            self.status = "failed"
                            return self
                    elif create_credential[create_snmpv3_ptr].get("snmpMode") == "AUTHPRIV":
                        privs = ["privacyPassword", "privacyType"]
                        for priv in privs:
                            if item.get(priv):
                                create_credential[create_snmpv3_ptr] \
                                    .update({priv: item.get(priv)})
                            else:
                                self.msg = priv + " is mandatory for creating \
                                           snmpV3 " + str(have_snmpv3_ptr)
                                self.status = "failed"
                                return self
                        if len(item.get("privacyPassword")):
                            self.msg = "privacyPassword should be greater than 8"
                            self.status = "failed"
                            return self
                    elif create_credential[create_snmpv3_ptr].get("snmpMode") != "NOAUTHNOPRIV":
                        self.msg = "snmpMode in snmpV3 is not \
                                    ['AUTHPRIV', 'AUTHNOPRIV', 'NOAUTHNOPRIV']"
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
                    if item.get("snmpMode"):
                        update_credential[update_snmpv3_ptr] \
                            .update({"snmpMode": item.get("snmpMode")})
                    if update_credential[update_snmpv3_ptr].get("snmpMode") == "AUTHNOPRIV" or \
                            update_credential[update_snmpv3_ptr].get("snmpMode") == "AUTHPRIV":
                        if item.get("authType"):
                            update_credential[update_snmpv3_ptr] \
                                .update({"authType": item.get("authType")})
                        elif self.have.get("globalCredential") \
                                .get("snmpMode")[have_snmpv3_ptr].get("authType"):
                            update_credential[update_snmpv3_ptr].update({
                                "authType": self.have.get("globalCredential")
                                .get("snmpMode")[have_snmpv3_ptr].get("authType")
                            })
                        else:
                            self.msg = "authType is required for updating snmpV3 " + \
                                       str(have_snmpv3_ptr)
                            self.status = "failed"
                            return self
                        if item.get("authPassword"):
                            update_credential[update_snmpv3_ptr] \
                                .update({"authPassword": item.get("authPassword")})
                        else:
                            self.msg = "authPassword is required for updating snmpV3 " + \
                                       str(have_snmpv3_ptr)
                            self.status = "failed"
                            return self
                        if len(item.get("authPassword")) < 8:
                            self.msg = "authPassword length should be greater than 8"
                            self.status = "failed"
                            return self
                    elif update_credential[update_snmpv3_ptr].get("snmpMode") == "AUTHPRIV":
                        if item.get("privacyType"):
                            update_credential[update_snmpv3_ptr] \
                                .update({"privacyType": item.get("privacyType")})
                        elif self.have.get("globalCredential") \
                                .get("snmpMode")[have_snmpv3_ptr].get("privacyType"):
                            update_credential[update_snmpv3_ptr].update({
                                "privacyType": self.have.get("globalCredential")
                                .get("snmpMode")[have_snmpv3_ptr].get("privacyType")
                            })
                        else:
                            self.msg = "privacyType is required for updating snmpV3 " + \
                                       str(have_snmpv3_ptr)
                            self.status = "failed"
                            return self
                        if item.get("privacyPassword"):
                            update_credential[update_snmpv3_ptr] \
                                .update({"privacyPassword": item.get("privacyPassword")})
                        else:
                            self.msg = "privacyPassword is required for updating snmpV3 " + \
                                       str(have_snmpv3_ptr)
                            self.status = "failed"
                            return self
                        if len(item.get("privacyPassword")) < 8:
                            self.msg = "privacyPassword length should be greater than 8"
                            self.status = "failed"
                            return self
                    update_snmpv3_ptr = update_snmpv3_ptr + 1
                have_snmpv3_ptr = have_snmpv3_ptr + 1
        self.want.update(want)
        self.msg = "Collected the Global Credentials from the Cisco DNA Center"
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
        siteName = AssignCredentials.get("siteName")
        if not siteName:
            self.msg = "siteName is required for AssignCredentials"
            self.status = "failed"
            return self
        site_id = []
        for site_name in siteName:
            siteId = self.get_site_id(site_name)
            if not site_name:
                self.msg = "siteName is invalid in AssignCredentials"
                self.status = "failed"
                return self
            site_id.append(siteId)
        want.update({"site_id": site_id})
        global_credentials = self.get_global_credentials_params()
        cliId = AssignCredentials.get("cliId")
        cliDescription = AssignCredentials.get("cliDescription")
        cliUsername = AssignCredentials.get("cliUsername")
        if cliId or cliDescription and cliUsername:

            # All CLI details from the Cisco DNA Center
            cli_details = global_credentials.get("cliCredential")
            if not cli_details:
                self.msg = "No Global CLI Credential is available"
                self.status = "failed"
                return self
            cliDetail = None
            if cliId:
                cliDetail = get_dict_result(cli_details, "id", cliId)
                if not cliDetail:
                    self.msg = "CLI credential ID is invalid"
                    self.status = "failed"
                    return self
            elif cliDescription and cliUsername:
                for item in cli_details:
                    if item.get("description") == cliDescription and \
                            item.get("username") == cliUsername:
                        cliDetail = item
                if not cliDetail:
                    self.msg = "CLI credential username and description is invalid"
                    self.status = "failed"
                    return self
            want.get("assign_credentials").update({"cliId": cliDetail.get("id")})

        snmpV2cReadId = AssignCredentials.get("snmpV2ReadId")
        snmpV2cReadDescription = AssignCredentials.get("snmpV2ReadDescription")
        if snmpV2cReadId or snmpV2cReadDescription:

            # All snmpV2cRead details from the Cisco DNA Center
            snmpV2cRead_details = global_credentials.get("snmpV2cRead")
            if not snmpV2cRead_details:
                self.msg = "No Global snmpV2cRead Credential is available"
                self.status = "failed"
                return self
            snmpV2cReadDetail = None
            if snmpV2cReadId:
                snmpV2cReadDetail = get_dict_result(snmpV2cRead_details, "id", snmpV2cReadId)
                if not snmpV2cReadDetail:
                    self.msg = "snmpV2cRead credential ID is invalid"
                    self.status = "failed"
                    return self
            elif snmpV2cReadDescription:
                for item in snmpV2cRead_details:
                    if item.get("description") == snmpV2cReadDescription:
                        snmpV2cReadDetail = item
                if not snmpV2cReadDetail:
                    self.msg = "snmpV2cRead credential username and description is invalid"
                    self.status = "failed"
                    return self
            want.get("assign_credentials").update({"snmpV2ReadId": snmpV2cReadDetail.get("id")})

        snmpV2cWriteId = AssignCredentials.get("snmpV2WriteId")
        snmpV2cWriteDescription = AssignCredentials.get("snmpV2WriteDescription")
        if snmpV2cWriteId or snmpV2cWriteDescription:

            # All snmpV2cWrite details from the Cisco DNA Center
            snmpV2cWrite_details = global_credentials.get("snmpV2cWrite")
            if not snmpV2cWrite_details:
                self.msg = "No Global snmpV2cWrite Credential is available"
                self.status = "failed"
                return self
            snmpV2cWriteDetail = None
            if snmpV2cWriteId:
                snmpV2cWriteDetail = get_dict_result(snmpV2cWrite_details, "id", snmpV2cWriteId)
                if not snmpV2cWriteDetail:
                    self.msg = "snmpV2cWrite credential ID is invalid"
                    self.status = "failed"
                    return self
            elif snmpV2cWriteDescription:
                for item in snmpV2cWrite_details:
                    if item.get("description") == snmpV2cWriteDescription:
                        snmpV2cWriteDetail = item
                if not snmpV2cWriteDetail:
                    self.msg = "snmpV2cWrite credential username and description is invalid"
                    self.status = "failed"
                    return self
            want.get("assign_credentials").update({"snmpV2WriteId": snmpV2cWriteDetail.get("id")})

        httpReadId = AssignCredentials.get("httpRead")
        httpReadDescription = AssignCredentials.get("httpReadDescription")
        httpReadUsername = AssignCredentials.get("httpReadUsername")
        if httpReadId or httpReadDescription and httpReadUsername:

            # All httpRead details from the Cisco DNA Center
            httpRead_details = global_credentials.get("httpsRead")
            if not httpRead_details:
                self.msg = "No Global httpRead Credential is available"
                self.status = "failed"
                return self
            httpReadDetail = None
            if httpReadId:
                httpReadDetail = get_dict_result(httpRead_details, "id", httpReadId)
                if not httpReadDetail:
                    self.msg = "httpRead credential ID is invalid"
                    self.status = "failed"
                    return self
            elif httpReadDescription and httpReadUsername:
                for item in httpRead_details:
                    if item.get("description") == httpReadDescription and \
                            item.get("username") == httpReadUsername:
                        httpReadDetail = item
                if not httpReadDetail:
                    self.msg = "httpRead credential description and username is invalid"
                    self.status = "failed"
                    return self
            want.get("assign_credentials").update({"httpRead": httpReadDetail.get("id")})

        httpWriteId = AssignCredentials.get("httpWrite")
        httpWriteDescription = AssignCredentials.get("httpWriteDescription")
        httpWriteUsername = AssignCredentials.get("httpWriteUsername")
        if httpWriteId or httpWriteDescription and httpWriteUsername:

            # All httpWrite details from the Cisco DNA Center
            httpWrite_details = global_credentials.get("httpsWrite")
            if not httpWrite_details:
                self.msg = "No Global httpWrite Credential is available"
                self.status = "failed"
                return self
            httpWriteDetail = None
            if httpWriteId:
                httpWriteDetail = get_dict_result(httpWrite_details, "id", httpWriteId)
                if not httpWriteDetail:
                    self.msg = "httpWrite credential ID is invalid"
                    self.status = "failed"
                    return self
            elif httpWriteDescription and httpWriteUsername:
                for item in httpWrite_details:
                    if item.get("description") == httpWriteDescription and \
                            item.get("username") == httpWriteUsername:
                        httpWriteDetail = item
                if not httpWriteDetail:
                    self.msg = "httpWrite credential description and username is invalid"
                    self.status = "failed"
                    return self
            want.get("assign_credentials").update({"httpWrite": httpWriteDetail.get("id")})

        snmpV3Id = AssignCredentials.get("snmpV3Id")
        snmpV3Description = AssignCredentials.get("snmpV3Description")
        if snmpV3Id or snmpV3Description:

            # All snmpV3 details from the Cisco DNA Center
            snmpV3_details = global_credentials.get("snmpV3")
            if not snmpV3_details:
                self.msg = "No Global snmpV3 Credential is available"
                self.status = "failed"
                return self
            snmpV3Detail = None
            if snmpV3Id:
                snmpV3Detail = get_dict_result(snmpV3_details, "id", snmpV3Id)
                if not snmpV3Detail:
                    self.msg = "snmpV3 credential ID is invalid"
                    self.status = "failed"
                    return self
            elif snmpV3Description:
                for item in snmpV3_details:
                    if item.get("description") == snmpV3Description:
                        snmpV3Detail = item
                if not snmpV3Detail:
                    self.msg = "snmpV2cWrite credential username and description is invalid"
                    self.status = "failed"
                    return self
            want.get("assign_credentials").update({"snmpV3Id": snmpV3Detail.get("id")})
        self.log("Assign Credentials to Site playbook values " + str(want))
        self.want.update(want)
        self.msg = "Collected the Credentials needed to be assigned from the Cisco DNA Center"
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

        if config.get("GlobalCredentialDetails"):
            CredentialDetails = config.get("GlobalCredentialDetails")
            self.get_want_device_credentials(CredentialDetails).check_return_status()

        if config.get("AssignCredentialsToSite"):
            AssignCredentials = config.get("AssignCredentialsToSite")
            self.get_want_assign_credentials(AssignCredentials).check_return_status()

        self.log("User details from the playbook " + str(self.want))
        self.msg = "Successfully retrieved details from the playbook"
        self.status = "success"
        return self

    def create_device_credentials(self):
        """
        Create Global Device Credential to the Cisco DNA
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
        self.log("Create Global Credential API input - " + str(credential_params))
        response = self.dnac._exec(
            family="discovery",
            function='create_global_credentials_v2',
            params=credential_params,
        )
        self.log(str(response))
        validation_string = "global credential addition performed"
        self.check_task_response_status(response, validation_string).check_return_status()
        self.log("Global Credential Created Successfully")
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
        Update Device Credential to the Cisco DNA Center based on the provided playbook details.
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
        self.log(str(want_update))
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
                    params=credential_params,
                )
                self.log(str(response))
                validation_string = "global credential update performed"
                self.check_task_response_status(response, validation_string).check_return_status()
        self.log("Update Device Credential API input - " + str(final_response))
        self.log("Global Device Credential Updated Successfully")
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
        Assign Global Device Credential to the Cisco DNA
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
        self.log("Assign Device Credential to site API input - " + str(credential_params))
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
            credential_params.update({"site_id": site_id})
            final_response.append(credential_params)
            response = self.dnac._exec(
                family="network_settings",
                function='assign_device_credential_to_site_v2',
                params=credential_params,
            )
            self.log(str(response))
            validation_string = "desired common settings operation successful"
            self.check_task_response_status(response, validation_string).check_return_status()
        self.log("Device Credential Assigned to site is Successfully")
        result_assign_credential.update({
            "Assign Credentials": {
                "response": final_response,
                "msg": "Device Credential Assigned to a site is Successfully"
            }
        })
        self.msg = "Global Credential is assigned Successfully"
        self.status = "success"
        return self

    def get_diff_merged(self, config):
        """
        Update or Create Global Device Credential and assign device
        credential to a site in Cisco DNA Center based on the playbook provided.

        Parameters:
            config (list of dict) - Playbook details containing Global
            Device Credential and assign credentials to a site information.

        Returns:
            self
        """

        if config.get("GlobalCredentialDetails") is not None:
            self.create_device_credentials().check_return_status()

        if config.get("GlobalCredentialDetails") is not None:
            self.update_device_credentials().check_return_status()

        if config.get("AssignCredentialsToSite") is not None:
            self.assign_credentials_to_site().check_return_status()

        return self

    def delete_device_credential(self, config):
        """
        Delete Global Device Credential in Cisco DNA Center based on the playbook details.
        Check the return value of the API with check_return_status().

        Parameters:
            config (dict) - Playbook details containing Global Device Credential information.
            self - The current object details.

        Returns:
            self
        """

        result_global_credential = self.result.get("response")[0].get("globalCredential")
        have_values = self.have.get("globalCredential")
        final_response = {}
        self.log(str(have_values))
        for item in have_values:
            config_itr = 0
            final_response.update({item: []})
            for value in have_values.get(item):
                if value is None:
                    self.msg = str(config.get("GlobalCredentialDetails")
                                   .get("item")[config_itr]) + "is not found"
                    self.status = "failed"
                    return self
                _id = have_values.get(item)[config_itr].get("id")
                response = self.dnac._exec(
                    family="discovery",
                    function="delete_global_credential_v2",
                    params={"id": _id},
                )
                self.log(str(response))
                validation_string = "global credential deleted successfully"
                self.check_task_response_status(response, validation_string).check_return_status()
                final_response.get(item).append(_id)
                config_itr = config_itr + 1

        self.log("Delete Device Credential API input - " + str(final_response))
        self.log("Global Device Credential Deleted Successfully")
        result_global_credential.update({
            "Deletion": {
                "response": final_response,
                "msg": "Global Device Credentials Deleted Successfully"
            }
        })
        self.msg = "Global Device Credentials Updated Successfully"
        self.status = "success"
        return self

    def get_diff_deleted(self, config):
        """
        Delete Global Device Credential in Cisco DNA Center based on the playbook details.

        Parameters:
            config (dict) - Playbook details containing Global Device Credential information.
            self - The current object details.

        Returns:
            self
        """

        if config.get("GlobalCredentialDetails") is not None:
            self.delete_device_credential(config).check_return_status()

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
        "config": {"type": 'list', "required": True, "elements": 'dict'},
        "state": {"default": 'merged', "choices": ['merged', 'deleted']},
        "validate_response_schema": {"type": 'bool', "default": True},
    }

    # Create an AnsibleModule object with argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=False)
    dnac_credential = DnacCredential(module)
    state = dnac_credential.params.get("state")
    if state not in dnac_credential.supported_states:
        dnac_credential.status = "invalid"
        dnac_credential.msg = "State {0} is invalid".format(state)
        dnac_credential.check_return_status()

    dnac_credential.validate_input().check_return_status()

    for config in dnac_credential.config:
        dnac_credential.reset_values()
        dnac_credential.get_have(config).check_return_status()
        if state != "deleted":
            dnac_credential.get_want(config).check_return_status()
        dnac_credential.get_diff_state_apply[state](config).check_return_status()

    module.exit_json(**dnac_credential.result)


if __name__ == "__main__":
    main()
