import json

module_definition = json.loads(
    """{
    "family": "discovery",
    "name": "global_credential_snmpv2_write_community",
    "operations": {
        "post": [
            "create_snmp_write_community"
        ],
        "put": [
            "update_snmp_write_community"
        ]
    },
    "parameters": {
        "create_snmp_write_community": [
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
                        "name": "writeCommunity",
                        "required": true,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ],
        "update_snmp_write_community": [
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
                "name": "writeCommunity",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "create_snmp_write_community": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "update_snmp_write_community": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
