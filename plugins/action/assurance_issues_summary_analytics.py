#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.plugins.action import ActionBase
try:
    from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
        AnsibleArgSpecValidator,
    )
except ImportError:
    ANSIBLE_UTILS_IS_INSTALLED = False
else:
    ANSIBLE_UTILS_IS_INSTALLED = True
from ansible.errors import AnsibleActionFail
from ansible_collections.cisco.dnac.plugins.plugin_utils.dnac import (
    DNACSDK,
    dnac_argument_spec,
)

# Get common arguements specification
argument_spec = dnac_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    startTime=dict(type="int"),
    endTime=dict(type="int"),
    filters=dict(type="list"),
    groupBy=dict(type="list"),
    attributes=dict(type="list"),
    aggregateAttributes=dict(type="list"),
    page=dict(type="dict"),
))

required_if = []
required_one_of = []
mutually_exclusive = []
required_together = []


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        if not ANSIBLE_UTILS_IS_INSTALLED:
            raise AnsibleActionFail("ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'")
        super(ActionModule, self).__init__(*args, **kwargs)
        self._supports_async = False
        self._supports_check_mode = False
        self._result = None

    # Checks the supplied parameters against the argument spec for this module
    def _check_argspec(self):
        aav = AnsibleArgSpecValidator(
            data=self._task.args,
            schema=dict(argument_spec=argument_spec),
            schema_format="argspec",
            schema_conditionals=dict(
                required_if=required_if,
                required_one_of=required_one_of,
                mutually_exclusive=mutually_exclusive,
                required_together=required_together,
            ),
            name=self._task.action,
        )
        valid, errors, self._task.args = aav.validate()
        if not valid:
            raise AnsibleActionFail(errors)

    def get_object(self, params):
        new_object = dict(
            startTime=params.get("startTime"),
            endTime=params.get("endTime"),
            filters=params.get("filters"),
            groupBy=params.get("groupBy"),
            attributes=params.get("attributes"),
            aggregateAttributes=params.get("aggregateAttributes"),
            page=params.get("page"),
        )
        return new_object

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        dnac = DNACSDK(params=self._task.args)

        response = dnac.exec(
            family="issues",
            # No function
            # Metadata: {'type': 'c', 'look_by': '', 'urls': ['/dna/data/api/v1/assuranceIssues/summaryAnalytics'], 'tag': 'Issues', 'version_added': '6.15.0', 'get_all': 'get_summary_analytics_data_of_issues', 'operation_id_list': ['get:GetSummaryAnalyticsDataOfIssues'], 'description': 'get:Gets the summary analytics data related to issues based on given filters and group by field. This data can be used to find issue counts grouped by different keys. https://github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-IssuesList-1.0.0-resolved.yaml.\n', 'method_url': 'get:post /dna/data/api/v1/assuranceIssues/summaryAnalytics,\n'}
            params=self.get_object(self._task.args),
        )
        self._result.update(dict(dnac_response=response))
        self._result.update(dnac.exit_json())
        return self._result
