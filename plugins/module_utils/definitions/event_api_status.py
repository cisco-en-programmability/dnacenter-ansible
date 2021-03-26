from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "event_management",
    "name": "event_api_status",
    "operations": {
        "get": [
            "get_status_api_for_events"
        ]
    },
    "parameters": {
        "get_status_api_for_events": [
            {
                "name": "execution_id",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "get_status_api_for_events": {
            "properties": [
                "errorMessage",
                "apiStatus",
                "statusMessage"
            ],
            "type": "object"
        }
    }
}"""
)
