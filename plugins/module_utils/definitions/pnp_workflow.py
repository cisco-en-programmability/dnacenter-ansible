from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "device_onboarding_pnp",
    "name": "pnp_workflow",
    "operations": {
        "delete": [
            "delete_workflow_by_id"
        ],
        "get": [
            "get_workflows",
            "get_workflow_by_id",
            "get_workflow_count"
        ],
        "post": [
            "add_a_workflow"
        ],
        "put": [
            "update_workflow"
        ]
    },
    "parameters": {
        "add_a_workflow": [
            {
                "name": "_id",
                "type": "string"
            },
            {
                "name": "addToInventory",
                "type": "boolean"
            },
            {
                "name": "addedOn",
                "type": "integer"
            },
            {
                "name": "configId",
                "type": "string"
            },
            {
                "name": "currTaskIdx",
                "type": "integer"
            },
            {
                "name": "description",
                "type": "string"
            },
            {
                "name": "endTime",
                "type": "integer"
            },
            {
                "name": "execTime",
                "type": "integer"
            },
            {
                "name": "imageId",
                "type": "string"
            },
            {
                "enum": [
                    "SystemWorkflow",
                    "UserWorkflow",
                    "SystemResetWorkflow"
                ],
                "name": "instanceType",
                "type": "string"
            },
            {
                "name": "lastupdateOn",
                "type": "integer"
            },
            {
                "name": "name",
                "type": "string"
            },
            {
                "name": "startTime",
                "type": "integer"
            },
            {
                "name": "_state",
                "type": "string"
            },
            {
                "array_type": "object",
                "name": "tasks",
                "required": false,
                "schema": [
                    {
                        "name": "currWorkItemIdx",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "endTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "startTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "state",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "taskSeqNo",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "timeTaken",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "type",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "workItemList",
                        "required": false,
                        "schema": [
                            {
                                "name": "command",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "endTime",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "outputStr",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "startTime",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "state",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "timeTaken",
                                "required": false,
                                "type": "integer"
                            }
                        ],
                        "type": "array"
                    }
                ],
                "type": "array"
            },
            {
                "name": "tenantId",
                "type": "string"
            },
            {
                "name": "type",
                "type": "string"
            },
            {
                "name": "useState",
                "type": "string"
            },
            {
                "name": "version",
                "type": "integer"
            }
        ],
        "delete_workflow_by_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_workflow_by_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_workflow_count": [
            {
                "name": "name",
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
        "get_workflows": [
            {
                "name": "limit",
                "required": false,
                "type": "integer"
            },
            {
                "name": "name",
                "required": false,
                "type": "string"
            },
            {
                "name": "offset",
                "required": false,
                "type": "integer"
            },
            {
                "name": "sort",
                "required": false,
                "type": "string"
            },
            {
                "name": "sort_order",
                "required": false,
                "type": "string"
            },
            {
                "name": "type",
                "required": false,
                "type": "string"
            }
        ],
        "update_workflow": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "name": "_id",
                "type": "string"
            },
            {
                "name": "addToInventory",
                "type": "boolean"
            },
            {
                "name": "addedOn",
                "type": "integer"
            },
            {
                "name": "configId",
                "type": "string"
            },
            {
                "name": "currTaskIdx",
                "type": "integer"
            },
            {
                "name": "description",
                "type": "string"
            },
            {
                "name": "endTime",
                "type": "integer"
            },
            {
                "name": "execTime",
                "type": "integer"
            },
            {
                "name": "imageId",
                "type": "string"
            },
            {
                "enum": [
                    "SystemWorkflow",
                    "UserWorkflow",
                    "SystemResetWorkflow"
                ],
                "name": "instanceType",
                "type": "string"
            },
            {
                "name": "lastupdateOn",
                "type": "integer"
            },
            {
                "name": "name",
                "type": "string"
            },
            {
                "name": "startTime",
                "type": "integer"
            },
            {
                "name": "_state",
                "type": "string"
            },
            {
                "array_type": "object",
                "name": "tasks",
                "required": false,
                "schema": [
                    {
                        "name": "currWorkItemIdx",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "endTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "startTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "state",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "taskSeqNo",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "timeTaken",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "type",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "workItemList",
                        "required": false,
                        "schema": [
                            {
                                "name": "command",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "endTime",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "outputStr",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "startTime",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "state",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "timeTaken",
                                "required": false,
                                "type": "integer"
                            }
                        ],
                        "type": "array"
                    }
                ],
                "type": "array"
            },
            {
                "name": "tenantId",
                "type": "string"
            },
            {
                "name": "type",
                "type": "string"
            },
            {
                "name": "useState",
                "type": "string"
            },
            {
                "name": "version",
                "type": "integer"
            }
        ]
    },
    "responses": {
        "add_a_workflow": {
            "properties": [
                "_id",
                "state",
                "type",
                "description",
                "lastupdateOn",
                "imageId",
                "currTaskIdx",
                "addedOn",
                "tasks",
                "addToInventory",
                "instanceType",
                "endTime",
                "execTime",
                "startTime",
                "useState",
                "configId",
                "name",
                "version",
                "tenantId"
            ],
            "type": "object"
        },
        "delete_workflow_by_id": {
            "properties": [
                "_id",
                "state",
                "type",
                "description",
                "lastupdateOn",
                "imageId",
                "currTaskIdx",
                "addedOn",
                "tasks",
                "addToInventory",
                "instanceType",
                "endTime",
                "execTime",
                "startTime",
                "useState",
                "configId",
                "name",
                "version",
                "tenantId"
            ],
            "type": "object"
        },
        "get_workflow_by_id": {
            "properties": [
                "_id",
                "state",
                "type",
                "description",
                "lastupdateOn",
                "imageId",
                "currTaskIdx",
                "addedOn",
                "tasks",
                "addToInventory",
                "instanceType",
                "endTime",
                "execTime",
                "startTime",
                "useState",
                "configId",
                "name",
                "version",
                "tenantId"
            ],
            "type": "object"
        },
        "get_workflow_count": {
            "properties": [
                "response"
            ],
            "type": "object"
        },
        "get_workflows": {
            "array_type": "object",
            "properties": [
                "_id",
                "state",
                "type",
                "description",
                "lastupdateOn",
                "imageId",
                "currTaskIdx",
                "addedOn",
                "tasks",
                "addToInventory",
                "instanceType",
                "endTime",
                "execTime",
                "startTime",
                "useState",
                "configId",
                "name",
                "version",
                "tenantId"
            ],
            "type": "array"
        },
        "update_workflow": {
            "properties": [
                "_id",
                "state",
                "type",
                "description",
                "lastupdateOn",
                "imageId",
                "currTaskIdx",
                "addedOn",
                "tasks",
                "addToInventory",
                "instanceType",
                "endTime",
                "execTime",
                "startTime",
                "useState",
                "configId",
                "name",
                "version",
                "tenantId"
            ],
            "type": "object"
        }
    }
}"""
)
