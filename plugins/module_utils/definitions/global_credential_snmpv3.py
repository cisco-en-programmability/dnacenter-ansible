import json

module_definition = json.loads(
    """{
    "family": "discovery",
    "name": "global_credential_snmpv3",
    "operations": {
        "post": [
            "create_snmpv3_credentials"
        ],
        "put": [
            "update_snmpv3_credentials"
        ]
    },
    "parameters": {
        "create_snmpv3_credentials": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "authPassword",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "authType",
                        "required": false,
                        "type": "string"
                    },
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
                        "name": "privacyPassword",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "privacyType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "snmpMode",
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
        "update_snmpv3_credentials": [
            {
                "name": "authPassword",
                "type": "string"
            },
            {
                "enum": [
                    "SHA",
                    "MD5"
                ],
                "name": "authType",
                "type": "string"
            },
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
                "name": "privacyPassword",
                "type": "string"
            },
            {
                "enum": [
                    "DES",
                    "AES128"
                ],
                "name": "privacyType",
                "type": "string"
            },
            {
                "enum": [
                    "AUTHPRIV",
                    "AUTHNOPRIV",
                    "NOAUTHNOPRIV"
                ],
                "name": "snmpMode",
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
        "create_snmpv3_credentials": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "update_snmpv3_credentials": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
