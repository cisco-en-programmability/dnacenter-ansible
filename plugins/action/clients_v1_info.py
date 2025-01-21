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
    limit=dict(type="float"),
    offset=dict(type="float"),
    sortBy=dict(type="str"),
    order=dict(type="str"),
    type=dict(type="str"),
    osType=dict(type="str"),
    osVersion=dict(type="str"),
    siteHierarchy=dict(type="str"),
    siteHierarchyId=dict(type="str"),
    siteId=dict(type="str"),
    ipv4Address=dict(type="str"),
    ipv6Address=dict(type="str"),
    macAddress=dict(type="str"),
    wlcName=dict(type="str"),
    connectedNetworkDeviceName=dict(type="str"),
    ssid=dict(type="str"),
    band=dict(type="str"),
    view=dict(type="str"),
    attribute=dict(type="str"),
    id=dict(type="str"),
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
            limit=params.get("limit"),
            offset=params.get("offset"),
            sort_by=params.get("sortBy"),
            order=params.get("order"),
            type=params.get("type"),
            os_type=params.get("osType"),
            os_version=params.get("osVersion"),
            site_hierarchy=params.get("siteHierarchy"),
            site_hierarchy_id=params.get("siteHierarchyId"),
            site_id=params.get("siteId"),
            ipv4_address=params.get("ipv4Address"),
            ipv6_address=params.get("ipv6Address"),
            mac_address=params.get("macAddress"),
            wlc_name=params.get("wlcName"),
            connected_network_device_name=params.get("connectedNetworkDeviceName"),
            ssid=params.get("ssid"),
            band=params.get("band"),
            view=params.get("view"),
            attribute=params.get("attribute"),
            headers=params.get("headers"),
            id=params.get("id"),
        )
        return new_object

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        self._result.update(dict(dnac_response={}))

        dnac = DNACSDK(params=self._task.args)

        id = self._task.args.get("id")
        if id:
            response = dnac.exec(
                family="clients",
                function='retrieves_specific_client_information_matching_the_macaddress_v1',
                params=self.get_object(self._task.args),
            )
            self._result.update(dict(dnac_response=response))
            self._result.update(dnac.exit_json())
            return self._result
        if not id:
            response = dnac.exec(
                family="clients",
                function='retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities_v1',
                params=self.get_object(self._task.args),
            )
            self._result.update(dict(dnac_response=response))
            self._result.update(dnac.exit_json())
            return self._result
