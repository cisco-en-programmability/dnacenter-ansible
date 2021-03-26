from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "sda",
    "name": "sda_fabric",
    "operations": {
        "delete": [
            "delete_sda_fabric"
        ],
        "get": [
            "get_sda_fabric_info"
        ],
        "post": [
            "add_fabric"
        ]
    },
    "parameters": {
        "add_fabric": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "fabricName",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ],
        "delete_sda_fabric": [
            {
                "name": "fabric_name",
                "required": true,
                "type": "string"
            }
        ],
        "get_sda_fabric_info": [
            {
                "name": "fabric_name",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "add_fabric": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        },
        "delete_sda_fabric": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        },
        "get_sda_fabric_info": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        }
    }
}"""
)
