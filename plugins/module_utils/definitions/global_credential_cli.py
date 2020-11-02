import json

module_definition = json.loads('''{
    "family": "discovery",
    "name": "global_credential_cli",
    "operations": {
        "post": [
            "create_cli_credentials"
        ],
        "put": [
            "update_cli_credentials"
        ]
    },
    "parameters": {
        "create_cli_credentials": [
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
                        "name": "enablePassword",
                        "required": true,
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
                        "name": "username",
                        "required": true,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ],
        "update_cli_credentials": [
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
                "name": "enablePassword",
                "required": true,
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
                "name": "username",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "create_cli_credentials": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "update_cli_credentials": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}''')