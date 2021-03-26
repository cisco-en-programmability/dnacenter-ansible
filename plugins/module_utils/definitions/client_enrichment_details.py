from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "clients",
    "name": "client_enrichment_details",
    "operations": {
        "get": [
            "get_client_enrichment_details"
        ]
    },
    "parameters": {
        "get_client_enrichment_details": [
            {
                "artificial": true,
                "name": "headers",
                "required": true,
                "schema": [],
                "type": "object"
            }
        ]
    },
    "responses": {
        "get_client_enrichment_details": {
            "array_type": "object",
            "properties": [
                "userDetails",
                "connectedDevice",
                "issueDetails"
            ],
            "type": "array"
        }
    }
}"""
)
