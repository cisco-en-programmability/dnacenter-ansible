from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "wireless",
    "name": "wireless_ap_provision",
    "operations": {
        "post": [
            "ap_provision_and_re_provision"
        ]
    },
    "parameters": {
        "ap_provision_and_re_provision": [
            {
                "array_type": "object",
                "name": "payload",
                "required": true,
                "schema": [
                    {
                        "name": "executionId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "executionUrl",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "message",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            }
        ]
    },
    "responses": {
        "ap_provision_and_re_provision": {
            "properties": [
                "executionId",
                "executionUrl",
                "provisionTasks"
            ],
            "type": "object"
        }
    }
}"""
)
