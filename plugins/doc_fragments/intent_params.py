#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ModuleDocFragment(object):

    # Standard files documentation fragment
    DOCUMENTATION = r'''
options:
    dnac_host:
        description:
          - The Cisco DNA Center hostname.
        type: str
        required: true
    dnac_port:
        description:
          - The Cisco DNA Center port.
        type: str
        default: '443'
    dnac_username:
        description:
          - The Cisco DNA Center username to authenticate.
        type: str
        default: admin
        aliases: [ user ]
    dnac_password:
        description:
          - The Cisco DNA Center password to authenticate.
        type: str
    dnac_verify:
        description:
          - Flag to enable or disable SSL certificate verification.
        type: bool
        default: true
    dnac_version:
        description:
          - Informs the SDK which version of Cisco DNA Center to use.
        type: str
        default: 2.2.3.3
    dnac_debug:
        description:
          - Flag for Cisco DNA Center SDK to enable debugging.
        type: bool
        default: false
    dnac_log:
        description:
          - Flag for logging playbook execution details.
            If set to true the log file will be created at the location of the execution with the name dnac.log
        type: bool
        default: false
    dnac_log_level:
      description:
        - Sets the threshold for log level. Messages with a level equal to or higher than
          this will be logged. Levels are listed in order of severity [CRITICAL, ERROR, WARNING, INFO, DEBUG].
        - CRITICAL indicates serious errors halting the program. Displays only CRITICAL messages.
        - ERROR indicates problems preventing a function. Displays ERROR and CRITICAL messages.
        - WARNING indicates potential future issues. Displays WARNING, ERROR, CRITICAL messages.
        - INFO tracks normal operation. Displays INFO, WARNING, ERROR, CRITICAL messages.
        - DEBUG provides detailed diagnostic info. Displays all log messages.
      type: str
      default: WARNING
    dnac_log_file_path:
      description:
      - Governs logging. Logs are recorded if dnac_log is True.
      - If path is not specified,
        - When 'dnac_log_append' is True, 'dnac.log' is generated in the
          current Ansible directory; logs are appended.
        - When 'dnac_log_append' is False, 'dnac.log' is generated; logs
          are overwritten.
      - If path is specified,
        - When 'dnac_log_append' is True, the file opens in append mode.
        - When 'dnac_log_append' is False, the file opens in write (w) mode.
        - In shared file scenarios, without append mode, content is
          overwritten after each module execution.
        - For a shared log file, set append to False for the 1st module
          (to overwrite); for subsequent modules, set append to True.
      type: str
      default: dnac.log
    dnac_log_append:
      description: Determines the mode of the file. Set to True for 'append' mode. Set to False for 'write' mode.
      type: bool
      default: True
    validate_response_schema:
        description:
          - Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.
        type: bool
        default: true
notes:
    - "Does not support C(check_mode)"
    - "The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK"
    - "The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection"
'''
