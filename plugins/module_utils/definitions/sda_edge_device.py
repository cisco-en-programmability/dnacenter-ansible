from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "sda",
    "name": "sda_edge_device",
    "operations": {
        "delete": [
            "delete_edge_device"
        ],
        "get": [
            "get_edge_device"
        ],
        "post": [
            "add_edge_device"
        ]
    },
    "parameters": {
        "add_edge_device": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "deviceManagementIpAddress",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "siteNameHierarchy",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ],
        "delete_edge_device": [
            {
                "name": "device_ipaddress",
                "required": true,
                "type": "string"
            }
        ],
        "get_edge_device": [
            {
                "name": "device_ipaddress",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "add_edge_device": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        },
        "delete_edge_device": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        },
        "get_edge_device": {
            "properties": [
                "status",
                "description",
                "name",
                "roles",
                "deviceManagementIpAddress",
                "siteHierarchy"
            ],
            "type": "object"
        }
    }
}"""
)
