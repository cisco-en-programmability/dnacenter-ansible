from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "devices",
    "name": "network_device_register",
    "operations": {
        "get": [
            "register_device_for_wsa"
        ]
    },
    "parameters": {
        "register_device_for_wsa": [
            {
                "name": "macaddress",
                "required": false,
                "type": "string"
            },
            {
                "name": "serial_number",
                "required": false,
                "type": "string"
            }
        ]
    },
    "responses": {
        "register_device_for_wsa": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
