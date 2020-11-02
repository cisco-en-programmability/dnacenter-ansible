import json

module_definition = json.loads('''{
    "family": "device_onboarding_pnp",
    "name": "pnp_device_virtual_account_sync_result",
    "operations": {
        "get": [
            "get_sync_result_for_virtual_account"
        ]
    },
    "parameters": {
        "get_sync_result_for_virtual_account": [
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
        ]
    },
    "responses": {
        "get_sync_result_for_virtual_account": {
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