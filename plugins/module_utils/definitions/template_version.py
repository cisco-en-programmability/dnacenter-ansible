from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "configuration_templates",
    "name": "template_version",
    "operations": {
        "get": [
            "get_template_versions"
        ],
        "post": [
            "version_template"
        ]
    },
    "parameters": {
        "get_template_versions": [
            {
                "name": "template_id",
                "required": true,
                "type": "string"
            }
        ],
        "version_template": [
            {
                "name": "comments",
                "type": "string"
            },
            {
                "name": "templateId",
                "type": "string"
            }
        ]
    },
    "responses": {
        "get_template_versions": {
            "array_type": "object",
            "properties": [
                "name",
                "projectName",
                "projectId",
                "templateId",
                "versionsInfo",
                "composite"
            ],
            "type": "array"
        },
        "version_template": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
