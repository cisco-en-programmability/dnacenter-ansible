from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "discovery",
    "name": "discovery_job",
    "operations": {
        "get": [
            "get_list_of_discoveries_by_discovery_id",
            "get_discovery_jobs_by_ip"
        ]
    },
    "parameters": {
        "get_discovery_jobs_by_ip": [
            {
                "name": "ip_address",
                "required": true,
                "type": "string"
            },
            {
                "name": "limit",
                "required": false,
                "type": "integer"
            },
            {
                "name": "name",
                "required": false,
                "type": "string"
            },
            {
                "name": "offset",
                "required": false,
                "type": "integer"
            }
        ],
        "get_list_of_discoveries_by_discovery_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "name": "ip_address",
                "required": false,
                "type": "string"
            },
            {
                "name": "limit",
                "required": false,
                "type": "integer"
            },
            {
                "name": "offset",
                "required": false,
                "type": "integer"
            }
        ]
    },
    "responses": {
        "get_discovery_jobs_by_ip": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_list_of_discoveries_by_discovery_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
