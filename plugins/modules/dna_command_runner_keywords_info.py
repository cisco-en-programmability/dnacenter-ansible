#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: dna_command_runner_keywords_info
short_description: Information module for Dna Command Runner Keywords Info
description:
  - This module represents an alias of the module dna_command_runner_keywords_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Command Runner GetAllKeywordsOfCLIsAcceptedByCommandRunnerV1
    description: Complete reference of the GetAllKeywordsOfCLIsAcceptedByCommandRunnerV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-all-keywords-of-cl-is-accepted-by-command-runner
notes:
  - SDK Method used are command_runner.CommandRunner.get_all_keywords_of_clis_accepted,
  - Paths used are get /dna/intent/api/v1/network-device-poller/cli/legit-reads,
  - It should be noted that this module is an alias of dna_command_runner_keywords_v1_info
"""
EXAMPLES = r"""
- name: Get all Dna Command Runner Keywords Info
  cisco.dnac.dna_command_runner_keywords_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        "string"
      ],
      "version": "string"
    }
"""
