# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ( "Madhan Sankaranarayanan")

DOCUMENTATION = r"""
---
module: backup_and_restore_workflow_manager

short_description: >
  Ansible module to automate backup, restore, NFS configuration, and backup cleanup on Cisco Catalyst Center.

description:
  - Automates configuration and management of NFS servers for backup storage in Cisco Catalyst Center.
  - Supports scheduling and on-demand creation of system backups.
  - Enables restoration from previously created backups, including encrypted backups.
  - Provides cleanup of old backups based on defined retention policies.
  - Allows deletion of NFS configurations and specific backups as part of lifecycle management.
version_added: "6.31.0"
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author:
  - Madhan Sankaranarayanan (@madhansansel)

options:
  config_verify:
    description:
      - Set to True to verify the Cisco Catalyst Center after applying changes.
    type: bool
    default: true
  state:
    description:
      - The desired state of the configuration.
      - Use C(merged) to apply or update configuration.
      - Use C(deleted) to remove configuration, NFS setups, or backups.
    type: str
    choices: ["merged", "deleted"]
    default: merged
  config:
    description:
      - List of configuration dictionaries for NFS setup, backup scheduling, or restoration.
    type: list
    elements: dict
    required: true
    suboptions:
      nfs_configuration:
        description:
          - Details for configuring NFS backup servers.
        type: list
        elements: dict
        suboptions:
          server_ip:
            description: IP address of the NFS server.
            type: str
            required: true
          source_path:
            description: Directory path on the NFS server for storing backups.
            type: str
            required: true
          nfs_port:
            description: Port used to access NFS services (default 2049).
            type: int
          nfs_version:
            description: NFS protocol version. Defaults to nfs4.
            type: str
            choices: ["nfs3", "nfs4"]
          nfs_port_mapper:
            description: Port for the NFS port mapper service (default 111).
            type: int
      backup_configuration:
        description:
          - Backup target, type, and retention settings.
        type: list
        elements: dict
        suboptions:
          server_type:
            description:
              - Type of storages are NFS or PHYSICAL_DISK.
            type: str
            required: true
            choices: ["NFS", "PHYSICAL_DISK"]
          nfs_details:
            description:
              - Connection details for NFS backup targets.
            type: dict
            suboptions:
              server_ip:
                description: IP address of the NFS server.
                type: str
                required: true
              source_path:
                description: Directory path on the NFS server.
                type: str
                required: true
              nfs_port:
                description: Port used to access NFS services.
                type: int
              nfs_version:
                description: NFS protocol version.
                type: str
                default: nfs4
                choices: ["nfs3", "nfs4"]
              nfs_port_mapper:
                description: Port for the NFS port mapper service.
                type: int
                default: 111
          data_retention_period:
            description:
              - Number of days to retain backups before cleanup.
              - Range must be between 3 and 60 days.
            type: int
            required: true
          encryption_passphrase:
            description:
              - Passphrase for encrypting backup data (recommended).
            type: str
      backup_schedule:
        description:
          - Specifies when and how to schedule backups.
        type: list
        elements: dict
        suboptions:
          name:
            description: Name of the backup schedule.
            type: str
            required: true
          scope:
            description: Defines backup scope (with or without assurance data).
            type: str
            choices: ["CISCO_DNA_DATA_WITH_ASSURANCE", "CISCO_DNA_DATA_WITHOUT_ASSURANCE"]
          # schedule_details:
          #   description: Details of the backup schedule.
          #   type: dict
          #   suboptions:
          #     schedule_type:
          #       description: Type of schedule (e.g., now, recurring).
          #       type: list
          #       elements: str
          #     time:
          #       description: Backup time (HH:MM format).
          #       type: str
          #     days:
          #       description: Days of the week to run backups.
          #       type: list
          #       elements: str
      restore_details:
        description:
          - Parameters for restoring from a backup.
        type: list
        elements: dict
        suboptions:
          name:
            description: Name of the backup to restore.
            type: str
            required: true
          encryption_passphrase:
            description: Passphrase for decrypting the backup during restore.
            type: str


requirements:
- dnacentersdk >= 2.9.3
- python >= 3.9.19

notes:
- SDK Methods used are
  - backup.Backup.get_backup_and_restore_execution
  - backup.Backup.get_backup_by_id
  - backup.Backup.get_backup_and_restore_executions
  - backup.Backup.get_backup_configuration
  - backup.Backup.create_n_f_s_configuration
  - backup.Backup.get_all_backup
  - backup.Backup.delete_n_f_s_configuration
  - backup.Backup.create_backup
  - backup.Backup.delete_backup
  - backup.Backup.get_backup_storages
  - backup.Backup.get_all_n_f_s_configurations
  - backup.Backup.create_backup_configuration
  - restore.Restore.restore_backup

- Paths used are
  - GET/dna/system/api/v1/backupRestoreExecutions/${id}
  - GET/dna/system/api/v1/backups/${id}
  - GET/dna/system/api/v1/backupRestoreExecutions
  - GET/dna/system/api/v1/backupConfiguration
  - POST/dna/system/api/v1/backupNfsConfigurations
  - GET/dna/system/api/v1/backups
  - DELETE/dna/system/api/v1/backupNfsConfigurations/${id}
  - POST/dna/system/api/v1/backups
  - DELETE/dna/system/api/v1/backups/${id}
  - GET/dna/system/api/v1/backupStorages
  - GET/dna/system/api/v1/backupNfsConfigurations
  - POST/dna/system/api/v1/backupConfiguration
  - POST/dna/system/api/v1/backups/${id}/restore
"""

EXAMPLES = r"""
---
#Playbook 1 – Configure NFS server 
---
- name: Configure NFS server in Cisco Catalyst Center
  hosts: localhost
  vars_files:
    - "credentials.yml"
  connection: local
  gather_facts: false
  tasks:
    - name: Configure NFS server
      cisco.dnac.backup_and_restore_workflow_manager:
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
          - nfs_configuration:
              - server_ip: 172.27.17.90
                source_path: /home/nfsshare/backups/TB18
                nfs_port: 2049
                nfs_version: nfs4  #default nfs4
                nfs_port_mapper: 111  #default 111
               
#Playbook 2 – Configure backup

- name: Configure backup on Cisco Catalyst Center
  hosts: localhost
  vars_files:
    - "credentials.yml"
  connection: local
  gather_facts: false
  tasks:
    - name: Configure backup
      cisco.dnac.backup_and_restore_workflow_manager:
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
          - backup_configuration:
              - server_type: NFS  #[NFS/PHYSICAL DISK]
                nfs_details:  
                  server_ip: 172.27.17.90
                  source_path: /home/nfsshare/backups/TB20
                  nfs_port: 2049
                  nfs_version: nfs4  #default nfs4
                  nfs_port_mapper: 111  #default 111
                data_retention_period: 56' #[3 to 60]
                encryption_passphrase: Karthick@zigzag333

#Playbook 3 – Create backup

- name: Create backup on Cisco Catalyst Center
  hosts: localhost
  vars_files:
    - "credentials.yml"
  connection: local
  gather_facts: false
  tasks:
    - name: Create backup
      cisco.dnac.backup_and_restore_workflow_manager:
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
          - backup_schedule:
              - name: BACKUP24_07
                scope: CISCO_DNA_DATA_WITHOUT_ASSURANCE

#Playbook 4 – Restore backup

- name: Restore backup on Cisco Catalyst Center
  hosts: localhost
  vars_files:
    - "credentials.yml"
  connection: local
  gather_facts: false
  tasks:
    - name: Restore backup
      cisco.dnac.backup_and_restore_workflow_manager:
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
          - restore_details:
              - name: newsample
                encryption_passphrase: asbfhhjw@12233

#Playbook 5 – Delete NFS configuration

- name: Delete NFS configuration from the Cisco Catalyst Center
  hosts: localhost
  vars_files:
    - "credentials.yml"
  connection: local
  gather_facts: false
  tasks:
    - name: Delete NFS configuration
      cisco.dnac.backup_and_restore_workflow_manager:
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
          - nfs_configuration:
              - server_ip: str

#Playbook 6 – Delete backup

- name: Delete backup from the Cisco Catalyst Center
  hosts: localhost
  vars_files:
    - "credentials.yml"
  connection: local
  gather_facts: false
  tasks:
    - name: Delete backup
      cisco.dnac.backup_and_restore_workflow_manager:
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
          - backup_details:
              - name: str
"""

RETURN = r"""

"""



from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
)
from ansible.module_utils.basic import AnsibleModule

import time
import json
import re
from datetime import datetime

from ansible_collections.cisco.dnac.plugins.module_utils.validation import (
    validate_list_of_dicts,)


