#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: compliance_device
short_description: Resource module for Compliance Device
description:
- This module represents an alias of the module compliance_device_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options: {}
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
notes:
  - Paths used are
  - It should be noted that this module is an alias of compliance_device_v1

"""

EXAMPLES = r"""
"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of compliance_device_v1.
"""
