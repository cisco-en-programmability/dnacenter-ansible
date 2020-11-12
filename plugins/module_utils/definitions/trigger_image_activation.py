import json

module_definition = json.loads(
    """{
    "family": "software_image_management_swim",
    "name": "trigger_image_activation",
    "operations": {
        "post": [
            "trigger_software_image_activation"
        ]
    },
    "parameters": {
        "trigger_software_image_activation": [
            {
                "name": "schedule_validate",
                "required": false,
                "type": "boolean"
            },
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "activateLowerImageVersion",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "deviceUpgradeMode",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "deviceUuid",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "distributeIfNeeded",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "array_type": "string",
                        "name": "imageUuidList",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "array_type": "string",
                        "name": "smuImageUuidList",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    }
                ],
                "type": "array"
            }
        ]
    },
    "responses": {
        "trigger_software_image_activation": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
