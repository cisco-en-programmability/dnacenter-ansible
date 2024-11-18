#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: security_threats_type_info
short_description: Information module for Security Threats Type Info
description:
- This module represents an alias of the module security_threats_type_v1_info
version_added: '6.16.0'
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
notes:
  - SDK Method used are
    devices.Devices.get_threat_types_v1,

  - Paths used are
    get /dna/intent/api/v1/security/threats/type,
  - It should be noted that this module is an alias of security_threats_type_v1_info

"""

EXAMPLES = r"""
- name: Get all Security Threats Type Info
  cisco.dnac.security_threats_type_info:
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
  description:
    - This alias returns the output of security_threats_type_v1_info.
"""