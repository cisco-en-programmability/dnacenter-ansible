from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "software_image_management_swim",
    "name": "import_image",
    "operations": {
        "get": [
            "get_software_image_details"
        ]
    },
    "parameters": {
        "get_software_image_details": [
            {
                "name": "application_type",
                "required": false,
                "type": "string"
            },
            {
                "name": "created_time",
                "required": false,
                "type": "integer"
            },
            {
                "name": "family",
                "required": false,
                "type": "string"
            },
            {
                "name": "image_integrity_status",
                "required": false,
                "type": "string"
            },
            {
                "name": "image_name",
                "required": false,
                "type": "string"
            },
            {
                "name": "image_series",
                "required": false,
                "type": "string"
            },
            {
                "name": "image_size_greater_than",
                "required": false,
                "type": "integer"
            },
            {
                "name": "image_size_lesser_than",
                "required": false,
                "type": "integer"
            },
            {
                "name": "image_uuid",
                "required": false,
                "type": "string"
            },
            {
                "name": "is_cco_latest",
                "required": false,
                "type": "boolean"
            },
            {
                "name": "is_cco_recommended",
                "required": false,
                "type": "boolean"
            },
            {
                "name": "is_tagged_golden",
                "required": false,
                "type": "boolean"
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
            },
            {
                "name": "sort_by",
                "required": false,
                "type": "string"
            },
            {
                "name": "sort_order",
                "required": false,
                "type": "string"
            },
            {
                "name": "version",
                "required": false,
                "type": "string"
            }
        ]
    },
    "responses": {
        "get_software_image_details": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
