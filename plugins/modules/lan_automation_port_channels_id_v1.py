#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: lan_automation_port_channels_id_v1
short_description: Resource module for Lan Automation Port Channels Id V1
description:
  - Manage operation delete of the resource Lan Automation Port Channels Id V1.
  - This API deletes a Port Channel between LAN Automation associated devices using
    a valid Port Channel ID.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. ID of the port channel.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for LAN Automation DeletePortChannelV1
    description: Complete reference of the DeletePortChannelV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-port-channel
notes:
  - SDK Method used are lan_automation.LanAutomation.delete_port_channel_v1,
  - Paths used are delete /dna/intent/api/v1/lanAutomation/portChannels/{id},
"""
EXAMPLES = r"""
- name: Delete by id
  cisco.dnac.lan_automation_port_channels_id_v1:
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
