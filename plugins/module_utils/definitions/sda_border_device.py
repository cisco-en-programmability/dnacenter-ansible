import json

module_definition = json.loads('''{
    "family": "sda",
    "name": "sda_border_device",
    "operations": {
        "delete": [
            "deletes_border_device"
        ],
        "get": [
            "gets_border_device_detail"
        ],
        "post": [
            "adds_border_device"
        ]
    },
    "parameters": {
        "adds_border_device": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "deviceManagementIpAddress",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "siteNameHierarchy",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "externalDomainRoutingProtocolName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "externalConnectivityIpPoolName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "internalAutonomouSystemNumber",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "borderSessionType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "connectedToInternet",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "array_type": "object",
                        "name": "externalConnectivitySettings",
                        "required": false,
                        "schema": [
                            {
                                "name": "interfaceName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "externalAutonomouSystemNumber",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "l3Handoff",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "virtualNetwork",
                                        "required": false,
                                        "schema": [
                                            {
                                                "name": "virtualNetworkName",
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
                        "type": "array"
                    }
                ],
                "type": "array"
            }
        ],
        "deletes_border_device": [
            {
                "name": "device_ipaddress",
                "required": true,
                "type": "string"
            }
        ],
        "gets_border_device_detail": [
            {
                "name": "device_ipaddress",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "adds_border_device": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        },
        "deletes_border_device": {
            "properties": [
                "status",
                "description",
                "executionStatusUrl"
            ],
            "type": "object"
        },
        "gets_border_device_detail": {
            "properties": [
                "status",
                "description",
                "payload"
            ],
            "type": "object"
        }
    }
}''')