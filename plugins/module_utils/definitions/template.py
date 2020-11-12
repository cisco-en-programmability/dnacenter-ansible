import json

module_definition = json.loads(
    """{
    "family": "configuration_templates",
    "name": "template",
    "operations": {
        "delete": [
            "delete_template"
        ],
        "get": [
            "gets_the_templates_available",
            "get_template_details"
        ],
        "post": [
            "create_template"
        ],
        "put": [
            "update_template"
        ]
    },
    "parameters": {
        "create_template": [
            {
                "name": "project_id",
                "required": true,
                "type": "string"
            },
            {
                "name": "author",
                "type": "string"
            },
            {
                "name": "composite",
                "type": "boolean"
            },
            {
                "array_type": "object",
                "name": "containingTemplates",
                "required": false,
                "schema": [
                    {
                        "name": "composite",
                        "required": false,
                        "type": "boolean"
                    },
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
                        "name": "version",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            },
            {
                "name": "createTime",
                "type": "integer"
            },
            {
                "name": "description",
                "type": "string"
            },
            {
                "array_type": "object",
                "name": "deviceTypes",
                "required": false,
                "schema": [
                    {
                        "name": "productFamily",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "productSeries",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "productType",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            },
            {
                "enum": [
                    "ABORT_ON_ERROR",
                    "CONTINUE_ON_ERROR",
                    "ROLLBACK_ON_ERROR",
                    "ROLLBACK_TARGET_ON_ERROR",
                    "ABORT_TARGET_ON_ERROR"
                ],
                "name": "failurePolicy",
                "type": "string"
            },
            {
                "name": "id",
                "type": "string"
            },
            {
                "name": "lastUpdateTime",
                "type": "integer"
            },
            {
                "name": "name",
                "type": "string"
            },
            {
                "name": "parentTemplateId",
                "type": "string"
            },
            {
                "name": "projectId",
                "type": "string"
            },
            {
                "name": "projectName",
                "type": "string"
            },
            {
                "name": "rollbackTemplateContent",
                "type": "string"
            },
            {
                "array_type": "object",
                "name": "rollbackTemplateParams",
                "required": false,
                "schema": [
                    {
                        "name": "binding",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "dataType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "defaultValue",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "displayName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "group",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instructionText",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "key",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "notParam",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "order",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "paramArray",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "parameterName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "provider",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "range",
                        "required": false,
                        "schema": [
                            {
                                "name": "id",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "maxValue",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "minValue",
                                "required": false,
                                "type": "integer"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "required",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "selection",
                        "required": false,
                        "schema": [
                            {
                                "name": "id",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "selectionType",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "selectionValues",
                                "required": false,
                                "schema": [],
                                "type": "object"
                            }
                        ],
                        "type": "object"
                    }
                ],
                "type": "array"
            },
            {
                "name": "softwareType",
                "type": "string"
            },
            {
                "name": "softwareVariant",
                "type": "string"
            },
            {
                "name": "softwareVersion",
                "type": "string"
            },
            {
                "array_type": "string",
                "name": "tags",
                "required": false,
                "schema": [],
                "type": "array"
            },
            {
                "name": "templateContent",
                "type": "string"
            },
            {
                "array_type": "object",
                "name": "templateParams",
                "required": false,
                "schema": [
                    {
                        "name": "binding",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "dataType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "defaultValue",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "displayName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "group",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instructionText",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "key",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "notParam",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "order",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "paramArray",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "parameterName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "provider",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "range",
                        "required": false,
                        "schema": [
                            {
                                "name": "id",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "maxValue",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "minValue",
                                "required": false,
                                "type": "integer"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "required",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "selection",
                        "required": false,
                        "schema": [
                            {
                                "name": "id",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "selectionType",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "selectionValues",
                                "required": false,
                                "schema": [],
                                "type": "object"
                            }
                        ],
                        "type": "object"
                    }
                ],
                "type": "array"
            },
            {
                "name": "version",
                "type": "string"
            }
        ],
        "delete_template": [
            {
                "name": "template_id",
                "required": true,
                "type": "string"
            }
        ],
        "get_template_details": [
            {
                "name": "template_id",
                "required": true,
                "type": "string"
            },
            {
                "name": "latest_version",
                "required": false,
                "type": "boolean"
            }
        ],
        "gets_the_templates_available": [
            {
                "name": "filter_conflicting_templates",
                "required": false,
                "type": "boolean"
            },
            {
                "name": "product_family",
                "required": false,
                "type": "string"
            },
            {
                "name": "product_series",
                "required": false,
                "type": "string"
            },
            {
                "name": "product_type",
                "required": false,
                "type": "string"
            },
            {
                "name": "project_id",
                "required": false,
                "type": "string"
            },
            {
                "name": "software_type",
                "required": false,
                "type": "string"
            },
            {
                "name": "software_version",
                "required": false,
                "type": "string"
            }
        ],
        "update_template": [
            {
                "name": "author",
                "type": "string"
            },
            {
                "name": "composite",
                "type": "boolean"
            },
            {
                "array_type": "object",
                "name": "containingTemplates",
                "required": false,
                "schema": [
                    {
                        "name": "composite",
                        "required": false,
                        "type": "boolean"
                    },
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
                        "name": "version",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            },
            {
                "name": "createTime",
                "type": "integer"
            },
            {
                "name": "description",
                "type": "string"
            },
            {
                "array_type": "object",
                "name": "deviceTypes",
                "required": false,
                "schema": [
                    {
                        "name": "productFamily",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "productSeries",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "productType",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            },
            {
                "enum": [
                    "ABORT_ON_ERROR",
                    "CONTINUE_ON_ERROR",
                    "ROLLBACK_ON_ERROR",
                    "ROLLBACK_TARGET_ON_ERROR",
                    "ABORT_TARGET_ON_ERROR"
                ],
                "name": "failurePolicy",
                "type": "string"
            },
            {
                "name": "id",
                "type": "string"
            },
            {
                "name": "lastUpdateTime",
                "type": "integer"
            },
            {
                "name": "name",
                "type": "string"
            },
            {
                "name": "parentTemplateId",
                "type": "string"
            },
            {
                "name": "projectId",
                "type": "string"
            },
            {
                "name": "projectName",
                "type": "string"
            },
            {
                "name": "rollbackTemplateContent",
                "type": "string"
            },
            {
                "array_type": "object",
                "name": "rollbackTemplateParams",
                "required": false,
                "schema": [
                    {
                        "name": "binding",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "dataType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "defaultValue",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "displayName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "group",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instructionText",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "key",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "notParam",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "order",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "paramArray",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "parameterName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "provider",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "range",
                        "required": false,
                        "schema": [
                            {
                                "name": "id",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "maxValue",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "minValue",
                                "required": false,
                                "type": "integer"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "required",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "selection",
                        "required": false,
                        "schema": [
                            {
                                "name": "id",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "selectionType",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "selectionValues",
                                "required": false,
                                "schema": [],
                                "type": "object"
                            }
                        ],
                        "type": "object"
                    }
                ],
                "type": "array"
            },
            {
                "name": "softwareType",
                "type": "string"
            },
            {
                "name": "softwareVariant",
                "type": "string"
            },
            {
                "name": "softwareVersion",
                "type": "string"
            },
            {
                "array_type": "string",
                "name": "tags",
                "required": false,
                "schema": [],
                "type": "array"
            },
            {
                "name": "templateContent",
                "type": "string"
            },
            {
                "array_type": "object",
                "name": "templateParams",
                "required": false,
                "schema": [
                    {
                        "name": "binding",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "dataType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "defaultValue",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "displayName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "group",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instructionText",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "key",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "notParam",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "order",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "paramArray",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "parameterName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "provider",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "range",
                        "required": false,
                        "schema": [
                            {
                                "name": "id",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "maxValue",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "minValue",
                                "required": false,
                                "type": "integer"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "required",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "selection",
                        "required": false,
                        "schema": [
                            {
                                "name": "id",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "selectionType",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "selectionValues",
                                "required": false,
                                "schema": [],
                                "type": "object"
                            }
                        ],
                        "type": "object"
                    }
                ],
                "type": "array"
            },
            {
                "name": "version",
                "type": "string"
            }
        ]
    },
    "responses": {
        "create_template": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "delete_template": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_template_details": {
            "properties": [
                "author",
                "composite",
                "containingTemplates",
                "createTime",
                "description",
                "deviceTypes",
                "failurePolicy",
                "id",
                "lastUpdateTime",
                "name",
                "parentTemplateId",
                "projectId",
                "projectName",
                "rollbackTemplateContent",
                "rollbackTemplateParams",
                "softwareType",
                "softwareVariant",
                "softwareVersion",
                "tags",
                "templateContent",
                "templateParams",
                "version"
            ],
            "type": "object"
        },
        "gets_the_templates_available": null,
        "update_template": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
