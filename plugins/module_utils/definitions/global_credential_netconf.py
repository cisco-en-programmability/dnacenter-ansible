from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "discovery",
    "name": "global_credential_netconf",
    "operations": {
        "post": [
            "create_netconf_credentials"
        ],
        "put": [
            "update_netconf_credentials"
        ]
    },
    "parameters": {
        "create_netconf_credentials": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "comments",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "credentialType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instanceTenantId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instanceUuid",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "netconfPort",
                        "required": true,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ],
        "update_netconf_credentials": [
            {
                "name": "comments",
                "type": "string"
            },
            {
                "enum": [
                    "GLOBAL",
                    "APP"
                ],
                "name": "credentialType",
                "type": "string"
            },
            {
                "name": "description",
                "type": "string"
            },
            {
                "name": "id",
                "type": "string"
            },
            {
                "name": "instanceTenantId",
                "type": "string"
            },
            {
                "name": "instanceUuid",
                "type": "string"
            },
            {
                "name": "netconfPort",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "create_netconf_credentials": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "update_netconf_credentials": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
