import json

module_definition = json.loads('''{
    "family": "device_onboarding_pnp",
    "name": "pnp_settings",
    "operations": {
        "get": [
            "get_pnp_global_settings"
        ],
        "put": [
            "update_pnp_global_settings"
        ]
    },
    "parameters": {
        "get_pnp_global_settings": [],
        "update_pnp_global_settings": [
            {
                "name": "_id",
                "type": "string"
            },
            {
                "name": "aaaCredentials",
                "required": false,
                "schema": [
                    {
                        "name": "password",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "username",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "object"
            },
            {
                "name": "acceptEula",
                "type": "boolean"
            },
            {
                "name": "defaultProfile",
                "required": false,
                "schema": [
                    {
                        "name": "cert",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "string",
                        "name": "fqdnAddresses",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "array_type": "string",
                        "name": "ipAddresses",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "name": "port",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "proxy",
                        "required": false,
                        "type": "boolean"
                    }
                ],
                "type": "object"
            },
            {
                "array_type": "object",
                "name": "savaMappingList",
                "required": false,
                "schema": [
                    {
                        "name": "autoSyncPeriod",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "ccoUser",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "expiry",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "lastSync",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "profile",
                        "required": true,
                        "schema": [
                            {
                                "name": "addressFqdn",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "addressIpV4",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "cert",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "makeDefault",
                                "required": false,
                                "type": "boolean"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "port",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "profileId",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "proxy",
                                "required": false,
                                "type": "boolean"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "smartAccountId",
                        "required": true,
                        "type": "string"
                    },
                    {
                        "name": "syncResult",
                        "required": false,
                        "schema": [
                            {
                                "array_type": "object",
                                "name": "syncList",
                                "required": false,
                                "schema": [
                                    {
                                        "array_type": "string",
                                        "name": "deviceSnList",
                                        "required": false,
                                        "schema": [],
                                        "type": "array"
                                    },
                                    {
                                        "name": "syncType",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            },
                            {
                                "name": "syncMsg",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "syncResultStr",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "syncStartTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "syncStatus",
                        "required": true,
                        "type": "string"
                    },
                    {
                        "name": "tenantId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "token",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "virtualAccountId",
                        "required": true,
                        "type": "string"
                    }
                ],
                "type": "array"
            },
            {
                "name": "taskTimeOuts",
                "required": false,
                "schema": [
                    {
                        "name": "configTimeOut",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "generalTimeOut",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "imageDownloadTimeOut",
                        "required": false,
                        "type": "integer"
                    }
                ],
                "type": "object"
            },
            {
                "name": "tenantId",
                "type": "string"
            },
            {
                "name": "version",
                "type": "integer"
            }
        ]
    },
    "responses": {
        "get_pnp_global_settings": {
            "properties": [
                "savaMappingList",
                "taskTimeOuts",
                "tenantId",
                "aaaCredentials",
                "defaultProfile",
                "acceptEula",
                "id",
                "_id",
                "version"
            ],
            "type": "object"
        },
        "update_pnp_global_settings": {
            "properties": [
                "savaMappingList",
                "taskTimeOuts",
                "tenantId",
                "aaaCredentials",
                "defaultProfile",
                "acceptEula",
                "id",
                "_id",
                "version"
            ],
            "type": "object"
        }
    }
}''')