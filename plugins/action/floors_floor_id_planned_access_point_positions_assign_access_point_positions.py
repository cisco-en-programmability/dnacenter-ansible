#!/usr/bin/env python
# -- coding: utf-8 --
from ansible.plugins.action import ActionBase
from ansible_collections.cisco.dnac.plugins.action.floors_floor_id_planned_access_point_positions_assign_access_point_positions_v2 import ActionModule


class ActionModule2(ActionBase):

    def __init__(self, *args, **kwargs):
        super(ActionModule2, self).__init__(*args, **kwargs)
        self._supports_async = False
        self._supports_check_mode = True
        self._result = None

    def run(self, tmp=None, task_vars=None):
        module = ActionModule(self._task.args, self._play_context, self._task)
        return module.run(tmp, task_vars)
