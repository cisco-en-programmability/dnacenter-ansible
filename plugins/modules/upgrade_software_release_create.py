#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: upgrade_software_release_create
short_description: Resource module for Upgrade Software Release Create
description:
  - Manage operation create of the resource Upgrade Software Release Create.
  - This api is used to trigger the workflow to upgrade the downloaded release.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  optionalPackages:
    description: Provide the list of optional package's id to be downloaded and upgraded. Use the `/dna/system/api/v1/releases/releaseSummary`
      API to obtain the optional package IDs. The `releaseName` and `releaseVersion` should correspond to the downloaded release.In
      the releases summary API response, optional packages can be identified by the attribute `packagesn.optional` is true.
      Provide the `packagesn.id` of these optional packages.
    elements: str
    type: list
  releaseName:
    description: The `releaseName` of the downloaded release to be upgraded.
    type: str
  releaseVersion:
    description: The `releaseVersion` of the downloaded release to be upgraded.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for System Software Upgrade UpgradeRelease
    description: Complete reference of the UpgradeRelease API.
    link: https://developer.cisco.com/docs/dna-center/#!upgrade-release
notes:
  - SDK Method used are
    system_software_upgrade.SystemSoftwareUpgrade.upgrade_release,
  - Paths used are
    post /dna/system/api/v1/upgradeSoftwareRelease,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.upgrade_software_release_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    optionalPackages:
      - string
    releaseName: string
    releaseVersion: string
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
