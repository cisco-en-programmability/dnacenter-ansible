import json

module_definition = json.loads('''{
    "family": "discovery",
    "name": "discovery",
    "operations": {
        "delete": [
            "delete_all_discovery",
            "delete_discovery_by_id",
            "delete_discovery_by_specified_range"
        ],
        "get": [
            "get_count_of_all_discovery_jobs",
            "get_discovery_by_id",
            "get_discoveries_by_range"
        ],
        "post": [
            "start_discovery"
        ],
        "put": [
            "updates_discovery_by_id"
        ]
    },
    "parameters": {
        "delete_all_discovery": [],
        "delete_discovery_by_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "delete_discovery_by_specified_range": [
            {
                "name": "records_to_delete",
                "required": true,
                "type": "integer"
            },
            {
                "name": "start_index",
                "required": true,
                "type": "integer"
            }
        ],
        "get_count_of_all_discovery_jobs": [
            {
                "artificial": true,
                "name": "count",
                "required": true,
                "type": "boolean"
            }
        ],
        "get_discoveries_by_range": [
            {
                "name": "records_to_return",
                "required": true,
                "type": "integer"
            },
            {
                "name": "start_index",
                "required": true,
                "type": "integer"
            }
        ],
        "get_discovery_by_id": [
            {
                "name": "id",
                "required": true,
                "type": "string"
            }
        ],
        "start_discovery": [
            {
                "name": "cdpLevel",
                "type": "integer"
            },
            {
                "name": "discoveryType",
                "required": true,
                "type": "string"
            },
            {
                "array_type": "string",
                "name": "enablePasswordList",
                "required": false,
                "schema": [],
                "type": "array"
            },
            {
                "array_type": "string",
                "name": "globalCredentialIdList",
                "required": false,
                "schema": [],
                "type": "array"
            },
            {
                "name": "httpReadCredential",
                "required": false,
                "schema": [
                    {
                        "name": "comments",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "credentialType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instanceTenantId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instanceUuid",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "password",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "port",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "secure",
                        "required": false,
                        "type": "boolean"
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
                "name": "httpWriteCredential",
                "required": false,
                "schema": [
                    {
                        "name": "comments",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "credentialType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instanceTenantId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instanceUuid",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "password",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "port",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "secure",
                        "required": false,
                        "type": "boolean"
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
                "name": "ipAddressList",
                "required": true,
                "type": "string"
            },
            {
                "array_type": "string",
                "name": "ipFilterList",
                "required": false,
                "schema": [],
                "type": "array"
            },
            {
                "name": "lldpLevel",
                "type": "integer"
            },
            {
                "name": "name",
                "required": true,
                "type": "string"
            },
            {
                "name": "netconfPort",
                "type": "string"
            },
            {
                "name": "noAddNewDevice",
                "type": "boolean"
            },
            {
                "name": "parentDiscoveryId",
                "type": "string"
            },
            {
                "array_type": "string",
                "name": "passwordList",
                "required": false,
                "schema": [],
                "type": "array"
            },
            {
                "name": "preferredMgmtIPMethod",
                "type": "string"
            },
            {
                "name": "protocolOrder",
                "type": "string"
            },
            {
                "name": "reDiscovery",
                "type": "boolean"
            },
            {
                "name": "retry",
                "type": "integer"
            },
            {
                "name": "snmpAuthPassphrase",
                "type": "string"
            },
            {
                "name": "snmpAuthProtocol",
                "type": "string"
            },
            {
                "name": "snmpMode",
                "type": "string"
            },
            {
                "name": "snmpPrivPassphrase",
                "type": "string"
            },
            {
                "name": "snmpPrivProtocol",
                "type": "string"
            },
            {
                "name": "snmpROCommunity",
                "type": "string"
            },
            {
                "name": "snmpROCommunityDesc",
                "type": "string"
            },
            {
                "name": "snmpRWCommunity",
                "type": "string"
            },
            {
                "name": "snmpRWCommunityDesc",
                "type": "string"
            },
            {
                "name": "snmpUserName",
                "type": "string"
            },
            {
                "name": "snmpVersion",
                "required": true,
                "type": "string"
            },
            {
                "name": "timeout",
                "type": "integer"
            },
            {
                "name": "updateMgmtIp",
                "type": "boolean"
            },
            {
                "array_type": "string",
                "name": "userNameList",
                "required": false,
                "schema": [],
                "type": "array"
            }
        ],
        "updates_discovery_by_id": [
            {
                "name": "attributeInfo",
                "required": false,
                "schema": [],
                "type": "object"
            },
            {
                "name": "cdpLevel",
                "type": "integer"
            },
            {
                "name": "deviceIds",
                "type": "string"
            },
            {
                "name": "discoveryCondition",
                "type": "string"
            },
            {
                "name": "discoveryStatus",
                "required": true,
                "type": "string"
            },
            {
                "name": "discoveryType",
                "type": "string"
            },
            {
                "name": "enablePasswordList",
                "type": "string"
            },
            {
                "array_type": "string",
                "name": "globalCredentialIdList",
                "required": false,
                "schema": [],
                "type": "array"
            },
            {
                "name": "httpReadCredential",
                "required": false,
                "schema": [
                    {
                        "name": "comments",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "credentialType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instanceTenantId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instanceUuid",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "password",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "port",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "secure",
                        "required": false,
                        "type": "boolean"
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
                "name": "httpWriteCredential",
                "required": false,
                "schema": [
                    {
                        "name": "comments",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "credentialType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "description",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instanceTenantId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "instanceUuid",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "password",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "port",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "name": "secure",
                        "required": false,
                        "type": "boolean"
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
                "name": "id",
                "required": true,
                "type": "string"
            },
            {
                "name": "ipAddressList",
                "type": "string"
            },
            {
                "name": "ipFilterList",
                "type": "string"
            },
            {
                "name": "isAutoCdp",
                "type": "boolean"
            },
            {
                "name": "lldpLevel",
                "type": "integer"
            },
            {
                "name": "name",
                "type": "string"
            },
            {
                "name": "netconfPort",
                "type": "string"
            },
            {
                "name": "numDevices",
                "type": "integer"
            },
            {
                "name": "parentDiscoveryId",
                "type": "string"
            },
            {
                "name": "passwordList",
                "type": "string"
            },
            {
                "name": "preferredMgmtIPMethod",
                "type": "string"
            },
            {
                "name": "protocolOrder",
                "type": "string"
            },
            {
                "name": "retryCount",
                "type": "integer"
            },
            {
                "name": "snmpAuthPassphrase",
                "type": "string"
            },
            {
                "name": "snmpAuthProtocol",
                "type": "string"
            },
            {
                "name": "snmpMode",
                "type": "string"
            },
            {
                "name": "snmpPrivPassphrase",
                "type": "string"
            },
            {
                "name": "snmpPrivProtocol",
                "type": "string"
            },
            {
                "name": "snmpRoCommunity",
                "type": "string"
            },
            {
                "name": "snmpRoCommunityDesc",
                "type": "string"
            },
            {
                "name": "snmpRwCommunity",
                "type": "string"
            },
            {
                "name": "snmpRwCommunityDesc",
                "type": "string"
            },
            {
                "name": "snmpUserName",
                "type": "string"
            },
            {
                "name": "timeOut",
                "type": "integer"
            },
            {
                "name": "updateMgmtIp",
                "type": "boolean"
            },
            {
                "name": "userNameList",
                "type": "string"
            }
        ]
    },
    "responses": {
        "delete_all_discovery": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "delete_discovery_by_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "delete_discovery_by_specified_range": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_count_of_all_discovery_jobs": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_discoveries_by_range": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "get_discovery_by_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "start_discovery": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        },
        "updates_discovery_by_id": {
            "properties": [
                "response",
                "version"
            ],
            "type": "object"
        }
    }
}''')