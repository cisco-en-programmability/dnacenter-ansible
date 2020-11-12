import json

module_definition = json.loads(
    """{
    "family": "tag",
    "name": "tag_member",
    "operations": {
        "delete": [
            "remove_tag_member"
        ],
        "get": [
            "get_tag_members_by_id",
            "get_tag_member_count",
            "get_tag_resource_types"
        ],
        "post": [
            "add_members_to_the_tag"
        ],
        "put": [
            "updates_tag_membership"
        ]
    },
    "parameters": {
        "add_members_to_the_tag": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_tag_member_count": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "name": "member_type",
                "required": true,
                "type": "string"
            },
            {
                "name": "level",
                "required": false,
                "type": "string"
            },
            {
                "name": "member_association_type",
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
        "get_tag_members_by_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "name": "member_type",
                "required": true,
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
                "name": "member_association_type",
                "required": false,
                "type": "string"
            },
            {
                "name": "offset",
                "required": false,
                "type": "string"
            }
        ],
        "get_tag_resource_types": [],
        "remove_tag_member": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "name": "member_id",
                "required": true,
                "type": "string"
            }
        ],
        "updates_tag_membership": [
            {
                "name": "memberToTags",
                "required": false,
                "schema": [
                    {
                        "array_type": "string",
                        "name": "key",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    }
                ],
                "type": "object"
            },
            {
                "name": "memberType",
                "type": "string"
            }
        ]
    },
    "responses": {
        "add_members_to_the_tag": {
            "properties": [
                "version",
                "response"
            ],
            "type": "object"
        },
        "get_tag_member_count": {
            "properties": [
                "version",
                "response"
            ],
            "type": "object"
        },
        "get_tag_members_by_id": {
            "properties": [
                "version",
                "response"
            ],
            "type": "object"
        },
        "get_tag_resource_types": {
            "properties": [
                "version",
                "response"
            ],
            "type": "object"
        },
        "remove_tag_member": {
            "properties": [
                "version",
                "response"
            ],
            "type": "object"
        },
        "updates_tag_membership": {
            "properties": [
                "version",
                "response"
            ],
            "type": "object"
        }
    }
}"""
)
