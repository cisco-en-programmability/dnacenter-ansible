from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.plugins.action import ActionBase
from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
    AnsibleArgSpecValidator,
)
from ansible.errors import AnsibleActionFail
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.event_subscription import (
    module_definition,
)

IDEMPOTENT = False

# Instantiate the module definition for this module
moddef = ModuleDefinition(module_definition)
# Get the argument spec for this module and add the 'state' param,
# which is common to all modules
argument_spec = moddef.get_argument_spec_dict()
argument_spec.update(dict(dnac_argument_spec(idempotent=IDEMPOTENT)))
# Get the schema conditionals, if applicable
required_if = moddef.get_required_if_list()


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        super(ActionModule, self).__init__(*args, **kwargs)
        self._supports_async = False
        self._result = None

    # Checks the supplied parameters against the argument spec for this module
    def _check_argspec(self):
        aav = AnsibleArgSpecValidator(
            data=self._task.args,
            schema=dict(argument_spec=argument_spec),
            schema_format="argspec",
            schema_conditionals=dict(required_if=required_if),
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

        dnac = DNACModule(
            moddef=moddef,
            params=self._task.args,
            verbosity=self._play_context.verbosity,
        )

        state = self._task.args.get("state")

        if state == "query":
            dnac.exec("get")

        elif state == "delete":
            dnac.exec("delete")

        elif state == "create":
            dnac.disable_validation()
            dnac.exec("post")

        elif state == "update":
            dnac.disable_validation()
            dnac.exec("put")

        self._result.update(dnac.exit_json())
        return self._result
