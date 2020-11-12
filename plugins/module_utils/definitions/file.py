import json

module_definition = json.loads(
    """{
    "family": "file",
    "name": "file",
    "operations": {
        "get": [
            "download_a_file_by_fileid"
        ]
    },
    "parameters": {
        "download_a_file_by_fileid": [
            {
                "name": "file_id",
                "required": true,
                "type": "string"
            },
            {
                "name": "dirpath",
                "required": false,
                "type": "string"
            },
            {
                "name": "save_file",
                "required": false,
                "type": "boolean"
            }
        ]
    },
    "responses": {
        "download_a_file_by_fileid": null
    }
}"""
)
