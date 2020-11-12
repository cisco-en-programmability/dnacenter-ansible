import json

module_definition = json.loads(
    """{
    "family": "wireless",
    "name": "enterprise_ssid",
    "operations": {
        "delete": [
            "delete_enterprise_ssid"
        ],
        "get": [
            "get_enterprise_ssid"
        ],
        "post": [
            "create_enterprise_ssid"
        ]
    },
    "parameters": {
        "create_enterprise_ssid": [
            {
                "name": "enableBroadcastSSID",
                "type": "boolean"
            },
            {
                "name": "enableFastLane",
                "type": "boolean"
            },
            {
                "name": "enableMACFiltering",
                "type": "boolean"
            },
            {
                "enum": [
                    "Adaptive",
                    "Enable",
                    "Disable"
                ],
                "name": "fastTransition",
                "type": "string"
            },
            {
                "maxLength": 32,
                "name": "name",
                "required": true,
                "type": "string"
            },
            {
                "maxLength": 63,
                "minLength": 8,
                "name": "passphrase",
                "type": "string"
            },
            {
                "enum": [
                    "Dual band operation (2.4GHz and 5GHz)",
                    "Dual band operation with band select",
                    "5GHz only",
                    "2.4GHz only"
                ],
                "name": "radioPolicy",
                "type": "string"
            },
            {
                "enum": [
                    "WPA2_ENTERPRISE",
                    "WPA2_PERSONAL",
                    "OPEN"
                ],
                "name": "securityLevel",
                "required": true,
                "type": "string"
            },
            {
                "enum": [
                    "voicedata",
                    "data"
                ],
                "name": "trafficType",
                "type": "string"
            }
        ],
        "delete_enterprise_ssid": [
            {
                "name": "ssid_name",
                "required": true,
                "type": "string"
            }
        ],
        "get_enterprise_ssid": [
            {
                "name": "ssid_name",
                "required": false,
                "type": "string"
            }
        ]
    },
    "responses": {
        "create_enterprise_ssid": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        },
        "delete_enterprise_ssid": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        },
        "get_enterprise_ssid": {
            "array_type": "object",
            "properties": [
                "instanceUuid",
                "version",
                "ssidDetails",
                "groupUuid",
                "inheritedGroupUuid",
                "inheritedGroupName"
            ],
            "type": "array"
        }
    }
}"""
)
