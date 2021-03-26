from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "sites",
    "name": "site",
    "operations": {
        "delete": [
            "delete_site"
        ],
        "get": [
            "get_site",
            "get_site_count"
        ],
        "post": [
            "create_site"
        ],
        "put": [
            "update_site"
        ]
    },
    "parameters": {
        "create_site": [
            {
                "name": "site",
                "required": true,
                "schema": [
                    {
                        "name": "area",
                        "required": false,
                        "schema": [
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "parentName",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "building",
                        "required": false,
                        "schema": [
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "address",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "parentName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "latitude",
                                "required": false,
                                "type": "number"
                            },
                            {
                                "name": "longitude",
                                "required": false,
                                "type": "number"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "floor",
                        "required": false,
                        "schema": [
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "parentName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "rfModel",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "width",
                                "required": false,
                                "type": "number"
                            },
                            {
                                "name": "length",
                                "required": false,
                                "type": "number"
                            },
                            {
                                "name": "height",
                                "required": false,
                                "type": "number"
                            }
                        ],
                        "type": "object"
                    }
                ],
                "type": "object"
            },
            {
                "enum": [
                    "area",
                    "building",
                    "floor"
                ],
                "name": "type",
                "required": true,
                "type": "string"
            }
        ],
        "delete_site": [
            {
                "name": "site_id",
                "required": true,
                "type": "string"
            }
        ],
        "get_site": [
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
                "name": "site_id",
                "required": false,
                "type": "string"
            },
            {
                "name": "type",
                "required": false,
                "type": "string"
            }
        ],
        "get_site_count": [
            {
                "name": "site_id",
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
        "update_site": [
            {
                "name": "site_id",
                "required": true,
                "type": "string"
            },
            {
                "name": "site",
                "required": true,
                "schema": [
                    {
                        "name": "area",
                        "required": false,
                        "schema": [
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "parentName",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "building",
                        "required": false,
                        "schema": [
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "address",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "parentName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "latitude",
                                "required": false,
                                "type": "number"
                            },
                            {
                                "name": "longitude",
                                "required": false,
                                "type": "number"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "floor",
                        "required": false,
                        "schema": [
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "rfModel",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "width",
                                "required": false,
                                "type": "number"
                            },
                            {
                                "name": "length",
                                "required": false,
                                "type": "number"
                            },
                            {
                                "name": "height",
                                "required": false,
                                "type": "number"
                            }
                        ],
                        "type": "object"
                    }
                ],
                "type": "object"
            },
            {
                "enum": [
                    "area",
                    "building",
                    "floor"
                ],
                "name": "type",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "create_site": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        },
        "delete_site": {
            "properties": [
                "status",
                "message"
            ],
            "type": "object"
        },
        "get_site": {
            "properties": [
                "response"
            ],
            "type": "object"
        },
        "get_site_count": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "update_site": {
            "properties": [
                "result",
                "response",
                "status"
            ],
            "type": "object"
        }
    }
}"""
)
