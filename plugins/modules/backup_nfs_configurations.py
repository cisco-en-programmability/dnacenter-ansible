#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: backup_nfs_configurations
short_description: Resource module for Backup Nfs Configurations
description:
  - This module represents an alias of the module backup_nfs_configurations_v1
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  nfsPort:
    description: NFS Port.
    type: int
  nfsVersion:
    description: NFS version.
    type: str
  portMapperPort:
    description: NFS port mapper port.
    type: int
  server:
    description: NFS server host.
    type: str
  sourcePath:
    description: NFS server path.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Backup CreateNFSConfigurationV1
    description: Complete reference of the CreateNFSConfigurationV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!create-nfs-configuration
notes:
  - SDK Method used are backup.Backup.create_n_f_s_configuration_v1,
  - Paths used are post /dna/system/api/v1/backupNfsConfigurations,
  - It should be noted that this module is an alias of backup_nfs_configurations_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.backup_nfs_configurations:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    nfsPort: 0
    nfsVersion: string
    portMapperPort: 0
    server: string
    sourcePath: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
