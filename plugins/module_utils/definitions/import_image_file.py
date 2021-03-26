from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "software_image_management_swim",
    "name": "import_image_file",
    "operations": {
        "post": [
            "import_local_software_image"
        ]
    },
    "parameters": {
        "import_local_software_image": [
            {
                "name": "filename",
                "required": true,
                "type": "string"
            },
            {
                "name": "filepath",
                "required": true,
                "type": "string"
            },
            {
                "name": "is_third_party",
                "required": false,
                "type": "boolean"
            },
            {
                "name": "third_party_application_type",
                "required": false,
                "type": "string"
            },
            {
                "name": "third_party_image_family",
                "required": false,
                "type": "string"
            },
            {
                "name": "third_party_vendor",
                "required": false,
                "type": "string"
            }
        ]
    },
    "responses": {
        "import_local_software_image": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
