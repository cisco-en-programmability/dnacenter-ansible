from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "device_onboarding_pnp",
    "name": "pnp_device_site_claim",
    "operations": {
        "post": [
            "claim_a_device_to_a_site"
        ]
    },
    "parameters": {
        "claim_a_device_to_a_site": [
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
        "claim_a_device_to_a_site": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}"""
)
