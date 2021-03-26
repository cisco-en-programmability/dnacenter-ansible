from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "command_runner",
    "name": "network_device_poller_read_request",
    "operations": {
        "post": [
            "run_read_only_commands_on_devices"
        ]
    },
    "parameters": {
        "run_read_only_commands_on_devices": [
            {
                "array_type": "string",
                "name": "commands",
                "required": true,
                "schema": [],
                "type": "array"
            },
            {
                "name": "description",
                "type": "string"
            },
            {
                "array_type": "string",
                "name": "deviceUuids",
                "required": true,
                "schema": [],
                "type": "array"
            },
            {
                "name": "name",
                "type": "string"
            },
            {
                "name": "timeout",
                "type": "integer"
            }
        ]
    },
    "responses": {
        "run_read_only_commands_on_devices": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
