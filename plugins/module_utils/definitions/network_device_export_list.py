from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "devices",
    "name": "network_device_export_list",
    "operations": {
        "post": [
            "export_device_list"
        ]
    },
    "parameters": {
        "export_device_list": [
            {
                "array_type": "string",
                "name": "deviceUuids",
                "required": true,
                "schema": [],
                "type": "array"
            },
            {
                "name": "id",
                "type": "string"
            },
            {
                "enum": [
                    "CREDENTIALDETAILS",
                    "DEVICEDETAILS"
                ],
                "name": "operationEnum",
                "type": "string"
            },
            {
                "array_type": "string",
                "name": "parameters",
                "required": false,
                "schema": [],
                "type": "array"
            },
            {
                "name": "password",
                "type": "string"
            }
        ]
    },
    "responses": {
        "export_device_list": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
