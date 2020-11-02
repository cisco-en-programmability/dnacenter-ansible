#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '0.0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: issue_enrichment_details
short_description: Manage IssueEnrichmentDetails objects of Issues
description:
- Enriches a given network issue context (an issue id or end user’s Mac Address) with details about the issue(s), impacted hosts and suggested actions for remediation.
version_added: '1.0'
author: first last (@GitHubID)
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
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Enriches a given network issue context (an issue id or end user’s Mac Address) with details about the issue(s), impacted hosts and suggested actions for remediation.
    returned: success,changed,always
    type: dict
    contains:
        issueDetails:
            description: Issue Details, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                issue:
                    description: It is the issue enrichment details's issue.
                    returned: success,changed,always
                    type: list
                    contains:
                        issueId:
                            description: It is the issue enrichment details's issueId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueSource:
                            description: It is the issue enrichment details's issueSource.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueCategory:
                            description: It is the issue enrichment details's issueCategory.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueName:
                            description: It is the issue enrichment details's issueName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueDescription:
                            description: It is the issue enrichment details's issueDescription.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueEntity:
                            description: It is the issue enrichment details's issueEntity.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueEntityValue:
                            description: It is the issue enrichment details's issueEntityValue.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueSeverity:
                            description: It is the issue enrichment details's issueSeverity.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issuePriority:
                            description: It is the issue enrichment details's issuePriority.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueSummary:
                            description: It is the issue enrichment details's issueSummary.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        issueTimestamp:
                            description: It is the issue enrichment details's issueTimestamp.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        suggestedActions:
                            description: It is the issue enrichment details's suggestedActions.
                            returned: success,changed,always
                            type: list
                            contains:
                                message:
                                    description: It is the issue enrichment details's message.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                steps:
                                    description: It is the issue enrichment details's steps.
                                    returned: success,changed,always
                                    type: list

                        impactedHosts:
                            description: It is the issue enrichment details's impactedHosts.
                            returned: success,changed,always
                            type: list



'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.issue_enrichment_details import module_definition


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    dnac.exit_json()


if __name__ == "__main__":
    main()