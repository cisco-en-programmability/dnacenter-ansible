import json

module_definition = json.loads('''{
    "family": "device_onboarding_pnp",
    "name": "pnp_settings_smart_account",
    "operations": {
        "get": [
            "get_smart_account_list"
        ]
    },
    "parameters": {
        "get_smart_account_list": []
    },
    "responses": {
        "get_smart_account_list": {
            "array_type": "string",
            "properties": [],
            "type": "array"
        }
    }
}''')