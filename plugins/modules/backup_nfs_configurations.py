#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: backup_nfs_configurations
short_description: Resource module for Backup Nfs Configurations
description:
  - Manage operations create and delete of the resource Backup Nfs Configurations.
  - This api is used to create NFS configuration.
  - This api is used to delete the NFS configuration.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. The `id` of the NFS configuration to be deleted.Obtain the `id` from the id attribute
      in the response of the `/dna/system/api/v1/backupNfsConfigurations` API.
    type: str
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
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Backup CreateNFSConfiguration
    description: Complete reference of the CreateNFSConfiguration API.
    link: https://developer.cisco.com/docs/dna-center/#!create-nfs-configuration
  - name: Cisco DNA Center documentation for Backup DeleteNFSConfiguration
    description: Complete reference of the DeleteNFSConfiguration API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-nfs-configuration
notes:
  - SDK Method used are
    backup.Backup.create_n_f_s_configuration,
    backup.Backup.delete_n_f_s_configuration,
  - Paths used are
    post /dna/system/api/v1/backupNfsConfigurations,
    delete /dna/system/api/v1/backupNfsConfigurations/{id},
"""

EXAMPLES = r"""
---
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
- name: Delete by id
  cisco.dnac.backup_nfs_configurations:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "message": "string"
      },
      "version": "string"
    }
"""
