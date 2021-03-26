from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "discovery",
    "name": "snmp_property",
    "operations": {
        "get": [
            "get_snmp_properties"
        ],
        "post": [
            "create_update_snmp_properties"
        ]
    },
    "parameters": {
        "create_update_snmp_properties": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
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
                        "name": "intValue",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "systemPropertyName",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ],
        "get_snmp_properties": []
    },
    "responses": {
        "create_update_snmp_properties": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_snmp_properties": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
