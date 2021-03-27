#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: issue_enrichment_details
short_description: Manage IssueEnrichmentDetails objects of Issues
description:
- Enriches a given network issue context (an issue id or end user's Mac Address) with details about the issue(s), impacted hosts and suggested actions for remediation.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  headers:
    description:
    - Adds the header parameters.
    type: dict
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.issue_enrichment_details
# Reference by Internet resource
- name: IssueEnrichmentDetails reference
  description: Complete reference of the IssueEnrichmentDetails object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: IssueEnrichmentDetails reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_issue_enrichment_details
  cisco.dnac.issue_enrichment_details:
    state: query  # required
    headers:  # required
  register: query_result

"""

RETURN = """
"""
