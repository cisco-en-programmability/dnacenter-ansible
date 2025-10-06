# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Priyadharshini B", "Karthick S N", "Madhan Sankaranarayanan")

DOCUMENTATION = r"""
---
module: backup_and_restore_workflow_manager

short_description: >
  Resource module for comprehensive backup and restore workflow management with NFS server configuration in Cisco Catalyst Center.

description:
  - Automates comprehensive backup and restore workflow management in Cisco
    Catalyst Center including NFS server configuration, backup target setup,
    create backup, and restoration operations.
  - Enables NFS server configuration for secure backup storage with
    customizable port settings, protocol versions, and source path management.
  - Supports backup configuration with encryption, retention policies, and
    server type specification for enterprise data protection.
  - Facilitates backup restoration with encryption passphrase validation for
    secure data recovery operations.
  - Supports deletion operations for NFS configurations and backups
    to maintain clean backup infrastructure.
  - Integrates with Cisco Catalyst Center's backup framework for centralized
    network infrastructure data protection and disaster recovery.

version_added: "6.31.0"
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params

author:
  - Priyadharshini B (@pbalaku2)
  - Karthick S N (@kasn)
  - Madhan Sankaranarayanan (@madhansansel)

options:
  config_verify:
    description:
      - Set to True to verify the Cisco Catalyst Center after applying changes.
    type: bool
    default: true
  state:
    description:
      - Specifies the desired operational state for backup and restore
        configuration management.
      - Use C(merged) to create new backup configurations or update existing
        NFS settings, backups, and restoration parameters.
      - Use C(deleted) to remove NFS configurations, backups, or
        cleanup backup infrastructure components based on configuration
        provided.
      - Supports selective deletion for backup lifecycle management and
        infrastructure cleanup operations.
    type: str
    choices: ["merged", "deleted"]
    default: merged
  config:
    description:
      - List of comprehensive backup and restore configuration specifications
        including NFS server setup, backup target configuration, creating backup
        parameters, and restoration details.
      - Each configuration supports NFS server management, backup policy
        definition, backup creation, and restore operation parameters for
        enterprise backup infrastructure automation.
    type: list
    elements: dict
    required: true
    suboptions:
      nfs_configuration:
        description:
          - Configuration details for NFS backup server setup and management.
          - Defines NFS server connection parameters including IP address,
            source paths, port configurations, and protocol version settings
            for secure backup storage infrastructure.
        type: list
        elements: dict
        suboptions:
          server_ip:
            description:
              - IP address of the NFS server for backup storage connectivity.
              - Must be a valid IPv4 address accessible from Cisco Catalyst
                Center for backup operations.
            type: str
            required: true
          source_path:
            description:
              - Directory path on the NFS server designated for storing backup
                files and data.
              - Path must exist on the NFS server and have appropriate
                permissions for backup operations.
            type: str
            required: true
          nfs_port:
            description:
              - Port number used for NFS service communication and data
                transfer operations.
              - Must be accessible and not blocked by firewalls between
                Catalyst Center and NFS server.
            type: int
            default: 2049
          nfs_version:
            description:
              - NFS protocol version for backup storage communication.
              - Determines compatibility and security features available for
                backup operations.
            type: str
            default: nfs4
            choices: ["nfs3", "nfs4"]
          nfs_portmapper_port:
            description:
              - Port number for the NFS portmapper service on target server.
              - Used for dynamic port allocation and service discovery.
            type: int
            default: 111
      backup_storage_configuration:
        description:
          - Configuration for backup storage infrastructure and data management policies.
          - Sets up NFS storage targets, encryption, and data retention settings.
          - This configures WHERE and HOW backup data will be stored.
          - Does not create or execute backups, only prepares storage infrastructure.
        type: list
        elements: dict
        suboptions:
          server_type:
            description:
              - Type of backup storage server for data preservation.
              - Only NFS storage type is supported in Catalyst Center version 3.1.3.0.
              - PHYSICAL_DISK type is not supported in Catalyst Center version 3.1.3.0.
            type: str
            required: true
            choices: ["NFS", "PHYSICAL_DISK"]
          nfs_details:
            description:
              - Connection details for NFS backup targets including server
                information and storage path specifications.
              - Used to retrieve mount path for backup storage operations.
            type: dict
            suboptions:
              server_ip:
                description: IP address of the NFS server for backup operations.
                type: str
                required: true
              source_path:
                description: Directory path on the NFS server for backup storage.
                type: str
                required: true
              nfs_port:
                description: Port number used to access NFS services.
                type: int
              nfs_version:
                description: NFS protocol version for backup communication.
                type: str
                default: nfs4
                choices: ["nfs3", "nfs4"]
              nfs_portmapper_port:
                description: Port number for the NFS portmapper service.
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
              - Passphrase for encrypting backup data during storage operations.
              - Strongly recommended for secure data protection and compliance.
            type: str
      backup_job_creation:
        description:
          - Configuration for creating and executing backup jobs.
          - Creates backup jobs with specified name and data scope.
          - This CREATES and EXECUTES backups immediately (not scheduling).
          - Requires backup storage configuration to be set up first.
        type: list
        elements: dict
        suboptions:
          name:
            description:
              - Unique name for the backup identification.
              - Backup name must begin with an alphabet and can contain letters, digits,
                and the following special characters @, _, -, and space, #.
            type: str
            required: true
          scope:
            description:
              - Defines backup scope including assurance data specifications.
              - Determines what data types are included in backup operations.
            type: str
            choices: ["CISCO_DNA_DATA_WITH_ASSURANCE", "CISCO_DNA_DATA_WITHOUT_ASSURANCE"]
      restore_operations:
        description:
          - Parameters for restoring data from previously created backups
            including authentication and validation requirements.
        type: list
        elements: dict
        suboptions:
          name:
            description: Name of the backup to restore from available backup list.
            type: str
            required: true
          encryption_passphrase:
            description:
              - Passphrase for decrypting backup data during restore operations.
              - Must match the passphrase used during backup creation.
            type: str

requirements:
- dnacentersdk >= 2.9.3
- python >= 3.9.19

notes:
- Backup and restore functionality is available in Cisco Catalyst Center
  version 3.1.3.0 and later for comprehensive data protection workflow
- NFS server configuration must be completed and healthy before backup
  target configuration to ensure proper mount path availability
- backups support immediate execution and future scheduling with
  configurable scope for data inclusion requirements
- Backup and restore functionality requires encryption passphrases for secure
  data protection. Never hardcode these values in playbooks.
- Use Ansible Vault to encrypt sensitive backup configuration parameters
  including encryption passphrases and NFS server credentials.
- Store backup encryption passphrases in separate encrypted variable files
  (e.g., backup_secrets.yml) and decrypt during playbook execution.
- Consider using environment variables for backup credentials in CI/CD
  pipelines to avoid exposing sensitive data in version control.
- The same encryption passphrase used during backup creation must be
  provided during restore operations for successful data recovery.
- Encryption passphrases are automatically masked in logs when using
  no_log parameter specifications in the module documentation.
- Encryption passphrases used during backup creation must be identical
  to those provided during restore operations for successful data recovery
- Data retention periods are enforced automatically with cleanup occurring
  after the specified retention period expires (3-60 days)
- Backup and restore operations are asynchronous with task monitoring
  to track completion status and provide operational feedback
- NFS configurations require proper network connectivity and permissions
  between Catalyst Center and the target NFS server infrastructure
- Only NFS storage type is supported for backup targets in version 3.1.3.0
  with additional storage types planned for future releases.

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

# Example 1: Configure NFS server for backup storage infrastructure
- name: Configure NFS backup server for enterprise data protection
  hosts: localhost
  vars_files:
    - "credentials.yml"
    - "backup_secrets.yml"
  connection: local
  gather_facts: false
  tasks:
    - name: Configure NFS server for secure backup storage connectivity
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
              - server_ip: "{{ nfs_configuration.server_ip }}"
                source_path: "{{ nfs_configuration.source_path }}"
                nfs_port: 2049
                nfs_version: nfs4
                nfs_portmapper_port: 111

# Example 2: Configure backup target with encryption and retention policies
- name: Configure backup target for automated data protection workflow
  hosts: localhost
  vars_files:
    - "credentials.yml"
    - "backup_secrets.yml"
  connection: local
  gather_facts: false
  tasks:
    - name: Configure backup target with encryption and data retention policies
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
          - backup_storage_configuration:
              - server_type: NFS
                nfs_details:
                  server_ip: "{{ nfs_configuration.server_ip }}"
                  source_path: "{{ nfs_configuration.source_path }}"
                  nfs_port: 2049
                  nfs_version: nfs4
                  nfs_portmapper_port: 111
                data_retention_period: 51
                encryption_passphrase: "{{ backup_storage_configuration.encryption_passphrase }}"

# Example 3: Create backups for systematic data preservation
- name: Create backups for automated network infrastructure backup
  hosts: localhost
  vars_files:
    - "credentials.yml"
  connection: local
  gather_facts: false
  tasks:
    - name: Create backup with name and scope specifications
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
          - backup_job_creation:
              - name: BACKUP24_07
                scope: CISCO_DNA_DATA_WITHOUT_ASSURANCE

# Example 4: Restore backup for disaster recovery operations
- name: Restore backup for disaster recovery and data restoration
  hosts: localhost
  vars_files:
    - "credentials.yml"
    - "backup_secrets.yml"
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
          - restore_operations:
              - name: "BACKUP17_09"
                encryption_passphrase: "{{ restore_operations.encryption_passphrase }}"

# Example 5: Delete NFS configuration for infrastructure cleanup
- name: Remove NFS configuration from backup infrastructure
  hosts: localhost
  vars_files:
    - "credentials.yml"
  connection: local
  gather_facts: false
  tasks:
    - name: Delete NFS configuration from backup infrastructure
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
              - server_ip: "{{ nfs_configuration.server_ip }}"
                source_path: "{{ nfs_configuration.source_path }}"

# Example 6: Delete backups for lifecycle management
- name: Remove backups from automated backup operations
  hosts: localhost
  vars_files:
    - "credentials.yml"
  connection: local
  gather_facts: false
  tasks:
    - name: Delete backups for backup lifecycle management
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
          - backup_job_creation:
              - name: BACKUP24_07

# Example 7: Comprehensive backup workflow for enterprise deployment
- name: Complete backup and restore workflow for enterprise infrastructure
  hosts: localhost
  vars_files:
    - "credentials.yml"
  connection: local
  gather_facts: false
  tasks:
    - name: Configure comprehensive backup infrastructure with NFS and scheduling
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
              - server_ip: "{{ nfs_configuration.server_ip }}"
                source_path: "{{ nfs_configuration.source_path }}"
                nfs_port: 2049
                nfs_version: nfs4
                nfs_portmapper_port: 111
            backup_configuration:
              - server_type: NFS
                nfs_details:
                  server_ip: "{{ backup_storage_configuration.server_ip }}"
                  source_path: "{{ backup_storage_configuration.source_path }}"
                  nfs_port: 2049
                  nfs_version: nfs4
                  nfs_portmapper_port: 111
                data_retention_period: 30
                encryption_passphrase: Enterprise@Backup2024
            backup_job_creation:
              - name: ENTERPRISE_DAILY_BACKUP
                scope: CISCO_DNA_DATA_WITH_ASSURANCE

# Example 8: Multiple NFS server configuration for redundant backup storage
- name: Configure multiple NFS servers for backup redundancy
  hosts: localhost
  vars_files:
    - "credentials.yml"
  connection: local
  gather_facts: false
  tasks:
    - name: Configure primary and secondary NFS servers for backup redundancy
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
              - server_ip: "{{ nfs_configuration.server_ip }}"
                source_path: "{{ nfs_configuration.source_path }}"
                nfs_port: 2049
                nfs_version: nfs4
                nfs_portmapper_port: 111
              - server_ip: "{{ nfs_configuration.server_ip }}"
                source_path: "{{ nfs_configuration.source_path }}"
                nfs_port: 2049
                nfs_version: nfs4
                nfs_portmapper_port: 111
"""

