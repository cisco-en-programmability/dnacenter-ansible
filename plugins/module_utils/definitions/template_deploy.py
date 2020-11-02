import json

module_definition = json.loads('''{
    "family": "configuration_templates",
    "name": "template_deploy",
    "operations": {
        "get": [
            "get_template_deployment_status"
        ],
        "post": [
            "deploy_template"
        ]
    },
    "parameters": {
        "deploy_template": [
            {
                "name": "forcePushTemplate",
                "type": "boolean"
            },
            {
                "name": "isComposite",
                "type": "boolean"
            },
            {
                "name": "mainTemplateId",
                "type": "string"
            },
            {
                "array_type": "any",
                "name": "memberTemplateDeploymentInfo",
                "required": false,
                "schema": [],
                "type": "array"
            },
            {
                "array_type": "object",
                "name": "targetInfo",
                "required": false,
                "schema": [
                    {
                        "name": "hostName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "params",
                        "required": false,
                        "schema": [],
                        "type": "object"
                    },
                    {
                        "name": "type",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            },
            {
                "name": "templateId",
                "type": "string"
            }
        ],
        "get_template_deployment_status": [
            {
                "name": "deployment_id",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "deploy_template": {
            "properties": [
                "deploymentId",
                "deploymentName",
                "devices",
                "duration",
                "endTime",
                "projectName",
                "startTime",
                "status",
                "templateName",
                "templateVersion"
            ],
            "type": "object"
        },
        "get_template_deployment_status": {
            "properties": [
                "deploymentId",
                "deploymentName",
                "devices",
                "duration",
                "endTime",
                "projectName",
                "startTime",
                "status",
                "templateName",
                "templateVersion"
            ],
            "type": "object"
        }
    }
}''')