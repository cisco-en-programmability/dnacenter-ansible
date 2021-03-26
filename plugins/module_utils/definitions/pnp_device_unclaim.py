from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "device_onboarding_pnp",
    "name": "pnp_device_unclaim",
    "operations": {
        "post": [
            "un_claim_device"
        ]
    },
    "parameters": {
        "un_claim_device": [
            {
                "array_type": "string",
                "name": "deviceIdList",
                "required": false,
                "schema": [],
                "type": "array"
            }
        ]
    },
    "responses": {
        "un_claim_device": {
            "properties": [
                "jsonArrayResponse",
                "jsonResponse",
                "message",
                "statusCode"
            ],
            "type": "object"
        }
    }
}"""
)
