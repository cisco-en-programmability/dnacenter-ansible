#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: download_software_release_update
short_description: Resource module for Download Software Release Update
description:
  - Manage operation update of the resource Download Software Release Update. - > After the specified release has been downloaded
    successfully, users can download additional optional packages using this API.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  optionalPackages:
    description: Provide the list of optional package's id to be downloaded.Obtain the `id` from the `packagesn.id` attribute
      where `packagesn.optional` is true from the `/dna/system/api/v1/releases/releaseSummary` API where the `releaseName`
      and `releaseVersion` is the requested download version.
    elements: str
    type: list
  releaseName:
    description: The `releaseName` of the downloaded release to be updated.
    type: str
  releaseVersion:
    description: The `releaseVersion` of the downloaded release to be updated.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for System Software Upgrade UpdateDownloadedRelease
    description: Complete reference of the UpdateDownloadedRelease API.
    link: https://developer.cisco.com/docs/dna-center/#!update-downloaded-release
notes:
  - SDK Method used are
    system_software_upgrade.SystemSoftwareUpgrade.update_downloaded_release,
  - Paths used are
    put /dna/system/api/v1/downloadSoftwareRelease,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.dnac.download_software_release_update:
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
