from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "clients",
    "name": "client_detail",
    "operations": {
        "get": [
            "get_client_detail"
        ]
    },
    "parameters": {
        "get_client_detail": [
            {
                "name": "mac_address",
                "required": true,
                "type": "string"
            },
            {
                "name": "timestamp",
                "required": false,
                "type": "integer"
            }
        ]
    },
    "responses": {
        "get_client_detail": {
            "properties": [
                "detail",
                "connectionInfo",
                "topology"
            ],
            "type": "object"
        }
    }
}"""
)
