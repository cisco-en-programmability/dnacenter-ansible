from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "configuration_templates",
    "name": "template_preview",
    "operations": {
        "put": [
            "preview_template"
        ]
    },
    "parameters": {
        "preview_template": [
            {
                "name": "params",
                "required": false,
                "schema": [],
                "type": "object"
            },
            {
                "name": "templateId",
                "type": "string"
            }
        ]
    },
    "responses": {
        "preview_template": {
            "properties": [
                "cliPreview",
                "templateId",
                "validationErrors"
            ],
            "type": "object"
        }
    }
}"""
)
