import json

module_definition = json.loads('''{
    "family": "discovery",
    "name": "global_credential_http_write",
    "operations": {
        "post": [
            "create_http_write_credentials"
        ],
        "put": [
            "update_http_write_credentials"
        ]
    },
    "parameters": {
        "create_http_write_credentials": [
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
                        "name": "password",
                        "required": true,
                        "type": "string"
                    },
                    {
                        "name": "port",
                        "required": true,
                        "type": "integer"
                    },
                    {
                        "name": "secure",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "username",
                        "required": true,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ],
        "update_http_write_credentials": [
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
                "name": "password",
                "required": true,
                "type": "string"
            },
            {
                "name": "port",
                "required": true,
                "type": "integer"
            },
            {
                "name": "secure",
                "type": "boolean"
            },
            {
                "name": "username",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "create_http_write_credentials": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "update_http_write_credentials": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}''')