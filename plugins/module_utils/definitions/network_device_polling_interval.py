from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "devices",
    "name": "network_device_polling_interval",
    "operations": {
        "get": [
            "get_polling_interval_by_id",
            "get_polling_interval_for_all_devices"
        ]
    },
    "parameters": {
        "get_polling_interval_by_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_polling_interval_for_all_devices": []
    },
    "responses": {
        "get_polling_interval_by_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_polling_interval_for_all_devices": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
