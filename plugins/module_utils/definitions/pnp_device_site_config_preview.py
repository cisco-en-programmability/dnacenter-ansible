import json

module_definition = json.loads(
    """{
    "family": "device_onboarding_pnp",
    "name": "pnp_device_site_config_preview",
    "operations": {
        "post": [
            "preview_config"
        ]
    },
    "parameters": {
        "preview_config": [
            {
                "name": "deviceId",
                "type": "string"
            },
            {
                "name": "siteId",
                "type": "string"
            },
            {
                "enum": [
                    "Default",
                    "AccessPoint",
                    "StackSwitch",
                    "Sensor",
                    "MobilityExpress"
                ],
                "name": "type",
                "type": "string"
            }
        ]
    },
    "responses": {
        "preview_config": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
