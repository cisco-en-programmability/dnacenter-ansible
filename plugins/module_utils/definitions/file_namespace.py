import json

module_definition = json.loads(
    """{
    "family": "file",
    "name": "file_namespace",
    "operations": {
        "get": [
            "get_list_of_available_namespaces",
            "get_list_of_files"
        ]
    },
    "parameters": {
        "get_list_of_available_namespaces": [],
        "get_list_of_files": [
            {
                "name": "name_space",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "get_list_of_available_namespaces": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_list_of_files": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
