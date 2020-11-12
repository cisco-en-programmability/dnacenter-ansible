import json

module_definition = json.loads(
    """{
    "family": "wireless",
    "name": "wireless_profile",
    "operations": {
        "delete": [
            "delete_wireless_profile"
        ],
        "get": [
            "get_wireless_profile"
        ],
        "post": [
            "create_wireless_profile"
        ],
        "put": [
            "update_wireless_profile"
        ]
    },
    "parameters": {
        "create_wireless_profile": [
            {
                "name": "profileDetails",
                "required": true,
                "schema": [
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "string",
                        "name": "sites",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "ssidDetails",
                        "required": false,
                        "schema": [
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "type",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "enableFabric",
                                "required": false,
                                "type": "boolean"
                            },
                            {
                                "name": "flexConnect",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "enableFlexConnect",
                                        "required": false,
                                        "type": "boolean"
                                    },
                                    {
                                        "name": "localToVlan",
                                        "required": false,
                                        "type": "integer"
                                    }
                                ],
                                "type": "object"
                            },
                            {
                                "name": "interfaceName",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    }
                ],
                "type": "object"
            }
        ],
        "delete_wireless_profile": [
            {
                "name": "wireless_profile_name",
                "required": true,
                "type": "string"
            }
        ],
        "get_wireless_profile": [
            {
                "name": "profile_name",
                "required": false,
                "type": "string"
            }
        ],
        "update_wireless_profile": [
            {
                "name": "profileDetails",
                "required": true,
                "schema": [
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "string",
                        "name": "sites",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "ssidDetails",
                        "required": false,
                        "schema": [
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "type",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "enableFabric",
                                "required": false,
                                "type": "boolean"
                            },
                            {
                                "name": "flexConnect",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "enableFlexConnect",
                                        "required": false,
                                        "type": "boolean"
                                    },
                                    {
                                        "name": "localToVlan",
                                        "required": false,
                                        "type": "integer"
                                    }
                                ],
                                "type": "object"
                            },
                            {
                                "name": "interfaceName",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    }
                ],
                "type": "object"
            }
        ]
    },
    "responses": {
        "create_wireless_profile": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        },
        "delete_wireless_profile": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        },
        "get_wireless_profile": {
            "array_type": "object",
            "properties": [
                "profileDetails"
            ],
            "type": "array"
        },
        "update_wireless_profile": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        }
    }
}"""
)
