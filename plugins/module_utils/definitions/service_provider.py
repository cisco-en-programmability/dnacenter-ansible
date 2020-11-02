import json

module_definition = json.loads('''{
    "family": "network_settings",
    "name": "service_provider",
    "operations": {
        "delete": [
            "delete_sp_profile"
        ],
        "get": [
            "get_service_provider_details"
        ],
        "post": [
            "create_sp_profile"
        ],
        "put": [
            "update_sp_profile"
        ]
    },
    "parameters": {
        "create_sp_profile": [
            {
                "name": "settings",
                "required": true,
                "schema": [
                    {
                        "array_type": "object",
                        "name": "qos",
                        "required": false,
                        "schema": [
                            {
                                "name": "profileName",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "model",
                                "required": true,
                                "type": "string"
                            },
                            {
                                "name": "wanProvider",
                                "required": true,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    }
                ],
                "type": "object"
            }
        ],
        "delete_sp_profile": [
            {
                "name": "sp_profile_name",
                "required": true,
                "type": "string"
            }
        ],
        "get_service_provider_details": [],
        "update_sp_profile": [
            {
                "name": "settings",
                "required": true,
                "schema": [
                    {
                        "array_type": "object",
                        "name": "qos",
                        "required": false,
                        "schema": [
                            {
                                "name": "profileName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "model",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "wanProvider",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "oldProfileName",
                                "required": true,
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
        "create_sp_profile": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        },
        "delete_sp_profile": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        },
        "get_service_provider_details": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "update_sp_profile": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        }
    }
}''')