RETURN = r"""

# Case 1: Successful NFS server configuration for backup storage
response_nfs_configuration_created:
  description:
    - Confirms successful creation of NFS server configuration for backup
      storage infrastructure in Cisco Catalyst Center.
    - Provides details about the configured NFS server path and connectivity
      status for backup operations.
  returned: when NFS configuration is successfully created
  type: dict
  sample:
    changed: true
    msg:  "NFS Configuration(s) '/home/nfsshare/backups/enterprise' created
          successfully in Cisco Catalyst Center."
    response: "NFS Configuration(s) '/home/nfsshare/backups/enterprise'
              created successfully in Cisco Catalyst Center."

# Case 2: Successful backup target configuration with encryption
response_backup_storage_configuration_created:
  description:
    - Confirms successful creation or update of backup target configuration
      including storage type, retention policies, and encryption settings.
    - Validates backup infrastructure readiness for automated data protection
      workflows in enterprise environments.
  returned: when backup configuration is successfully created or updated
  type: dict
  sample:
    changed: true
    msg: "Backup Configuration(s) '/home/nfsshare/backups/enterprise'
          created successfully in Cisco Catalyst Center."
    response: "Backup Configuration(s) '/home/nfsshare/backups/enterprise'
              created successfully in Cisco Catalyst Center."

# Case 3: Successful backups creation for automated operations
response_backup_created:
  description:
    - Confirms successful creation of backups for systematic data
      preservation with scope-based inclusion specifications.
    - Provides verification of backup operations for network
      infrastructure data protection and disaster recovery preparedness.
  returned: when backups is successfully created
  type: dict
  sample:
    changed: true
    msg: "Backup(s) 'ENTERPRISE_BACKUP_2024' created
          successfully in Cisco Catalyst Center."
    response: "Backup(s) 'ENTERPRISE_BACKUP_2024' created
              successfully in Cisco Catalyst Center."

# Case 4: Successful backup restoration for disaster recovery
response_backup_restored:
  description:
    - Confirms successful restoration of network infrastructure data from
      encrypted backup for disaster recovery operations.
    - Validates data recovery completion with encryption passphrase
      authentication for secure backup restoration workflows.
  returned: when backup restoration is successfully completed
  type: dict
  sample:
    changed: true
    msg: "Backup(s) 'enterprise_backup_20240315' restored successfully
          in Cisco Catalyst Center."
    response: "Backup(s) 'enterprise_backup_20240315' restored successfully
               in Cisco Catalyst Center."

# Case 5: Successful NFS configuration removal for infrastructure cleanup
response_nfs_configuration_deleted:
  description:
    - Confirms successful deletion of NFS server configuration from backup
      infrastructure for decommissioning or reconfiguration purposes.
    - Validates cleanup of backup storage connectivity for infrastructure
      lifecycle management and resource optimization.
  returned: when NFS configuration is successfully deleted
  type: dict
  sample:
    changed: true
    msg: "NFS Configuration(s) '/home/nfsshare/backups/legacy' deleted
          successfully from Cisco Catalyst Center."
    response: "NFS Configuration(s) '/home/nfsshare/backups/legacy' deleted
              successfully from Cisco Catalyst Center."

# Case 6: Successful backups removal for lifecycle management
response_backup_deleted:
  description:
    - Confirms successful deletion of backups from automated backup
      operations for schedule lifecycle management.
    - Provides verification of backups cleanup for operational
      efficiency and resource management in backup infrastructure.
  returned: when backups is successfully deleted
  type: dict
  sample:
    changed: true
    msg: "Backup(s) 'LEGACY_BACKUP_2023' deleted successfully
          from Cisco Catalyst Center."
    response: "Backup(s) 'LEGACY_BACKUP_2023' deleted successfully
              from Cisco Catalyst Center."

# Case 7: Configuration already exists - no changes required
response_no_changes_required:
  description:
    - Indicates that the requested backup and restore configuration already
      exists in the desired state, requiring no modifications.
    - Confirms idempotent operation completion with existing configuration
      validation for backup infrastructure consistency.
  returned: when configuration already exists in desired state
  type: dict
  sample:
    changed: false
    msg: "NFS Configuration(s) '/home/nfsshare/backups/existing' already
          exist in Cisco Catalyst Center."
    response: "NFS Configuration(s) '/home/nfsshare/backups/existing'
              already exist in Cisco Catalyst Center."

# Case 8: Operation failure with detailed error information
response_operation_failed:
  description:
    - Provides detailed error information when backup and restore operations
      fail due to validation, connectivity, or configuration issues.
    - Includes specific failure reasons for troubleshooting backup
      infrastructure problems and operational recovery guidance.
  returned: when operations fail due to errors or validation issues
  type: dict
  sample:
    changed: false
    failed: true
    msg: "Mount path not retrievable as NFS node is unhealthy for server IP '172.27.17.90',
          source path '/home/nfsshare/backups/TB19'."
    response: "Mount path not retrievable as NFS node is unhealthy for server IP '172.27.17.90',
              source path '/home/nfsshare/backups/TB19'."

"""

