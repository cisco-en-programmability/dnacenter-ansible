from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "sda",
    "name": "sda_auth_profile",
    "operations": {
        "delete": [
            "delete_default_authentication_profile"
        ],
        "get": [
            "get_default_authentication_profile"
        ],
        "post": [
            "add_default_authentication_profile"
        ],
        "put": [
            "update_default_authentication_profile"
        ]
    },
    "parameters": {
        "add_default_authentication_profile": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "siteNameHierarchy",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "authenticateTemplateName",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ],
        "delete_default_authentication_profile": [
            {
                "name": "site_name_hierarchy",
                "required": true,
                "type": "string"
            }
        ],
        "get_default_authentication_profile": [
            {
                "name": "site_name_hierarchy",
                "required": true,
                "type": "string"
            }
        ],
        "update_default_authentication_profile": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "siteNameHierarchy",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "authenticateTemplateName",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ]
    },
    "responses": {
        "add_default_authentication_profile": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        },
        "delete_default_authentication_profile": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        },
        "get_default_authentication_profile": {
            "properties": [
                "siteNameHierarchy",
                "authenticateTemplateName",
                "authenticateTemplateId"
            ],
            "type": "object"
        },
        "update_default_authentication_profile": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        }
    }
}"""
)
