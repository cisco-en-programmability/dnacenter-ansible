import json

module_definition = json.loads('''{
    "family": "event_management",
    "name": "event_subscription",
    "operations": {
        "delete": [
            "delete_event_subscriptions"
        ],
        "get": [
            "get_event_subscriptions",
            "count_of_event_subscriptions"
        ],
        "post": [
            "create_event_subscriptions"
        ],
        "put": [
            "update_event_subscriptions"
        ]
    },
    "parameters": {
        "count_of_event_subscriptions": [
            {
                "name": "event_ids",
                "required": true,
                "type": "string"
            },
            {
                "artificial": true,
                "name": "count",
                "required": true,
                "type": "boolean"
            }
        ],
        "create_event_subscriptions": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "subscriptionId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "version",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "subscriptionEndpoints",
                        "required": false,
                        "schema": [
                            {
                                "name": "instanceId",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "subscriptionDetails",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "name",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "url",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "method",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "connectorType",
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
                        "name": "filter",
                        "required": true,
                        "schema": [
                            {
                                "array_type": "string",
                                "name": "eventIds",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            }
                        ],
                        "type": "object"
                    }
                ],
                "type": "array"
            }
        ],
        "delete_event_subscriptions": [
            {
                "name": "subscriptions",
                "required": true,
                "type": "string"
            }
        ],
        "get_event_subscriptions": [
            {
                "name": "event_ids",
                "required": false,
                "type": "string"
            },
            {
                "name": "limit",
                "required": false,
                "type": "number"
            },
            {
                "name": "offset",
                "required": false,
                "type": "number"
            },
            {
                "name": "order",
                "required": false,
                "type": "string"
            },
            {
                "name": "sort_by",
                "required": false,
                "type": "string"
            }
        ],
        "update_event_subscriptions": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "subscriptionId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "version",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "subscriptionEndpoints",
                        "required": false,
                        "schema": [
                            {
                                "name": "instanceId",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "subscriptionDetails",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "name",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "url",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "method",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "connectorType",
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
                        "name": "filter",
                        "required": true,
                        "schema": [
                            {
                                "array_type": "string",
                                "name": "eventIds",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            }
                        ],
                        "type": "object"
                    }
                ],
                "type": "array"
            }
        ]
    },
    "responses": {
        "count_of_event_subscriptions": {
            "properties": [
                "response"
            ],
            "type": "object"
        },
        "create_event_subscriptions": {
            "properties": [
                "statusUri"
            ],
            "type": "object"
        },
        "delete_event_subscriptions": {
            "properties": [
                "statusUri"
            ],
            "type": "object"
        },
        "get_event_subscriptions": {
            "array_type": "object",
            "properties": [
                "version",
                "name",
                "description",
                "subscriptionEndpoints",
                "filter"
            ],
            "type": "array"
        },
        "update_event_subscriptions": {
            "properties": [
                "statusUri"
            ],
            "type": "object"
        }
    }
}''')