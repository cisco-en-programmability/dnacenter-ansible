import json

module_definition = json.loads('''{
    "family": "application_policy",
    "name": "application_set",
    "operations": {
        "delete": [
            "delete_application_set"
        ],
        "get": [
            "get_application_sets",
            "get_application_sets_count"
        ],
        "post": [
            "create_application_set"
        ]
    },
    "parameters": {
        "create_application_set": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ],
        "delete_application_set": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_application_sets": [
            {
                "name": "limit",
                "required": false,
                "type": "number"
            },
            {
                "name": "name",
                "required": false,
                "type": "string"
            },
            {
                "name": "offset",
                "required": false,
                "type": "number"
            }
        ],
        "get_application_sets_count": [
            {
                "name": "count",
                "required": true,
                "type": "boolean"
            }
        ]
    },
    "responses": {
        "create_application_set": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "delete_application_set": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_application_sets": {
            "properties": [
                "response"
            ],
            "type": "object"
        },
        "get_application_sets_count": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}''')

from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ObjectExistenceCriteria

class ApplicationSetExistenceCriteria(ObjectExistenceCriteria):
    def __init__(self, dnac):
        super(ApplicationSetExistenceCriteria, self).__init__(
            dnac = dnac,
            get_function = "get_application_sets",
            get_params = {},
            list_field = "response"
        )
        self.ERR_OBJECT_EXISTS = "Application already exists."
        self.ERR_MISSING_PARAM = "Missing 'name' parameter"

    # Modify the logic to determine if the object exists based on the specific
    # criteria used by each module
    def _object_is_equal(self, existing_object, candidate_params):
        for param in candidate_params["payload"]:
            if "name" in param.keys():
                return existing_object["name"] == candidate_params["payload"][0]["name"]
            else:
                self.dnac.fail_json(msg=self.ERR_MISSING_PARAM)