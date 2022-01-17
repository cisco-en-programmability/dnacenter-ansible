#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site_delete
short_description: Resource module for Site Delete
description:
- Manage operation delete of the resource Site Delete.
- Delete site with area/building/floor by siteId.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  siteId:
    description: SiteId path parameter. Site id to which site details to be deleted.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function delete_site used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.sites.Sites.delete_site

notes:
  - Paths used: delete /dna/intent/api/v1/site/{siteId}
"""

EXAMPLES = r"""
- name: Delete by id
  cisco.dnac.site_delete:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    siteId: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "result": "string",
      "response": {
        "endTime": "string",
        "version": "string",
        "startTime": "string",
        "progress": "string",
        "data": "string",
        "serviceType": "string",
        "operationIdList": [
          "string"
        ],
        "isError": "string",
        "rootId": "string",
        "instanceTenantId": "string",
        "id": "string"
      },
      "status": "string"
    }
"""
