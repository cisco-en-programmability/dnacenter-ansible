from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "sites",
    "name": "site_device",
    "operations": {
        "post": [
            "assign_device_to_site"
        ]
    },
    "parameters": {
        "assign_device_to_site": [
            {
                "name": "site_id",
                "required": true,
                "type": "string"
            },
            {
                "array_type": "object",
                "name": "device",
                "required": true,
                "schema": [
                    {
                        "name": "ip",
                        "required": true,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ]
    },
    "responses": {
        "assign_device_to_site": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        }
    }
}"""
)
