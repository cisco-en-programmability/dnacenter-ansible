import json

module_definition = json.loads('''{
    "family": "wireless",
    "name": "wireless_rf_profile",
    "operations": {
        "delete": [
            "delete_rf_profiles"
        ],
        "get": [
            "retrieve_rf_profiles"
        ],
        "post": [
            "create_or_update_rf_profile"
        ]
    },
    "parameters": {
        "create_or_update_rf_profile": [
            {
                "name": "channelWidth",
                "required": true,
                "type": "string"
            },
            {
                "name": "defaultRfProfile",
                "required": true,
                "type": "boolean"
            },
            {
                "name": "enableBrownField",
                "required": true,
                "type": "boolean"
            },
            {
                "name": "enableCustom",
                "required": true,
                "type": "boolean"
            },
            {
                "name": "enableRadioTypeA",
                "required": true,
                "type": "boolean"
            },
            {
                "name": "enableRadioTypeB",
                "required": true,
                "type": "boolean"
            },
            {
                "name": "name",
                "required": true,
                "type": "string"
            },
            {
                "name": "radioTypeAProperties",
                "required": false,
                "schema": [
                    {
                        "name": "parentProfile",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "radioChannels",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "dataRates",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "mandatoryDataRates",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "powerThresholdV1",
                        "required": false,
                        "type": "number"
                    },
                    {
                        "name": "rxSopThreshold",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "minPowerLevel",
                        "required": false,
                        "type": "number"
                    },
                    {
                        "name": "maxPowerLevel",
                        "required": false,
                        "type": "number"
                    }
                ],
                "type": "object"
            },
            {
                "name": "radioTypeBProperties",
                "required": false,
                "schema": [
                    {
                        "name": "parentProfile",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "radioChannels",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "dataRates",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "mandatoryDataRates",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "powerThresholdV1",
                        "required": false,
                        "type": "number"
                    },
                    {
                        "name": "rxSopThreshold",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "minPowerLevel",
                        "required": false,
                        "type": "number"
                    },
                    {
                        "name": "maxPowerLevel",
                        "required": false,
                        "type": "number"
                    }
                ],
                "type": "object"
            }
        ],
        "delete_rf_profiles": [
            {
                "name": "rf_profile_name",
                "required": true,
                "type": "string"
            }
        ],
        "retrieve_rf_profiles": [
            {
                "name": "rf_profile_name",
                "required": false,
                "type": "string"
            }
        ]
    },
    "responses": {
        "create_or_update_rf_profile": {
            "properties": [
                "executionId",
                "executionUrl",
                "message"
            ],
            "type": "object"
        },
        "delete_rf_profiles": {
            "properties": [
                "executionId",
                "executionUrl",
                "message"
            ],
            "type": "object"
        },
        "retrieve_rf_profiles": {
            "properties": [
                "response"
            ],
            "type": "object"
        }
    }
}''')