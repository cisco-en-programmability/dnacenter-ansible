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
    ids=dict(type="str"),
    managementAddress=dict(type="str"),
    hostname=dict(type="str"),
    siteId=dict(type="str"),
    appTelemetryDeploymentStatus=dict(type="str"),
    appTelemetryReadinessStatus=dict(type="str"),
    cbarDeploymentStatus=dict(type="str"),
    cbarReadinessStatus=dict(type="str"),
    protocolPackStatus=dict(type="str"),
    protocolPackUpdateStatus=dict(type="str"),
    applicationRegistrySyncStatus=dict(type="str"),
    offset=dict(type="str"),
    limit=dict(type="str"),
    sortBy=dict(type="str"),
    order=dict(type="str"),
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
            ids=params.get("ids"),
            management_address=params.get("managementAddress"),
            hostname=params.get("hostname"),
            site_id=params.get("siteId"),
            app_telemetry_deployment_status=params.get("appTelemetryDeploymentStatus"),
            app_telemetry_readiness_status=params.get("appTelemetryReadinessStatus"),
            cbar_deployment_status=params.get("cbarDeploymentStatus"),
            cbar_readiness_status=params.get("cbarReadinessStatus"),
            protocol_pack_status=params.get("protocolPackStatus"),
            protocol_pack_update_status=params.get("protocolPackUpdateStatus"),
            application_registry_sync_status=params.get("applicationRegistrySyncStatus"),
            offset=params.get("offset"),
            limit=params.get("limit"),
            sort_by=params.get("sortBy"),
            order=params.get("order"),
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
            family="application_policy",
            function='retrieve_the_list_of_network_devices_with_their_application_visibility_status_v1',
            params=self.get_object(self._task.args),
        )
        self._result.update(dict(dnac_response=response))
        self._result.update(dnac.exit_json())
        return self._result
