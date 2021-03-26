from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "discovery",
    "name": "global_credential",
    "operations": {
        "delete": [
            "delete_global_credentials_by_id"
        ],
        "get": [
            "get_global_credentials",
            "get_credential_sub_type_by_credential_id"
        ],
        "put": [
            "update_global_credentials"
        ]
    },
    "parameters": {
        "delete_global_credentials_by_id": [
            {
                "name": "global_credential_id",
                "required": true,
                "type": "string"
            }
        ],
        "get_credential_sub_type_by_credential_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_global_credentials": [
            {
                "name": "credential_sub_type",
                "required": true,
                "type": "string"
            },
            {
                "name": "order",
                "required": false,
                "type": "string"
            },
            {
                "name": "sort_by",
                "required": false,
                "type": "string"
            }
        ],
        "update_global_credentials": [
            {
                "name": "global_credential_id",
                "required": true,
                "type": "string"
            },
            {
                "array_type": "string",
                "name": "siteUuids",
                "required": false,
                "schema": [],
                "type": "array"
            }
        ]
    },
    "responses": {
        "delete_global_credentials_by_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_credential_sub_type_by_credential_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_global_credentials": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "update_global_credentials": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
