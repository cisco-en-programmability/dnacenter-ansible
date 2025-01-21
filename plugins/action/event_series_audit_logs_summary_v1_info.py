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
    parentInstanceId=dict(type="str"),
    isParentOnly=dict(type="bool"),
    instanceId=dict(type="str"),
    name=dict(type="str"),
    eventId=dict(type="str"),
    category=dict(type="str"),
    severity=dict(type="str"),
    domain=dict(type="str"),
    subDomain=dict(type="str"),
    source=dict(type="str"),
    userId=dict(type="str"),
    context=dict(type="str"),
    eventHierarchy=dict(type="str"),
    siteId=dict(type="str"),
    deviceId=dict(type="str"),
    isSystemEvents=dict(type="bool"),
    description=dict(type="str"),
    startTime=dict(type="float"),
    endTime=dict(type="float"),
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
            parent_instance_id=params.get("parentInstanceId"),
            is_parent_only=params.get("isParentOnly"),
            instance_id=params.get("instanceId"),
            name=params.get("name"),
            event_id=params.get("eventId"),
            category=params.get("category"),
            severity=params.get("severity"),
            domain=params.get("domain"),
            sub_domain=params.get("subDomain"),
            source=params.get("source"),
            user_id=params.get("userId"),
            context=params.get("context"),
            event_hierarchy=params.get("eventHierarchy"),
            site_id=params.get("siteId"),
            device_id=params.get("deviceId"),
            is_system_events=params.get("isSystemEvents"),
            description=params.get("description"),
            start_time=params.get("startTime"),
            end_time=params.get("endTime"),
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
            family="event_management",
            function='get_auditlog_summary',
            params=self.get_object(self._task.args),
        )
        self._result.update(dict(dnac_response=response))
        self._result.update(dnac.exit_json())
        return self._result
