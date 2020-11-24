#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: network_device_poller_read_request
short_description: Manage NetworkDevicePollerReadRequest objects of CommandRunner
description:
- Submit request for read-only CLIs.
version_added: '1.0'
author: first last (@GitHubID)
options:
  commands:
    description:
    - CommandRunnerDTO's commands (list of strings).
    type: list
    required: True
  description:
    description:
    - CommandRunnerDTO's description.
    type: str
  deviceUuids:
    description:
    - CommandRunnerDTO's deviceUuids (list of strings).
    type: list
    required: True
  name:
    description:
    - CommandRunnerDTO's name.
    type: str
  timeout:
    description:
    - CommandRunnerDTO's timeout.
    type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_poller_read_request
# Reference by Internet resource
- name: NetworkDevicePollerReadRequest reference
  description: Complete reference of the NetworkDevicePollerReadRequest object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDevicePollerReadRequest reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: run_read_only_commands_on_devices
  cisco.dnac.network_device_poller_read_request
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: create  # required
    commands:  # required
    - SomeValue  # string
    deviceUuids:  # required
    - SomeValue  # string
    description: SomeValue  # string
    name: SomeValue  # string
    timeout: 1  #  integer
  delegate_to: localhost
  
"""

RETURN = """
run_read_only_commands_on_devices:
    description: Submit request for read-only CLIs.
    returned: success
    type: dict
    contains:
    response:
      description: CommandRunnerDTO's response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the network device poller read request's taskId.
          returned: success
          type: dict
        url:
          description: It is the network device poller read request's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: CommandRunnerDTO's version.
      returned: success
      type: str
      sample: '1.0'

"""