class BackupRestore(DnacBase):
    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]
        self.total_response = []
        self.max_timeout = self.params.get('dnac_api_task_timeout')
        self.created_nfs_config = []
        self.already_exists_nfs_config = []
        self.deleted_nfs_config = []
        self.already_deleted_nfs_config = []
        self.created_backup_config = []
        self.already_exists_backup_config = []
        self.updated_backup_config = []
        self.scheduled_backup = []
        self.deleted_backup_schedule = []
        self.already_backup_exists = []
        self.restored_backup = []

    def validate_input(self):
        """
            Validate the playbook configuration for backup and restore workflow.

            This method verifies the structure, types, and content of the 'config' attribute to ensure that it aligns
            with the expected schema for backup, restore, NFS, and scheduling configurations. It performs multiple
            checks to prevent malformed or incomplete input from proceeding further in the workflow.

            Args:
                self: The instance containing the 'config' attribute to be validated.

            Returns:
                The current instance with updated attributes:
                - self.msg: A descriptive message indicating the validation outcome.
                - self.status: The validation result ('success' or 'failed').
                - self.validated_config: The validated configuration if validation passes.

            Validations Performed:
                - Ensures 'config' is present and is a list.
                - Each item in 'config' must be a dictionary.
                - Uses a predefined specification ('config_spec') to validate structure and data types of fields including:
                    - 'nfs_configuration': Validates server IP, path, port, version (nfs3/nfs4), port mapper.
                    - 'backup_configuration': Validates server type, NFS details, retention period (3–60), passphrase.
                    - 'backup_schedule': Validates schedule type (now/daily/weekly), time format, allowed weekdays.
                    - 'restore_details': Validates presence of backup name and encryption passphrase.
                - Validates allowed values, default values, and optional/mandatory constraints using 'validate_list_of_dicts'.
                - Logs both the input and the result of validation for traceability.
            """
        self.log("Validating backup and restore configuration...", "INFO")

        if not self.config:
            self.msg = "Configuration is not available in the playbook for validation"
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        if not isinstance(self.config, list):
            self.msg = "Config should be a list, found: {0}".format(type(self.config))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        config_data = self.config

        for config_item in config_data:
            if not isinstance(config_item, dict):
                self.msg = "Each item in 'config' should be a dictionary, found: {0}".format(type(config_item))
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

        self.validated_config = self.config

        config_spec = {
            "nfs_configuration": {
            "type": "list",
            "elements": "dict",
            "server_ip": {"type": "str"},
            "source_path": {"type": "str"},
            "nfs_port": {"type": "int"},
            "nfs_version": {
                "type": "str",
                "allowed_values": ["nfs3", "nfs4"],
                "default": "nfs4"
            },
            "nfs_port_mapper": {
                "type": "int",
                "default": 111
            }
            },
            "backup_configuration": {
                "type": "list",
                "elements": "dict",
                "server_type": {"type": "str"},
                "nfs_details": {
                    "type": "dict",
                    "elements": "dict",
                    "server_ip": {"type": "str"},
                    "source_path": {"type": "str"},
                    "nfs_port": {"type": "int"},
                    "nfs_version": {"type": "str", "default": "nfs4"},
                    "nfs_port_mapper": {"type": "int", "default": 111},
                },
                "data_retention_period": {"type": "int", "range_min": 3, "range_max": 60},
                "encryption_passphrase": {"type": "str"},
            },
            "backup_schedule": {
                "type": "list",
                "elements": "dict",
                "name": {"type": "str"},
                "scope": {"type": "str"},
                "schedule_details": {
                    "type": "dict",
                    "elements": "dict",
                    "schedule_type": {"type": "str", "allowed_values": ["now", "weekly", "daily"]},
                    "time": {"type": "str"},
                    "days": {
                        "type": "list",
                        "elements": "str",
                        "allowed_values": ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
                    },
                },
            },
            "restore_details": {
                "type": "list",
                "elements": "dict",
                "name": {"type": "str"},
                "encryption_passphrase": {"type": "str"},
            },
        }

        self.log("Validating backup/restore configuration: {0}".format(json.dumps(self.config, indent=4)), "INFO")

        valid_config, invalid_params = validate_list_of_dicts(self.config, config_spec)

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.log("Configuration validated successfully: {0}".format(valid_config), "INFO")
        return self
    
    def get_want(self, config):
        """
        Extract the desired state ('want') from the backup and restore playbook block.

        Args:
            self (object): An instance of a class interacting with Cisco Catalyst Center.
            config (dict): A dictionary containing the playbook configuration, expected to include
                            one or more of the following keys:
                            - 'backup_configuration'
                            - 'nfs_configuration'
                            - 'backup_schedule'
                            - 'restore_details'

        Returns:
            self: The current instance of the class with the 'want' attribute populated
                    based on the validated backup and restore configuration from the playbook.

        Description:
            This method processes the user-provided configuration to extract only the relevant
            sections required for backup and restore operations. Specifically, it performs the following steps:

            - Validates that at least one of the expected keys is present in the config.
            - Extracts values from 'backup_configuration', 'nfs_configuration', 'backup_schedule',
                and 'restore_details', if present.
            - Logs the final desired state for visibility.
        """
        self.log("Extracting desired state (want) from the playbook configuration...", "INFO")

        want = {}
        backup_config = config.get("backup_configuration")
        nfs_config = config.get("nfs_configuration")
        backup_schedule = config.get("backup_schedule")
        restore_details = config.get("restore_details")

        if not any([backup_config, nfs_config, backup_schedule, restore_details]):
            self.msg = (
                "At least one of 'backup_configuration', 'nfs_configuration', 'backup_schedule', or 'restore_details' must be specified."
            )
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        
        want["backup_configuration"] = backup_config
        want["backup_schedule"] = backup_schedule
        want["restore_details"] = restore_details
        want["nfs_configuration"] = nfs_config


        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        return self
    
    def get_nfs_configuration_details(self):
        """
            Retrieve and match NFS configuration from Cisco Catalyst Center based on user input.

            Args:
                self (object): An instance of a class interacting with Cisco Catalyst Center.

            Returns:
                - nfs_configuration_exists (bool): Indicates whether any NFS configurations exist in the system.
                - current_nfs_configs (list): List of all current NFS configurations retrieved from Catalyst Center.
                - matched_config (dict): A dictionary representing the matched NFS configuration, if found.

            Description:
                This method evaluates the desired NFS configuration from the playbook-provided input and attempts to
                locate a matching NFS configuration from Catalyst Center.

                It performs the following operations:
                - Parses the 'server_ip' and 'source_path' from either:
                    - The first item in 'nfs_configuration', or
                    - The nested 'nfs_details' under 'backup_configuration'.
                - Calls the Catalyst Center API ('get_all_n_f_s_configurations') to retrieve existing NFS configurations.
                - Validates the API response structure and logs it for traceability.
                - Iterates through existing NFS configs to find a match based on both 'server' and 'sourcePath' fields.
        """
        self.log("Retrieving all NFS configuration details from Catalyst Center...", "DEBUG")

        current_nfs_configs = []

        try:
            response = self.dnac._exec(
                family="backup",
                function="get_all_n_f_s_configurations",
            )
            self.log(
                "Received API response from 'get_all_n_f_s_configurations': {0}".format(str(response)),
                "DEBUG",
            )

            if not response or "response" not in response:
                self.log(
                    "Invalid or empty response for NFS configurations: {0}".format(response),
                    "ERROR",
                )
                return []

            current_nfs_configs = response.get("response", [])

        except Exception as e:
            self.msg = "An error occurred while retrieving all NFS configuration details: {0}".format(e)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
            return []

        return current_nfs_configs

    def get_backup_configuration(self):
        """
            Retrieve and match backup configuration from Cisco Catalyst Center based on user input.

            Args:
                self (object): An instance of a class interacting with Cisco Catalyst Center.

            Returns:
                - backup_configuration_exists (bool): Indicates whether any backup configuration exists in the system.
                - current_backup_configuration (dict): The backup configuration retrieved from Catalyst Center.
                - matched_config (dict): A dictionary representing the matched backup configuration, if found.

            Description:
                This method checks the desired backup configuration provided in the playbook and attempts to match it
                with the backup configuration retrieved from Catalyst Center.

                This includes:
                    - Executes the Catalyst Center API 'get_backup_configuration' to retrieve current backup settings.
                    - If the expected type is NFS, compares the retrieved 'server' and 'sourcePath' values against expected input.
                    - Logs and returns the matched configuration if all values align.
        """
        self.log("Retrieving backup configuration details...", "DEBUG")

        backup_configuration_exists = False
        current_backup_configuration = {}
        matched_config = {}

        backup_config_list = self.want.get("backup_configuration", [])
        expected_server_type = expected_server_ip = expected_source_path = None

        if backup_config_list and isinstance(backup_config_list, list):
            backup_config = backup_config_list[0]
            expected_server_type = backup_config.get("type")
            nfs_details = backup_config.get("nfs_details", {})
            expected_server_ip = nfs_details.get("server_ip")
            expected_source_path = nfs_details.get("source_path")

        try:
            response = self.dnac._exec(
                family="backup",
                function="get_backup_configuration",
            )
            self.log(
                "Received API response from 'get_backup_configuration': {0}".format(str(response)),
                "DEBUG",
            )

            if not response or "response" not in response:
                self.log(
                    "Invalid or empty response for backup configurations: {0}".format(response),
                    "ERROR",
                )
                return backup_configuration_exists, current_backup_configuration, matched_config

            current_backup_configuration = response.get("response", {})
            backup_configuration_exists = bool(current_backup_configuration)

            if expected_server_type and expected_server_type.upper() == "NFS":
                current_server = current_backup_configuration.get("server")
                current_path = current_backup_configuration.get("sourcePath")

                if current_server == expected_server_ip and current_path == expected_source_path:
                    matched_config = current_backup_configuration

        except Exception as e:
            self.msg = "An error occurred while retrieving the backup configuration details: {0}".format(e)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        return backup_configuration_exists, current_backup_configuration, matched_config
 
    def get_backup(self):
        """
            Retrieve and match backup schedule from Cisco Catalyst Center based on user input.

            Args:
                self (object): An instance of a class interacting with Cisco Catalyst Center.

            Returns:
                - backup_exists (bool): Indicates whether any backups exist in the system.
                - current_backups (list): A list of all backup entries retrieved from Catalyst Center.
                - matched_config (dict): The matched backup configuration by name, if found.

            Description:
                This method processes the desired backup schedule configuration from the playbook input
                and attempts to identify a matching backup from Catalyst Center.

                Specifically, it performs the following operations:
                - Extracts the 'name' field from the first entry in the 'backup_schedule' section of the 'want' state.
                - Invokes the 'get_all_backup' API to retrieve the list of all backups from Catalyst Center.
                - Validates the structure of the API response.
                - Iterates through the list of backups to find an entry with a matching name.
                - Logs and returns the matched backup configuration, if found.
        """
        self.log("Retrieving backup details...", "DEBUG")

        backup_exists = False
        current_backups = []
        matched_config = {}

        backup_list = self.want.get("backup_schedule", [])
        name = None

        if backup_list and isinstance(backup_list, list):
            backup = backup_list[0]
            name = backup.get("name")

        try:
            response = self.dnac._exec(
                family="backup",
                function="get_all_backup",
            )
            self.log(
                "Received API response from 'get_all_backup': {0}".format(str(response)),
                "DEBUG",
            )

            if not response or "response" not in response:
                self.log(
                    "Invalid or empty response for backups: {0}".format(response),
                    "ERROR",
                )
                return backup_exists, current_backups, matched_config

            current_backups = response.get("response", [])
            backup_exists = bool(current_backups)

            if name:
                for backup in current_backups:
                    if backup.get("name") == name:
                        matched_config = backup
                        self.log(
                            "Matched backup configuration found by name: {0}".format(matched_config),
                            "DEBUG",
                        )
                        break

        except Exception as e:
            self.log(
                "An error occurred while retrieving backups: {0}".format(e),
                "ERROR"
            )

        return backup_exists, current_backups, matched_config

    def get_have(self):
        """
            Retrieve the current (actual) state from Cisco Catalyst Center for comparison with the desired state.

            Args:
                self (object): An instance of a class interacting with Cisco Catalyst Center.

            Returns:
                self: The current instance with the 'have' attribute populated with actual system state details
                    including NFS configuration, backup configuration, and backup schedule.

            Description:
                This method evaluates the desired configuration ('want') and gathers corresponding current state
                ('have') from Cisco Catalyst Center.

                Specifically, it performs the following actions:
                    - If 'nfs_configuration' is provided in the desired state:
                        - Calls 'get_nfs_configuration_details()' to fetch and match the NFS config.
                        - Extracts and stores the matched configuration and its existence flag.
                    - If 'backup_configuration' is present:
                        - Calls 'get_backup_configuration()' to retrieve the existing backup config.
                        - Stores the matched configuration and existence flag.
                    - If 'backup_schedule' is provided:
                        - Calls 'get_backup()' to retrieve and match backup schedules by name.
                        - Stores the matched backup and its existence flag.
                    - If 'restore_details' is provided:
                        - Logs that restore processing is initiated, though no current state is retrieved for it.
            """
        self.log("Retrieving current state (have) from Catalyst Center...", "INFO")
        have = {}

        # Fetch all current NFS configurations, regardless of what's in 'want'
        current_nfs_configs = self.get_nfs_configuration_details()
        have["current_nfs_configurations"] = current_nfs_configs
        self.log("All current NFS configurations: {0}".format(have["current_nfs_configurations"]), "DEBUG")

        backup_configuration_details = self.want.get("backup_configuration", [])

        if backup_configuration_details:
            backup_configuration_exists, current_backup_config, matched_backup = self.get_backup_configuration()
            have["backup_configuration_exists"] = bool(current_backup_config)
            have["current_backup_configuration"] = current_backup_config if current_backup_config else {}

            self.log("Matched current backup configuration: {0}".format(have["current_backup_configuration"]), "DEBUG")

        backup_details = self.want.get("backup_schedule", [])
        if backup_details:
            backup_exists, current_backups, matched_backup = self.get_backup()
            matched_exists = isinstance(matched_backup, dict) and matched_backup.get("name")
            have["backup_exists"] = bool(matched_exists)
            have["current_backup"] = matched_backup if matched_exists else {}

            self.log("Matched current backup details: {0}".format(have["current_backup"]), "DEBUG")

        restore_details = self.want.get("restore_details", [])
        if restore_details:
            self.log("Processing restore details...", "DEBUG")

        self.have = have
        return self

    def get_diff_merged(self, config):
        """
            Retrieves backup workflow configuration details and triggers related diff computations based on the configuration provided in the playbook.

            Args:
                self (object): An instance of the class used for interacting with Cisco Catalyst Center.
                config (dict): The configuration dictionary containing the desired state for:
                            - NFS configuration
                            - Backup configuration
                            - Backup schedule
                            - Restore details

            Returns:
                self: The current instance of the class, with updated diff state for each applicable configuration section.

            Description:
                This method processes the configuration details provided in the playbook for Catalyst Center backup and restore workflows.
                It checks for the presence of specific configuration options—such as NFS configuration, backup configuration, backup schedule,
                and restore details—and triggers corresponding diff methods for each section:
                
                - 'get_diff_nfs_configuration()': Validates and computes the difference between current and desired NFS settings.
                - 'get_diff_backup_configuration()': Handles comparison for backup configuration profiles.
                - 'get_diff_backup_schedule()': Evaluates the defined backup schedule settings.
                - 'get_diff_restore_backup()': Verifies restore parameters and validates their applicability.

                These methods compare the desired state (from 'self.want') with the current state (from 'self.have') and determine
                what changes (if any) need to be made. The result is used later in execution to decide whether a configuration
                update or restore action is required.

                The method also logs the progress of each configuration section for traceability and debugging purposes.
            """
        self.log("Processing configuration for merged state...", "INFO")
        self.config = config

        if config.get("nfs_configuration"):
            self.log("Processing NFS configuration details...", "INFO")
            self.get_diff_nfs_configuration()

        if config.get("backup_configuration"):
            self.log("Processing backup configuration details...", "INFO")
            self.get_diff_backup_configuration()
        
        if config.get("backup_schedule"):
            self.log("Processing backup schedule details...", "INFO")
            self.get_diff_backup_schedule()

        if config.get("restore_details"):
            self.log("Processing restore details...", "INFO")
            self.get_diff_restore_backup()

    def get_diff_deleted(self, config):
        """
            Processes backup and NFS deletion requests based on the configuration provided in the playbook.

            Args:
                self (object): An instance of the class used for interacting with Cisco Catalyst Center.
                config (dict): The configuration dictionary containing the details for NFS configuration and backup schedules
                            that are marked for deletion.

            Returns:
                self: The current instance of the class, with updated 'result' and 'have' attributes reflecting deletion operations.

            Description:
                This method analyzes the playbook configuration to determine which backup and NFS components should be removed
                from the Catalyst Center. It checks for keys like 'nfs_configuration' and 'backup_schedule' and invokes the
                appropriate deletion workflows:

                - 'delete_nfs_configuration()': Initiates deletion of the specified NFS configuration.
                - 'delete_backup_schedule()': Triggers removal of scheduled backups if they exist.

                Each operation is logged for traceability and debugging. The outcomes from these deletion tasks are used to
                update internal tracking attributes like 'result', which determines if a change occurred ('changed: True')
                during execution.
            """
        self.log("Processing configuration for deleted state...", "INFO")
        self.config = config

        if config.get("nfs_configuration"):
            self.log("Processing NFS configuration details for deletion...", "INFO")
            self.delete_nfs_configuration()

        if config.get("backup_schedule"):
            self.log("Processing backup schedule details for deletion...", "INFO")
            self.delete_backup_schedule()

    def get_diff_nfs_configuration(self):
        """
            Validates and manages the creation of NFS configuration based on desired state in the playbook.

            Args:
                self (object): An instance of the class used for interacting with Cisco Catalyst Center.

            Returns:
                self: The current instance with updated 'result' and 'have' attributes based on the NFS configuration status.

            Description:
                This method checks the desired NFS configuration provided in the playbook and compares it with the existing
                (current) state ('self.have'). For each NFS configuration entry:
                
                - It ensures that both 'server_ip' and 'source_path' are provided.
                - If no matching configuration exists in the current state, it initiates the creation of the new NFS configuration.
                - If the configuration already exists, it logs an informational message and sets the operation result accordingly.

                The method ensures only missing NFS configurations are created and avoids duplicates. If input validation fails,
                an appropriate error message is set and the operation is marked as failed.
        """
        self.log("Processing NFS configuration details for diff...", "INFO")
        current_nfs_configs = self.have.get("current_nfs_configurations", [])

        for nfs_config_details in self.want.get("nfs_configuration", []):
            server_ip = nfs_config_details.get("server_ip")
            source_path = nfs_config_details.get("source_path")

            if not server_ip or not source_path:
                self.msg = "Both 'server_ip' and 'source_path' must be specified to create an NFS configuration."
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                continue

            self.log("Checking NFS configuration for server: {0}, path: {1}".format(server_ip, source_path), "DEBUG")

            nfs_found = False
            for existing_config in current_nfs_configs:
                spec = existing_config.get("spec", {})
                if spec.get("server") == server_ip and spec.get("sourcePath") == source_path:
                    nfs_found = True
                    break

            if not nfs_found:
                self.log(
                    "NFS configuration for server '{0}' and source_path '{1}' does not exist. Initiating creation process.".format(
                        server_ip, source_path
                    ),
                    "INFO",
                )
                self.create_nfs_configuration(nfs_config_details)
            else:
                self.msg = (
                    "NFS configuration with server_ip '{0}' and source_path '{1}' already exists.".format(
                        server_ip, source_path
                    )
                )
                self.already_exists_nfs_config.append(source_path)
                self.set_operation_result("success", False, self.msg, "INFO")

    def get_diff_backup_configuration(self):
        """
            Validates and manages the creation or update of backup configuration in Cisco Catalyst Center.

            Args:
                self (object): An instance of the class responsible for backup and restore workflows.

            Returns:
                self: The current instance with updated result based on the success or failure of the backup configuration logic.

            Description:
                This method performs a diff operation to reconcile the desired backup configuration state ('self.want')
                with the current system state ('self.have').

                For each backup configuration provided:
                - It validates that required 'server_ip' and 'source_path' under 'nfs_details' are present.
                - If a backup configuration does not already exist, it initiates the creation using 'create_backup_configuration'.
                - If it exists, it checks for the health of associated NFS nodes.
                    - If nodes are unhealthy, the operation is halted with an appropriate failure message.
                    - If healthy, it retrieves the mount path from the matched configuration.
                - It then compares the current backup settings (server type, retention period, mount path) with the desired ones.
                    - If all match, the method exits without making changes.
                    - If any differ, a payload is constructed and the configuration is updated via the Catalyst Center API.

                The method sets the operation result and logs all relevant details for debugging and auditability.
        """
        self.log("Processing backup configuration details...", "INFO")
        backup_configuration = self.have

        for backup_config_details in self.want.get("backup_configuration", []):
            nfs_details = backup_config_details.get("nfs_details", {})
            server_ip = nfs_details.get("server_ip")
            source_path = nfs_details.get("source_path")

            self.log(
                "Checking backup configuration for server IP: {0}, source_path: {1}".format(
                    server_ip, source_path
                ),
                "DEBUG",
            )
            backup_configuration_exists = backup_configuration.get("backup_configuration_exists")
            self.log("Backup configuration exists: {0}".format(backup_configuration_exists), "DEBUG")
            if backup_configuration.get("backup_configuration_exists") is False:
                self.log(
                    "Backup configuration does not exist. Initiating creation process.",
                    "INFO",
                )
                self.create_backup_configuration(backup_config_details)
                continue

            self.log("Required Backup configuration details: {0}".format(backup_config_details), "DEBUG")
            self.log("Existing Backup configuration details: {0}".format(backup_configuration.get('current_backup_configuration')), "DEBUG")
            self.log("Existing NFS details: {0}".format(nfs_details), "DEBUG")

            current_nfs_config = self.get_nfs_configuration_details()
            self.log("Current NFS configurations: {0}".format(current_nfs_config), "DEBUG")

            nfs_exists = False
            matched_config = None
            mount_path = None

            if current_nfs_config:
                for current_nfs_config_item in current_nfs_config:
                    current_nfs_server = current_nfs_config_item.get('spec', {}).get('server')
                    current_nfs_source_path = current_nfs_config_item.get('spec', {}).get('sourcePath')

                    if (server_ip == current_nfs_server and source_path == current_nfs_source_path):
                        nfs_exists = True
                        matched_config = current_nfs_config_item
                        break

            self.log("NFS exists: {0}".format(nfs_exists), "DEBUG")

            if not nfs_exists:
                self.log("NFS mount path not found for {0}:{1}, attempting to create/verify NFS configuration.".format(server_ip, source_path), "INFO")
                self.create_nfs_configuration(nfs_details)

            if nfs_exists:
                unhealthy_nodes = matched_config.get("status", {}).get("unhealthyNodes") if matched_config else None
                self.log("Unhealthy NFS nodes: {0}".format(unhealthy_nodes), "DEBUG")
                if unhealthy_nodes:
                    spec = matched_config.get("spec", {})
                    server_ip = spec.get("server")
                    source_path = spec.get("sourcePath")

                    self.msg = (
                        "Mount path not retrievable as NFS node is unhealthy for server IP '{0}', source path '{1}'."
                        .format(server_ip, source_path)
                    )
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                else:
                    self.log(
                        "Mount path retrievable. NFS node is healthy.",
                        "INFO"
                    )
                    mount_path = matched_config.get("status", {}).get("destinationPath") if matched_config else None

            current_backup = backup_configuration.get('current_backup_configuration', {})
            config_server_type = backup_config_details.get('server_type')
            current_type = current_backup.get('type')

            final_server_type = current_backup.get('type') if config_server_type == current_type else config_server_type

            config_retention = backup_config_details.get('data_retention_period')
            current_retention = current_backup.get('dataRetention')
            final_data_retention = (
                config_retention if config_retention is not None else current_retention
            )
            current_mount_path = current_backup.get('mountPath')

            if (
                config_server_type == current_type and
                config_retention == current_retention and
                mount_path == current_mount_path
            ):
                self.msg = (
                    "Backup with current config already exists."
                )
                self.already_exists_backup_config.append(source_path)
                self.set_operation_result("success", False, self.msg, "INFO")
                return self

            payload = {
                'mountPath': mount_path,
                'type': final_server_type,
                'dataRetention': final_data_retention
            }

            if 'encryption_passphrase' in backup_config_details and backup_config_details['encryption_passphrase']:
                payload['encryptionPassphrase'] = backup_config_details['encryption_passphrase']

            self.log("Final payload for backup configuration: {0}".format(json.dumps(payload, indent=4)), "DEBUG")
        try:
            response = self.dnac._exec(
                family="backup",
                function="create_backup_configuration",
                op_modifies=True,
                params={"payload": payload}
            )
            self.log("Received API response from 'create_backup_configuration': {0}".format(response), "DEBUG")
            self.updated_backup_config.append(source_path)

            if response is None:
                self.msg = "Backup configuration updated successfully"
                self.set_operation_result("success", True, self.msg, "INFO")
                return self

        except Exception as e:
            self.msg = "An error occurred while updating backup configuration: {0}".format(e)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def get_diff_backup_schedule(self):
        """
            Validates and manages the creation of a backup schedule in Cisco Catalyst Center.

            Args:
                self (object): An instance of the class responsible for backup and restore workflows.

            Returns:
                self: The current instance with updated result based on the success or failure of the backup schedule logic.

            Description:
                This method checks the desired backup schedule configuration ('self.want') against the existing
                schedule configuration ('self.have') to determine whether a new schedule needs to be created.

                For each backup schedule provided:
                    - It ensures that both the 'name' and 'scope' fields are specified.
                    - If these mandatory fields are missing, the operation fails with an appropriate error message.
                    - If the backup schedule does not exist ('backup_exists' is False), it initiates the creation
                    of the backup schedule.
                    - If the schedule already exists, no changes are made, and an informational success message is logged.
        """
        self.log("Processing backup schedule details...", "INFO")
        backup_schedule = self.have

        for schedule_details in self.want.get("backup_schedule", []):
            name = schedule_details.get("name")
            scope = schedule_details.get("scope")

            if not name or not scope:
                self.msg = (
                    "Mandatory fields 'name', 'scope' must be specified for backup schedule."
                )
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            self.log(
                "Checking backup schedule for name: {0}, scope: {1}".format(
                    name, scope
                ),
                "DEBUG",
            )

            if not backup_schedule.get("backup_exists"):
                self.log(
                    "Backup schedule does not exist. Initiating creation process.",
                    "INFO",
                )
                self.create_backup_schedule(schedule_details)
                continue

            else:
                self.msg = (
                    "Backup schedule '{0}' already exists.".format(
                        name
                    )
                )
                self.already_backup_exists.append(name)
                self.set_operation_result("success", False, self.msg, "INFO")

    def get_diff_restore_backup(self):
        """
            Validates and initiates backup restoration in Cisco Catalyst Center.

            Args:
                self (object): An instance of the class handling backup and restore workflows.

            Returns:
                self: The current instance with updated result after attempting restore operation(s).

            Description:
                This method processes the restore configuration provided in 'self.want["restore_details"]'.

                For each restore entry:
                - It checks for the presence of mandatory fields 'name' and 'encryption_passphrase'.
                - If either field is missing, the operation fails with an appropriate error message.
                - If both fields are present, it logs the action and initiates the restore operation.
        """
        self.log("Processing restore details...", "INFO")
        restore_details = self.want.get("restore_details", [])

        for restore_detail in restore_details:
            name = restore_detail.get("name")
            encryption_passphrase = restore_detail.get("encryption_passphrase")

            if not name or not encryption_passphrase:
                self.msg = "Both 'name' and 'encryption_passphrase' must be specified for restore."
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            self.log("Initiating restore for backup name: {0}".format(name), "INFO")
            self.restore_backup()

        return self

    def create_backup_configuration(self, backup_config_details):
        """
            Validates and creates a backup configuration in Cisco Catalyst Center.

            Args:
                backup_config_details (dict): Dictionary containing the backup configuration parameters.
                    Mandatory fields:
                        - server_type (str): Type of server (e.g., NFS).
                        - nfs_details (dict): Dictionary with 'server_ip' and 'source_path'.
                        - data_retention_period (int): Number of days to retain backup data (between 3 and 60).
                        - encryption_passphrase (str): Passphrase for encrypting backup data.

            Returns:
                self: The current class instance with updated operation result.

            Description:
                - Validates presence of all mandatory fields.
                - Validates NFS details ('server_ip' and 'source_path').
                - Retrieves or creates NFS configuration to obtain a valid mount path.
                - Ensures 'data_retention_period' is within allowed limits (3–60 days).
                - Constructs and sends the backup configuration payload using Catalyst Center APIs.
                - Logs API responses and updates the operation result accordingly.
        """
        self.log("Creating backup configuration: {0}".format(backup_config_details), "INFO")

        mandatory_fields = ["server_type", "nfs_details", "data_retention_period", "encryption_passphrase"]
        for field in mandatory_fields:
            if field not in backup_config_details:
                self.msg = "Mandatory field '{0}' is missing in backup configuration.".format(field)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        nfs_details = backup_config_details.get("nfs_details", {})
        server_ip = nfs_details.get("server_ip")
        source_path = nfs_details.get("source_path")

        if not server_ip or not source_path:
            self.msg = "Both 'server_ip' and 'source_path' must be specified in NFS details."
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        current_nfs_configs = self.get_nfs_configuration_details()
        matched_config = None
        for config in current_nfs_configs:
            spec = config.get("spec", {})
            if spec.get("server") == server_ip and spec.get("sourcePath") == source_path:
                matched_config = config
                break

        mount_path = None
        if matched_config:
            mount_path = matched_config.get("status", {}).get("destinationPath")

        if not mount_path:
            self.log("NFS mount path not found for {0}:{1}, attempting to create/verify NFS configuration.".format(server_ip, source_path), "INFO")
            try:
                self.create_nfs_configuration(nfs_details)
               
                current_nfs_configs_after_create = self.get_nfs_configuration_details()
                matched_config_after_create = None
                for config in current_nfs_configs_after_create:
                    spec = config.get("spec", {})
                    if spec.get("server") == server_ip and spec.get("sourcePath") == source_path:
                        matched_config_after_create = config
                        break
                if matched_config_after_create:
                    mount_path = matched_config_after_create.get("status", {}).get("destinationPath")
                    self.log("Successfully created/verified NFS configuration. Retrieved destinationPath: {0}".format(mount_path), "INFO")
                else:
                    self.msg = "Failed to find newly created NFS configuration for {0}:{1}.".format(server_ip, source_path)
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            except Exception as e:
                self.msg = "Failed to create NFS configuration: {0}".format(e)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        if not mount_path:
            self.msg = "Failed to retrieve NFS destinationPath even after creation/verification."
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        data_retention_period = backup_config_details.get("data_retention_period")
        if not (3 <= data_retention_period <= 60):
            self.msg = (
                "Data retention period must be between 3 and 60 days, found: {0}".format(data_retention_period)
            )
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        payload = {
            "type": backup_config_details["server_type"].upper(),
            "encryptionPassphrase": backup_config_details["encryption_passphrase"],
            "mountPath": mount_path,
            "dataRetention": data_retention_period,
        }

        optional_fields = [("encryption_passphrase", "encryptionPassphrase")]
        self.log("Adding optional fields to backup configuration payload", "DEBUG")
        for field, key in optional_fields:
            value = backup_config_details.get(field)
            if value is not None:
                payload[key] = value
                self.log("Added optional field: {0} with value: {1}".format(key, payload[key]), "DEBUG")

        self.log("Generated payload for create backup configuration: {0}".format(json.dumps(payload, indent=4)), "DEBUG")

        try:
            response = self.dnac._exec(
                family="backup",
                function="create_backup_configuration",
                op_modifies=True,
                params={"payload": payload}
            )
            self.log("Received API response from 'create_backup_configuration': {0}".format(response), "DEBUG")
            self.created_backup_config.append(source_path)

            if response is None:
                self.msg = "Backup configuration created successfully for {0}".format(server_ip)
                self.set_operation_result("success", True, self.msg, "INFO")
                return self

        except Exception as e:
            self.msg = "An error occurred while creating backup configuration: {0}".format(e)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def create_nfs_configuration(self, nfs_config_details):
        """
            Validates and creates an NFS configuration in Cisco Catalyst Center.

            Args:
                nfs_config_details (dict): Dictionary containing details of the NFS configuration.
                    Mandatory fields:
                        - server_ip (str): IP address of the NFS server.
                        - source_path (str): Source path on the NFS server.
                    Optional fields:
                        - nfs_port (int): Port number used for NFS communication.
                        - nfs_version (str): Version of NFS protocol (e.g., "v3", "v4").
                        - nfs_port_mapper (int): Port number for the port mapper service.

            Returns:
                self: The current class instance with updated operation result.

            Description:
                - Validates presence of mandatory fields ('server_ip', 'source_path').
                - Constructs a payload with optional fields if provided.
                - Sends the configuration to Catalyst Center using the 'create_n_f_s_configuration' API.
                - Logs API responses and updates the operation result accordingly.
        """
        self.log("Creating NFS configuration: {0}".format(nfs_config_details), "INFO")
        mandatory_fields = ["server_ip", "source_path"]

        for field in mandatory_fields:
            if field not in nfs_config_details:
                self.msg = "Mandatory field '{0}' is missing in NFS configuration.".format(field)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
        
        payload = {
            "server": nfs_config_details["server_ip"],
            "sourcePath": nfs_config_details["source_path"],
        }

        optional_fields = [
            ("nfs_port", "nfsPort"),
            ("nfs_version", "nfsVersion"),
            ("nfs_port_mapper", "portMapperPort"),
        ]

        self.log("Adding optional fields to NFS payload", "DEBUG")
        for field, key in optional_fields:
            value = nfs_config_details.get(field)
            if value is not None:
                payload[key] = (
                    int(value)
                    if field in ("nfs_port", "nfs_port_mapper")
                    else value
                )
                self.log(
                    "Added optional field: {0} with value: {1}".format(key, payload[key]),
                    "DEBUG"
                )
        self.log("Generated payload for create NFS configuration:{0}".format(json.dumps(payload, indent=4)), "DEBUG")

        try:
            response = self.dnac._exec(
                family="backup",
                function="create_n_f_s_configuration",
                op_modifies=True,
                params={"payload": payload}
            )
            self.log("Received API response from 'create_n_f_s_configuration': {0}".format(response), "DEBUG")
            self.created_nfs_config.append(nfs_config_details["source_path"])

            if response is None:
                self.msg = "NFS configuration created successfully for server {0} with source_path {1}".format(nfs_config_details["server_ip"], nfs_config_details["source_path"])
                self.set_operation_result("success", True, self.msg, "INFO")
                return self

        except Exception as e:
            self.msg = "An error occurred while creating NFS configuration: {0}".format(e)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def create_backup_schedule(self, schedule_details):
        """
            Validates and creates a backup schedule in Cisco Catalyst Center.

            Args:
                schedule_details (dict): Dictionary containing backup schedule details.
                    Mandatory fields:
                        - name (str): Name of the backup schedule. Must start with an alphabet
                        and can include alphanumeric characters and special characters
                        (@, #, _, -, space).
                        - scope (str): Scope of the backup schedule (e.g., "SYSTEM").

            Returns:
                self: The current class instance with updated operation result.

            Workflow:
                - Validates mandatory fields ('name', 'scope').
                - Ensures 'name' follows the naming convention.
                - Constructs and sends a payload to the Catalyst Center API using 'create_backup'.
                - Extracts the task ID from the API response.
                - Polls task status using 'get_backup_status_by_task_id'.
                - Based on task status, sets the operation result to success, failure, or warning.
        """
        self.log("Creating backup schedule: {0}".format(schedule_details), "INFO")
        name_pattern = r"^[A-Za-z][A-Za-z0-9@#_\-]*$"

        name = schedule_details.get("name")
        self.log("Validating backup schedule name: {0}".format(name), "DEBUG")
        if not re.match(name_pattern, name):
            self.msg = (
                "Backup name must begin with an alphabet and can contain letters, digits, "
                "and the following special characters: @, #, _, -, and space."
            )
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        payload = {
            "name": name,
            "scope": schedule_details["scope"],
        }

        self.log("Generated payload for create backup schedule: {0}".format(json.dumps(payload, indent=4)), "DEBUG")

        try:
            response = self.dnac._exec(
                family="backup",
                function="create_backup",
                op_modifies=True,
                params={"payload": payload}
            )
            self.log("Received API response from 'create_backup': {0}".format(response), "DEBUG")
            self.scheduled_backup.append(name)

            task_id = self.get_backup_task_id_from_response(response, "create_backup")
            status = self.get_backup_status_by_task_id(task_id)

            if status not in ["FAILED", "CANCELLED", "IN_PROGRESS"]:
                self.msg = "Backup schedule '{0}' created successfully.".format(name)
                self.set_operation_result("success", True, self.msg, "INFO")
                return self

            if status == "FAILED":
                self.msg = "Creation of backup schedule '{0}' failed".format(name)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            if status == "CANCELLED":
                self.msg = "Creation of backup schedule '{0}' was cancelled.".format(name)
                self.set_operation_result("failed", False, self.msg, "WARNING").check_return_status()

        except Exception as e:
            self.msg = "An error occurred while creating backup schedule: {0}".format(e)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def restore_backup(self):
        """
            Validates restore details and initiates backup restoration in Cisco Catalyst Center.

            Returns:
                self: The current instance with updated operation result status.

            Description:
                This method performs the following steps:
                    - Extracts restore details ('name' and 'encryption_passphrase') from 'self.want'.
                    - Validates input fields and ensures a backup with the specified name exists.
                    - Retrieves the configured backup encryption passphrase.
                    - Validates the input passphrase against the configured one.
                    - Constructs the payload and calls the 'restore_backup' API to start the restore operation.
                    - Monitors the task status to confirm success, failure, or cancellation.
                    - Sets the operation result based on the final status of the restore task.
        """
        self.log("Processing restoration for existing backup...", "INFO")
        restore_details = self.want.get("restore_details", [])

        for restore in restore_details:
            name = restore.get("name")
            encryption_passphrase = restore.get("encryption_passphrase")

            self.log("Validating restore details: name={0}, encryption_passphrase={1}".format(name, encryption_passphrase), "DEBUG")

            if not name or not encryption_passphrase:
                self.msg = "Both 'name' and 'encryption_passphrase' must be specified for restore."
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            backup_exists, current_backups, backup_schedules = self.get_backup()

            matched_schedule = None

            for backup in current_backups:
                self.log("Comparing backup name: '{0}' with expected: '{1}'".format(backup.get("name"), name), "DEBUG")
                if backup.get("name") == name:
                    matched_schedule = backup
                    break

            self.log("Matched backup schedule: {0}".format(matched_schedule), "DEBUG")

            if not matched_schedule:
                self.msg = "No backup found with the name '{0}'.".format(name)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            payload = {
                "name": name,
                "encryptionPassphrase": encryption_passphrase
            }

            self.log("Payload for restore operation: {0}".format(json.dumps(payload, indent=4)), "DEBUG")
            self.log("Initiating restore operation for backup '{0}'".format(name), "INFO")

            try:
                response = self.dnac._exec(
                    family="backup",
                    function="restore_backup",
                    op_modifies=True,
                    params={"payload": payload}
                )
                self.log("Received API response from 'restore_backup': {0}".format(response), "DEBUG")
                self.restored_backup.append(name)

                task_id = self.get_backup_task_id_from_response(response, "restore_backup")
                status = self.get_backup_status_by_task_id(task_id)

                if status not in ["FAILED", "CANCELLED", "IN_PROGRESS"]:
                    self.msg = "Restore operation for '{0}' completed successfully.".format(name)
                    self.set_operation_result("success", True, self.msg, "INFO")
                    return self

                if status == "FAILED":
                    self.msg = "Restore operation for '{0}' failed.".format(name)
                    self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

                if status == "CANCELLED":
                    self.msg = "Restore operation for '{0}' was cancelled.".format(name)
                    self.set_operation_result("failed", False, self.msg, "WARNING").check_return_status()

            except Exception as e:
                self.msg = "An error occurred while restoring backup: {0}".format(e)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def get_backup_task_id_from_response(self, response, api_name):
        """
            Extracts the task ID from the given API response dictionary.

            This method is used to retrieve the task ID associated with a backup-related operation
            (e.g., create or restore), which is later used to track the status of the task.

            Args:
                response (dict): The response returned from the Catalyst Center API call.
                api_name (str): The name of the API function for logging context.

            Returns:
                str or None: The extracted task ID if available; otherwise, None.
        """
        self.log("Extracting task ID from response of '{0}'.".format(api_name), "DEBUG")

        if not response or not isinstance(response, dict):
            self.log("Invalid or empty response received from '{0}'.".format(api_name), "ERROR")
            return None

        task_info = response.get("response", {})
        task_id = task_info.get("taskId")

        if not task_id:
            self.log("Task ID not found in response from '{0}'.".format(api_name), "ERROR")
            return None

        self.log("Extracted Task ID '{0}' from '{1}' response.".format(task_id, api_name), "DEBUG")
        return task_id

    def get_backup_status_by_task_id(self, task_id):
        """
            Polls the backup and restore execution status using the provided task ID.

            This method repeatedly queries the Cisco Catalyst Center API to retrieve the current execution
            status of a backup or restore operation. It continues polling until a terminal state is reached
            ('SUCCESS', 'FAILED', or 'CANCELLED'), or until the configured timeout period is exceeded.

            Args:
                task_id (str): The task ID associated with a backup or restore operation.

            Returns:
                str: The final status of the task. Possible values are:
                    - 'SUCCESS': The operation completed successfully.
                    - 'FAILED': The operation failed.
                    - 'CANCELLED': The operation was cancelled.
                    - 'UNKNOWN': No valid status could be determined (e.g., invalid task ID).
        """
        self.log("Checking backup status for task ID: {0}".format(task_id), "INFO")

        if not task_id:
            self.log("No task ID provided to get_backup_status_by_task_id.", "ERROR")
            return "UNKNOWN"

        start_time = time.time()

        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= self.max_timeout:
                self.msg = "Max timeout of {0} sec reached while waiting for backup task ID '{1}'.".format(self.max_timeout, task_id)
                self.log(self.msg, "WARNING")
                self.status = "failed"
                return "FAILED"

            try:
                response = self.dnac._exec(
                    family="backup",
                    function="get_backup_and_restore_execution",
                    params={"id": task_id}
                )

                self.log("Received API response from 'get_backup_and_restore_execution': {0}".format(response), "DEBUG")

                if isinstance(response, list):
                    response = response[0] if response else {}

                execution_data = response.get("response", {})
                status = execution_data.get("status", "UNKNOWN").upper()

                self.log("Backup execution status for task ID '{0}': '{1}'.".format(task_id, status), "DEBUG")

                if status in ["SUCCESS", "FAILED", "CANCELLED"]:
                    self.status = status.lower()
                    return status
                else:
                    self.log("Backup task ID '{0}' is still in progress. Status: '{1}'. Retrying...".format(task_id, status), "DEBUG")
                    time.sleep(5)

            except Exception as e:
                self.msg = "Error while retrieving status for task ID '{0}': {1}".format(task_id, str(e))
                self.log(self.msg, "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def delete_nfs_configuration(self):
        """
            Deletes an existing NFS configuration from Cisco Catalyst Center.

            Returns:
                self: Returns the instance with updated operation result.

            Description:
                - Validates that both 'server_ip' and 'source_path' are provided.
                - Checks if the NFS configuration exists in the current state.
                - If the configuration exists, it calls the API to delete it.
                - If the configuration does not exist, it logs a message and exits successfully.
        """
        self.log("Deleting NFS configuration(s)...", "INFO")

        desired_nfs_configs = self.want.get("nfs_configuration", [])
        current_nfs_configs = self.have.get("current_nfs_configurations", [])

        for nfs_config_details in desired_nfs_configs:
            server_ip = nfs_config_details.get("server_ip")
            source_path = nfs_config_details.get("source_path")

            if not server_ip or not source_path:
                self.msg = "Both 'server_ip' and 'source_path' must be specified to delete an NFS configuration."
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                continue

            self.log("Attempting to delete NFS configuration for server: {0}, path: {1}".format(server_ip, source_path), "DEBUG")

            nfs_to_delete = None
            for existing_config in current_nfs_configs:
                spec = existing_config.get("spec", {})
                if spec.get("server") == server_ip and spec.get("sourcePath") == source_path:
                    nfs_to_delete = existing_config
                    break

            if not nfs_to_delete:
                self.msg = "NFS configuration with server_ip '{0}' and source_path '{1}' does not exist in the Cisco Catalyst Center or has already been deleted.".format(
                    server_ip, source_path
                )
                self.set_operation_result("success", False, self.msg, "INFO")
                self.deleted_nfs_config.append(source_path)
                continue

            nfs_config_id = nfs_to_delete.get("id")
            if not nfs_config_id:
                self.msg = "Unable to retrieve ID for NFS configuration '{0}:{1}'.".format(server_ip, source_path)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                continue

            try:
                response = self.dnac._exec(
                    family="backup",
                    function="delete_n_f_s_configuration",
                    op_modifies=True,
                    params={"id": nfs_config_id},
                )

                self.log(
                    "Received API response from 'delete_n_f_s_configuration' for {0}:{1}: {2}".format(
                        server_ip, source_path, response
                    ),
                    "DEBUG",
                )
                self.deleted_nfs_config.append(source_path)

                if response:
                    self.msg = "NFS configuration deleted successfully for {0}:{1}".format(server_ip, source_path)
                    self.set_operation_result("success", True, self.msg, "INFO")
                    return self

                self.msg = "Failed to delete NFS configuration for {0}:{1}. API response: {2}".format(server_ip, source_path, response)
                self.set_operation_result("failed", False, self.msg, "ERROR")

            except Exception as e:
                self.msg = "Error occurred while deleting NFS configuration {0}:{1}: {2}".format(server_ip, source_path, e)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def delete_backup_schedule(self):
        """
            Deletes an existing backup schedule from Cisco Catalyst Center.

            Returns:
                self: Returns the instance with updated operation result.

            Description:
                - Validates that the 'name' of the backup schedule is provided in the desired state.
                - Checks if the backup schedule exists in the current state.
                - If the backup schedule exists, retrieves its ID and calls the API to delete it.
                - Monitors the deletion task until completion and updates the result accordingly.
                - If the schedule does not exist or is already deleted, logs an informational message and exits successfully.
                - Handles failures and unexpected task status with appropriate error messages.
        """
        self.log("Deleting backup schedule...", "INFO")

        backup_schedule_details = self.want.get("backup_schedule", [])
        self.log("Backup schedule details: {0}".format(backup_schedule_details), "INFO")

        backup_schedule = self.have
        self.log("Current backup schedule: {0}".format(backup_schedule), "DEBUG")

        name = backup_schedule_details[0].get("name")
        if not name:
            self.msg = "'name' must be specified to delete a backup schedule."
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.log("Checking backup schedule for name: {0}".format(name), "DEBUG")

        if backup_schedule.get("backup_exists") is False:
            self.msg = "Backup schedule with name '{0}' does not exist in the Cisco Catalyst Center or has already been deleted.".format(name)
            self.set_operation_result("success", False, self.msg, "INFO")
            return self

        schedule_id = backup_schedule.get("current_backup", {}).get("id")
        if not schedule_id:
            self.msg = "Unable to retrieve schedule ID for backup schedule '{0}'.".format(name)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        try:
            response = self.dnac._exec(
                family="backup",
                function="delete_backup",
                op_modifies=True,
                params={"id": schedule_id},
            )
            self.log("Received API response from 'delete_backup': {0}".format(response), "DEBUG")
            self.deleted_backup_schedule.append(name)

            task_id = self.get_backup_task_id_from_response(response, "delete_backup")
            status = self.get_backup_status_by_task_id(task_id)

            if status == "SUCCESS":
                self.msg = "Backup schedule '{0}' deleted successfully.".format(name)
                self.set_operation_result("success", True, self.msg, "INFO")
                return self

            elif status == "FAILED":
                self.msg = "Deletion of backup schedule '{0}' failed.".format(name)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            else:
                self.msg = "Unexpected deletion status '{0}' for backup schedule '{1}'.".format(status, name)
                self.set_operation_result("failed", False, self.msg, "WARNING").check_return_status()

        except Exception as e:
            self.msg = "An error occurred while deleting backup schedule: {0}".format(e)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def verify_diff_merged(self):
        """
            Verifies the successful creation of NFS configuration, backup schedule, and backup configuration
            in Cisco Catalyst Center by comparing the desired state with the current state.

            Returns:
                self: Returns the instance after performing verification and logging results.

            Description:
                - For each provided configuration type (NFS, backup schedule, backup configuration), fetches the current state.
                - Compares the current state (have) against the desired state (want).
                - Logs verification success if the configuration is found in the current state.
                - Logs a warning or info message if the configuration is not found, indicating a possible failure in execution.
        """
        self.log("Verification of creation and updation starts here...", "INFO")

        if self.want.get("nfs_configuration"):
            self.get_have()
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            nfs_configuration_exists = self.have.get("nfs_configuration_exists")
            desired_config = self.want.get("nfs_configuration", [])[0]
            server_ip = desired_config.get("server_ip")
            source_path = desired_config.get("source_path")

            if nfs_configuration_exists:
                self.msg = (
                    "The requested NFS configuration with server_ip '{0}' and source_path '{1}' is present in the "
                    "Cisco Catalyst Center and its creation has been verified.".format(server_ip, source_path)
                )
                self.log(self.msg, "INFO")
            else:
                self.msg = (
                    "The playbook input for NFS configuration with server_ip '{0}' and source_path '{1}' does not align with "
                    "the Cisco Catalyst Center, indicating that the creation task may not have executed successfully.".format(
                        server_ip, source_path
                    )
                )
                self.log(self.msg, "INFO")

        if self.want.get("backup_schedule"):
            self.get_have()
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            backup_schedule_exists = self.have.get("backup_exists")
            schedule = self.want.get("backup_schedule", [])[0]
            name = schedule.get("name")
            scope = schedule.get("scope")

            if backup_schedule_exists:
                self.msg = (
                    "The requested backup schedule with name '{0}' and scope '{1}' is present in the "
                    "Cisco Catalyst Center and its creation has been verified.".format(name, scope)
                )
                self.log(self.msg, "INFO")
            else:
                self.msg = (
                    "The playbook input for backup schedule with name '{0}' and scope '{1}' does not align with the "
                    "Cisco Catalyst Center, indicating that the creation task may not have executed successfully.".format(
                        name, scope
                    )
                )
                self.log(self.msg, "INFO")

        if self.want.get("backup_configuration"):
            self.get_have()
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            backup_config_exists = self.have.get("backup_configuration_exists")
            backup_config = self.want.get("backup_configuration", [])[0]
            server_ip = backup_config.get("server_ip")
            path = backup_config.get("path")

            if backup_config_exists:
                self.msg = (
                    "The requested backup configuration with server_ip '{0}' and path '{1}' is present in the "
                    "Cisco Catalyst Center and its creation has been verified.".format(server_ip, path)
                )
                self.log(self.msg, "INFO")
            else:
                self.msg = (
                    "The playbook input for backup configuration with server_ip '{0}' and path '{1}' does not align with the "
                    "Cisco Catalyst Center, indicating that the creation task may not have executed successfully.".format(
                        server_ip, path
                    )
                )
                self.log(self.msg, "WARNING")

        return self
    
    def verify_diff_deleted(self):
        """
            Verifies the successful deletion of NFS configuration and backup schedule
            from Cisco Catalyst Center by comparing the desired state with the current state.

            Returns:
                self: Returns the instance after performing verification and logging results.

            Description:
                - For each configuration type marked for deletion (NFS, backup schedule), fetches the current state.
                - Compares the current state (have) against the desired state (want).
                - Logs confirmation if the configuration is no longer present, verifying successful deletion.
                - Logs a warning if the configuration is still present, indicating the deletion may have failed.
                - Introduces a delay for backup schedule verification to allow for asynchronous cleanup on the backend.
        """
        self.log("Verification of deletion starts here...", "INFO")

        if self.want.get("nfs_configuration"):
            self.get_have()
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            nfs_config_exists = self.have.get("nfs_configuration_exists")
            nfs_details = self.want.get("nfs_configuration", [])[0]
            server_ip = nfs_details.get("server_ip")
            source_path = nfs_details.get("source_path")

            if not nfs_config_exists:
                self.msg = (
                    "The NFS configuration with server_ip '{0}' and source_path '{1}' is not present in Cisco Catalyst Center "
                    "and its deletion has been verified.".format(server_ip, source_path)
                )
                self.log(self.msg, "INFO")
            else:
                self.log(
                    "The playbook input for NFS configuration with server_ip '{0}' and source_path '{1}' does not align with Cisco Catalyst Center, "
                    "indicating that the merge task may not have executed deletion successfully.".format(server_ip, source_path),
                    "WARNING",
                )

        if self.want.get("backup_schedule"):
            time.sleep(120)
            self.get_have()
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            backup_exists = self.have.get("backup_exists")
            self.log("Backup exists: {0}".format(backup_exists), "DEBUG")
            backup_name = self.want.get("backup_schedule", [])[0].get("name")

            if not backup_exists:
                self.msg = (
                    "The backup schedule '{0}' is not present in Cisco Catalyst Center "
                    "and its deletion has been verified.".format(backup_name)
                )
                self.log(self.msg, "INFO")
            else:
                self.log(
                    "The playbook input for backup schedule '{0}' does not align with Cisco Catalyst Center, "
                    "indicating that the merge task may not have executed deletion successfully.".format(backup_name),
                    "WARNING",
                )

        return self
    
    def update_messages(self):
        self.result["changed"] = False
        result_msg_list = []
        no_update_list = []
        # === NFS CONFIGURATIONS ===
        if self.created_nfs_config:
            msg = "NFS Configuration(s) '{0}' created successfully in Cisco Catalyst Center.".format(
                "', '".join(self.created_nfs_config)
            )
            result_msg_list.append(msg)

        if self.already_exists_nfs_config:
            msg = "NFS Configuration(s) '{0}' already exist in Cisco Catalyst Center.".format(
                "', '".join(self.already_exists_nfs_config)
            )
            no_update_list.append(msg)

        if self.deleted_nfs_config:
            msg = "NFS Configuration(s) '{0}' deleted successfully from Cisco Catalyst Center.".format(
                "', '".join(self.deleted_nfs_config)
            )
            result_msg_list.append(msg)

        # === BACKUP CONFIGURATIONS ===
        if self.created_backup_config:
            msg = "Backup Configuration(s) '{0}' created successfully in Cisco Catalyst Center.".format(
                "', '".join(self.created_backup_config)
            )
            result_msg_list.append(msg)

        if self.already_exists_backup_config:
            msg = "Backup Configuration(s) '{0}' already exist in Cisco Catalyst Center.".format(
                "', '".join(self.already_exists_backup_config)
            )
            no_update_list.append(msg)

        if self.updated_backup_config:
            msg = "Backup Configuration(s) '{0}' updated successfully in Cisco Catalyst Center.".format(
                "', '".join(self.updated_backup_config)
            )
            result_msg_list.append(msg)

        # === BACKUP SCHEDULES ===
        if self.scheduled_backup:
            msg = "Backup Schedule(s) '{0}' created/scheduled successfully in Cisco Catalyst Center.".format(
                "', '".join(self.scheduled_backup)
            )
            result_msg_list.append(msg)

        if self.deleted_backup_schedule:
            msg = "Backup Schedule(s) '{0}' deleted successfully from Cisco Catalyst Center.".format(
                "', '".join(self.deleted_backup_schedule)
            )
            result_msg_list.append(msg)

        # === RESTORED BACKUPS ===
        if self.restored_backup:
            msg = "Backup(s) '{0}' restored successfully in Cisco Catalyst Center.".format(
                "', '".join(self.restored_backup)
            )
            result_msg_list.append(msg)


        if result_msg_list and no_update_list:
            self.result["changed"] = True
            self.msg = "{0} {1}".format(
                " ".join(result_msg_list), " ".join(no_update_list)
            )
        elif result_msg_list:
            self.result["changed"] = True
            self.msg = " ".join(result_msg_list)
        elif no_update_list:
            self.msg = " ".join(no_update_list)

        self.log(self.msg, "INFO")
        self.result["response"] = self.msg
        self.result["msg"] = self.msg

        return self

def main():
    """ main entry point for module execution """
    element_spec = {'dnac_host': {'required': True, 'type': 'str'},
                    'dnac_port': {'type': 'str', 'default': '443'},
                    'dnac_username': {'type': 'str', 'default': 'admin', 'aliases': ['user']},
                    'dnac_password': {'type': 'str', 'no_log': True},
                    'dnac_verify': {'type': 'bool', 'default': True},
                    'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
                    'dnac_debug': {'type': 'bool', 'default': False},
                    'dnac_log_level': {'type': 'str', 'default': 'WARNING'},
                    "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
                    "dnac_log_append": {"type": 'bool', "default": True},
                    'dnac_log': {'type': 'bool', 'default': False},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'config_verify': {'type': 'bool', "default": True},
                    'dnac_api_task_timeout': {'type': 'int', "default": 1200},
                    'dnac_task_poll_interval': {'type': 'int', "default": 2},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ["merged", "deleted"]}
                    }

    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=False)
    ccc_backup_restore = BackupRestore(module)
    state = ccc_backup_restore.params.get("state")

    current_version = ccc_backup_restore.get_ccc_version()
    min_supported_version = "3.1.3.0"

    if ccc_backup_restore.compare_dnac_versions(current_version, min_supported_version) < 0:
        ccc_backup_restore.status = "failed"
        ccc_backup_restore.msg = (
            "The specified version '{0}' does not support the 'Backup and restore' feature. "
            "Supported version(s) start from '{1}' onwards.".format(current_version, min_supported_version)
        )
        ccc_backup_restore.log(ccc_backup_restore.msg, "ERROR")
        ccc_backup_restore.check_return_status()

    if state not in ccc_backup_restore.supported_states:
        ccc_backup_restore.status = "invalid"
        ccc_backup_restore.msg = "State {0} is invalid".format(state)
        ccc_backup_restore.check_return_status()

    ccc_backup_restore.validate_input().check_return_status()
    config_verify = ccc_backup_restore.params.get("config_verify")

    for config in ccc_backup_restore.validated_config:
        ccc_backup_restore.reset_values()
        ccc_backup_restore.get_want(config).check_return_status()
        ccc_backup_restore.get_have().check_return_status()

        ccc_backup_restore.get_diff_state_apply[state](config)

        if config_verify:
            ccc_backup_restore.verify_diff_state_apply[state]().check_return_status()

    ccc_backup_restore.update_messages()
    module.exit_json(**ccc_backup_restore.result)


if __name__ == '__main__':
    main()

