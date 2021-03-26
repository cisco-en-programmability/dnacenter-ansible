from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "device_replacement",
    "name": "device_replacement_workflow",
    "operations": {
        "post": [
            "deploy_device_replacement_workflow"
        ]
    },
    "parameters": {
        "deploy_device_replacement_workflow": [
            {
                "name": "faultyDeviceSerialNumber",
                "required": true,
                "type": "string"
            },
            {
                "name": "replacementDeviceSerialNumber",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "deploy_device_replacement_workflow": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
