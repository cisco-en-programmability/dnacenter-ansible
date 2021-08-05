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
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DNACSDK,
    dnac_argument_spec,
)

# Get common arguements specification
argument_spec = dnac_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    _id=dict(type="str"),
    deviceInfo=dict(type="dict"),
    systemResetWorkflow=dict(type="dict"),
    systemWorkflow=dict(type="dict"),
    workflow=dict(type="dict"),
    runSummaryList=dict(type="list"),
    workflowParameters=dict(type="dict"),
    dayZeroConfig=dict(type="dict"),
    dayZeroConfigPreview=dict(type="dict"),
    version=dict(type="int"),
    tenantId=dict(type="str"),
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
        self._supports_async = True
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
            _id=params.get("_id"),
            deviceInfo=params.get("deviceInfo"),
            systemResetWorkflow=params.get("systemResetWorkflow"),
            systemWorkflow=params.get("systemWorkflow"),
            workflow=params.get("workflow"),
            runSummaryList=params.get("runSummaryList"),
            workflowParameters=params.get("workflowParameters"),
            dayZeroConfig=params.get("dayZeroConfig"),
            dayZeroConfigPreview=params.get("dayZeroConfigPreview"),
            version=params.get("version"),
            tenantId=params.get("tenantId"),
        )
        return new_object

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        dnac = DNACSDK(params=self._task.args)

        response = dnac.exec(
            family="device_onboarding_pnp",
            function='import_devices_in_bulk',
            op_modifies=True,
            params=self.get_object(self._task.args),
        )
        self._result.update(dict(dnac_response=response))
        self._result.update(dnac.exit_json())
        return self._result
