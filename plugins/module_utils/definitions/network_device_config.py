from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "devices",
    "name": "network_device_config",
    "operations": {
        "get": [
            "get_device_config_for_all_devices",
            "get_device_config_count"
        ]
    },
    "parameters": {
        "get_device_config_count": [
            {
                "artificial": true,
                "name": "count",
                "required": true,
                "type": "boolean"
            }
        ],
        "get_device_config_for_all_devices": []
    },
    "responses": {
        "get_device_config_count": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_device_config_for_all_devices": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
