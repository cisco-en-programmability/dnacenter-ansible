import json

module_definition = json.loads(
    """{
    "family": "software_image_management_swim",
    "name": "trigger_image_distribution",
    "operations": {
        "post": [
            "trigger_software_image_distribution"
        ]
    },
    "parameters": {
        "trigger_software_image_distribution": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "deviceUuid",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "imageUuid",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ]
    },
    "responses": {
        "trigger_software_image_distribution": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
