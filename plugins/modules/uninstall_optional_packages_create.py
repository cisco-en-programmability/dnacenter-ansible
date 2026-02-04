#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: uninstall_optional_packages_create
short_description: Resource module for Uninstall Optional Packages Create
description:
  - Manage operation create of the resource Uninstall Optional Packages Create.
  - This API is used to trigger the workflow for uninstalling optional packages.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  optionalPackages:
    description: Provide the list of optional package's id to be uninstalled. Use the `/dna/system/api/v1/installedRelease`
      API to obtain the optional package IDs. In the installedRelease API response, installed optional packages can be identified
      by the attributes `packagesn.optional` is true. And `packagesn.status` is DEPLOYED. Provide the `packagesn.id` of these
      optional packages.
    elements: str
    type: list
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for System Software Upgrade UninstallOptionalPackages
    description: Complete reference of the UninstallOptionalPackages API.
    link: https://developer.cisco.com/docs/dna-center/#!uninstall-optional-packages
notes:
  - SDK Method used are
    system_software_upgrade.SystemSoftwareUpgrade.uninstall_optional_packages,
  - Paths used are
    post /dna/system/api/v1/uninstallOptionalPackages,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.uninstall_optional_packages_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    optionalPackages:
      - string
"""
RETURN = r"""
dnac_response:
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
