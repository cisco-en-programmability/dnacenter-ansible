from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json

module_definition = json.loads(
    """{
    "family": "device_onboarding_pnp",
    "name": "pnp_device",
    "operations": {
        "delete": [
            "delete_device_by_id_from_pnp"
        ],
        "get": [
            "get_device_list",
            "get_device_by_id",
            "get_device_count",
            "get_device_history"
        ],
        "post": [
            "add_device"
        ],
        "put": [
            "update_device"
        ]
    },
    "parameters": {
        "add_device": [
            {
                "name": "_id",
                "type": "string"
            },
            {
                "name": "deviceInfo",
                "required": true,
                "schema": [
                    {
                        "name": "aaaCredentials",
                        "required": false,
                        "schema": [
                            {
                                "name": "password",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "username",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "addedOn",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "array_type": "string",
                        "name": "addnMacAddrs",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "name": "agentType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "authStatus",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "authenticatedSudiSerialNo",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "string",
                        "name": "capabilitiesSupported",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "name": "cmState",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "string",
                        "name": "deviceSudiSerialNos",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "name": "deviceType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "string",
                        "name": "featuresSupported",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "fileSystemList",
                        "required": false,
                        "schema": [
                            {
                                "name": "freespace",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "readable",
                                "required": false,
                                "type": "boolean"
                            },
                            {
                                "name": "size",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "type",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "writeable",
                                "required": false,
                                "type": "boolean"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "firstContact",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "hostname",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "httpHeaders",
                        "required": false,
                        "schema": [
                            {
                                "name": "key",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "value",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "imageFile",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "imageVersion",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "ipInterfaces",
                        "required": false,
                        "schema": [
                            {
                                "name": "ipv4Address",
                                "required": false,
                                "type": "any"
                            },
                            {
                                "array_type": "object",
                                "name": "ipv6AddressList",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            },
                            {
                                "name": "macAddress",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "status",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "lastContact",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "lastSyncTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "lastUpdateOn",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "location",
                        "required": false,
                        "schema": [
                            {
                                "name": "address",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "altitude",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "latitude",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "longitude",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "siteId",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "macAddress",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "mode",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "neighborLinks",
                        "required": false,
                        "schema": [
                            {
                                "name": "localInterfaceName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "localMacAddress",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "localShortInterfaceName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "remoteDeviceName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "remoteInterfaceName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "remoteMacAddress",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "remotePlatform",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "remoteShortInterfaceName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "remoteVersion",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "onbState",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "pid",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "pnpProfileList",
                        "required": false,
                        "schema": [
                            {
                                "name": "createdBy",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "discoveryCreated",
                                "required": false,
                                "type": "boolean"
                            },
                            {
                                "name": "primaryEndpoint",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "certificate",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "fqdn",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "ipv4Address",
                                        "required": false,
                                        "type": "any"
                                    },
                                    {
                                        "name": "ipv6Address",
                                        "required": false,
                                        "type": "any"
                                    },
                                    {
                                        "name": "port",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "protocol",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "object"
                            },
                            {
                                "name": "profileName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "secondaryEndpoint",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "certificate",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "fqdn",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "ipv4Address",
                                        "required": false,
                                        "type": "any"
                                    },
                                    {
                                        "name": "ipv6Address",
                                        "required": false,
                                        "type": "any"
                                    },
                                    {
                                        "name": "port",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "protocol",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "object"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "populateInventory",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "array_type": "object",
                        "name": "preWorkflowCliOuputs",
                        "required": false,
                        "schema": [
                            {
                                "name": "cli",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "cliOutput",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "projectId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "projectName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "reloadRequested",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "serialNumber",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "smartAccountId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "source",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "stack",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "stackInfo",
                        "required": false,
                        "schema": [
                            {
                                "name": "isFullRing",
                                "required": false,
                                "type": "boolean"
                            },
                            {
                                "array_type": "object",
                                "name": "stackMemberList",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "hardwareVersion",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "licenseLevel",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "licenseType",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "macAddress",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "pid",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "priority",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "role",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "serialNumber",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "softwareVersion",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "stackNumber",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "state",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "sudiSerialNumber",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            },
                            {
                                "name": "stackRingProtocol",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "supportsStackWorkflows",
                                "required": false,
                                "type": "boolean"
                            },
                            {
                                "name": "totalMemberCount",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "array_type": "string",
                                "name": "validLicenseLevels",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "state",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "sudiRequired",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "tags",
                        "required": false,
                        "type": "any"
                    },
                    {
                        "array_type": "string",
                        "name": "userSudiSerialNos",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "name": "virtualAccountId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "workflowId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "workflowName",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "object"
            },
            {
                "array_type": "object",
                "name": "runSummaryList",
                "required": false,
                "schema": [
                    {
                        "name": "details",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "errorFlag",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "historyTaskInfo",
                        "required": false,
                        "schema": [
                            {
                                "array_type": "object",
                                "name": "addnDetails",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "key",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "value",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "timeTaken",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "type",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "workItemList",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "command",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "endTime",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "outputStr",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "startTime",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "state",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "timeTaken",
                                        "required": false,
                                        "type": "integer"
                                    }
                                ],
                                "type": "array"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "timestamp",
                        "required": false,
                        "type": "integer"
                    }
                ],
                "type": "array"
            },
            {
                "name": "systemResetWorkflow",
                "required": false,
                "schema": [
                    {
                        "name": "_id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "addToInventory",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "addedOn",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "configId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "currTaskIdx",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "endTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "execTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "imageId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instanceType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "lastupdateOn",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "startTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "state",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "tasks",
                        "required": false,
                        "schema": [
                            {
                                "name": "currWorkItemIdx",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "endTime",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "startTime",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "state",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "taskSeqNo",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "timeTaken",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "type",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "workItemList",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "command",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "endTime",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "outputStr",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "startTime",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "state",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "timeTaken",
                                        "required": false,
                                        "type": "integer"
                                    }
                                ],
                                "type": "array"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "tenantId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "type",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "useState",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "version",
                        "required": false,
                        "type": "integer"
                    }
                ],
                "type": "object"
            },
            {
                "name": "systemWorkflow",
                "required": false,
                "schema": [
                    {
                        "name": "_id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "addToInventory",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "addedOn",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "configId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "currTaskIdx",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "endTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "execTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "imageId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instanceType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "lastupdateOn",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "startTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "state",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "tasks",
                        "required": false,
                        "schema": [
                            {
                                "name": "currWorkItemIdx",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "endTime",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "startTime",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "state",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "taskSeqNo",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "timeTaken",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "type",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "workItemList",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "command",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "endTime",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "outputStr",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "startTime",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "state",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "timeTaken",
                                        "required": false,
                                        "type": "integer"
                                    }
                                ],
                                "type": "array"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "tenantId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "type",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "useState",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "version",
                        "required": false,
                        "type": "integer"
                    }
                ],
                "type": "object"
            },
            {
                "name": "tenantId",
                "type": "string"
            },
            {
                "name": "version",
                "type": "integer"
            },
            {
                "name": "workflow",
                "required": false,
                "schema": [
                    {
                        "name": "_id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "addToInventory",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "addedOn",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "configId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "currTaskIdx",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "endTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "execTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "imageId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instanceType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "lastupdateOn",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "startTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "state",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "tasks",
                        "required": false,
                        "schema": [
                            {
                                "name": "currWorkItemIdx",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "endTime",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "startTime",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "state",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "taskSeqNo",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "timeTaken",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "type",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "workItemList",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "command",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "endTime",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "outputStr",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "startTime",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "state",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "timeTaken",
                                        "required": false,
                                        "type": "integer"
                                    }
                                ],
                                "type": "array"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "tenantId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "type",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "useState",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "version",
                        "required": false,
                        "type": "integer"
                    }
                ],
                "type": "object"
            },
            {
                "name": "workflowParameters",
                "required": false,
                "schema": [
                    {
                        "array_type": "object",
                        "name": "configList",
                        "required": false,
                        "schema": [
                            {
                                "name": "configId",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "configParameters",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "key",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "value",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "licenseLevel",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "licenseType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "topOfStackSerialNumber",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "object"
            }
        ],
        "delete_device_by_id_from_pnp": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_device_by_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "get_device_count": [
            {
                "name": "cm_state",
                "required": false,
                "type": "string"
            },
            {
                "name": "last_contact",
                "required": false,
                "type": "boolean"
            },
            {
                "name": "name",
                "required": false,
                "type": "string"
            },
            {
                "name": "onb_state",
                "required": false,
                "type": "string"
            },
            {
                "name": "pid",
                "required": false,
                "type": "string"
            },
            {
                "name": "project_id",
                "required": false,
                "type": "string"
            },
            {
                "name": "project_name",
                "required": false,
                "type": "string"
            },
            {
                "name": "serial_number",
                "required": false,
                "type": "string"
            },
            {
                "name": "smart_account_id",
                "required": false,
                "type": "string"
            },
            {
                "name": "source",
                "required": false,
                "type": "string"
            },
            {
                "name": "_state",
                "required": false,
                "type": "string"
            },
            {
                "name": "virtual_account_id",
                "required": false,
                "type": "string"
            },
            {
                "name": "workflow_id",
                "required": false,
                "type": "string"
            },
            {
                "name": "workflow_name",
                "required": false,
                "type": "string"
            },
            {
                "artificial": true,
                "name": "count",
                "required": true,
                "type": "boolean"
            }
        ],
        "get_device_history": [
            {
                "name": "serial_number",
                "required": true,
                "type": "string"
            },
            {
                "name": "sort",
                "required": false,
                "type": "string"
            },
            {
                "name": "sort_order",
                "required": false,
                "type": "string"
            }
        ],
        "get_device_list": [
            {
                "name": "cm_state",
                "required": false,
                "type": "string"
            },
            {
                "name": "last_contact",
                "required": false,
                "type": "boolean"
            },
            {
                "name": "limit",
                "required": false,
                "type": "integer"
            },
            {
                "name": "name",
                "required": false,
                "type": "string"
            },
            {
                "name": "offset",
                "required": false,
                "type": "integer"
            },
            {
                "name": "onb_state",
                "required": false,
                "type": "string"
            },
            {
                "name": "pid",
                "required": false,
                "type": "string"
            },
            {
                "name": "project_id",
                "required": false,
                "type": "string"
            },
            {
                "name": "project_name",
                "required": false,
                "type": "string"
            },
            {
                "name": "serial_number",
                "required": false,
                "type": "string"
            },
            {
                "name": "smart_account_id",
                "required": false,
                "type": "string"
            },
            {
                "name": "sort",
                "required": false,
                "type": "string"
            },
            {
                "name": "sort_order",
                "required": false,
                "type": "string"
            },
            {
                "name": "source",
                "required": false,
                "type": "string"
            },
            {
                "name": "_state",
                "required": false,
                "type": "string"
            },
            {
                "name": "virtual_account_id",
                "required": false,
                "type": "string"
            },
            {
                "name": "workflow_id",
                "required": false,
                "type": "string"
            },
            {
                "name": "workflow_name",
                "required": false,
                "type": "string"
            }
        ],
        "update_device": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "name": "_id",
                "type": "string"
            },
            {
                "name": "deviceInfo",
                "required": true,
                "schema": [
                    {
                        "name": "aaaCredentials",
                        "required": false,
                        "schema": [
                            {
                                "name": "password",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "username",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "addedOn",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "array_type": "string",
                        "name": "addnMacAddrs",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "name": "agentType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "authStatus",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "authenticatedSudiSerialNo",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "string",
                        "name": "capabilitiesSupported",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "name": "cmState",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "string",
                        "name": "deviceSudiSerialNos",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "name": "deviceType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "string",
                        "name": "featuresSupported",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "array_type": "object",
                        "name": "fileSystemList",
                        "required": false,
                        "schema": [
                            {
                                "name": "freespace",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "readable",
                                "required": false,
                                "type": "boolean"
                            },
                            {
                                "name": "size",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "type",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "writeable",
                                "required": false,
                                "type": "boolean"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "firstContact",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "hostname",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "httpHeaders",
                        "required": false,
                        "schema": [
                            {
                                "name": "key",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "value",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "imageFile",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "imageVersion",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "ipInterfaces",
                        "required": false,
                        "schema": [
                            {
                                "name": "ipv4Address",
                                "required": false,
                                "type": "any"
                            },
                            {
                                "array_type": "object",
                                "name": "ipv6AddressList",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            },
                            {
                                "name": "macAddress",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "status",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "lastContact",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "lastSyncTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "lastUpdateOn",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "location",
                        "required": false,
                        "schema": [
                            {
                                "name": "address",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "altitude",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "latitude",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "longitude",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "siteId",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "macAddress",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "mode",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "neighborLinks",
                        "required": false,
                        "schema": [
                            {
                                "name": "localInterfaceName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "localMacAddress",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "localShortInterfaceName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "remoteDeviceName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "remoteInterfaceName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "remoteMacAddress",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "remotePlatform",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "remoteShortInterfaceName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "remoteVersion",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "onbState",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "pid",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "pnpProfileList",
                        "required": false,
                        "schema": [
                            {
                                "name": "createdBy",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "discoveryCreated",
                                "required": false,
                                "type": "boolean"
                            },
                            {
                                "name": "primaryEndpoint",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "certificate",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "fqdn",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "ipv4Address",
                                        "required": false,
                                        "type": "any"
                                    },
                                    {
                                        "name": "ipv6Address",
                                        "required": false,
                                        "type": "any"
                                    },
                                    {
                                        "name": "port",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "protocol",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "object"
                            },
                            {
                                "name": "profileName",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "secondaryEndpoint",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "certificate",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "fqdn",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "ipv4Address",
                                        "required": false,
                                        "type": "any"
                                    },
                                    {
                                        "name": "ipv6Address",
                                        "required": false,
                                        "type": "any"
                                    },
                                    {
                                        "name": "port",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "protocol",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "object"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "populateInventory",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "array_type": "object",
                        "name": "preWorkflowCliOuputs",
                        "required": false,
                        "schema": [
                            {
                                "name": "cli",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "cliOutput",
                                "required": false,
                                "type": "string"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "projectId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "projectName",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "reloadRequested",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "serialNumber",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "smartAccountId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "source",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "stack",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "stackInfo",
                        "required": false,
                        "schema": [
                            {
                                "name": "isFullRing",
                                "required": false,
                                "type": "boolean"
                            },
                            {
                                "array_type": "object",
                                "name": "stackMemberList",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "hardwareVersion",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "licenseLevel",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "licenseType",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "macAddress",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "pid",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "priority",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "role",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "serialNumber",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "softwareVersion",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "stackNumber",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "state",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "sudiSerialNumber",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            },
                            {
                                "name": "stackRingProtocol",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "supportsStackWorkflows",
                                "required": false,
                                "type": "boolean"
                            },
                            {
                                "name": "totalMemberCount",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "array_type": "string",
                                "name": "validLicenseLevels",
                                "required": false,
                                "schema": [],
                                "type": "array"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "state",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "sudiRequired",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "tags",
                        "required": false,
                        "type": "any"
                    },
                    {
                        "array_type": "string",
                        "name": "userSudiSerialNos",
                        "required": false,
                        "schema": [],
                        "type": "array"
                    },
                    {
                        "name": "virtualAccountId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "workflowId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "workflowName",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "object"
            },
            {
                "array_type": "object",
                "name": "runSummaryList",
                "required": false,
                "schema": [
                    {
                        "name": "details",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "errorFlag",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "historyTaskInfo",
                        "required": false,
                        "schema": [
                            {
                                "array_type": "object",
                                "name": "addnDetails",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "key",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "value",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "timeTaken",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "type",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "workItemList",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "command",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "endTime",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "outputStr",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "startTime",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "state",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "timeTaken",
                                        "required": false,
                                        "type": "integer"
                                    }
                                ],
                                "type": "array"
                            }
                        ],
                        "type": "object"
                    },
                    {
                        "name": "timestamp",
                        "required": false,
                        "type": "integer"
                    }
                ],
                "type": "array"
            },
            {
                "name": "systemResetWorkflow",
                "required": false,
                "schema": [
                    {
                        "name": "_id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "addToInventory",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "addedOn",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "configId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "currTaskIdx",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "endTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "execTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "imageId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instanceType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "lastupdateOn",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "startTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "state",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "tasks",
                        "required": false,
                        "schema": [
                            {
                                "name": "currWorkItemIdx",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "endTime",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "startTime",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "state",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "taskSeqNo",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "timeTaken",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "type",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "workItemList",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "command",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "endTime",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "outputStr",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "startTime",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "state",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "timeTaken",
                                        "required": false,
                                        "type": "integer"
                                    }
                                ],
                                "type": "array"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "tenantId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "type",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "useState",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "version",
                        "required": false,
                        "type": "integer"
                    }
                ],
                "type": "object"
            },
            {
                "name": "systemWorkflow",
                "required": false,
                "schema": [
                    {
                        "name": "_id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "addToInventory",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "addedOn",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "configId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "currTaskIdx",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "endTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "execTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "imageId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instanceType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "lastupdateOn",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "startTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "state",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "tasks",
                        "required": false,
                        "schema": [
                            {
                                "name": "currWorkItemIdx",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "endTime",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "startTime",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "state",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "taskSeqNo",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "timeTaken",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "type",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "workItemList",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "command",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "endTime",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "outputStr",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "startTime",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "state",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "timeTaken",
                                        "required": false,
                                        "type": "integer"
                                    }
                                ],
                                "type": "array"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "tenantId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "type",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "useState",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "version",
                        "required": false,
                        "type": "integer"
                    }
                ],
                "type": "object"
            },
            {
                "name": "tenantId",
                "type": "string"
            },
            {
                "name": "version",
                "type": "integer"
            },
            {
                "name": "workflow",
                "required": false,
                "schema": [
                    {
                        "name": "_id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "addToInventory",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "name": "addedOn",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "configId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "currTaskIdx",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "endTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "execTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "imageId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instanceType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "lastupdateOn",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "startTime",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "state",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "array_type": "object",
                        "name": "tasks",
                        "required": false,
                        "schema": [
                            {
                                "name": "currWorkItemIdx",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "endTime",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "name",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "startTime",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "state",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "name": "taskSeqNo",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "timeTaken",
                                "required": false,
                                "type": "integer"
                            },
                            {
                                "name": "type",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "workItemList",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "command",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "endTime",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "outputStr",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "startTime",
                                        "required": false,
                                        "type": "integer"
                                    },
                                    {
                                        "name": "state",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "timeTaken",
                                        "required": false,
                                        "type": "integer"
                                    }
                                ],
                                "type": "array"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "tenantId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "type",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "useState",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "version",
                        "required": false,
                        "type": "integer"
                    }
                ],
                "type": "object"
            },
            {
                "name": "workflowParameters",
                "required": false,
                "schema": [
                    {
                        "array_type": "object",
                        "name": "configList",
                        "required": false,
                        "schema": [
                            {
                                "name": "configId",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "configParameters",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "key",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "value",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "licenseLevel",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "licenseType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "topOfStackSerialNumber",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "object"
            }
        ]
    },
    "responses": {
        "add_device": {
            "properties": [
                "_id",
                "deviceInfo",
                "systemResetWorkflow",
                "systemWorkflow",
                "workflow",
                "runSummaryList",
                "workflowParameters",
                "dayZeroConfig",
                "dayZeroConfigPreview",
                "version",
                "tenantId"
            ],
            "type": "object"
        },
        "delete_device_by_id_from_pnp": {
            "properties": [
                "_id",
                "deviceInfo",
                "systemResetWorkflow",
                "systemWorkflow",
                "workflow",
                "runSummaryList",
                "workflowParameters",
                "dayZeroConfig",
                "dayZeroConfigPreview",
                "version",
                "tenantId"
            ],
            "type": "object"
        },
        "get_device_by_id": {
            "properties": [
                "_id",
                "deviceInfo",
                "systemResetWorkflow",
                "systemWorkflow",
                "workflow",
                "runSummaryList",
                "workflowParameters",
                "dayZeroConfig",
                "dayZeroConfigPreview",
                "version",
                "tenantId"
            ],
            "type": "object"
        },
        "get_device_count": {
            "properties": [
                "response"
            ],
            "type": "object"
        },
        "get_device_history": {
            "properties": [
                "response",
                "statusCode"
            ],
            "type": "object"
        },
        "get_device_list": {
            "properties": [
                "deviceInfo",
                "systemResetWorkflow",
                "systemWorkflow",
                "workflow",
                "runSummaryList",
                "workflowParameters",
                "dayZeroConfig",
                "dayZeroConfigPreview",
                "version",
                "tenantId"
            ],
            "type": "object"
        },
        "update_device": {
            "properties": [
                "_id",
                "deviceInfo",
                "systemResetWorkflow",
                "systemWorkflow",
                "workflow",
                "runSummaryList",
                "workflowParameters",
                "dayZeroConfig",
                "dayZeroConfigPreview",
                "version",
                "tenantId"
            ],
            "type": "object"
        }
    }
}"""
)
