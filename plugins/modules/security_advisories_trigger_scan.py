#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: security_advisories_trigger_scan
short_description: Resource module for Security Advisories Trigger Scan
description:
- This module represents an alias of the module security_advisories_trigger_scan_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  failedDevicesOnly:
    description: FailedDevicesOnly query parameter. Used to specify if the scan should
      run only for the network devices that failed during the previous scan. If not
      specified, this parameter defaults to false.
    type: bool
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Compliance TriggersASecurityAdvisoriesScanForTheSupportedNetworkDevicesV1
  description: Complete reference of the TriggersASecurityAdvisoriesScanForTheSupportedNetworkDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!triggers-a-security-advisories-scan-for-the-supported-network-devices
notes:
  - SDK Method used are
    compliance.Compliance.triggers_a_security_advisories_scan_for_the_supported_network_devices_v1,

  - Paths used are
    post /dna/intent/api/v1/securityAdvisories/triggerScan,
  - It should be noted that this module is an alias of security_advisories_trigger_scan_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.security_advisories_trigger_scan:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    failedDevicesOnly: true

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "url": "string",
        "taskId": "string"
      }
    }
"""
