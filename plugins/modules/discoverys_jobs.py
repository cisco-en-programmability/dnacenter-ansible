#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discoverys_jobs
short_description: Resource module for Discoverys Jobs
description:
  - Manage operation create of the resource Discoverys Jobs. - > This API starts a discovery job using the given discovery
    id. The response includes a task url that provides access to the task's details. By accessing this URL, users will receive
    a response containing a resultLocation attribute, which provides details of the discovery job that was started, including
    the jobId. A new discovery job is created every time this API is triggered.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. The id of the discovery.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices StartsTheExistingDiscovery
    description: Complete reference of the StartsTheExistingDiscovery API.
    link: https://developer.cisco.com/docs/dna-center/#!starts-the-existing-discovery
notes:
  - SDK Method used are
    devices.Devices.starts_the_existing_discovery,
  - Paths used are
    post /dna/intent/api/v1/discoverys/{id}/jobs,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.discoverys_jobs:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
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
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
