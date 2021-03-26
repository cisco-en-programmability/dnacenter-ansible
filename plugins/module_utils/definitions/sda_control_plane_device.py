from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "sda",
    "name": "sda_control_plane_device",
    "operations": {
        "delete": [
            "delete_control_plane_device"
        ],
        "get": [
            "get_control_plane_device"
        ],
        "post": [
            "add_control_plane_device"
        ]
    },
    "parameters": {
        "add_control_plane_device": [
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
        "delete_control_plane_device": [
            {
                "name": "device_ipaddress",
                "required": true,
                "type": "string"
            }
        ],
        "get_control_plane_device": [
            {
                "name": "device_ipaddress",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "add_control_plane_device": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        },
        "delete_control_plane_device": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        },
        "get_control_plane_device": {
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
