from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "topology",
    "name": "network_health",
    "operations": {
        "get": [
            "get_overall_network_health"
        ]
    },
    "parameters": {
        "get_overall_network_health": [
            {
                "name": "timestamp",
                "required": false,
                "type": "integer"
            }
        ]
    },
    "responses": {
        "get_overall_network_health": {
            "properties": [
                "version",
                "response",
                "measuredBy",
                "latestMeasuredByEntity",
                "latestHealthScore",
                "monitoredDevices",
                "monitoredHealthyDevices",
                "monitoredUnHealthyDevices",
                "unMonitoredDevices",
                "healthDistirubution"
            ],
            "type": "object"
        }
    }
}"""
)
