#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: event_syslog_config
short_description: Resource module for Event Syslog Config
description:
  - This module represents an alias of the module event_syslog_config_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  configId:
    description: Required only for update syslog configuration.
    type: str
  description:
    description: Description.
    type: str
  host:
    description: Host.
    type: str
  name:
    description: Name.
    type: str
  port:
    description: Port.
    type: int
  protocol:
    description: Protocol.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Event Management CreateSyslogDestinationV1
    description: Complete reference of the CreateSyslogDestinationV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!create-syslog-destination
  - name: Cisco DNA Center documentation for Event Management UpdateSyslogDestinationV1
    description: Complete reference of the UpdateSyslogDestinationV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-syslog-destination
notes:
  - SDK Method used are event_management.EventManagement.create_syslog_destination_v1,
    event_management.EventManagement.update_syslog_destination_v1,
  - Paths used are post /dna/intent/api/v1/event/syslog-config, put /dna/intent/api/v1/event/syslog-config,
  - It should be noted that this module is an alias of event_syslog_config_v1
"""
EXAMPLES = r"""
- name: Update all
  cisco.dnac.event_syslog_config:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    configId: string
    description: string
    host: string
    name: string
    port: 0
    protocol: string
- name: Create
  cisco.dnac.event_syslog_config:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    configId: string
    description: string
    host: string
    name: string
    port: 0
    protocol: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "errorMessage": {
        "errors": [
          "string"
        ]
      },
      "apiStatus": "string",
      "statusMessage": "string"
    }
"""
