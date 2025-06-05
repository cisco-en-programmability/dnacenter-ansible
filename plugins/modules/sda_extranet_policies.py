#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_extranet_policies
short_description: Resource module for Sda Extranet Policies
description:
  - This module represents an alias of the module sda_extranet_policies_v1
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  extranetPolicyName:
    description: ExtranetPolicyName query parameter. Name of the extranet policy.
    type: str
  id:
    description: Id path parameter. ID of the extranet policy.
    type: str
  payload:
    description: Sda Extranet Policies's payload.
    elements: dict
    suboptions:
      extranetPolicyName:
        description: Name of the existing extranet policy (updating this field is
          not allowed).
        type: str
      fabricIds:
        description: IDs of the fabric sites associated with this extranet policy.
        elements: str
        type: list
      id:
        description: ID of the existing extranet policy (updating this field is not
          allowed).
        type: str
      providerVirtualNetworkName:
        description: Name of the existing provider virtual network (updating this
          field is not allowed).
        type: str
      subscriberVirtualNetworkNames:
        description: Name of the subscriber virtual networks.
        elements: str
        type: list
    type: list
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA AddExtranetPolicyV1
    description: Complete reference of the AddExtranetPolicyV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!add-extranet-policy
  - name: Cisco DNA Center documentation for SDA DeleteExtranetPoliciesV1
    description: Complete reference of the DeleteExtranetPoliciesV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-extranet-policies
  - name: Cisco DNA Center documentation for SDA DeleteExtranetPolicyByIdV1
    description: Complete reference of the DeleteExtranetPolicyByIdV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-extranet-policy-by-id
  - name: Cisco DNA Center documentation for SDA UpdateExtranetPolicyV1
    description: Complete reference of the UpdateExtranetPolicyV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-extranet-policy
notes:
  - SDK Method used are sda.Sda.add_extranet_policy_v1, sda.Sda.delete_extranet_policy_by_id_v1,
    sda.Sda.update_extranet_policy_v1,
  - Paths used are post /dna/intent/api/v1/sda/extranetPolicies, delete /dna/intent/api/v1/sda/extranetPolicies,
    delete /dna/intent/api/v1/sda/extranetPolicies/{id}, put /dna/intent/api/v1/sda/extranetPolicies,
  - It should be noted that this module is an alias of sda_extranet_policies_v1
"""
EXAMPLES = r"""
- name: Delete all
  cisco.dnac.sda_extranet_policies:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    extranetPolicyName: string
- name: Update all
  cisco.dnac.sda_extranet_policies:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
      - extranetPolicyName: string
        fabricIds:
          - string
        id: string
        providerVirtualNetworkName: string
        subscriberVirtualNetworkNames:
          - string
- name: Create
  cisco.dnac.sda_extranet_policies:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
      - extranetPolicyName: string
        fabricIds:
          - string
        providerVirtualNetworkName: string
        subscriberVirtualNetworkNames:
          - string
- name: Delete by id
  cisco.dnac.sda_extranet_policies:
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
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
