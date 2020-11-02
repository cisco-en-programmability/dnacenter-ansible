import json

module_definition = json.loads('''{
    "family": "device_onboarding_pnp",
    "name": "pnp_settings_virtual_account",
    "operations": {
        "delete": [
            "deregister_virtual_account"
        ],
        "get": [
            "get_virtual_account_list"
        ],
        "post": [
            "add_virtual_account"
        ],
        "put": [
            "update_pnp_server_profile"
        ]
    },
    "parameters": {
        "add_virtual_account": [
            {
                "name": "autoSyncPeriod",
                "type": "integer"
            },
            {
                "name": "ccoUser",
                "type": "string"
            },
            {
                "name": "expiry",
                "type": "integer"
            },
            {
                "name": "lastSync",
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
                "type": "string"
            },
            {
                "name": "syncStartTime",
                "type": "integer"
            },
            {
                "enum": [
                    "NOT_SYNCED",
                    "SYNCING",
                    "SUCCESS",
                    "FAILURE"
                ],
                "name": "syncStatus",
                "required": true,
                "type": "string"
            },
            {
                "name": "tenantId",
                "type": "string"
            },
            {
                "name": "token",
                "type": "string"
            },
            {
                "name": "virtualAccountId",
                "required": true,
                "type": "string"
            }
        ],
        "deregister_virtual_account": [
            {
                "name": "domain",
                "required": true,
                "type": "string"
            },
            {
                "name": "name",
                "required": true,
                "type": "string"
            }
        ],
        "get_virtual_account_list": [
            {
                "name": "domain",
                "required": true,
                "type": "string"
            }
        ],
        "update_pnp_server_profile": [
            {
                "name": "autoSyncPeriod",
                "type": "integer"
            },
            {
                "name": "ccoUser",
                "type": "string"
            },
            {
                "name": "expiry",
                "type": "integer"
            },
            {
                "name": "lastSync",
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
                "type": "string"
            },
            {
                "name": "syncStartTime",
                "type": "integer"
            },
            {
                "enum": [
                    "NOT_SYNCED",
                    "SYNCING",
                    "SUCCESS",
                    "FAILURE"
                ],
                "name": "syncStatus",
                "required": true,
                "type": "string"
            },
            {
                "name": "tenantId",
                "type": "string"
            },
            {
                "name": "token",
                "type": "string"
            },
            {
                "name": "virtualAccountId",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "add_virtual_account": {
            "properties": [
                "virtualAccountId",
                "autoSyncPeriod",
                "syncResultStr",
                "profile",
                "ccoUser",
                "syncResult",
                "token",
                "syncStartTime",
                "lastSync",
                "tenantId",
                "smartAccountId",
                "expiry",
                "syncStatus"
            ],
            "type": "object"
        },
        "deregister_virtual_account": {
            "properties": [
                "virtualAccountId",
                "autoSyncPeriod",
                "syncResultStr",
                "profile",
                "ccoUser",
                "syncResult",
                "token",
                "syncStartTime",
                "lastSync",
                "tenantId",
                "smartAccountId",
                "expiry",
                "syncStatus"
            ],
            "type": "object"
        },
        "get_virtual_account_list": {
            "array_type": "string",
            "properties": [],
            "type": "array"
        },
        "update_pnp_server_profile": {
            "properties": [
                "virtualAccountId",
                "autoSyncPeriod",
                "syncResultStr",
                "profile",
                "ccoUser",
                "syncResult",
                "token",
                "syncStartTime",
                "lastSync",
                "tenantId",
                "smartAccountId",
                "expiry",
                "syncStatus"
            ],
            "type": "object"
        }
    }
}''')