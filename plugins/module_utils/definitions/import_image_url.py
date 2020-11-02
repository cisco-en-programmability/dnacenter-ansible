import json

module_definition = json.loads('''{
    "family": "software_image_management_swim",
    "name": "import_image_url",
    "operations": {
        "post": [
            "import_software_image_via_url"
        ]
    },
    "parameters": {
        "import_software_image_via_url": [
            {
                "name": "schedule_at",
                "required": false,
                "type": "string"
            },
            {
                "name": "schedule_desc",
                "required": false,
                "type": "string"
            },
            {
                "name": "schedule_origin",
                "required": false,
                "type": "string"
            },
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "applicationType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "imageFamily",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "sourceURL",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "thirdParty",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "vendor",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ]
    },
    "responses": {
        "import_software_image_via_url": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}''')