#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: integrate_ise
short_description: Resource module for Integrate Ise
description:
  - This module represents an alias of the module integrate_ise_v1
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Cisco ISE Server Identifier. Use 'Get Authentication
      and Policy Servers' intent API to find the identifier.
    type: str
  isCertAcceptedByUser:
    description: Value true for accept, false for deny. Remove this field and send
      empty request payload ( {} ) to retry the failed integration.
    type: bool
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for System Settings AcceptCiscoISEServerCertificateForCiscoISEServerIntegrationV1
    description: Complete reference of the AcceptCiscoISEServerCertificateForCiscoISEServerIntegrationV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!accept-cisco-ise-server-certificate-for-cisco-ise-server-integration
notes:
  - SDK Method used are
    system_settings.SystemSettings.accept_cisco_ise_server_certificate_for_cisco_ise_server_integration_v1,
  - Paths used are put /dna/intent/api/v1/integrate-ise/{id},
  - It should be noted that this module is an alias of integrate_ise_v1
"""
EXAMPLES = r"""
- name: Update by id
  cisco.dnac.integrate_ise:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    id: string
    isCertAcceptedByUser: true
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "object": "string"
    }
"""
