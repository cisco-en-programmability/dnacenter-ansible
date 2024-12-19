#!/usr/bin/env python
# -- coding: utf-8 --
# noqa: E501
from ansible.plugins.action import ActionBase
from ansible_collections.cisco.dnac.plugins.action.icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config_v1 import ActionModule  # noqa: E501


class ActionModule2(ActionBase):

    def __init__(self, *args, **kwargs):
        super(ActionModule2, self).__init__(*args, **kwargs)
        self._supports_async = False
        self._supports_check_mode = True
        self._result = None

    def run(self, tmp=None, task_vars=None):
        module = ActionModule(self._task.args, self._play_context, self._task)
        return module.run(tmp, task_vars)
