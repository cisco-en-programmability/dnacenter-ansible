import json

module_definition = json.loads('''{
    "family": "sites",
    "name": "site_membership",
    "operations": {
        "get": [
            "get_membership"
        ]
    },
    "parameters": {
        "get_membership": [
            {
                "name": "site_id",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "get_membership": {
            "properties": [
                "site",
                "device"
            ],
            "type": "object"
        }
    }
}''')