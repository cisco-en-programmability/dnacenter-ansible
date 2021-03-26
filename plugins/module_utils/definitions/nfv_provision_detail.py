from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "site_design",
    "name": "nfv_provision_detail",
    "operations": {
        "post": [
            "nfv_provisioning_detail"
        ]
    },
    "parameters": {
        "nfv_provisioning_detail": [
            {
                "name": "device_ip",
                "required": true,
                "type": "string"
            }
        ]
    },
    "responses": {
        "nfv_provisioning_detail": {
            "properties": [
                "executionId",
                "executionStatusUrl",
                "message"
            ],
            "type": "object"
        }
    }
}"""
)
