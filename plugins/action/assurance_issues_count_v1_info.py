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

# Get common arguments specification
argument_spec = dnac_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    startTime=dict(type="float"),
    endTime=dict(type="float"),
    isGlobal=dict(type="bool"),
    priority=dict(type="str"),
    severity=dict(type="str"),
    status=dict(type="str"),
    entityType=dict(type="str"),
    category=dict(type="str"),
    deviceType=dict(type="str"),
    name=dict(type="str"),
    issueId=dict(type="str"),
    entityId=dict(type="str"),
    updatedBy=dict(type="str"),
    siteHierarchy=dict(type="str"),
    siteHierarchyId=dict(type="str"),
    siteName=dict(type="str"),
    siteId=dict(type="str"),
    fabricSiteId=dict(type="str"),
    fabricVnName=dict(type="str"),
    fabricTransitSiteId=dict(type="str"),
    networkDeviceId=dict(type="str"),
    networkDeviceIpAddress=dict(type="str"),
    macAddress=dict(type="str"),
    aiDriven=dict(type="bool"),
    fabricDriven=dict(type="bool"),
    fabricSiteDriven=dict(type="bool"),
    fabricVnDriven=dict(type="bool"),
    fabricTransitDriven=dict(type="bool"),
    headers=dict(type="dict"),
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
        self._supports_check_mode = True
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
            start_time=params.get("startTime"),
            end_time=params.get("endTime"),
            is_global=params.get("isGlobal"),
            priority=params.get("priority"),
            severity=params.get("severity"),
            status=params.get("status"),
            entity_type=params.get("entityType"),
            category=params.get("category"),
            device_type=params.get("deviceType"),
            name=params.get("name"),
            issue_id=params.get("issueId"),
            entity_id=params.get("entityId"),
            updated_by=params.get("updatedBy"),
            site_hierarchy=params.get("siteHierarchy"),
            site_hierarchy_id=params.get("siteHierarchyId"),
            site_name=params.get("siteName"),
            site_id=params.get("siteId"),
            fabric_site_id=params.get("fabricSiteId"),
            fabric_vn_name=params.get("fabricVnName"),
            fabric_transit_site_id=params.get("fabricTransitSiteId"),
            network_device_id=params.get("networkDeviceId"),
            network_device_ip_address=params.get("networkDeviceIpAddress"),
            mac_address=params.get("macAddress"),
            ai_driven=params.get("aiDriven"),
            fabric_driven=params.get("fabricDriven"),
            fabric_site_driven=params.get("fabricSiteDriven"),
            fabric_vn_driven=params.get("fabricVnDriven"),
            fabric_transit_driven=params.get("fabricTransitDriven"),
            headers=params.get("headers"),
        )
        return new_object

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        self._result.update(dict(dnac_response={}))

        dnac = DNACSDK(params=self._task.args)

        response = dnac.exec(
            family="issues",
            function='get_the_total_number_of_issues_for_given_set_of_filters_know_your_network_v1',
            params=self.get_object(self._task.args),
        )
        self._result.update(dict(dnac_response=response))
        self._result.update(dnac.exit_json())
        return self._result
