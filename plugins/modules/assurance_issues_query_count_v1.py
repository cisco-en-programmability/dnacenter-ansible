#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: assurance_issues_query_count_v1
short_description: Resource module for Assurance Issues Query Count V1
description:
- Manage operation create of the resource Assurance Issues Query Count V1.
- >
  Returns all details of each issue along with suggested actions for given set
  of filters specified in request body. If there is no start and/or end time, then end time will be defaulted to current
  time and start time will be defaulted to 24-hours ago from end time.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options: {}
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
notes:
  - Paths used are

"""

EXAMPLES = r"""
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