from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
)
from ansible.module_utils.basic import AnsibleModule

import time
import json
import re

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
        self.backup = []
        self.deleted_backup = []
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
                - 'nfs_configuration': Validates server IP, path, port, version (nfs3/nfs4), portmapper.
                - 'backup_storage_configuration': Validates server type, NFS details, retention period (3–60), passphrase.
                - 'backup': Validates backup name format and scope values.
                - 'restore_operations': Validates presence of backup name and encryption passphrase.
            - Validates allowed values, default values, and optional/mandatory constraints using 'validate_list_of_dicts'.
            - Logs both the input and the result of validation for traceability.
        """
        self.log("Validating backup and restore configuration...", "INFO")

        if not self.config:
            self.msg = "Backup and restore configuration is not available in playbook for validation"
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        if not isinstance(self.config, list):
            self.msg = "Backup configuration must be a list structure, found type: {0}".format(type(self.config))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        config_data = self.config

        for config_index, config_item in enumerate(self.config):
            if not isinstance(config_item, dict):
                self.msg = "Configuration item {0} must be dictionary structure, found type: {1}".format(
                    config_index + 1, type(config_item).__name__)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

        self.validated_config = self.config

        config_spec = {
            "nfs_configuration": {
                "type": "list",
                "elements": "dict",
                "server_ip": {
                    "type": "str",
                    "required": True
                },
                "source_path": {
                    "type": "str",
                    "required": True
                },
                "nfs_port": {
                    "type": "int",
                    "default": 2049,
                    "range_min": 1,
                    "range_max": 65535
                },
                "nfs_version": {
                    "type": "str",
                    "allowed_values": ["nfs3", "nfs4"],
                    "default": "nfs4"
                },
                "nfs_portmapper_port": {
                    "type": "int",
                    "default": 111,
                    "range_min": 1,
                    "range_max": 65535
                }
            },
            "backup_storage_configuration": {
                "type": "list",
                "elements": "dict",
                "server_type": {
                    "type": "str",
                    "required": True,
                    "allowed_values": ["NFS", "PHYSICAL_DISK"]
                },
                "nfs_details": {
                    "type": "dict",
                    "elements": "dict",
                    "server_ip": {
                        "type": "str",
                        "required": True
                    },
                    "source_path": {
                        "type": "str",
                        "required": True
                    },
                    "nfs_port": {
                        "type": "int",
                        "default": 2049,
                        "range_min": 1,
                        "range_max": 65535
                    },
                    "nfs_version": {
                        "type": "str",
                        "allowed_values": ["nfs3", "nfs4"],
                        "default": "nfs4"
                    },
                    "nfs_portmapper_port": {
                        "type": "int",
                        "default": 111,
                        "range_min": 1,
                        "range_max": 65535
                    }
                },
                "data_retention_period": {"type": "int", "range_min": 3, "range_max": 60},
                "encryption_passphrase": {"type": "str"},
            },
            "backup_job_creation": {
                "type": "list",
                "elements": "dict",
                "name": {
                    "type": "str",
                    "required": True
                },
                "scope": {
                    "type": "str",
                    "allowed_values": [
                        "CISCO_DNA_DATA_WITH_ASSURANCE",
                        "CISCO_DNA_DATA_WITHOUT_ASSURANCE"
                    ]
                },
            },
            "restore_operations": {
                "type": "list",
                "elements": "dict",
                "name": {
                    "type": "str",
                    "required": True
                },
                "encryption_passphrase": {
                    "type": "str",
                    "required": True
                }
            }
        }

        try:
            valid_config, invalid_params = validate_list_of_dicts(self.config, config_spec)

            if invalid_params:
                self.msg = "Configuration validation failed with invalid parameters: {0}".format(
                    invalid_params)
                self.set_operation_result("failed", False, self.msg, "ERROR")
                return self

            self.validated_config = valid_config

            self.log("Backup and restore configuration validation completed successfully", "INFO")
            self.log("Validated {0} configuration sections for workflow processing".format(
                len(valid_config)), "DEBUG")

            return self

        except Exception as validation_exception:
            self.msg = "Configuration validation encountered error: {0}".format(
                str(validation_exception))
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

    def get_want(self, config):
        """
        Extract the desired state ('want') from the backup and restore playbook block.

        Args:
            self (object): An instance of a class interacting with Cisco Catalyst Center.
            config (dict): A dictionary containing the playbook configuration, expected to include
                            one or more of the following keys:
                            - 'backup_storage_configuration'
                            - 'nfs_configuration'
                            - 'backup_job_creation'
                            - 'restore_operations'

        Returns:
            self: The current instance of the class with the 'want' attribute populated
                    based on the validated backup and restore configuration from the playbook.

        Description:
            This method processes the user-provided configuration to extract only the relevant
            sections required for backup and restore operations. Specifically, it performs the following steps:

            - Validates that at least one of the expected keys is present in the config.
            - Extracts values from 'backup_storage_configuration', 'nfs_configuration', 'backup_job_creation',
                and 'restore_operations', if present.
            - Logs the final desired state for visibility.
        """
        self.log("Extracting desired backup and restore workflow state from playbook configuration", "DEBUG")
        self.log("Processing configuration sections for comprehensive workflow validation", "DEBUG")

        want = {}
        backup_config = config.get("backup_storage_configuration")
        nfs_config = config.get("nfs_configuration")
        backup = config.get("backup_job_creation")
        restore_operations = config.get("restore_operations")

        config_sections = []
        if backup_config:
            config_sections.append("backup_storage_configuration")
        if nfs_config:
            config_sections.append("nfs_configuration")
        if backup:
            config_sections.append("backup_job_creation")
        if restore_operations:
            config_sections.append("restore_operations")

        self.log("Available configuration sections: {0}".format(", ".join(config_sections) if config_sections else "none"), "DEBUG")

        if not any([backup_config, nfs_config, backup, restore_operations]):
            self.msg = (
                "Backup and restore workflow requires at least one configuration section: "
                "'backup_storage_configuration', 'nfs_configuration', 'backup_job_creation', or 'restore_operations'"
            )
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        want = {
            "backup_storage_configuration": backup_config,
            "backup_job_creation": backup,
            "restore_operations": restore_operations,
            "nfs_configuration": nfs_config
        }

        self.want = want
        self.log("Backup and restore workflow desired state extraction completed successfully", "DEBUG")
        self.log("Extracted {0} configuration sections for workflow processing".format(len(config_sections)), "DEBUG")
        return self

    def get_nfs_configuration_details(self):
        """
        Retrieves all NFS server configurations for backup storage infrastructure validation.

        This method fetches comprehensive NFS configuration data from Cisco Catalyst Center
        to support backup workflow operations including server connectivity validation,
        mount path verification, and configuration matching for backup target setup.

        Args:
            self (object): An instance of a class interacting with Cisco Catalyst Center.

        Returns:
            list: Complete list of current NFS configurations from Catalyst Center
                  containing server specifications, mount paths, and health status.
                  Returns empty list if no configurations exist or on API failure.
        Description:
            This method evaluates the desired NFS configuration from the playbook-provided input and attempts to
            locate a matching NFS configuration from Catalyst Center.

            It performs the following operations:
            - Parses the 'server_ip' and 'source_path' from either:
                - The first item in 'nfs_configuration', or
                - The nested 'nfs_details' under 'backup_storage_configuration'.
            - Calls the Catalyst Center API ('get_all_n_f_s_configurations') to retrieve existing NFS configurations.
            - Validates the API response structure and logs it for traceability.
            - Iterates through existing NFS configs to find a match based on both 'server' and 'sourcePath' fields.
        """
        self.log("Retrieving NFS server configurations for backup infrastructure validation", "DEBUG")
        self.log("Executing API call to fetch all existing NFS configurations from Catalyst Center", "DEBUG")

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
                self.log("Invalid NFS configuration API response structure - missing required response field", "ERROR")
                self.log("Received response data: {0}".format(response), "ERROR")
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            current_nfs_configs = response.get("response", [])

        except Exception as e:
            self.msg = "An error occurred while retrieving all NFS configuration details: {0}".format(e)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.log("Retrieved {0} NFS configurations for backup infrastructure evaluation".format(
            len(current_nfs_configs)), "DEBUG")

        return current_nfs_configs

    def get_backup_configuration(self):
        """
        Retrieves and validates backup target configuration for enterprise data protection.

        This method fetches current backup configuration from Cisco Catalyst Center
        and performs validation against desired backup settings including server type,
        NFS connectivity details, and storage path specifications for backup
        infrastructure verification and configuration management.

        Args:
            self (object): An instance of a class interacting with Cisco Catalyst Center.

        Returns:
            tuple: Contains backup configuration status and data:
                - backup_configuration_exists (bool): Whether backup configuration
                exists in Catalyst Center
                - current_backup_configuration (dict): Current backup settings
                retrieved from system
                - matched_config (dict): Matched configuration if server and path
                align with desired state

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

        backup_config_list = self.want.get("backup_storage_configuration", [])
        expected_server_type = expected_server_ip = expected_source_path = None

        if backup_config_list and isinstance(backup_config_list, list):
            backup_config = backup_config_list[0]
            expected_server_type = backup_config.get("type")
            nfs_details = backup_config.get("nfs_details", {})
            expected_server_ip = nfs_details.get("server_ip")
            expected_source_path = nfs_details.get("source_path")

        self.log("Retrieving backup target configuration for enterprise data protection validation", "DEBUG")
        self.log("Expected backup configuration - server_type: {0}, server_ip: {1}, source_path: {2}".format(
            expected_server_type, expected_server_ip, expected_source_path), "DEBUG")

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

            self.log("Backup configuration exists in system: {0}".format(backup_configuration_exists), "DEBUG")

            if expected_server_type and expected_server_type.upper() == "NFS":
                self.log("Validating NFS backup configuration against desired state", "DEBUG")

                current_server = current_backup_configuration.get("server")
                current_path = current_backup_configuration.get("sourcePath")

                self.log("Current NFS configuration - server: {0}, sourcePath: {1}".format(
                    current_server, current_path), "DEBUG")

                if current_server == expected_server_ip and current_path == expected_source_path:
                    matched_config = current_backup_configuration
                    self.log("Backup configuration successfully matched with desired NFS settings", "DEBUG")
                else:
                    self.log("Backup configuration does not match desired NFS settings", "DEBUG")

        except Exception as e:
            self.msg = "An error occurred while retrieving the backup configuration details: {0}".format(e)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        return backup_configuration_exists, current_backup_configuration, matched_config

    def get_backup(self):
        """
        Retrieves and validates backups for enterprise data protection management.

        This method fetches existing backups from Cisco Catalyst Center
        and performs validation against desired backups configuration
        including name matching and schedule status verification for backup
        infrastructure planning and schedule management operations.

        Args:
            self (object): An instance of a class interacting with Cisco Catalyst Center.

        Returns:
            tuple: Contains backups status and data:
                - backup_exists (bool): Whether any backups exist in the system
                - current_backups (list): Complete list of backups
                    retrieved from Catalyst Center
                - matched_config (dict): Matched backups configuration
                    by name if found

        Description:
            This method processes the desired backups configuration from the playbook input
            and attempts to identify a matching backup from Catalyst Center.

            Specifically, it performs the following operations:
            - Extracts the 'name' field from the first entry in the 'backup' section of the 'want' state.
            - Invokes the 'get_all_backup' API to retrieve the list of all backups from Catalyst Center.
            - Validates the structure of the API response.
            - Iterates through the list of backups to find an entry with a matching name.
            - Logs and returns the matched backup configuration, if found.
        """
        self.log("Retrieving backup details...", "DEBUG")

        backup_exists = False
        current_backups = []
        matched_config = {}

        backup_list = self.want.get("backup_job_creation", [])
        expected_backup_name = None

        if backup_list and isinstance(backup_list, list):
            backup = backup_list[0]
            expected_backup_name = backup.get("name")

        self.log("Retrieving backups for enterprise data protection validation", "DEBUG")
        self.log("Expected backups name: {0}".format(expected_backup_name), "DEBUG")

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

            self.log("Retrieved {0} backups for validation".format(len(current_backups)), "DEBUG")
            self.log("backups exist in system: {0}".format(backup_exists), "DEBUG")

            if expected_backup_name:
                self.log("Searching for backups with name: {0}".format(expected_backup_name), "DEBUG")

                for backup in current_backups:
                    current_backup_name = backup.get("name")
                    if current_backup_name == expected_backup_name:
                        matched_config = backup
                        self.log("Successfully matched backups configuration by name", "DEBUG")
                        break

                if not matched_config:
                    self.log("No backups found with name: {0}".format(expected_backup_name), "DEBUG")
            else:
                self.log("No backups name specified for matching", "DEBUG")

        except Exception as e:
            self.log(
                "An error occurred while retrieving backups: {0}".format(e),
                "ERROR"
            )

        return backup_exists, current_backups, matched_config

    def get_have(self):
        """
        Retrieves current backup infrastructure state for enterprise workflow validation.

        This method fetches comprehensive current state information from Cisco Catalyst
        Center including NFS server configurations, backup target settings, and backup
        details for comparison against desired state in backup and restore
        workflow management operations.

        Args:
            self (object): An instance of a class interacting with Cisco Catalyst Center.

        Returns:
            self: The current instance with the 'have' attribute populated with actual system state details
                including NFS configuration, backup configuration, and backups.

        Description:
            This method evaluates the desired configuration ('want') and gathers corresponding current state
            ('have') from Cisco Catalyst Center.

            Specifically, it performs the following actions:
                - If 'nfs_configuration' is provided in the desired state:
                    - Calls 'get_nfs_configuration_details()' to fetch and match the NFS config.
                    - Extracts and stores the matched configuration and its existence flag.
                - If 'backup_storage_configuration' is present:
                    - Calls 'get_backup_configuration()' to retrieve the existing backup config.
                    - Stores the matched configuration and existence flag.
                - If 'backup_job_creation' is provided:
                    - Calls 'get_backup()' to retrieve and match backups by name.
                    - Stores the matched backup and its existence flag.
                - If 'restore_operations' is provided:
                    - Logs that restore processing is initiated, though no current state is retrieved for it.
        """
        self.log("Retrieving current backup infrastructure state for enterprise workflow validation", "DEBUG")
        self.log("Processing desired configuration sections for current state comparison", "DEBUG")
        have = {}
        self.log("Fetching NFS server configurations for backup storage validation", "DEBUG")

        current_nfs_configs = self.get_nfs_configuration_details()
        have["current_nfs_configurations"] = current_nfs_configs
        self.log("Retrieved {0} NFS configurations for backup infrastructure evaluation".format(
            len(current_nfs_configs)), "DEBUG")

        backup_configuration_details = self.want.get("backup_storage_configuration", [])

        if backup_configuration_details:
            self.log("Retrieving current backup target configuration for validation", "DEBUG")
            backup_configuration_exists, current_backup_config, matched_backup = self.get_backup_configuration()
            have["backup_configuration_exists"] = bool(current_backup_config)
            have["current_backup_configuration"] = current_backup_config if current_backup_config else {}

            self.log("Backup configuration exists in system: {0}".format(
                have["backup_configuration_exists"]), "DEBUG")
            self.log("Current backup configuration details retrieved for comparison", "DEBUG")

        backup_details = self.want.get("backup_job_creation", [])
        if backup_details:
            self.log("Retrieving current backup information for validation", "DEBUG")
            backup_exists, current_backups, matched_backup = self.get_backup()
            matched_exists = isinstance(matched_backup, dict) and matched_backup.get("name")
            have["backup_exists"] = bool(matched_exists)
            have["current_backup"] = matched_backup if matched_exists else {}

            self.log("Backup exists in system: {0}".format(have["backup_exists"]), "DEBUG")
            self.log("Current backup details retrieved for comparison", "DEBUG")

        restore_operations = self.want.get("restore_operations", [])
        if restore_operations:
            self.log("Processing restore operation context for backup workflow validation", "DEBUG")
            self.log("Processing restore details...", "DEBUG")

        self.have = have

        self.log("Current backup infrastructure state retrieval completed successfully", "DEBUG")
        self.log("Retrieved state includes {0} configuration sections for validation".format(
            len([k for k in have.keys() if have[k]])), "DEBUG")
        return self

    def get_diff_merged(self, config):
        """
        Processes backup workflow configuration for merged state operations.

        This method orchestrates comprehensive backup and restore workflow processing
        by analyzing desired configuration sections and triggering appropriate diff
        computations for NFS server setup, backup target configuration, backup
        scheduling, and restore operations in enterprise data protection workflows.

        Args:
            self (object): An instance of the class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing the desired state for:
                        - NFS configuration
                        - Backup configuration
                        - backup create
                        - Restore details

        Returns:
            self: The current instance of the class, with updated diff state for each applicable configuration section.

        Description:
            This method processes the configuration details provided in the playbook for Catalyst Center backup and restore workflows.
            It checks for the presence of specific configuration options—such as NFS configuration, backup configuration, backup create,
            and restore details—and triggers corresponding diff methods for each section:

            - 'get_diff_nfs_configuration()': Validates and computes the difference between current and desired NFS settings.
            - 'get_diff_backup_configuration()': Handles comparison for backup configuration profiles.
            - 'get_diff_backup()': Evaluates the defined backups settings.
            - 'get_diff_restore_backup()': Verifies restore parameters and validates their applicability.

            These methods compare the desired state (from 'self.want') with the current state (from 'self.have') and determine
            what changes (if any) need to be made. The result is used later in execution to decide whether a configuration
            update or restore action is required.

            The method also logs the progress of each configuration section for traceability and debugging purposes.
            """
        self.log("Processing backup workflow configuration for merged state operations", "DEBUG")
        self.log("Configuration sections for processing: {0}".format(
            ", ".join([k for k in config.keys() if config.get(k)])), "DEBUG")

        self.config = config

        if config.get("nfs_configuration"):
            self.log("Processing NFS server configuration for backup storage validation", "DEBUG")
            self.get_diff_nfs_configuration()

        if config.get("backup_storage_configuration"):
            self.log("Processing backup target configuration for data protection workflow", "DEBUG")
            self.get_diff_backup_configuration()

        if config.get("backup_job_creation"):
            self.log("Processing backup details...", "INFO")
            self.get_diff_backup()

        if config.get("restore_operations"):
            self.log("Processing restore operation configuration for disaster recovery workflow", "DEBUG")
            self.get_diff_restore_backup()

        self.log("Backup workflow configuration processing completed for merged state", "DEBUG")
        return self

    def get_diff_deleted(self, config):
        """
        Processes backup infrastructure deletion requests for cleanup operations.

        This method orchestrates comprehensive backup and NFS component removal
        by analyzing configuration sections marked for deletion and triggering
        appropriate cleanup workflows for NFS server configurations and backups
        in enterprise backup infrastructure lifecycle management.

        Args:
            self (object): An instance of the class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration dictionary containing the details for NFS configuration and backups
                        that are marked for deletion.

        Returns:
            self: The current instance of the class, with updated 'result' and 'have' attributes reflecting deletion operations.

        Description:
            This method analyzes the playbook configuration to determine which backup and NFS components should be removed
            from the Catalyst Center. It checks for keys like 'nfs_configuration' and 'backup' and invokes the
            appropriate deletion workflows:

            - 'delete_nfs_configuration()': Initiates deletion of the specified NFS configuration.
            - 'delete_backup()': Triggers removal of backups if they exist.

            Each operation is logged for traceability and debugging. The outcomes from these deletion tasks are used to
            update internal tracking attributes like 'result', which determines if a change occurred ('changed: True')
            during execution.
            """
        self.log("Processing backup infrastructure deletion requests for cleanup operations", "DEBUG")
        self.log("Configuration sections for deletion: {0}".format(
            ", ".join([k for k in config.keys() if config.get(k)])), "DEBUG")

        self.config = config

        if config.get("nfs_configuration"):
            self.log("Processing NFS server configuration deletion for infrastructure cleanup", "DEBUG")
            self.delete_nfs_configuration()

        if config.get("backup_job_creation"):
            self.log("Processing backup details for deletion...", "INFO")
            self.delete_backup()

        self.log("Backup infrastructure deletion processing completed successfully", "DEBUG")
        return self

    def get_diff_nfs_configuration(self):
        """
        Validates and manages NFS server configuration for backup storage infrastructure.

        This method processes desired NFS server configurations against current state
        to determine necessary actions for backup storage infrastructure setup. It
        ensures only missing NFS configurations are created while avoiding duplicates
        and validates connectivity specifications for enterprise data protection workflows.

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
        expected_nfs_configs = self.want.get("nfs_configuration", [])

        self.log("Processing NFS server configurations for backup storage infrastructure validation", "DEBUG")
        self.log("Expected NFS configurations: {0}, Current NFS configurations: {1}".format(
            len(expected_nfs_configs), len(current_nfs_configs)), "DEBUG")

        for config_index, nfs_config_details in enumerate(expected_nfs_configs):
            server_ip = nfs_config_details.get("server_ip")
            source_path = nfs_config_details.get("source_path")
            self.log("Processing NFS configuration {0}: server_ip={1}, source_path={2}".format(
                config_index + 1, server_ip, source_path), "DEBUG")

            if not server_ip or not source_path:
                self.msg = ("NFS configuration validation failed: Both 'server_ip' and 'source_path' "
                            "must be specified for backup storage infrastructure setup")
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                continue

            self.log("Searching for existing NFS configuration matching server: {0}, path: {1}".format(
                server_ip, source_path), "DEBUG")

            nfs_configuration_found = False
            for existing_config in current_nfs_configs:
                spec = existing_config.get("spec", {})
                existing_server = spec.get("server")
                existing_path = spec.get("sourcePath")

                self.log("Comparing with existing NFS: server={0}, path={1}".format(
                    existing_server, existing_path), "DEBUG")

                if existing_server == server_ip and existing_path == source_path:
                    nfs_configuration_found = True
                    self.log("Found matching NFS configuration for backup storage infrastructure", "DEBUG")
                    break

            if not nfs_configuration_found:
                self.log("NFS configuration not found - initiating creation for backup storage infrastructure", "DEBUG")
                self.log("Creating NFS server configuration for server '{0}' with source path '{1}'".format(
                    server_ip, source_path), "INFO")
                self.create_nfs_configuration(nfs_config_details)

            else:
                self.msg = ("NFS server configuration already exists for server_ip '{0}' "
                            "and source_path '{1}' in backup storage infrastructure").format(
                    server_ip, source_path)
                self.already_exists_nfs_config.append(source_path)
                self.set_operation_result("success", False, self.msg, "INFO")

        self.log("NFS server configuration processing completed for backup storage infrastructure", "DEBUG")
        return self

    def get_diff_backup_configuration(self):
        """
        Validates and manages the creation or update of backup configuration in Cisco Catalyst Center.

        This method processes desired backup target configurations against current state
        to determine necessary actions for backup infrastructure setup. It ensures proper
        NFS connectivity validation, mount path retrieval, and configuration updates for
        enterprise backup and restore workflows.

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

        expected_backup_configs = self.want.get("backup_storage_configuration", [])
        backup_configuration = self.have

        self.log("Processing backup target configurations for enterprise data protection validation", "DEBUG")
        self.log("Expected backup configurations: {0}".format(len(expected_backup_configs)), "DEBUG")

        # Process each desired backup configuration for enterprise data protection
        for config_index, backup_config_details in enumerate(expected_backup_configs):
            nfs_details = backup_config_details.get("nfs_details", {})
            server_ip = nfs_details.get("server_ip")
            source_path = nfs_details.get("source_path")

            self.log("Processing backup configuration {0}: server_ip={1}, source_path={2}".format(
                config_index + 1, server_ip, source_path), "DEBUG")

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

                    self.log("Comparing NFS config: server={0}, path={1}".format(
                        current_nfs_server, current_nfs_source_path), "DEBUG")

                    if (server_ip == current_nfs_server and source_path == current_nfs_source_path):
                        nfs_exists = True
                        matched_config = current_nfs_config_item
                        self.log("Found matching NFS configuration for backup target", "DEBUG")
                        break

            self.log("NFS exists: {0}".format(nfs_exists), "DEBUG")

            if not nfs_exists:
                self.log("NFS mount path not found for {0}:{1}, attempting to create/verify NFS configuration.".format(server_ip, source_path), "INFO")
                self.create_nfs_configuration(nfs_details)

            if nfs_exists:
                unhealthy_nodes = matched_config.get("status", {}).get("unhealthyNodes") if matched_config else None
                self.log("NFS node health status - unhealthy nodes: {0}".format(unhealthy_nodes), "DEBUG")
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
                    self.log("NFS node is healthy - retrieving mount path for backup configuration", "DEBUG")
                    mount_path = matched_config.get("status", {}).get("destinationPath") if matched_config else None
                    self.log("Retrieved mount path: {0}".format(mount_path), "DEBUG")

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

            self.log("Comparing backup parameters - server_type: {0}=={1}, retention: {2}=={3}, mount_path: {4}=={5}".format(
                config_server_type, current_type, config_retention, current_retention, mount_path, current_mount_path), "DEBUG")

            if (
                config_server_type == current_type and
                config_retention == current_retention and
                mount_path == current_mount_path
            ):
                self.msg = (
                    "Backup configuration already exists with desired settings for source path '{0}'".format(source_path)
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

        self.log("Backup target configuration processing completed for enterprise data protection", "DEBUG")
        return self

    def get_diff_backup(self):
        """
        Validates and manages the creation of a backups in Cisco Catalyst Center.

        Args:
            self (object): An instance of the class responsible for backup and restore workflows.

        Returns:
            self: The current instance with updated result based on the success or failure of the backups logic.

        Description:
            This method checks the desired backups configuration ('self.want') against the existing
            backup configuration ('self.have') to determine whether a new backup needs to be created.

            For each backups provided:
                - It ensures that both the 'name' and 'scope' fields are specified.
                - If these mandatory fields are missing, the operation fails with an appropriate error message.
                - If the backups does not exist ('backup_exists' is False), it initiates the creation
                of the backups.
                - If the backup already exists, no changes are made, and an informational success message is logged.
        """
        self.log("Processing backups details...", "INFO")

        backup = self.have

        for backup_details in self.want.get("backup_job_creation", []):
            name = backup_details.get("name")
            scope = backup_details.get("scope")

            if not name or not scope:
                self.msg = (
                    "Mandatory fields 'name', 'scope' must be specified for backups."
                )
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            self.log(
                "Checking backups for name: {0}, scope: {1}".format(
                    name, scope
                ),
                "DEBUG",
            )

            if not backup.get("backup_exists"):
                self.log(
                    "backups does not exist. Initiating creation process.",
                    "INFO",
                )
                self.create_backup(backup_details)
                continue

            else:
                self.msg = (
                    "Backup '{0}' already exists.".format(
                        name
                    )
                )
                self.already_backup_exists.append(name)
                self.set_operation_result("success", False, self.msg, "INFO")
                return self

    def get_diff_restore_backup(self):
        """
        Validates and manages backup restoration operations for disaster recovery workflows.

        This method processes desired backup restoration requests against available backups
        to determine restoration feasibility and initiate recovery operations. It ensures
        proper validation of restore parameters including backup existence, encryption
        credentials, and restoration prerequisites for enterprise disaster recovery.

        Args:
            self (object): An instance of the class handling backup and restore workflows.

        Returns:
            self: The current instance with updated result after attempting restore operation(s).

        Description:
            This method processes the restore configuration provided in 'self.want["restore_operations"]'.

            For each restore entry:
            - It checks for the presence of mandatory fields 'name' and 'encryption_passphrase'.
            - If either field is missing, the operation fails with an appropriate error message.
            - If both fields are present, it logs the action and initiates the restore operation.
        """
        self.log("Processing restore details...", "INFO")

        expected_restore_details = self.want.get("restore_operations", [])

        self.log("Processing backup restoration requests for disaster recovery workflows", "DEBUG")
        self.log("Expected restore operations: {0}".format(len(expected_restore_details)), "DEBUG")

        if not expected_restore_details:
            self.log("No restore operations specified - skipping restoration processing", "DEBUG")
            return self

        # Process each restore request for validation and execution
        for restore_index, restore_detail in enumerate(expected_restore_details):
            backup_name = restore_detail.get("name")
            encryption_passphrase = restore_detail.get("encryption_passphrase")

            self.log("Processing restore operation {0}: backup_name={1}".format(
                restore_index + 1, backup_name), "DEBUG")

            if not backup_name or not encryption_passphrase:
                self.msg = ("Restore operation validation failed: Both 'name' and 'encryption_passphrase' "
                            "must be specified for backup restoration and disaster recovery")
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            self.log("Initiating restore for backup name: {0}".format(backup_name), "INFO")
            self.restore_backup()

        self.log("Backup restoration processing completed for disaster recovery workflows", "DEBUG")
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
        self.log(
            "Starting backup configuration creation for server_type={0}, retention={1}".format(
                backup_config_details.get("server_type"),
                backup_config_details.get("data_retention_period")
            ),
            "INFO"
        )

        mandatory_fields = ["server_type", "nfs_details", "data_retention_period", "encryption_passphrase"]
        for field in mandatory_fields:
            if field not in backup_config_details:
                self.msg = "Mandatory field '{0}' is missing in backup configuration.".format(field)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        nfs_details = backup_config_details.get("nfs_details", {})
        server_ip = nfs_details.get("server_ip")
        source_path = nfs_details.get("source_path")

        self.log(
            "Extracted NFS details for backup configuration: server_ip={0}, source_path={1}".format(
                server_ip, source_path
            ),
            "DEBUG"
        )

        if not server_ip or not source_path:
            self.msg = "Both 'server_ip' and 'source_path' must be specified in NFS details."
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        current_nfs_configs = self.get_nfs_configuration_details()
        matched_config = None
        for config in current_nfs_configs:
            spec = config.get("spec", {})
            if spec.get("server") == server_ip and spec.get("sourcePath") == source_path:
                matched_config = config
                self.log(
                    "Found existing NFS configuration for server_ip={0}, source_path={1}. Using existing mount path."
                    .format(server_ip, source_path),
                    "INFO"
                )
                break

        mount_path = None
        if matched_config:
            mount_path = matched_config.get("status", {}).get("destinationPath")

        if not mount_path:
            self.log(
                "NFS mount path not found for server_ip={0}, source_path={1}. Attempting to create/verify NFS configuration."
                .format(server_ip, source_path),
                "INFO"
            )
            try:
                self.create_nfs_configuration(nfs_details)

                current_nfs_configs_after_create = self.get_nfs_configuration_details()
                matched_config_after_create = None
                for config in current_nfs_configs_after_create:
                    spec = config.get("spec", {})
                    if spec.get("server") == server_ip and spec.get("sourcePath") == source_path:
                        matched_config_after_create = config
                        self.log(
                            "Found newly created NFS configuration for server_ip={0}, source_path={1}."
                            .format(server_ip, source_path),
                            "INFO"
                        )
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
            self.msg = "Failed to retrieve NFS destination path even after creation/verification."
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

        self.log(
            "Completed backup configuration creation for server_ip={0}, source_path={1}".format(
                server_ip, source_path
            ),
            "INFO"
        )
        return self

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
                    - nfs_portmapper_port (int): Port number for the portmapper service.

        Returns:
            self: The current class instance with updated operation result.

        Description:
            - Validates presence of mandatory fields ('server_ip', 'source_path').
            - Constructs a payload with optional fields if provided.
            - Sends the configuration to Catalyst Center using the 'create_n_f_s_configuration' API.
            - Logs API responses and updates the operation result accordingly.
        """
        self.log(
            "Starting NFS configuration creation for server_ip={0}, source_path={1}".format(
                nfs_config_details.get("server_ip"), nfs_config_details.get("source_path")
            ),
            "INFO"
        )

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
            ("nfs_portmapper_port", "portMapperPort"),
        ]

        self.log("Adding optional fields to NFS payload", "DEBUG")
        for field, key in optional_fields:
            value = nfs_config_details.get(field)
            if value is not None:
                payload[key] = (
                    int(value)
                    if field in ("nfs_port", "nfs_portmapper_port")
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
                self.msg = (
                    "NFS configuration created successfully for server {0} "
                    "with source_path {1}".format(
                        nfs_config_details["server_ip"],
                        nfs_config_details["source_path"]
                    )
                )
                self.set_operation_result("success", True, self.msg, "INFO")
                return self

        except Exception as e:
            self.msg = "An error occurred while creating NFS configuration: {0}".format(e)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.log(
            "Exiting NFS configuration creation for server_ip={0}, source_path={1}".format(
                nfs_config_details.get("server_ip"), nfs_config_details.get("source_path")
            ),
            "INFO"
        )

        return self

    def create_backup(self, backup_details):
        """
        Validates and creates a backups in Cisco Catalyst Center.

        Args:
            backup_details (dict): Dictionary containing backups details.
                Mandatory fields:
                    - name (str): Name of the backups. Must start with an alphabet
                    and can include alphanumeric characters and special characters
                    (@, #, _, -, space).
                    - scope (str): Scope of the backups (e.g., "SYSTEM").

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
        self.log("Creating backups: {0}".format(backup_details), "INFO")

        name_pattern = r"^[A-Za-z][A-Za-z0-9@#_\-]*$"

        name = backup_details.get("name")
        self.log("Validating backups name: {0}".format(name), "DEBUG")
        if not re.match(name_pattern, name):
            self.msg = (
                "Backup name must begin with an alphabet and can contain letters, digits, "
                "and the following special characters: @, #, _, -, and space."
            )
            self.set_operation_result(
                "failed", False, self.msg, "ERROR"
            ).check_return_status()

        scope = backup_details.get("scope")

        if not name or not scope:
            self.msg = "Mandatory fields 'name' and 'scope' must be specified for backups."
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        payload = {
            "name": name,
            "scope": scope,
        }

        self.log("Generated payload for create backups: {0}".format(json.dumps(payload, indent=4)), "DEBUG")

        try:
            response = self.dnac._exec(
                family="backup",
                function="create_backup",
                op_modifies=True,
                params={"payload": payload}
            )
            self.log("Received API response from 'create_backup': {0}".format(response), "DEBUG")
            self.backup.append(name)

            task_id = self.get_backup_task_id_from_response(response, "create_backup")
            status = self.get_backup_status_by_task_id(task_id)

            if status not in ["FAILED", "CANCELLED", "IN_PROGRESS"]:
                self.msg = "backups '{0}' created successfully.".format(name)
                self.set_operation_result("success", True, self.msg, "INFO")
                return self

            if status == "FAILED":
                self.msg = "Creation of backups '{0}' failed".format(name)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            if status == "CANCELLED":
                self.msg = "Creation of backups '{0}' was cancelled.".format(name)
                self.set_operation_result("failed", False, self.msg, "WARNING").check_return_status()

        except Exception as e:
            self.msg = "An error occurred while creating backups: {0}".format(e)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.log(
            "Exiting backup creation for name='{0}', scope='{1}'".format(name, scope),
            "INFO"
        )
        return self

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
        restore_operations = self.want.get("restore_operations", [])

        for restore in restore_operations:
            name = restore.get("name")
            encryption_passphrase = restore.get("encryption_passphrase")

            self.log("Validating restore details: name={0}, encryption_passphrase={1}".format(name, encryption_passphrase), "DEBUG")

            if not name or not encryption_passphrase:
                self.msg = "Both 'name' and 'encryption_passphrase' must be specified for restore."
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            backup_exists, current_backups, backup = self.get_backup()

            matched_backup = None

            for backup in current_backups:
                self.log("Comparing backup name: '{0}' with expected: '{1}'".format(backup.get("name"), name), "DEBUG")
                if backup.get("name") == name:
                    self.log(
                        "Found matching backup for restoration: name={0}".format(name),
                        "INFO"
                    )
                    matched_backup = backup
                    matched_backup_id = backup.get("id")
                    break

            self.log("Matched backups: {0}".format(matched_backup), "DEBUG")

            if not matched_backup:
                self.msg = "No backup found with the name '{0}'.".format(name)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            payload = {
                "encryption_passphrase": encryption_passphrase
            }

            self.log("Payload for restore operation: {0}".format(json.dumps(payload, indent=4)), "DEBUG")
            self.log("Initiating restore operation for backup '{0}'".format(name), "INFO")

            try:
                response = self.dnac._exec(
                    family="restore",
                    function="restore_backup",
                    op_modifies=True,
                    params={"id": matched_backup_id, "payload": payload}
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

            self.log("Exiting backup restoration workflow.", "INFO")
            return self

    def get_backup_task_id_from_response(self, response, api_name):
        """
            Extracts the task ID from the given API response dictionary.

            This method is used to retrieve the task ID associated with a backup-related operation
            (e.g., create or restore), which is later used to track the status of the task.

            Args:
                response (dict): The response returned from the Catalyst Center API call.
                api_name (str): The name of the API function for logging context.

            Returns:
                str or None: The extracted task ID if available, otherwise, None.
        """
        self.log("Extracting task ID from response of '{0}'.".format(api_name), "DEBUG")

        if not response or not isinstance(response, dict):
            self.log("Invalid or empty response received from '{0}'.".format(api_name), "ERROR")
            return None

        task_info = response.get("response", {})
        task_id = task_info.get("taskId")

        if not task_id:
            self.log("Returning None as task ID for '{0}'.".format(api_name), "DEBUG")
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
                    self.log("Returning backup status '{0}' for task ID '{1}'.".format(status, task_id), "INFO")
                    return status
                else:
                    self.log("Backup task ID '{0}' is still in progress. Status: '{1}'. Retrying...".format(task_id, status), "DEBUG")
                    time.sleep(5)

            except Exception as e:
                self.msg = "Error while retrieving status for task ID '{0}': {1}".format(task_id, str(e))
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            self.log("Backup status polling for task ID '{0}' completed.".format(task_id), "DEBUG")

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
        self.log(
            "Starting NFS configuration deletion workflow for {0} configurations".format(
                len(self.want.get("nfs_configuration", []))
            ),
            "INFO"
        )

        desired_nfs_configs = self.want.get("nfs_configuration", [])
        current_nfs_configs = self.have.get("current_nfs_configurations", [])

        for config_index, nfs_config_details in enumerate(desired_nfs_configs):
            server_ip = nfs_config_details.get("server_ip")
            source_path = nfs_config_details.get("source_path")

            self.log(
                "Processing NFS deletion {0}: server_ip={1}, source_path={2}".format(
                    config_index + 1, server_ip, source_path
                ),
                "DEBUG"
            )

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
                    self.log(
                        "Found existing NFS configuration for deletion: server_ip={0}, source_path={1}".format(
                            server_ip, source_path
                        ),
                        "INFO"
                    )
                    break

            if not nfs_to_delete:
                self.msg = (
                    "NFS configuration with server_ip '{0}' and source_path '{1}' "
                    "does not exist in the Cisco Catalyst Center or has already been deleted."
                ).format(server_ip, source_path)
                self.set_operation_result("success", False, self.msg, "INFO")
                self.deleted_nfs_config.append(source_path)
                continue

            nfs_config_id = nfs_to_delete.get("id")
            if not nfs_config_id:
                self.msg = "Unable to retrieve ID for NFS configuration '{0}:{1}'.".format(server_ip, source_path)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()
                continue

            try:
                self.log(
                    "Initiating deletion of NFS configuration via Catalyst Center API for server_ip={0}, source_path={1}".format(
                        server_ip, source_path
                    ),
                    "INFO"
                )
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

            self.log("Completed NFS configuration deletion workflow", "INFO")
            return self

    def delete_backup(self):
        """
        Deletes an existing backups from Cisco Catalyst Center.

        Returns:
            self: Returns the instance with updated operation result.

        Description:
            - Validates that the 'name' of the backups is provided in the desired state.
            - Checks if the backups exists in the current state.
            - If the backups exists, retrieves its ID and calls the API to delete it.
            - Monitors the deletion task until completion and updates the result accordingly.
            - If the backup does not exist or is already deleted, logs an informational message and exits successfully.
            - Handles failures and unexpected task status with appropriate error messages.
        """
        self.log("Starting backups deletion workflow", "INFO")

        backup_details = self.want.get("backup_job_creation", [])
        self.log("backups details: {0}".format(backup_details), "INFO")

        if not backup_details:
            self.log("No backups details provided for deletion", "DEBUG")
            return self

        backup = self.have
        self.log("Current backups: {0}".format(backup), "DEBUG")

        name = backup_details[0].get("name")
        if not name:
            self.msg = "'name' must be specified to delete a backups."
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.log(
            "Processing backups deletion for name='{0}'".format(name),
            "DEBUG"
        )

        if backup.get("backup_exists") is False:
            self.msg = "Backups with name '{0}' does not exist in the Cisco Catalyst Center or has already been deleted.".format(name)
            self.set_operation_result("success", False, self.msg, "INFO")
            return self

        backup_id = backup.get("current_backup", {}).get("id")
        if not backup_id:
            self.msg = "Unable to retrieve backup ID for backups '{0}'.".format(name)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        try:
            self.log(
                "Initiating deletion of backups '{0}' via Catalyst Center API".format(name),
                "INFO"
            )
            response = self.dnac._exec(
                family="backup",
                function="delete_backup",
                op_modifies=True,
                params={"id": backup_id},
            )
            self.log("Received API response from 'delete_backup': {0}".format(response), "DEBUG")
            self.deleted_backup.append(name)

            task_id = self.get_backup_task_id_from_response(response, "delete_backup")
            status = self.get_backup_status_by_task_id(task_id)

            if status == "SUCCESS":
                self.msg = "backups '{0}' deleted successfully.".format(name)
                self.set_operation_result("success", True, self.msg, "INFO")
                return self

            elif status == "FAILED":
                self.msg = "Deletion of backups '{0}' failed.".format(name)
                self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

            else:
                self.msg = "Unexpected deletion status '{0}' for backups '{1}'.".format(status, name)
                self.set_operation_result("failed", False, self.msg, "WARNING").check_return_status()

        except Exception as e:
            self.msg = "An error occurred while deleting backups: {0}".format(e)
            self.set_operation_result("failed", False, self.msg, "ERROR").check_return_status()

        self.log("Exiting backups deletion workflow", "INFO")
        return self

    def verify_diff_merged(self):
        """
        Verifies the successful creation of NFS configuration, backups, and backup configuration
        in Cisco Catalyst Center by comparing the desired state with the current state.

        Returns:
            self: Returns the instance after performing verification and logging results.

        Description:
            - For each provided configuration type (NFS, backups, backup configuration), fetches the current state.
            - Compares the current state (have) against the desired state (want).
            - Logs verification success if the configuration is found in the current state.
            - Logs a warning or info message if the configuration is not found, indicating a possible failure in execution.
        """
        self.log("Starting verification of merged configuration changes in Catalyst Center", "INFO")

        if self.want.get("nfs_configuration"):
            self.log("Verifying NFS configuration creation/update results", "DEBUG")
            self.get_have()
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            nfs_configuration_exists = self.have.get("nfs_configuration_exists")
            desired_config = self.want.get("nfs_configuration", [])[0]
            server_ip = desired_config.get("server_ip")
            source_path = desired_config.get("source_path")

            if nfs_configuration_exists:
                self.log(
                    "The playbook input for NFS configuration with server_ip '{0}' and source_path "
                    "'{1}' does not align with the Cisco Catalyst Center, indicating that the creation "
                    "task may not have executed successfully.".format(server_ip, source_path)
                )
            else:
                self.log(
                    "The playbook input for NFS configuration with server_ip '{0}' and source_path '{1}' does not align with "
                    "the Cisco Catalyst Center, indicating that the creation task may not have executed successfully.".format(
                        server_ip, source_path
                    )
                )

        if self.want.get("backup_job_creation"):
            self.log("Verifying backups creation results", "DEBUG")
            self.get_have()
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            backup_exists = self.have.get("backup_exists")
            backup = self.want.get("backup_job_creation", [])[0]
            name = backup.get("name")
            scope = backup.get("scope")

            if backup_exists:
                self.log(
                    "The playbook input for backups with name '{0}' and scope '{1}' does not "
                    "align with the Cisco Catalyst Center, indicating that the creation task may not "
                    "have executed successfully.".format(name, scope)
                )
            else:
                self.log(
                    "The playbook input for backups with name '{0}' and scope '{1}' does not align with the "
                    "Cisco Catalyst Center, indicating that the creation task may not have executed successfully.".format(
                        name, scope
                    )
                )

        if self.want.get("backup_storage_configuration"):
            self.log("Verifying backup configuration creation/update results", "DEBUG")
            self.get_have()
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            backup_config_exists = self.have.get("backup_configuration_exists")
            backup_config = self.want.get("backup_storage_configuration", [])[0]
            server_ip = backup_config.get("server_ip")
            path = backup_config.get("path")

            if backup_config_exists:
                self.log(
                    "The playbook input for backup configuration with server_ip '{0}' and source_path "
                    "'{1}' does not align with the Cisco Catalyst Center, indicating that the creation "
                    "task may not have executed successfully.".format(server_ip, path)
                )
            else:
                self.log(
                    "The playbook input for backup configuration with server_ip '{0}' and path '{1}' does not align with the "
                    "Cisco Catalyst Center, indicating that the creation task may not have executed successfully.".format(
                        server_ip, path
                    )
                )

        self.log("Completed verification of merged configuration changes", "INFO")
        return self

    def verify_diff_deleted(self):
        """
        Verifies the successful deletion of NFS configuration and backups
        from Cisco Catalyst Center by comparing the desired state with the current state.

        Returns:
            self: Returns the instance after performing verification and logging results.

        Description:
            - For each configuration type marked for deletion (NFS, backups), fetches the current state.
            - Compares the current state (have) against the desired state (want).
            - Logs confirmation if the configuration is no longer present, verifying successful deletion.
            - Logs a warning if the configuration is still present, indicating the deletion may have failed.
            - Introduces a delay for backups verification to allow for asynchronous cleanup on the backend.
        """
        self.log("Starting verification of deleted configuration changes in Catalyst Center", "INFO")

        if self.want.get("nfs_configuration"):
            self.log("Verifying NFS configuration deletion results", "DEBUG")
            self.get_have()
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            nfs_config_exists = self.have.get("nfs_configuration_exists")
            nfs_details = self.want.get("nfs_configuration", [])[0]
            server_ip = nfs_details.get("server_ip")
            source_path = nfs_details.get("source_path")

            if not nfs_config_exists:
                self.log(
                    "The playbook input for NFS configuration with server_ip '{0}' and source_path "
                    "'{1}' does not align with Cisco Catalyst Center, indicating that the deletion "
                    "task may not have executed successfully.".format(server_ip, source_path),
                    "WARNING"
                )
            else:
                self.log(
                    "The playbook input for NFS configuration with server_ip '{0}' and source_path '{1}' does not align with Cisco Catalyst Center, "
                    "indicating that the merge task may not have executed deletion successfully.".format(server_ip, source_path),
                    "WARNING"
                )

        if self.want.get("backup_job_creation"):
            self.log("Waiting for backups deletion to complete on backend", "DEBUG")
            time.sleep(120)
            self.get_have()
            self.log("Current State (have): {0}".format(str(self.have)), "INFO")
            self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

            backup_exists = self.have.get("backup_exists")
            self.log("Backup exists: {0}".format(backup_exists), "DEBUG")
            backup_name = self.want.get("backup_job_creation", [])[0].get("name")

            if not backup_exists:
                self.log(
                    "The backups '{0}' is not present in Cisco Catalyst Center "
                    "and its deletion has been verified.".format(backup_name)
                )
            else:
                self.log(
                    "The playbook input for backups '{0}' does not align with Cisco Catalyst "
                    "Center, indicating that the deletion task may not have executed successfully."
                    .format(backup_name),
                    "WARNING"
                )

        self.log("Completed verification of deleted configuration changes", "INFO")
        return self

    def update_messages(self):
        """
        Consolidates and logs messages for backup and restore operations including NFS
        configurations, backup configurations, create backups, and restore operations.
        Ensures no duplicates and builds a clean response.

        Returns:
            self (object): The updated instance with populated result and msg.
        """
        self.result["changed"] = False
        result_msg_list = []
        no_update_list = []

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

        if self.backup:
            msg = "Backup(s) '{0}' created successfully in Cisco Catalyst Center.".format(
                "', '".join(self.backup)
            )
            result_msg_list.append(msg)

        if self.deleted_backup:
            msg = "Backup(s) '{0}' deleted successfully from Cisco Catalyst Center.".format(
                "', '".join(self.deleted_backup)
            )
            result_msg_list.append(msg)

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
