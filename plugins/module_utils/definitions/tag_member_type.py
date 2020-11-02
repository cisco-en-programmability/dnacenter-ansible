import json

module_definition = json.loads('''{
    "family": "tag",
    "name": "tag_member_type",
    "operations": {
        "get": [
            "get_tag_resource_types"
        ]
    },
    "parameters": {
        "get_tag_resource_types": []
    },
    "responses": {
        "get_tag_resource_types": {
            "properties": [
                "version",
                "response"
            ],
            "type": "object"
        }
    }
}''')