# Copyright (c) 2022 Cisco and/or its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os
import json

from ansible_collections.ansible.netcommon.tests.unit.modules.utils import (
    AnsibleExitJson,
    AnsibleFailJson,
    ModuleTestCase,
)
from ansible_collections.ansible.netcommon.tests.unit.modules.utils import (
    set_module_args as _set_module_args,
)
from unittest.mock import patch


def set_module_args(args):
    return _set_module_args(args)


fixture_path = os.path.join(os.path.dirname(__file__), "fixtures")
fixture_data = {}


def loadPlaybookData(module_name):
    path = os.path.join(fixture_path, "{0}.json".format(module_name))
    print(path)

    with open(path) as f:
        data = f.read()

    try:
        j_data = json.loads(data)
    except Exception as e:
        print(e)
        pass

    return j_data


def load_fixture(module_name, name, device=""):
    path = os.path.join(fixture_path, module_name, device, name)
    if not os.path.exists(path):
        path = os.path.join(fixture_path, module_name, name)

    if path in fixture_data:
        return fixture_data[path]

    with open(path) as f:
        data = f.read()

    try:
        data = json.loads(data)
    except Exception:
        pass

    fixture_data[path] = data
    return data


class TestDnacModule(ModuleTestCase):

    def __init__(self, module):

        """
        Initialize an instance of class .

        Parameters:
            - module (ModuleType): The Python module associated with this instance.

        Attributes:
            - module (ModuleType): The provided module.
            - test_data (dict): The loaded playbook data from the module.
            - playbook_config (dict): The playbook configuration.
            - playbook_config_missing_param (dict): The playbook configuration with missing parameters.
        """

        self.module = module
        self.test_data = self.loadPlaybookData(str(self.module.__name__))
        self.playbook_config = self.test_data.get("playbook_config")
        self.playbook_config_missing_param = self.test_data.get("playbook_config_missing_param")

    def setUp(self):

        """
        Set up the test environment by mocking Cisco DNA Center SDK initialization and execution.
        This method is automatically called before each test case to ensure a clean and controlled environment.
        Mocks the initialization and execution of the Cisco DNA Center SDK to isolate testing from actual SDK operations.

        Mocked attributes:
            - mock_dnac_init: Mocks the initialization of the DNACSDK class.
            - run_dnac_init: The started mock for DNACSDK initialization.
            - mock_dnac_exec: Mocks the execution of DNACSDK methods.
            - run_dnac_exec: The started mock for DNACSDK method execution.
        """

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

    def tearDown(self):

        """
        Clean up the test environment by stopping the mocked Cisco DNA Center SDK initialization and execution.
        This method is automatically called after each test case to clean up any resources or mocks created during testing.
        Stops the mock instances of the Cisco DNA Center SDK initialization and execution.
        """

        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def loadPlaybookData(self, module):

        """
        Load JSON data from a file.

        Parameters:
            - module (str): The name of the module used to construct the filename.

        Returns:
            - dict: The loaded JSON data.

        Raises:
            - FileNotFoundError: If the file does not exist.
            - json.JSONDecodeError: If there is an error decoding the JSON data.
        """

        file_path = os.path.join(fixture_path, "{0}.json".format(module))
        print(file_path)
        try:
            with open(file_path) as f:
                data = f.read()
            j_data = json.loads(data)
        except Exception as e:
            print(e)
            pass

        return j_data

    def execute_module_devices(
        self, failed=False, changed=False, response=None, sort=True, defaults=False
    ):

        """
        This method executes a module for a single device.

        Parameters:
            - failed (bool, optional): If True, check for failures. Defaults to False.
            - changed (bool, optional): If True, check for changes. Defaults to False.
            - response (list, optional): The expected response data. Defaults to None.
            - sort (bool, optional): If True, sort the response data before comparison. Defaults to True.
            - device (str, optional): The device to execute the module on. Defaults to an empty string.

        Returns:
            - dict: A dictionary containing the execution result.
        """

        module_name = self.module.__name__.rsplit(".", 1)[1]
        local_fixture_path = os.path.join(fixture_path, module_name)

        models = []
        for path in os.listdir(local_fixture_path):
            path = os.path.join(local_fixture_path, path)
            if os.path.isdir(path):
                models.append(os.path.basename(path))
        if not models:
            models = [""]

        retvals = {}
        for model in models:
            retvals[model] = self.execute_module(
                failed, changed, response, sort, device=model
            )

        return retvals

    def execute_module(
        self, failed=False, changed=False, response=None, sort=True, device=""
    ):

        """
        Execute a module for a specific device and perform validation.

        This method executes the module for a specific device, performs validation checks, and returns the result.

        Parameters:
            - failed (bool, optional): If True, check for failures. Defaults to False.
            - changed (bool, optional): If True, check for changes. Defaults to False.
            - response (list, optional): The expected response data. Defaults to None.
            - sort (bool, optional): If True, sort the response data before comparison. Defaults to True.
            - device (str, optional): The device to execute the module on. Defaults to an empty string.

        Returns:
            - dict: A dictionary containing the execution result, including 'failed', 'changed', and 'response' keys.
        """

        self.load_fixtures(response, device=device)

        if failed:
            result = self.failed()
            self.assertTrue(result["failed"], result)
        else:
            result = self.changed(changed)
            self.assertEqual(result["changed"], changed, result)

        if response is not None:
            if sort:
                self.assertEqual(
                    sorted(response), sorted(result["response"]), result["response"]
                )
            else:
                self.assertEqual(response, result["response"], result["response"])

        return result

    def failed(self):

        """
        Check for failures during module execution.

        Returns:
            - dict: A dictionary containing the failure status and additional information.
        """

        with self.assertRaises(AnsibleFailJson) as exc:
            self.module.main()

        result = exc.exception.args[0]
        self.assertTrue(result["failed"], result)
        return result

    def changed(self, changed=False):

        """
        Check for changes during module execution.

        Parameters:
            - changed (bool, optional): If True, check for changes. Defaults to False.

        Returns:
            - dict: A dictionary containing the change status and additional information.
        """

        with self.assertRaises(AnsibleExitJson) as exc:
            self.module.main()

        result = exc.exception.args[0]
        self.assertEqual(result["changed"], changed, result)
        return result
