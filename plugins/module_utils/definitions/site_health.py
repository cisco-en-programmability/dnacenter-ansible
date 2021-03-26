from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "sites",
    "name": "site_health",
    "operations": {
        "get": [
            "get_site_health"
        ]
    },
    "parameters": {
        "get_site_health": [
            {
                "name": "timestamp",
                "required": false,
                "type": "integer"
            }
        ]
    },
    "responses": {
        "get_site_health": {
            "properties": [
                "response"
            ],
            "type": "object"
        }
    }
}"""
)
