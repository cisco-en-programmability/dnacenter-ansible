#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_fabric_authentication_profile
short_description: Resource module for Sda Fabric Authentication Profile
description:
  - This module represents an alias of the module sda_fabric_authentication_profile_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Sda Fabric Authentication Profile's payload.
    elements: dict
    suboptions:
      authenticateTemplateName:
        description: Authenticate Template Name.
        type: str
        version_added: 4.0.0
      siteNameHierarchy:
        description: Path of sda Fabric Site.
        type: str
    type: list
  siteNameHierarchy:
    description: SiteNameHierarchy query parameter.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA AddDefaultAuthenticationTemplateInSDAFabricV1
    description: Complete reference of the AddDefaultAuthenticationTemplateInSDAFabricV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!add-default-authentication-template-in-sda-fabric
  - name: Cisco DNA Center documentation for SDA DeleteDefaultAuthenticationProfileFromSDAFabricV1
    description: Complete reference of the DeleteDefaultAuthenticationProfileFromSDAFabricV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!delete-default-authentication-profile-from-sda-fabric
  - name: Cisco DNA Center documentation for SDA UpdateDefaultAuthenticationProfileInSDAFabricV1
    description: Complete reference of the UpdateDefaultAuthenticationProfileInSDAFabricV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!update-default-authentication-profile-in-sda-fabric
notes:
  - SDK Method used are sda.Sda.add_default_authentication_profile, sda.Sda.delete_default_authentication_profile,
    sda.Sda.update_default_authentication_profile,
  - Paths used are post /dna/intent/api/v1/business/sda/authentication-profile, delete
    /dna/intent/api/v1/business/sda/authentication-profile, put /dna/intent/api/v1/business/sda/authentication-profile,
  - It should be noted that this module is an alias of sda_fabric_authentication_profile_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.sda_fabric_authentication_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
      - authenticateTemplateName: string
        siteNameHierarchy: string
- name: Update all
  cisco.dnac.sda_fabric_authentication_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
      - authenticateTemplateName: string
        authenticationOrder: string
        dot1xToMabFallbackTimeout: string
        numberOfHosts: string
        siteNameHierarchy: string
        wakeOnLan: true
- name: Delete all
  cisco.dnac.sda_fabric_authentication_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    siteNameHierarchy: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "description": "string",
      "taskId": "string",
      "taskStatusUrl": "string",
      "executionStatusUrl": "string",
      "executionId": "string"
    }
"""
