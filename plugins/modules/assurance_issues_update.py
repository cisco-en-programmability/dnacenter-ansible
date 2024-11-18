#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: assurance_issues_update
short_description: Resource module for Assurance Issues Update
description:
- This module represents an alias of the module assurance_issues_update_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description: Id path parameter. The issue Uuid.
    type: str
  notes:
    description: Notes.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Issues UpdateTheGivenIssueByUpdatingSelectedFieldsV1
  description: Complete reference of the UpdateTheGivenIssueByUpdatingSelectedFieldsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-the-given-issue-by-updating-selected-fields-v-1
notes:
  - SDK Method used are
    issues.Issues.update_the_given_issue_by_updating_selected_fields_v1,

  - Paths used are
    post /dna/intent/api/v1/assuranceIssues/{id}/update,
  - It should be noted that this module is an alias of assurance_issues_update_v1

"""

EXAMPLES = r"""
"""
RETURN = r"""
dnac_response:
  This alias returns the output of assurance_issues_update_v1.
"""
