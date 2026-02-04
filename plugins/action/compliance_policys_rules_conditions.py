#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

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
    dnac_compare_equality,
    get_dict_result,
)
from ansible_collections.cisco.dnac.plugins.plugin_utils.exceptions import (
    InconsistentParameters,
)

# Get common arguments specification
argument_spec = dnac_argument_spec()
# Add arguments specific for this module
argument_spec.update(
    dict(
        state=dict(type="str", default="present", choices=["present", "absent"]),
        scope=dict(type="str"),
        deviceProperty=dict(type="str"),
        showCommand=dict(type="str"),
        parseAsBlocks=dict(type="bool"),
        blockStartExpression=dict(type="str"),
        blockEndExpression=dict(type="str"),
        blockViolationCriteria=dict(type="str"),
        operator=dict(type="str"),
        regexViolationCriteria=dict(type="str"),
        value=dict(type="str"),
        action=dict(type="dict"),
        policyId=dict(type="str"),
        ruleId=dict(type="str"),
        id=dict(type="str"),
    )
)

required_if = [
    ("state", "present", ["id", "policyId", "ruleId"], True),
    ("state", "absent", ["id", "policyId", "ruleId"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class CompliancePolicysRulesConditions(object):
    def __init__(self, params, dnac):
        self.dnac = dnac
        self.new_object = dict(
            scope=params.get("scope"),
            deviceProperty=params.get("deviceProperty"),
            showCommand=params.get("showCommand"),
            parseAsBlocks=params.get("parseAsBlocks"),
            blockStartExpression=params.get("blockStartExpression"),
            blockEndExpression=params.get("blockEndExpression"),
            blockViolationCriteria=params.get("blockViolationCriteria"),
            operator=params.get("operator"),
            regexViolationCriteria=params.get("regexViolationCriteria"),
            value=params.get("value"),
            action=params.get("action"),
            policy_id=params.get("policyId"),
            rule_id=params.get("ruleId"),
            id=params.get("id"),
        )

    def get_all_params(self, name=None, id=None):
        new_object_params = {}
        new_object_params["offset"] = self.new_object.get("offset")
        new_object_params["limit"] = self.new_object.get("limit")
        new_object_params["policy_id"] = self.new_object.get(
            "policyId"
        ) or self.new_object.get("policy_id")
        new_object_params["rule_id"] = self.new_object.get(
            "ruleId"
        ) or self.new_object.get("rule_id")
        return new_object_params

    def create_params(self):
        new_object_params = {}
        new_object_params["scope"] = self.new_object.get("scope")
        new_object_params["deviceProperty"] = self.new_object.get("deviceProperty")
        new_object_params["showCommand"] = self.new_object.get("showCommand")
        new_object_params["parseAsBlocks"] = self.new_object.get("parseAsBlocks")
        new_object_params["blockStartExpression"] = self.new_object.get(
            "blockStartExpression"
        )
        new_object_params["blockEndExpression"] = self.new_object.get(
            "blockEndExpression"
        )
        new_object_params["blockViolationCriteria"] = self.new_object.get(
            "blockViolationCriteria"
        )
        new_object_params["operator"] = self.new_object.get("operator")
        new_object_params["regexViolationCriteria"] = self.new_object.get(
            "regexViolationCriteria"
        )
        new_object_params["value"] = self.new_object.get("value")
        new_object_params["action"] = self.new_object.get("action")
        new_object_params["policyId"] = self.new_object.get("policyId")
        new_object_params["ruleId"] = self.new_object.get("ruleId")
        return new_object_params

    def delete_by_id_params(self):
        new_object_params = {}
        new_object_params["policy_id"] = self.new_object.get("policy_id")
        new_object_params["rule_id"] = self.new_object.get("rule_id")
        new_object_params["id"] = self.new_object.get("id")
        return new_object_params

    def update_by_id_params(self):
        new_object_params = {}
        new_object_params["scope"] = self.new_object.get("scope")
        new_object_params["deviceProperty"] = self.new_object.get("deviceProperty")
        new_object_params["showCommand"] = self.new_object.get("showCommand")
        new_object_params["parseAsBlocks"] = self.new_object.get("parseAsBlocks")
        new_object_params["blockStartExpression"] = self.new_object.get(
            "blockStartExpression"
        )
        new_object_params["blockEndExpression"] = self.new_object.get(
            "blockEndExpression"
        )
        new_object_params["blockViolationCriteria"] = self.new_object.get(
            "blockViolationCriteria"
        )
        new_object_params["operator"] = self.new_object.get("operator")
        new_object_params["regexViolationCriteria"] = self.new_object.get(
            "regexViolationCriteria"
        )
        new_object_params["value"] = self.new_object.get("value")
        new_object_params["action"] = self.new_object.get("action")
        new_object_params["policyId"] = self.new_object.get("policyId")
        new_object_params["ruleId"] = self.new_object.get("ruleId")
        new_object_params["id"] = self.new_object.get("id")
        return new_object_params

    def get_object_by_name(self, name):
        result = None
        # NOTE: Does not have a get by name method or it is in another action
        try:
            items = self.dnac.exec(
                family="compliance",
                function="retrieve_the_conditions",
                params=self.get_all_params(name=name),
            )
            if isinstance(items, dict):
                if "response" in items:
                    items = items.get("response")
            result = get_dict_result(items, "name", name)
        except Exception:
            result = None
        return result

    def get_object_by_id(self, id):
        result = None
        try:
            items = self.dnac.exec(
                family="compliance",
                function="retrieve_a_specific_condition",
                params={"id": id},
            )
            if isinstance(items, dict):
                if "response" in items:
                    items = items.get("response")
            result = get_dict_result(items, "id", id)
        except Exception:
            result = None
        return result

    def exists(self):
        id_exists = False
        name_exists = False
        prev_obj = None
        o_id = self.new_object.get("id")
        name = self.new_object.get("name")
        if o_id:
            prev_obj = self.get_object_by_id(o_id)
            id_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if not id_exists and name:
            prev_obj = self.get_object_by_name(name)
            name_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if name_exists:
            _id = prev_obj.get("id")
            if id_exists and name_exists and o_id != _id:
                raise InconsistentParameters(
                    "The 'id' and 'name' params don't refer to the same object"
                )
            if _id:
                self.new_object.update(dict(id=_id))
            if _id:
                prev_obj = self.get_object_by_id(_id)
        it_exists = prev_obj is not None and isinstance(prev_obj, dict)
        return (it_exists, prev_obj)

    def requires_update(self, current_obj):
        requested_obj = self.new_object

        obj_params = [
            ("scope", "scope"),
            ("deviceProperty", "deviceProperty"),
            ("showCommand", "showCommand"),
            ("parseAsBlocks", "parseAsBlocks"),
            ("blockStartExpression", "blockStartExpression"),
            ("blockEndExpression", "blockEndExpression"),
            ("blockViolationCriteria", "blockViolationCriteria"),
            ("operator", "operator"),
            ("regexViolationCriteria", "regexViolationCriteria"),
            ("value", "value"),
            ("action", "action"),
            ("policyId", "policy_id"),
            ("ruleId", "rule_id"),
            ("id", "id"),
        ]
        # Method 1. Params present in request (Ansible) obj are the same as the current (DNAC) params
        # If any does not have eq params, it requires update
        return any(
            not dnac_compare_equality(
                current_obj.get(dnac_param), requested_obj.get(ansible_param)
            )
            for (dnac_param, ansible_param) in obj_params
        )

    def create(self):
        result = self.dnac.exec(
            family="compliance",
            function="create_a_new_condition",
            params=self.create_params(),
            op_modifies=True,
        )
        return result

    def update(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        result = None
        if not id:
            prev_obj_name = self.get_object_by_name(name)
            id_ = None
            if prev_obj_name:
                id_ = prev_obj_name.get("id")
            if id_:
                self.new_object.update(dict(id=id_))
        result = self.dnac.exec(
            family="compliance",
            function="update_an_existing_condition",
            params=self.update_by_id_params(),
            op_modifies=True,
        )
        return result

    def delete(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        result = None
        if not id:
            prev_obj_name = self.get_object_by_name(name)
            id_ = None
            if prev_obj_name:
                id_ = prev_obj_name.get("id")
            if id_:
                self.new_object.update(dict(id=id_))
        result = self.dnac.exec(
            family="compliance",
            function="delete_a_specific_condition",
            params=self.delete_by_id_params(),
        )
        return result


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        if not ANSIBLE_UTILS_IS_INSTALLED:
            raise AnsibleActionFail(
                "ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'"
            )
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

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        dnac = DNACSDK(self._task.args)
        obj = CompliancePolicysRulesConditions(self._task.args, dnac)

        state = self._task.args.get("state")

        response = None

        if state == "present":
            obj_exists, prev_obj = obj.exists()
            if obj_exists:
                if obj.requires_update(prev_obj):
                    response = obj.update()
                    dnac.object_updated()
                else:
                    response = prev_obj
                    dnac.object_already_present()
            else:
                response = obj.create()
                dnac.object_created()

        elif state == "absent":
            obj_exists, prev_obj = obj.exists()
            if obj_exists:
                response = obj.delete()
                dnac.object_deleted()
            else:
                dnac.object_already_absent()

        self._result.update(dict(dnac_response=response))
        self._result.update(dnac.exit_json())
        return self._result
