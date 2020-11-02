import json

module_definition = json.loads('''{
    "family": "wireless",
    "name": "ssid",
    "operations": {
        "delete": [
            "delete_ssid_and_provision_it_to_devices"
        ],
        "post": [
            "create_and_provision_ssid"
        ]
    },
    "parameters": {
        "create_and_provision_ssid": [
            {
                "name": "enableFabric",
                "required": true,
                "type": "boolean"
            },
            {
                "name": "flexConnect",
                "required": false,
                "schema": [
                    {
                        "name": "enableFlexConnect",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "localToVlan",
                        "required": false,
                        "type": "integer"
                    }
                ],
                "type": "object"
            },
            {
                "array_type": "string",
                "name": "managedAPLocations",
                "required": true,
                "schema": [],
                "type": "array"
            },
            {
                "name": "ssidDetails",
                "required": true,
                "schema": [
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "securityLevel",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "enableFastLane",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "passphrase",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "trafficType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "enableBroadcastSSID",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "radioPolicy",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "enableMACFiltering",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "fastTransition",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "webAuthURL",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "object"
            },
            {
                "enum": [
                    "Guest",
                    "Enterprise"
                ],
                "name": "ssidType",
                "required": true,
                "type": "string"
            }
        ],
        "delete_ssid_and_provision_it_to_devices": [
            {
                "name": "managed_aplocations",
                "required": true,
                "type": "string"
            },
            {
                "name": "ssid_name",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "create_and_provision_ssid": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        },
        "delete_ssid_and_provision_it_to_devices": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        }
    }
}''')