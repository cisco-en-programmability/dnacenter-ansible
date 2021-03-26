from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "tag",
    "name": "tag",
    "operations": {
        "delete": [
            "delete_tag"
        ],
        "get": [
            "get_tag",
            "get_tag_by_id",
            "get_tag_count"
        ],
        "post": [
            "create_tag"
        ],
        "put": [
            "update_tag"
        ]
    },
    "parameters": {
        "create_tag": [
            {
                "name": "description",
                "type": "string"
            },
            {
                "array_type": "object",
                "name": "dynamicRules",
                "required": false,
                "schema": [
                    {
                        "name": "memberType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "rules",
                        "required": false,
                        "schema": [
                            {
                                "array_type": "string",
                                "name": "values",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            },
                            {
                                "array_type": "any",
                                "name": "items",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            },
                            {
                                "name": "operation",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "value",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    }
                ],
                "type": "array"
            },
            {
                "name": "id",
                "type": "string"
            },
            {
                "name": "instanceTenantId",
                "type": "string"
            },
            {
                "name": "name",
                "type": "string"
            },
            {
                "name": "systemTag",
                "type": "boolean"
            }
        ],
        "delete_tag": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_tag": [
            {
                "name": "additional_info_attributes",
                "required": false,
                "type": "string"
            },
            {
                "name": "additional_info_name_space",
                "required": false,
                "type": "string"
            },
            {
                "name": "field",
                "required": false,
                "type": "string"
            },
            {
                "name": "level",
                "required": false,
                "type": "string"
            },
            {
                "name": "limit",
                "required": false,
                "type": "string"
            },
            {
                "name": "name",
                "required": false,
                "type": "string"
            },
            {
                "name": "offset",
                "required": false,
                "type": "string"
            },
            {
                "name": "order",
                "required": false,
                "type": "string"
            },
            {
                "name": "size",
                "required": false,
                "type": "string"
            },
            {
                "name": "sort_by",
                "required": false,
                "type": "string"
            },
            {
                "name": "system_tag",
                "required": false,
                "type": "string"
            }
        ],
        "get_tag_by_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_tag_count": [
            {
                "name": "attribute_name",
                "required": false,
                "type": "string"
            },
            {
                "name": "level",
                "required": false,
                "type": "string"
            },
            {
                "name": "name",
                "required": false,
                "type": "string"
            },
            {
                "name": "name_space",
                "required": false,
                "type": "string"
            },
            {
                "name": "size",
                "required": false,
                "type": "string"
            },
            {
                "name": "system_tag",
                "required": false,
                "type": "string"
            },
            {
                "artificial": true,
                "name": "count",
                "required": true,
                "type": "boolean"
            }
        ],
        "update_tag": [
            {
                "name": "description",
                "type": "string"
            },
            {
                "array_type": "object",
                "name": "dynamicRules",
                "required": false,
                "schema": [
                    {
                        "name": "memberType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "rules",
                        "required": false,
                        "schema": [
                            {
                                "array_type": "string",
                                "name": "values",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            },
                            {
                                "array_type": "any",
                                "name": "items",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            },
                            {
                                "name": "operation",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "value",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    }
                ],
                "type": "array"
            },
            {
                "name": "id",
                "type": "string"
            },
            {
                "name": "instanceTenantId",
                "type": "string"
            },
            {
                "name": "name",
                "type": "string"
            },
            {
                "name": "systemTag",
                "type": "boolean"
            }
        ]
    },
    "responses": {
        "create_tag": {
            "properties": [
                "version",
                "response"
            ],
            "type": "object"
        },
        "delete_tag": {
            "properties": [
                "version",
                "response"
            ],
            "type": "object"
        },
        "get_tag": {
            "properties": [
                "version",
                "response"
            ],
            "type": "object"
        },
        "get_tag_by_id": {
            "properties": [
                "version",
                "response"
            ],
            "type": "object"
        },
        "get_tag_count": {
            "properties": [
                "version",
                "response"
            ],
            "type": "object"
        },
        "update_tag": {
            "properties": [
                "version",
                "response"
            ],
            "type": "object"
        }
    }
}"""
)

from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ObjectExistenceCriteria,
)


class TagExistenceCriteria(ObjectExistenceCriteria):
    def __init__(self, dnac):
        super(TagExistenceCriteria, self).__init__(
            dnac=dnac, get_function="get_tag", get_params={}, list_field="response"
        )
        self.WARN_OBJECT_EXISTS = "Tag already exists and was updated."
        self.ERR_MISSING_PARAM = "Missing 'name' parameter"

    def _object_is_equal(self, existing_object, candidate_params):
        if "name" in candidate_params.keys():
            return existing_object["name"] == candidate_params["name"]
        else:
            self.dnac.fail_json(msg=self.ERR_MISSING_PARAM)
