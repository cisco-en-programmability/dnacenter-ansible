import json

module_definition = json.loads('''{
    "family": "application_policy",
    "name": "applications",
    "operations": {
        "delete": [
            "delete_application"
        ],
        "get": [
            "get_applications",
            "get_applications_count"
        ],
        "post": [
            "create_application"
        ],
        "put": [
            "edit_application"
        ]
    },
    "parameters": {
        "create_application": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "networkApplications",
                        "required": false,
                        "schema": [
                            {
                                "name": "appProtocol",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "applicationSubType",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "applicationType",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "categoryId",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "displayName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "engineId",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "helpString",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "longDescription",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "popularity",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "rank",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "trafficClass",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "serverName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "url",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "dscp",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "ignoreConflict",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "networkIdentity",
                        "required": false,
                        "schema": [
                            {
                                "name": "displayName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "lowerPort",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "ports",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "protocol",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "upperPort",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "applicationSet",
                        "required": false,
                        "schema": [
                            {
                                "name": "idRef",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    }
                ],
                "type": "array"
            }
        ],
        "delete_application": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "edit_application": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "networkApplications",
                        "required": false,
                        "schema": [
                            {
                                "name": "id",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "appProtocol",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "applicationSubType",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "applicationType",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "categoryId",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "displayName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "engineId",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "helpString",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "longDescription",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "popularity",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "rank",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "trafficClass",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "serverName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "url",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "dscp",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "ignoreConflict",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "networkIdentity",
                        "required": false,
                        "schema": [
                            {
                                "name": "id",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "displayName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "lowerPort",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "ports",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "protocol",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "upperPort",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "applicationSet",
                        "required": false,
                        "schema": [
                            {
                                "name": "idRef",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    }
                ],
                "type": "array"
            }
        ],
        "get_applications": [
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
        "get_applications_count": [
            {
                "artificial": true,
                "name": "count",
                "required": true,
                "type": "boolean"
            }
        ]
    },
    "responses": {
        "create_application": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "delete_application": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "edit_application": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_applications": {
            "array_type": "object",
            "properties": [
                "id",
                "name",
                "networkApplications",
                "networkIdentity",
                "applicationSet"
            ],
            "type": "array"
        },
        "get_applications_count": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}''')