import json

module_definition = json.loads('''{
    "family": "device_onboarding_pnp",
    "name": "pnp_device_virtual_account_sync",
    "operations": {
        "post": [
            "sync_virtual_account_devices"
        ]
    },
    "parameters": {
        "sync_virtual_account_devices": [
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
        "sync_virtual_account_devices": {
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