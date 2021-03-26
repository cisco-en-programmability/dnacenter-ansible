from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "network_settings",
    "name": "credential_to_site",
    "operations": {
        "post": [
            "assign_credential_to_site"
        ]
    },
    "parameters": {
        "assign_credential_to_site": [
            {
                "name": "site_id",
                "required": true,
                "type": "string"
            },
            {
                "name": "cliId",
                "type": "string"
            },
            {
                "name": "httpRead",
                "type": "string"
            },
            {
                "name": "httpWrite",
                "type": "string"
            },
            {
                "name": "snmpV2ReadId",
                "type": "string"
            },
            {
                "name": "snmpV2WriteId",
                "type": "string"
            },
            {
                "name": "snmpV3Id",
                "type": "string"
            }
        ]
    },
    "responses": {
        "assign_credential_to_site": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        }
    }
}"""
)
