#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '0.0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: pnp_device
short_description: Manage PnpDevice objects of DeviceOnboardingPnp
description:
- Returns list of devices based on filter crieteria. If a limit is not specified, it will default to return 50 devices. Pagination and sorting are also supported by this endpoint.
- Adds a device to the PnP database.
- Returns device details specified by device id.
- Deletes specified device from PnP database.
- Updates device details specified by device id in PnP database.
- Returns the device count based on filter criteria. This is useful for pagination.
- Returns history for a specific device. Serial number is a required parameter.
version_added: '1.0'
author: first last (@GitHubID)
options:
    cm_state:
        description:
        - Device Connection Manager State.
        type: str
    last_contact:
        description:
        - Device Has Contacted lastContact > 0.
        type: bool
    limit:
        description:
        - Limits number of results.
        type: int
    name:
        description:
        - Device Name.
        type: str
    offset:
        description:
        - Index of first result.
        type: int
    onb_state:
        description:
        - Device Onboarding State.
        type: str
    pid:
        description:
        - Device ProductId.
        type: str
    project_id:
        description:
        - Device Project Id.
        type: str
    project_name:
        description:
        - Device Project Name.
        type: str
    serial_number:
        description:
        - Device Serial Number.
        type: str
    smart_account_id:
        description:
        - Device Smart Account.
        type: str
    sort:
        description:
        - Comma seperated list of fields to sort on.
        type: str
    sort_order:
        description:
        - Sort Order Ascending (asc) or Descending (des).
        type: str
    source:
        description:
        - Device Source.
        type: str
    state:
        description:
        - Device State.
        type: str
    virtual_account_id:
        description:
        - Device Virtual Account.
        type: str
    workflow_id:
        description:
        - Device Workflow Id.
        type: str
    workflow_name:
        description:
        - Device Workflow Name.
        type: str
    _id:
        description:
        - Device's _id.
        type: str
    deviceInfo:
        description:
        - Device's deviceInfo.
        type: dict
        required: True
        suboptions:
            aaaCredentials:
                description:
                - It is the pnp device's aaaCredentials.
                type: dict
                suboptions:
                    password:
                        description:
                        - It is the pnp device's password.
                        type: str
                    username:
                        description:
                        - It is the pnp device's username.
                        type: str

            addedOn:
                description:
                - It is the pnp device's addedOn.
                type: int
            addnMacAddrs:
                description:
                - It is the pnp device's addnMacAddrs.
                type: list
            agentType:
                description:
                - It is the pnp device's agentType.
                type: str
            authStatus:
                description:
                - It is the pnp device's authStatus.
                type: str
            authenticatedSudiSerialNo:
                description:
                - It is the pnp device's authenticatedSudiSerialNo.
                type: str
            capabilitiesSupported:
                description:
                - It is the pnp device's capabilitiesSupported.
                type: list
            cmState:
                description:
                - It is the pnp device's cmState.
                type: str
            description:
                description:
                - It is the pnp device's description.
                type: str
            deviceSudiSerialNos:
                description:
                - It is the pnp device's deviceSudiSerialNos.
                type: list
            deviceType:
                description:
                - It is the pnp device's deviceType.
                type: str
            featuresSupported:
                description:
                - It is the pnp device's featuresSupported.
                type: list
            fileSystemList:
                description:
                - It is the pnp device's fileSystemList.
                type: list
                elements: dict
                suboptions:
                    freespace:
                        description:
                        - It is the pnp device's freespace.
                        type: int
                    name:
                        description:
                        - It is the pnp device's name.
                        type: str
                    readable:
                        description:
                        - It is the pnp device's readable.
                        type: bool
                    size:
                        description:
                        - It is the pnp device's size.
                        type: int
                    type:
                        description:
                        - It is the pnp device's type.
                        type: str
                    writeable:
                        description:
                        - It is the pnp device's writeable.
                        type: bool

            firstContact:
                description:
                - It is the pnp device's firstContact.
                type: int
            hostname:
                description:
                - It is the pnp device's hostname.
                type: str
            httpHeaders:
                description:
                - It is the pnp device's httpHeaders.
                type: list
                elements: dict
                suboptions:
                    key:
                        description:
                        - It is the pnp device's key.
                        type: str
                    value:
                        description:
                        - It is the pnp device's value.
                        type: str

            imageFile:
                description:
                - It is the pnp device's imageFile.
                type: str
            imageVersion:
                description:
                - It is the pnp device's imageVersion.
                type: str
            ipInterfaces:
                description:
                - It is the pnp device's ipInterfaces.
                type: list
                elements: dict
                suboptions:
                    ipv4Address:
                        description:
                        - It is the pnp device's ipv4Address.
                        type: dict
                    ipv6AddressList:
                        description:
                        - It is the pnp device's ipv6AddressList.
                        type: list
                    macAddress:
                        description:
                        - It is the pnp device's macAddress.
                        type: str
                    name:
                        description:
                        - It is the pnp device's name.
                        type: str
                    status:
                        description:
                        - It is the pnp device's status.
                        type: str

            lastContact:
                description:
                - It is the pnp device's lastContact.
                type: int
            lastSyncTime:
                description:
                - It is the pnp device's lastSyncTime.
                type: int
            lastUpdateOn:
                description:
                - It is the pnp device's lastUpdateOn.
                type: int
            location:
                description:
                - It is the pnp device's location.
                type: dict
                suboptions:
                    address:
                        description:
                        - It is the pnp device's address.
                        type: str
                    altitude:
                        description:
                        - It is the pnp device's altitude.
                        type: str
                    latitude:
                        description:
                        - It is the pnp device's latitude.
                        type: str
                    longitude:
                        description:
                        - It is the pnp device's longitude.
                        type: str
                    siteId:
                        description:
                        - It is the pnp device's siteId.
                        type: str

            macAddress:
                description:
                - It is the pnp device's macAddress.
                type: str
            mode:
                description:
                - It is the pnp device's mode.
                type: str
            name:
                description:
                - It is the pnp device's name.
                type: str
            neighborLinks:
                description:
                - It is the pnp device's neighborLinks.
                type: list
                elements: dict
                suboptions:
                    localInterfaceName:
                        description:
                        - It is the pnp device's localInterfaceName.
                        type: str
                    localMacAddress:
                        description:
                        - It is the pnp device's localMacAddress.
                        type: str
                    localShortInterfaceName:
                        description:
                        - It is the pnp device's localShortInterfaceName.
                        type: str
                    remoteDeviceName:
                        description:
                        - It is the pnp device's remoteDeviceName.
                        type: str
                    remoteInterfaceName:
                        description:
                        - It is the pnp device's remoteInterfaceName.
                        type: str
                    remoteMacAddress:
                        description:
                        - It is the pnp device's remoteMacAddress.
                        type: str
                    remotePlatform:
                        description:
                        - It is the pnp device's remotePlatform.
                        type: str
                    remoteShortInterfaceName:
                        description:
                        - It is the pnp device's remoteShortInterfaceName.
                        type: str
                    remoteVersion:
                        description:
                        - It is the pnp device's remoteVersion.
                        type: str

            onbState:
                description:
                - It is the pnp device's onbState.
                type: str
            pid:
                description:
                - It is the pnp device's pid.
                type: str
            pnpProfileList:
                description:
                - It is the pnp device's pnpProfileList.
                type: list
                elements: dict
                suboptions:
                    createdBy:
                        description:
                        - It is the pnp device's createdBy.
                        type: str
                    discoveryCreated:
                        description:
                        - It is the pnp device's discoveryCreated.
                        type: bool
                    primaryEndpoint:
                        description:
                        - It is the pnp device's primaryEndpoint.
                        type: dict
                        suboptions:
                            certificate:
                                description:
                                - It is the pnp device's certificate.
                                type: str
                            fqdn:
                                description:
                                - It is the pnp device's fqdn.
                                type: str
                            ipv4Address:
                                description:
                                - It is the pnp device's ipv4Address.
                                type: dict
                            ipv6Address:
                                description:
                                - It is the pnp device's ipv6Address.
                                type: dict
                            port:
                                description:
                                - It is the pnp device's port.
                                type: int
                            protocol:
                                description:
                                - It is the pnp device's protocol.
                                type: str

                    profileName:
                        description:
                        - It is the pnp device's profileName.
                        type: str
                    secondaryEndpoint:
                        description:
                        - It is the pnp device's secondaryEndpoint.
                        type: dict
                        suboptions:
                            certificate:
                                description:
                                - It is the pnp device's certificate.
                                type: str
                            fqdn:
                                description:
                                - It is the pnp device's fqdn.
                                type: str
                            ipv4Address:
                                description:
                                - It is the pnp device's ipv4Address.
                                type: dict
                            ipv6Address:
                                description:
                                - It is the pnp device's ipv6Address.
                                type: dict
                            port:
                                description:
                                - It is the pnp device's port.
                                type: int
                            protocol:
                                description:
                                - It is the pnp device's protocol.
                                type: str


            populateInventory:
                description:
                - It is the pnp device's populateInventory.
                type: bool
            preWorkflowCliOuputs:
                description:
                - It is the pnp device's preWorkflowCliOuputs.
                type: list
                elements: dict
                suboptions:
                    cli:
                        description:
                        - It is the pnp device's cli.
                        type: str
                    cliOutput:
                        description:
                        - It is the pnp device's cliOutput.
                        type: str

            projectId:
                description:
                - It is the pnp device's projectId.
                type: str
            projectName:
                description:
                - It is the pnp device's projectName.
                type: str
            reloadRequested:
                description:
                - It is the pnp device's reloadRequested.
                type: bool
            serialNumber:
                description:
                - It is the pnp device's serialNumber.
                type: str
            smartAccountId:
                description:
                - It is the pnp device's smartAccountId.
                type: str
            source:
                description:
                - It is the pnp device's source.
                type: str
            stack:
                description:
                - It is the pnp device's stack.
                type: bool
            stackInfo:
                description:
                - It is the pnp device's stackInfo.
                type: dict
                suboptions:
                    isFullRing:
                        description:
                        - It is the pnp device's isFullRing.
                        type: bool
                    stackMemberList:
                        description:
                        - It is the pnp device's stackMemberList.
                        type: list
                        elements: dict
                        suboptions:
                            hardwareVersion:
                                description:
                                - It is the pnp device's hardwareVersion.
                                type: str
                            licenseLevel:
                                description:
                                - It is the pnp device's licenseLevel.
                                type: str
                            licenseType:
                                description:
                                - It is the pnp device's licenseType.
                                type: str
                            macAddress:
                                description:
                                - It is the pnp device's macAddress.
                                type: str
                            pid:
                                description:
                                - It is the pnp device's pid.
                                type: str
                            priority:
                                description:
                                - It is the pnp device's priority.
                                type: int
                            role:
                                description:
                                - It is the pnp device's role.
                                type: str
                            serialNumber:
                                description:
                                - It is the pnp device's serialNumber.
                                type: str
                            softwareVersion:
                                description:
                                - It is the pnp device's softwareVersion.
                                type: str
                            stackNumber:
                                description:
                                - It is the pnp device's stackNumber.
                                type: int
                            state:
                                description:
                                - It is the pnp device's state.
                                type: str
                            sudiSerialNumber:
                                description:
                                - It is the pnp device's sudiSerialNumber.
                                type: str

                    stackRingProtocol:
                        description:
                        - It is the pnp device's stackRingProtocol.
                        type: str
                    supportsStackWorkflows:
                        description:
                        - It is the pnp device's supportsStackWorkflows.
                        type: bool
                    totalMemberCount:
                        description:
                        - It is the pnp device's totalMemberCount.
                        type: int
                    validLicenseLevels:
                        description:
                        - It is the pnp device's validLicenseLevels.
                        type: list

            state:
                description:
                - It is the pnp device's state.
                type: str
            sudiRequired:
                description:
                - It is the pnp device's sudiRequired.
                type: bool
            tags:
                description:
                - It is the pnp device's tags.
                type: dict
            userSudiSerialNos:
                description:
                - It is the pnp device's userSudiSerialNos.
                type: list
            virtualAccountId:
                description:
                - It is the pnp device's virtualAccountId.
                type: str
            workflowId:
                description:
                - It is the pnp device's workflowId.
                type: str
            workflowName:
                description:
                - It is the pnp device's workflowName.
                type: str

    runSummaryList:
        description:
        - Device's runSummaryList (list of objects).
        type: list
        elements: dict
        suboptions:
            details:
                description:
                - It is the pnp device's details.
                type: str
            errorFlag:
                description:
                - It is the pnp device's errorFlag.
                type: bool
            historyTaskInfo:
                description:
                - It is the pnp device's historyTaskInfo.
                type: dict
                suboptions:
                    addnDetails:
                        description:
                        - It is the pnp device's addnDetails.
                        type: list
                        elements: dict
                        suboptions:
                            key:
                                description:
                                - It is the pnp device's key.
                                type: str
                            value:
                                description:
                                - It is the pnp device's value.
                                type: str

                    name:
                        description:
                        - It is the pnp device's name.
                        type: str
                    timeTaken:
                        description:
                        - It is the pnp device's timeTaken.
                        type: int
                    type:
                        description:
                        - It is the pnp device's type.
                        type: str
                    workItemList:
                        description:
                        - It is the pnp device's workItemList.
                        type: list
                        elements: dict
                        suboptions:
                            command:
                                description:
                                - It is the pnp device's command.
                                type: str
                            endTime:
                                description:
                                - It is the pnp device's endTime.
                                type: int
                            outputStr:
                                description:
                                - It is the pnp device's outputStr.
                                type: str
                            startTime:
                                description:
                                - It is the pnp device's startTime.
                                type: int
                            state:
                                description:
                                - It is the pnp device's state.
                                type: str
                            timeTaken:
                                description:
                                - It is the pnp device's timeTaken.
                                type: int


            timestamp:
                description:
                - It is the pnp device's timestamp.
                type: int

    systemResetWorkflow:
        description:
        - Device's systemResetWorkflow.
        type: dict
        suboptions:
            _id:
                description:
                - It is the pnp device's _id.
                type: str
            addToInventory:
                description:
                - It is the pnp device's addToInventory.
                type: bool
            addedOn:
                description:
                - It is the pnp device's addedOn.
                type: int
            configId:
                description:
                - It is the pnp device's configId.
                type: str
            currTaskIdx:
                description:
                - It is the pnp device's currTaskIdx.
                type: int
            description:
                description:
                - It is the pnp device's description.
                type: str
            endTime:
                description:
                - It is the pnp device's endTime.
                type: int
            execTime:
                description:
                - It is the pnp device's execTime.
                type: int
            imageId:
                description:
                - It is the pnp device's imageId.
                type: str
            instanceType:
                description:
                - It is the pnp device's instanceType.
                type: str
            lastupdateOn:
                description:
                - It is the pnp device's lastupdateOn.
                type: int
            name:
                description:
                - It is the pnp device's name.
                type: str
            startTime:
                description:
                - It is the pnp device's startTime.
                type: int
            state:
                description:
                - It is the pnp device's state.
                type: str
            tasks:
                description:
                - It is the pnp device's tasks.
                type: list
                elements: dict
                suboptions:
                    currWorkItemIdx:
                        description:
                        - It is the pnp device's currWorkItemIdx.
                        type: int
                    endTime:
                        description:
                        - It is the pnp device's endTime.
                        type: int
                    name:
                        description:
                        - It is the pnp device's name.
                        type: str
                    startTime:
                        description:
                        - It is the pnp device's startTime.
                        type: int
                    state:
                        description:
                        - It is the pnp device's state.
                        type: str
                    taskSeqNo:
                        description:
                        - It is the pnp device's taskSeqNo.
                        type: int
                    timeTaken:
                        description:
                        - It is the pnp device's timeTaken.
                        type: int
                    type:
                        description:
                        - It is the pnp device's type.
                        type: str
                    workItemList:
                        description:
                        - It is the pnp device's workItemList.
                        type: list
                        elements: dict
                        suboptions:
                            command:
                                description:
                                - It is the pnp device's command.
                                type: str
                            endTime:
                                description:
                                - It is the pnp device's endTime.
                                type: int
                            outputStr:
                                description:
                                - It is the pnp device's outputStr.
                                type: str
                            startTime:
                                description:
                                - It is the pnp device's startTime.
                                type: int
                            state:
                                description:
                                - It is the pnp device's state.
                                type: str
                            timeTaken:
                                description:
                                - It is the pnp device's timeTaken.
                                type: int


            tenantId:
                description:
                - It is the pnp device's tenantId.
                type: str
            type:
                description:
                - It is the pnp device's type.
                type: str
            useState:
                description:
                - It is the pnp device's useState.
                type: str
            version:
                description:
                - It is the pnp device's version.
                type: int

    systemWorkflow:
        description:
        - Device's systemWorkflow.
        type: dict
        suboptions:
            _id:
                description:
                - It is the pnp device's _id.
                type: str
            addToInventory:
                description:
                - It is the pnp device's addToInventory.
                type: bool
            addedOn:
                description:
                - It is the pnp device's addedOn.
                type: int
            configId:
                description:
                - It is the pnp device's configId.
                type: str
            currTaskIdx:
                description:
                - It is the pnp device's currTaskIdx.
                type: int
            description:
                description:
                - It is the pnp device's description.
                type: str
            endTime:
                description:
                - It is the pnp device's endTime.
                type: int
            execTime:
                description:
                - It is the pnp device's execTime.
                type: int
            imageId:
                description:
                - It is the pnp device's imageId.
                type: str
            instanceType:
                description:
                - It is the pnp device's instanceType.
                type: str
            lastupdateOn:
                description:
                - It is the pnp device's lastupdateOn.
                type: int
            name:
                description:
                - It is the pnp device's name.
                type: str
            startTime:
                description:
                - It is the pnp device's startTime.
                type: int
            state:
                description:
                - It is the pnp device's state.
                type: str
            tasks:
                description:
                - It is the pnp device's tasks.
                type: list
                elements: dict
                suboptions:
                    currWorkItemIdx:
                        description:
                        - It is the pnp device's currWorkItemIdx.
                        type: int
                    endTime:
                        description:
                        - It is the pnp device's endTime.
                        type: int
                    name:
                        description:
                        - It is the pnp device's name.
                        type: str
                    startTime:
                        description:
                        - It is the pnp device's startTime.
                        type: int
                    state:
                        description:
                        - It is the pnp device's state.
                        type: str
                    taskSeqNo:
                        description:
                        - It is the pnp device's taskSeqNo.
                        type: int
                    timeTaken:
                        description:
                        - It is the pnp device's timeTaken.
                        type: int
                    type:
                        description:
                        - It is the pnp device's type.
                        type: str
                    workItemList:
                        description:
                        - It is the pnp device's workItemList.
                        type: list
                        elements: dict
                        suboptions:
                            command:
                                description:
                                - It is the pnp device's command.
                                type: str
                            endTime:
                                description:
                                - It is the pnp device's endTime.
                                type: int
                            outputStr:
                                description:
                                - It is the pnp device's outputStr.
                                type: str
                            startTime:
                                description:
                                - It is the pnp device's startTime.
                                type: int
                            state:
                                description:
                                - It is the pnp device's state.
                                type: str
                            timeTaken:
                                description:
                                - It is the pnp device's timeTaken.
                                type: int


            tenantId:
                description:
                - It is the pnp device's tenantId.
                type: str
            type:
                description:
                - It is the pnp device's type.
                type: str
            useState:
                description:
                - It is the pnp device's useState.
                type: str
            version:
                description:
                - It is the pnp device's version.
                type: int

    tenantId:
        description:
        - Device's tenantId.
        type: str
    version:
        description:
        - Device's version.
        type: int
    workflow:
        description:
        - Device's workflow.
        type: dict
        suboptions:
            _id:
                description:
                - It is the pnp device's _id.
                type: str
            addToInventory:
                description:
                - It is the pnp device's addToInventory.
                type: bool
            addedOn:
                description:
                - It is the pnp device's addedOn.
                type: int
            configId:
                description:
                - It is the pnp device's configId.
                type: str
            currTaskIdx:
                description:
                - It is the pnp device's currTaskIdx.
                type: int
            description:
                description:
                - It is the pnp device's description.
                type: str
            endTime:
                description:
                - It is the pnp device's endTime.
                type: int
            execTime:
                description:
                - It is the pnp device's execTime.
                type: int
            imageId:
                description:
                - It is the pnp device's imageId.
                type: str
            instanceType:
                description:
                - It is the pnp device's instanceType.
                type: str
            lastupdateOn:
                description:
                - It is the pnp device's lastupdateOn.
                type: int
            name:
                description:
                - It is the pnp device's name.
                type: str
            startTime:
                description:
                - It is the pnp device's startTime.
                type: int
            state:
                description:
                - It is the pnp device's state.
                type: str
            tasks:
                description:
                - It is the pnp device's tasks.
                type: list
                elements: dict
                suboptions:
                    currWorkItemIdx:
                        description:
                        - It is the pnp device's currWorkItemIdx.
                        type: int
                    endTime:
                        description:
                        - It is the pnp device's endTime.
                        type: int
                    name:
                        description:
                        - It is the pnp device's name.
                        type: str
                    startTime:
                        description:
                        - It is the pnp device's startTime.
                        type: int
                    state:
                        description:
                        - It is the pnp device's state.
                        type: str
                    taskSeqNo:
                        description:
                        - It is the pnp device's taskSeqNo.
                        type: int
                    timeTaken:
                        description:
                        - It is the pnp device's timeTaken.
                        type: int
                    type:
                        description:
                        - It is the pnp device's type.
                        type: str
                    workItemList:
                        description:
                        - It is the pnp device's workItemList.
                        type: list
                        elements: dict
                        suboptions:
                            command:
                                description:
                                - It is the pnp device's command.
                                type: str
                            endTime:
                                description:
                                - It is the pnp device's endTime.
                                type: int
                            outputStr:
                                description:
                                - It is the pnp device's outputStr.
                                type: str
                            startTime:
                                description:
                                - It is the pnp device's startTime.
                                type: int
                            state:
                                description:
                                - It is the pnp device's state.
                                type: str
                            timeTaken:
                                description:
                                - It is the pnp device's timeTaken.
                                type: int


            tenantId:
                description:
                - It is the pnp device's tenantId.
                type: str
            type:
                description:
                - It is the pnp device's type.
                type: str
            useState:
                description:
                - It is the pnp device's useState.
                type: str
            version:
                description:
                - It is the pnp device's version.
                type: int

    workflowParameters:
        description:
        - Device's workflowParameters.
        type: dict
        suboptions:
            configList:
                description:
                - It is the pnp device's configList.
                type: list
                elements: dict
                suboptions:
                    configId:
                        description:
                        - It is the pnp device's configId.
                        type: str
                    configParameters:
                        description:
                        - It is the pnp device's configParameters.
                        type: list
                        elements: dict
                        suboptions:
                            key:
                                description:
                                - It is the pnp device's key.
                                type: str
                            value:
                                description:
                                - It is the pnp device's value.
                                type: str


            licenseLevel:
                description:
                - It is the pnp device's licenseLevel.
                type: str
            licenseType:
                description:
                - It is the pnp device's licenseType.
                type: str
            topOfStackSerialNumber:
                description:
                - It is the pnp device's topOfStackSerialNumber.
                type: str

    id:
        description:
        - Id path parameter.
        type: str
        required: True
    count:
        description:
        - If true gets the number of objects.
        type: bool
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.pnp_device
# Reference by Internet resource
- name: PnpDevice reference
  description: Complete reference of the PnpDevice object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpDevice reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns list of devices based on filter crieteria. If a limit is not specified, it will default to return 50 devices. Pagination and sorting are also supported by this endpoint.
    returned: success,changed,always
    type: dict
    contains:
        deviceInfo:
            description: Device Info, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                source:
                    description: It is the pnp device's source.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNumber:
                    description: It is the pnp device's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                stack:
                    description: It is the pnp device's stack.
                    returned: success,changed,always
                    type: bool
                    sample: false
                mode:
                    description: It is the pnp device's mode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                location:
                    description: It is the pnp device's location.
                    returned: success,changed,always
                    type: dict
                    contains:
                        siteId:
                            description: It is the pnp device's siteId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        address:
                            description: It is the pnp device's address.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        latitude:
                            description: It is the pnp device's latitude.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        longitude:
                            description: It is the pnp device's longitude.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        altitude:
                            description: It is the pnp device's altitude.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                onbState:
                    description: It is the pnp device's onbState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authenticatedMicNumber:
                    description: It is the pnp device's authenticatedMicNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authenticatedSudiSerialNo:
                    description: It is the pnp device's authenticatedSudiSerialNo.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                capabilitiesSupported:
                    description: It is the pnp device's capabilitiesSupported.
                    returned: success,changed,always
                    type: list
                featuresSupported:
                    description: It is the pnp device's featuresSupported.
                    returned: success,changed,always
                    type: list
                cmState:
                    description: It is the pnp device's cmState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                firstContact:
                    description: It is the pnp device's firstContact.
                    returned: success,changed,always
                    type: int
                    sample: 0
                lastContact:
                    description: It is the pnp device's lastContact.
                    returned: success,changed,always
                    type: int
                    sample: 0
                macAddress:
                    description: It is the pnp device's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                pid:
                    description: It is the pnp device's pid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceSudiSerialNos:
                    description: It is the pnp device's deviceSudiSerialNos.
                    returned: success,changed,always
                    type: list
                lastUpdateOn:
                    description: It is the pnp device's lastUpdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                workflowId:
                    description: It is the pnp device's workflowId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                workflowName:
                    description: It is the pnp device's workflowName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                projectId:
                    description: It is the pnp device's projectId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                projectName:
                    description: It is the pnp device's projectName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceType:
                    description: It is the pnp device's deviceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                agentType:
                    description: It is the pnp device's agentType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                imageVersion:
                    description: It is the pnp device's imageVersion.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                fileSystemList:
                    description: It is the pnp device's fileSystemList.
                    returned: success,changed,always
                    type: list
                    contains:
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        writeable:
                            description: It is the pnp device's writeable.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        freespace:
                            description: It is the pnp device's freespace.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        readable:
                            description: It is the pnp device's readable.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        size:
                            description: It is the pnp device's size.
                            returned: success,changed,always
                            type: int
                            sample: 0

                pnpProfileList:
                    description: It is the pnp device's pnpProfileList.
                    returned: success,changed,always
                    type: list
                    contains:
                        profileName:
                            description: It is the pnp device's profileName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        discoveryCreated:
                            description: It is the pnp device's discoveryCreated.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        createdBy:
                            description: It is the pnp device's createdBy.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        primaryEndpoint:
                            description: It is the pnp device's primaryEndpoint.
                            returned: success,changed,always
                            type: dict
                            contains:
                                port:
                                    description: It is the pnp device's port.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                protocol:
                                    description: It is the pnp device's protocol.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ipv4Address:
                                    description: It is the pnp device's ipv4Address.
                                    returned: success,changed,always
                                    type: dict
                                ipv6Address:
                                    description: It is the pnp device's ipv6Address.
                                    returned: success,changed,always
                                    type: dict
                                fqdn:
                                    description: It is the pnp device's fqdn.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                certificate:
                                    description: It is the pnp device's certificate.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        secondaryEndpoint:
                            description: It is the pnp device's secondaryEndpoint.
                            returned: success,changed,always
                            type: dict
                            contains:
                                port:
                                    description: It is the pnp device's port.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                protocol:
                                    description: It is the pnp device's protocol.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ipv4Address:
                                    description: It is the pnp device's ipv4Address.
                                    returned: success,changed,always
                                    type: dict
                                ipv6Address:
                                    description: It is the pnp device's ipv6Address.
                                    returned: success,changed,always
                                    type: dict
                                fqdn:
                                    description: It is the pnp device's fqdn.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                certificate:
                                    description: It is the pnp device's certificate.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'


                imageFile:
                    description: It is the pnp device's imageFile.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                httpHeaders:
                    description: It is the pnp device's httpHeaders.
                    returned: success,changed,always
                    type: list
                    contains:
                        key:
                            description: It is the pnp device's key.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        value:
                            description: It is the pnp device's value.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                neighborLinks:
                    description: It is the pnp device's neighborLinks.
                    returned: success,changed,always
                    type: list
                    contains:
                        localInterfaceName:
                            description: It is the pnp device's localInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        localShortInterfaceName:
                            description: It is the pnp device's localShortInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        localMacAddress:
                            description: It is the pnp device's localMacAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteInterfaceName:
                            description: It is the pnp device's remoteInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteShortInterfaceName:
                            description: It is the pnp device's remoteShortInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteMacAddress:
                            description: It is the pnp device's remoteMacAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteDeviceName:
                            description: It is the pnp device's remoteDeviceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remotePlatform:
                            description: It is the pnp device's remotePlatform.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteVersion:
                            description: It is the pnp device's remoteVersion.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                lastSyncTime:
                    description: It is the pnp device's lastSyncTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                ipInterfaces:
                    description: It is the pnp device's ipInterfaces.
                    returned: success,changed,always
                    type: list
                    contains:
                        status:
                            description: It is the pnp device's status.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        macAddress:
                            description: It is the pnp device's macAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        ipv4Address:
                            description: It is the pnp device's ipv4Address.
                            returned: success,changed,always
                            type: dict
                        ipv6AddressList:
                            description: It is the pnp device's ipv6AddressList.
                            returned: success,changed,always
                            type: list
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                hostname:
                    description: It is the pnp device's hostname.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authStatus:
                    description: It is the pnp device's authStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                stackInfo:
                    description: It is the pnp device's stackInfo.
                    returned: success,changed,always
                    type: dict
                    contains:
                        supportsStackWorkflows:
                            description: It is the pnp device's supportsStackWorkflows.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        isFullRing:
                            description: It is the pnp device's isFullRing.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        stackMemberList:
                            description: It is the pnp device's stackMemberList.
                            returned: success,changed,always
                            type: list
                            contains:
                                serialNumber:
                                    description: It is the pnp device's serialNumber.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                role:
                                    description: It is the pnp device's role.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                macAddress:
                                    description: It is the pnp device's macAddress.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                pid:
                                    description: It is the pnp device's pid.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                licenseLevel:
                                    description: It is the pnp device's licenseLevel.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                licenseType:
                                    description: It is the pnp device's licenseType.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                sudiSerialNumber:
                                    description: It is the pnp device's sudiSerialNumber.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                hardwareVersion:
                                    description: It is the pnp device's hardwareVersion.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                stackNumber:
                                    description: It is the pnp device's stackNumber.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                softwareVersion:
                                    description: It is the pnp device's softwareVersion.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                priority:
                                    description: It is the pnp device's priority.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        stackRingProtocol:
                            description: It is the pnp device's stackRingProtocol.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        validLicenseLevels:
                            description: It is the pnp device's validLicenseLevels.
                            returned: success,changed,always
                            type: list
                        totalMemberCount:
                            description: It is the pnp device's totalMemberCount.
                            returned: success,changed,always
                            type: int
                            sample: 0

                reloadRequested:
                    description: It is the pnp device's reloadRequested.
                    returned: success,changed,always
                    type: bool
                    sample: false
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                siteId:
                    description: It is the pnp device's siteId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                aaaCredentials:
                    description: It is the pnp device's aaaCredentials.
                    returned: success,changed,always
                    type: dict
                    contains:
                        password:
                            description: It is the pnp device's password.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        username:
                            description: It is the pnp device's username.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                userMicNumbers:
                    description: It is the pnp device's userMicNumbers.
                    returned: success,changed,always
                    type: list
                userSudiSerialNos:
                    description: It is the pnp device's userSudiSerialNos.
                    returned: success,changed,always
                    type: list
                addnMacAddrs:
                    description: It is the pnp device's addnMacAddrs.
                    returned: success,changed,always
                    type: list
                preWorkflowCliOuputs:
                    description: It is the pnp device's preWorkflowCliOuputs.
                    returned: success,changed,always
                    type: list
                    contains:
                        cli:
                            description: It is the pnp device's cli.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        cliOutput:
                            description: It is the pnp device's cliOutput.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                tags:
                    description: It is the pnp device's tags.
                    returned: success,changed,always
                    type: dict
                sudiRequired:
                    description: It is the pnp device's sudiRequired.
                    returned: success,changed,always
                    type: bool
                    sample: false
                smartAccountId:
                    description: It is the pnp device's smartAccountId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                virtualAccountId:
                    description: It is the pnp device's virtualAccountId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                populateInventory:
                    description: It is the pnp device's populateInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                siteName:
                    description: It is the pnp device's siteName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        systemResetWorkflow:
            description: System Reset Workflow, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                _id:
                    description: It is the pnp device's _id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastupdateOn:
                    description: It is the pnp device's lastupdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                imageId:
                    description: It is the pnp device's imageId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currTaskIdx:
                    description: It is the pnp device's currTaskIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tasks:
                    description: It is the pnp device's tasks.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp device's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currWorkItemIdx:
                            description: It is the pnp device's currWorkItemIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        taskSeqNo:
                            description: It is the pnp device's taskSeqNo.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        endTime:
                            description: It is the pnp device's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                addToInventory:
                    description: It is the pnp device's addToInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                instanceType:
                    description: It is the pnp device's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the pnp device's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                execTime:
                    description: It is the pnp device's execTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp device's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                useState:
                    description: It is the pnp device's useState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configId:
                    description: It is the pnp device's configId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the pnp device's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp device's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        systemWorkflow:
            description: System Workflow, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                _id:
                    description: It is the pnp device's _id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastupdateOn:
                    description: It is the pnp device's lastupdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                imageId:
                    description: It is the pnp device's imageId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currTaskIdx:
                    description: It is the pnp device's currTaskIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tasks:
                    description: It is the pnp device's tasks.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp device's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currWorkItemIdx:
                            description: It is the pnp device's currWorkItemIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        taskSeqNo:
                            description: It is the pnp device's taskSeqNo.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        endTime:
                            description: It is the pnp device's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                addToInventory:
                    description: It is the pnp device's addToInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                instanceType:
                    description: It is the pnp device's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the pnp device's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                execTime:
                    description: It is the pnp device's execTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp device's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                useState:
                    description: It is the pnp device's useState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configId:
                    description: It is the pnp device's configId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the pnp device's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp device's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        workflow:
            description: Workflow, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                _id:
                    description: It is the pnp device's _id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastupdateOn:
                    description: It is the pnp device's lastupdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                imageId:
                    description: It is the pnp device's imageId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currTaskIdx:
                    description: It is the pnp device's currTaskIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tasks:
                    description: It is the pnp device's tasks.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp device's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currWorkItemIdx:
                            description: It is the pnp device's currWorkItemIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        taskSeqNo:
                            description: It is the pnp device's taskSeqNo.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        endTime:
                            description: It is the pnp device's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                addToInventory:
                    description: It is the pnp device's addToInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                instanceType:
                    description: It is the pnp device's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the pnp device's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                execTime:
                    description: It is the pnp device's execTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp device's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                useState:
                    description: It is the pnp device's useState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configId:
                    description: It is the pnp device's configId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the pnp device's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp device's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        runSummaryList:
            description: Run Summary List, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                details:
                    description: It is the pnp device's details.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                historyTaskInfo:
                    description: It is the pnp device's historyTaskInfo.
                    returned: success,changed,always
                    type: dict
                    contains:
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        addnDetails:
                            description: It is the pnp device's addnDetails.
                            returned: success,changed,always
                            type: list
                            contains:
                                key:
                                    description: It is the pnp device's key.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                value:
                                    description: It is the pnp device's value.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                errorFlag:
                    description: It is the pnp device's errorFlag.
                    returned: success,changed,always
                    type: bool
                    sample: false
                timestamp:
                    description: It is the pnp device's timestamp.
                    returned: success,changed,always
                    type: int
                    sample: 0

        workflowParameters:
            description: Workflow Parameters, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                topOfStackSerialNumber:
                    description: It is the pnp device's topOfStackSerialNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                licenseLevel:
                    description: It is the pnp device's licenseLevel.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                licenseType:
                    description: It is the pnp device's licenseType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configList:
                    description: It is the pnp device's configList.
                    returned: success,changed,always
                    type: list
                    contains:
                        configParameters:
                            description: It is the pnp device's configParameters.
                            returned: success,changed,always
                            type: list
                            contains:
                                key:
                                    description: It is the pnp device's key.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                value:
                                    description: It is the pnp device's value.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        configId:
                            description: It is the pnp device's configId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'


        dayZeroConfig:
            description: Day Zero Config, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                config:
                    description: It is the pnp device's config.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        dayZeroConfigPreview:
            description: Day Zero Config Preview, property of the response body.
            returned: success,changed,always
            type: dict
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        tenantId:
            description: Tenant Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Adds a device to the PnP database.
    returned: success,changed,always
    type: dict
    contains:
        _id:
            description: Device's Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        deviceInfo:
            description: Device's Device Info.
            returned: success,changed,always
            type: dict
            contains:
                source:
                    description: It is the pnp device's source.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNumber:
                    description: It is the pnp device's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                stack:
                    description: It is the pnp device's stack.
                    returned: success,changed,always
                    type: bool
                    sample: false
                mode:
                    description: It is the pnp device's mode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                location:
                    description: It is the pnp device's location.
                    returned: success,changed,always
                    type: dict
                    contains:
                        siteId:
                            description: It is the pnp device's siteId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        address:
                            description: It is the pnp device's address.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        latitude:
                            description: It is the pnp device's latitude.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        longitude:
                            description: It is the pnp device's longitude.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        altitude:
                            description: It is the pnp device's altitude.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                onbState:
                    description: It is the pnp device's onbState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authenticatedMicNumber:
                    description: It is the pnp device's authenticatedMicNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authenticatedSudiSerialNo:
                    description: It is the pnp device's authenticatedSudiSerialNo.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                capabilitiesSupported:
                    description: It is the pnp device's capabilitiesSupported.
                    returned: success,changed,always
                    type: list
                featuresSupported:
                    description: It is the pnp device's featuresSupported.
                    returned: success,changed,always
                    type: list
                cmState:
                    description: It is the pnp device's cmState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                firstContact:
                    description: It is the pnp device's firstContact.
                    returned: success,changed,always
                    type: int
                    sample: 0
                lastContact:
                    description: It is the pnp device's lastContact.
                    returned: success,changed,always
                    type: int
                    sample: 0
                macAddress:
                    description: It is the pnp device's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                pid:
                    description: It is the pnp device's pid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceSudiSerialNos:
                    description: It is the pnp device's deviceSudiSerialNos.
                    returned: success,changed,always
                    type: list
                lastUpdateOn:
                    description: It is the pnp device's lastUpdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                workflowId:
                    description: It is the pnp device's workflowId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                workflowName:
                    description: It is the pnp device's workflowName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                projectId:
                    description: It is the pnp device's projectId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                projectName:
                    description: It is the pnp device's projectName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceType:
                    description: It is the pnp device's deviceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                agentType:
                    description: It is the pnp device's agentType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                imageVersion:
                    description: It is the pnp device's imageVersion.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                fileSystemList:
                    description: It is the pnp device's fileSystemList.
                    returned: success,changed,always
                    type: list
                    contains:
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        writeable:
                            description: It is the pnp device's writeable.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        freespace:
                            description: It is the pnp device's freespace.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        readable:
                            description: It is the pnp device's readable.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        size:
                            description: It is the pnp device's size.
                            returned: success,changed,always
                            type: int
                            sample: 0

                pnpProfileList:
                    description: It is the pnp device's pnpProfileList.
                    returned: success,changed,always
                    type: list
                    contains:
                        profileName:
                            description: It is the pnp device's profileName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        discoveryCreated:
                            description: It is the pnp device's discoveryCreated.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        createdBy:
                            description: It is the pnp device's createdBy.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        primaryEndpoint:
                            description: It is the pnp device's primaryEndpoint.
                            returned: success,changed,always
                            type: dict
                            contains:
                                port:
                                    description: It is the pnp device's port.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                protocol:
                                    description: It is the pnp device's protocol.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ipv4Address:
                                    description: It is the pnp device's ipv4Address.
                                    returned: success,changed,always
                                    type: dict
                                ipv6Address:
                                    description: It is the pnp device's ipv6Address.
                                    returned: success,changed,always
                                    type: dict
                                fqdn:
                                    description: It is the pnp device's fqdn.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                certificate:
                                    description: It is the pnp device's certificate.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        secondaryEndpoint:
                            description: It is the pnp device's secondaryEndpoint.
                            returned: success,changed,always
                            type: dict
                            contains:
                                port:
                                    description: It is the pnp device's port.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                protocol:
                                    description: It is the pnp device's protocol.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ipv4Address:
                                    description: It is the pnp device's ipv4Address.
                                    returned: success,changed,always
                                    type: dict
                                ipv6Address:
                                    description: It is the pnp device's ipv6Address.
                                    returned: success,changed,always
                                    type: dict
                                fqdn:
                                    description: It is the pnp device's fqdn.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                certificate:
                                    description: It is the pnp device's certificate.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'


                imageFile:
                    description: It is the pnp device's imageFile.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                httpHeaders:
                    description: It is the pnp device's httpHeaders.
                    returned: success,changed,always
                    type: list
                    contains:
                        key:
                            description: It is the pnp device's key.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        value:
                            description: It is the pnp device's value.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                neighborLinks:
                    description: It is the pnp device's neighborLinks.
                    returned: success,changed,always
                    type: list
                    contains:
                        localInterfaceName:
                            description: It is the pnp device's localInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        localShortInterfaceName:
                            description: It is the pnp device's localShortInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        localMacAddress:
                            description: It is the pnp device's localMacAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteInterfaceName:
                            description: It is the pnp device's remoteInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteShortInterfaceName:
                            description: It is the pnp device's remoteShortInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteMacAddress:
                            description: It is the pnp device's remoteMacAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteDeviceName:
                            description: It is the pnp device's remoteDeviceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remotePlatform:
                            description: It is the pnp device's remotePlatform.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteVersion:
                            description: It is the pnp device's remoteVersion.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                lastSyncTime:
                    description: It is the pnp device's lastSyncTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                ipInterfaces:
                    description: It is the pnp device's ipInterfaces.
                    returned: success,changed,always
                    type: list
                    contains:
                        status:
                            description: It is the pnp device's status.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        macAddress:
                            description: It is the pnp device's macAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        ipv4Address:
                            description: It is the pnp device's ipv4Address.
                            returned: success,changed,always
                            type: dict
                        ipv6AddressList:
                            description: It is the pnp device's ipv6AddressList.
                            returned: success,changed,always
                            type: list
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                hostname:
                    description: It is the pnp device's hostname.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authStatus:
                    description: It is the pnp device's authStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                stackInfo:
                    description: It is the pnp device's stackInfo.
                    returned: success,changed,always
                    type: dict
                    contains:
                        supportsStackWorkflows:
                            description: It is the pnp device's supportsStackWorkflows.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        isFullRing:
                            description: It is the pnp device's isFullRing.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        stackMemberList:
                            description: It is the pnp device's stackMemberList.
                            returned: success,changed,always
                            type: list
                            contains:
                                serialNumber:
                                    description: It is the pnp device's serialNumber.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                role:
                                    description: It is the pnp device's role.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                macAddress:
                                    description: It is the pnp device's macAddress.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                pid:
                                    description: It is the pnp device's pid.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                licenseLevel:
                                    description: It is the pnp device's licenseLevel.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                licenseType:
                                    description: It is the pnp device's licenseType.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                sudiSerialNumber:
                                    description: It is the pnp device's sudiSerialNumber.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                hardwareVersion:
                                    description: It is the pnp device's hardwareVersion.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                stackNumber:
                                    description: It is the pnp device's stackNumber.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                softwareVersion:
                                    description: It is the pnp device's softwareVersion.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                priority:
                                    description: It is the pnp device's priority.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        stackRingProtocol:
                            description: It is the pnp device's stackRingProtocol.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        validLicenseLevels:
                            description: It is the pnp device's validLicenseLevels.
                            returned: success,changed,always
                            type: list
                        totalMemberCount:
                            description: It is the pnp device's totalMemberCount.
                            returned: success,changed,always
                            type: int
                            sample: 0

                reloadRequested:
                    description: It is the pnp device's reloadRequested.
                    returned: success,changed,always
                    type: bool
                    sample: false
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                siteId:
                    description: It is the pnp device's siteId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                aaaCredentials:
                    description: It is the pnp device's aaaCredentials.
                    returned: success,changed,always
                    type: dict
                    contains:
                        password:
                            description: It is the pnp device's password.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        username:
                            description: It is the pnp device's username.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                userMicNumbers:
                    description: It is the pnp device's userMicNumbers.
                    returned: success,changed,always
                    type: list
                userSudiSerialNos:
                    description: It is the pnp device's userSudiSerialNos.
                    returned: success,changed,always
                    type: list
                addnMacAddrs:
                    description: It is the pnp device's addnMacAddrs.
                    returned: success,changed,always
                    type: list
                preWorkflowCliOuputs:
                    description: It is the pnp device's preWorkflowCliOuputs.
                    returned: success,changed,always
                    type: list
                    contains:
                        cli:
                            description: It is the pnp device's cli.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        cliOutput:
                            description: It is the pnp device's cliOutput.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                tags:
                    description: It is the pnp device's tags.
                    returned: success,changed,always
                    type: dict
                sudiRequired:
                    description: It is the pnp device's sudiRequired.
                    returned: success,changed,always
                    type: bool
                    sample: false
                smartAccountId:
                    description: It is the pnp device's smartAccountId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                virtualAccountId:
                    description: It is the pnp device's virtualAccountId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                populateInventory:
                    description: It is the pnp device's populateInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                siteName:
                    description: It is the pnp device's siteName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        systemResetWorkflow:
            description: Device's System Reset Workflow.
            returned: success,changed,always
            type: dict
            contains:
                _id:
                    description: It is the pnp device's _id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastupdateOn:
                    description: It is the pnp device's lastupdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                imageId:
                    description: It is the pnp device's imageId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currTaskIdx:
                    description: It is the pnp device's currTaskIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tasks:
                    description: It is the pnp device's tasks.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp device's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currWorkItemIdx:
                            description: It is the pnp device's currWorkItemIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        taskSeqNo:
                            description: It is the pnp device's taskSeqNo.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        endTime:
                            description: It is the pnp device's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                addToInventory:
                    description: It is the pnp device's addToInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                instanceType:
                    description: It is the pnp device's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the pnp device's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                execTime:
                    description: It is the pnp device's execTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp device's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                useState:
                    description: It is the pnp device's useState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configId:
                    description: It is the pnp device's configId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the pnp device's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp device's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        systemWorkflow:
            description: Device's System Workflow.
            returned: success,changed,always
            type: dict
            contains:
                _id:
                    description: It is the pnp device's _id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastupdateOn:
                    description: It is the pnp device's lastupdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                imageId:
                    description: It is the pnp device's imageId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currTaskIdx:
                    description: It is the pnp device's currTaskIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tasks:
                    description: It is the pnp device's tasks.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp device's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currWorkItemIdx:
                            description: It is the pnp device's currWorkItemIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        taskSeqNo:
                            description: It is the pnp device's taskSeqNo.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        endTime:
                            description: It is the pnp device's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                addToInventory:
                    description: It is the pnp device's addToInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                instanceType:
                    description: It is the pnp device's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the pnp device's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                execTime:
                    description: It is the pnp device's execTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp device's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                useState:
                    description: It is the pnp device's useState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configId:
                    description: It is the pnp device's configId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the pnp device's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp device's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        workflow:
            description: Device's Workflow.
            returned: success,changed,always
            type: dict
            contains:
                _id:
                    description: It is the pnp device's _id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastupdateOn:
                    description: It is the pnp device's lastupdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                imageId:
                    description: It is the pnp device's imageId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currTaskIdx:
                    description: It is the pnp device's currTaskIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tasks:
                    description: It is the pnp device's tasks.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp device's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currWorkItemIdx:
                            description: It is the pnp device's currWorkItemIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        taskSeqNo:
                            description: It is the pnp device's taskSeqNo.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        endTime:
                            description: It is the pnp device's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                addToInventory:
                    description: It is the pnp device's addToInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                instanceType:
                    description: It is the pnp device's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the pnp device's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                execTime:
                    description: It is the pnp device's execTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp device's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                useState:
                    description: It is the pnp device's useState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configId:
                    description: It is the pnp device's configId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the pnp device's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp device's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        runSummaryList:
            description: Device's Run Summary List (list of objects).
            returned: success,changed,always
            type: list
            contains:
                details:
                    description: It is the pnp device's details.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                historyTaskInfo:
                    description: It is the pnp device's historyTaskInfo.
                    returned: success,changed,always
                    type: dict
                    contains:
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        addnDetails:
                            description: It is the pnp device's addnDetails.
                            returned: success,changed,always
                            type: list
                            contains:
                                key:
                                    description: It is the pnp device's key.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                value:
                                    description: It is the pnp device's value.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                errorFlag:
                    description: It is the pnp device's errorFlag.
                    returned: success,changed,always
                    type: bool
                    sample: false
                timestamp:
                    description: It is the pnp device's timestamp.
                    returned: success,changed,always
                    type: int
                    sample: 0

        workflowParameters:
            description: Device's Workflow Parameters.
            returned: success,changed,always
            type: dict
            contains:
                topOfStackSerialNumber:
                    description: It is the pnp device's topOfStackSerialNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                licenseLevel:
                    description: It is the pnp device's licenseLevel.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                licenseType:
                    description: It is the pnp device's licenseType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configList:
                    description: It is the pnp device's configList.
                    returned: success,changed,always
                    type: list
                    contains:
                        configParameters:
                            description: It is the pnp device's configParameters.
                            returned: success,changed,always
                            type: list
                            contains:
                                key:
                                    description: It is the pnp device's key.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                value:
                                    description: It is the pnp device's value.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        configId:
                            description: It is the pnp device's configId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'


        dayZeroConfig:
            description: Device's Day Zero Config.
            returned: success,changed,always
            type: dict
            contains:
                config:
                    description: It is the pnp device's config.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        dayZeroConfigPreview:
            description: Device's Day Zero Config Preview.
            returned: success,changed,always
            type: dict
        version:
            description: Device's version.
            returned: success,changed,always
            type: int
            sample: 0
        tenantId:
            description: Device's Tenant Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_2:
    description: Returns device details specified by device id.
    returned: success,changed,always
    type: dict
    contains:
        _id:
            description: Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        deviceInfo:
            description: Device Info, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                source:
                    description: It is the pnp device's source.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNumber:
                    description: It is the pnp device's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                stack:
                    description: It is the pnp device's stack.
                    returned: success,changed,always
                    type: bool
                    sample: false
                mode:
                    description: It is the pnp device's mode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                location:
                    description: It is the pnp device's location.
                    returned: success,changed,always
                    type: dict
                    contains:
                        siteId:
                            description: It is the pnp device's siteId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        address:
                            description: It is the pnp device's address.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        latitude:
                            description: It is the pnp device's latitude.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        longitude:
                            description: It is the pnp device's longitude.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        altitude:
                            description: It is the pnp device's altitude.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                onbState:
                    description: It is the pnp device's onbState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authenticatedMicNumber:
                    description: It is the pnp device's authenticatedMicNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authenticatedSudiSerialNo:
                    description: It is the pnp device's authenticatedSudiSerialNo.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                capabilitiesSupported:
                    description: It is the pnp device's capabilitiesSupported.
                    returned: success,changed,always
                    type: list
                featuresSupported:
                    description: It is the pnp device's featuresSupported.
                    returned: success,changed,always
                    type: list
                cmState:
                    description: It is the pnp device's cmState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                firstContact:
                    description: It is the pnp device's firstContact.
                    returned: success,changed,always
                    type: int
                    sample: 0
                lastContact:
                    description: It is the pnp device's lastContact.
                    returned: success,changed,always
                    type: int
                    sample: 0
                macAddress:
                    description: It is the pnp device's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                pid:
                    description: It is the pnp device's pid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceSudiSerialNos:
                    description: It is the pnp device's deviceSudiSerialNos.
                    returned: success,changed,always
                    type: list
                lastUpdateOn:
                    description: It is the pnp device's lastUpdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                workflowId:
                    description: It is the pnp device's workflowId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                workflowName:
                    description: It is the pnp device's workflowName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                projectId:
                    description: It is the pnp device's projectId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                projectName:
                    description: It is the pnp device's projectName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceType:
                    description: It is the pnp device's deviceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                agentType:
                    description: It is the pnp device's agentType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                imageVersion:
                    description: It is the pnp device's imageVersion.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                fileSystemList:
                    description: It is the pnp device's fileSystemList.
                    returned: success,changed,always
                    type: list
                    contains:
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        writeable:
                            description: It is the pnp device's writeable.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        freespace:
                            description: It is the pnp device's freespace.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        readable:
                            description: It is the pnp device's readable.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        size:
                            description: It is the pnp device's size.
                            returned: success,changed,always
                            type: int
                            sample: 0

                pnpProfileList:
                    description: It is the pnp device's pnpProfileList.
                    returned: success,changed,always
                    type: list
                    contains:
                        profileName:
                            description: It is the pnp device's profileName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        discoveryCreated:
                            description: It is the pnp device's discoveryCreated.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        createdBy:
                            description: It is the pnp device's createdBy.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        primaryEndpoint:
                            description: It is the pnp device's primaryEndpoint.
                            returned: success,changed,always
                            type: dict
                            contains:
                                port:
                                    description: It is the pnp device's port.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                protocol:
                                    description: It is the pnp device's protocol.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ipv4Address:
                                    description: It is the pnp device's ipv4Address.
                                    returned: success,changed,always
                                    type: dict
                                ipv6Address:
                                    description: It is the pnp device's ipv6Address.
                                    returned: success,changed,always
                                    type: dict
                                fqdn:
                                    description: It is the pnp device's fqdn.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                certificate:
                                    description: It is the pnp device's certificate.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        secondaryEndpoint:
                            description: It is the pnp device's secondaryEndpoint.
                            returned: success,changed,always
                            type: dict
                            contains:
                                port:
                                    description: It is the pnp device's port.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                protocol:
                                    description: It is the pnp device's protocol.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ipv4Address:
                                    description: It is the pnp device's ipv4Address.
                                    returned: success,changed,always
                                    type: dict
                                ipv6Address:
                                    description: It is the pnp device's ipv6Address.
                                    returned: success,changed,always
                                    type: dict
                                fqdn:
                                    description: It is the pnp device's fqdn.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                certificate:
                                    description: It is the pnp device's certificate.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'


                imageFile:
                    description: It is the pnp device's imageFile.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                httpHeaders:
                    description: It is the pnp device's httpHeaders.
                    returned: success,changed,always
                    type: list
                    contains:
                        key:
                            description: It is the pnp device's key.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        value:
                            description: It is the pnp device's value.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                neighborLinks:
                    description: It is the pnp device's neighborLinks.
                    returned: success,changed,always
                    type: list
                    contains:
                        localInterfaceName:
                            description: It is the pnp device's localInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        localShortInterfaceName:
                            description: It is the pnp device's localShortInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        localMacAddress:
                            description: It is the pnp device's localMacAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteInterfaceName:
                            description: It is the pnp device's remoteInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteShortInterfaceName:
                            description: It is the pnp device's remoteShortInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteMacAddress:
                            description: It is the pnp device's remoteMacAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteDeviceName:
                            description: It is the pnp device's remoteDeviceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remotePlatform:
                            description: It is the pnp device's remotePlatform.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteVersion:
                            description: It is the pnp device's remoteVersion.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                lastSyncTime:
                    description: It is the pnp device's lastSyncTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                ipInterfaces:
                    description: It is the pnp device's ipInterfaces.
                    returned: success,changed,always
                    type: list
                    contains:
                        status:
                            description: It is the pnp device's status.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        macAddress:
                            description: It is the pnp device's macAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        ipv4Address:
                            description: It is the pnp device's ipv4Address.
                            returned: success,changed,always
                            type: dict
                        ipv6AddressList:
                            description: It is the pnp device's ipv6AddressList.
                            returned: success,changed,always
                            type: list
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                hostname:
                    description: It is the pnp device's hostname.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authStatus:
                    description: It is the pnp device's authStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                stackInfo:
                    description: It is the pnp device's stackInfo.
                    returned: success,changed,always
                    type: dict
                    contains:
                        supportsStackWorkflows:
                            description: It is the pnp device's supportsStackWorkflows.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        isFullRing:
                            description: It is the pnp device's isFullRing.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        stackMemberList:
                            description: It is the pnp device's stackMemberList.
                            returned: success,changed,always
                            type: list
                            contains:
                                serialNumber:
                                    description: It is the pnp device's serialNumber.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                role:
                                    description: It is the pnp device's role.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                macAddress:
                                    description: It is the pnp device's macAddress.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                pid:
                                    description: It is the pnp device's pid.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                licenseLevel:
                                    description: It is the pnp device's licenseLevel.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                licenseType:
                                    description: It is the pnp device's licenseType.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                sudiSerialNumber:
                                    description: It is the pnp device's sudiSerialNumber.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                hardwareVersion:
                                    description: It is the pnp device's hardwareVersion.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                stackNumber:
                                    description: It is the pnp device's stackNumber.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                softwareVersion:
                                    description: It is the pnp device's softwareVersion.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                priority:
                                    description: It is the pnp device's priority.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        stackRingProtocol:
                            description: It is the pnp device's stackRingProtocol.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        validLicenseLevels:
                            description: It is the pnp device's validLicenseLevels.
                            returned: success,changed,always
                            type: list
                        totalMemberCount:
                            description: It is the pnp device's totalMemberCount.
                            returned: success,changed,always
                            type: int
                            sample: 0

                reloadRequested:
                    description: It is the pnp device's reloadRequested.
                    returned: success,changed,always
                    type: bool
                    sample: false
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                siteId:
                    description: It is the pnp device's siteId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                aaaCredentials:
                    description: It is the pnp device's aaaCredentials.
                    returned: success,changed,always
                    type: dict
                    contains:
                        password:
                            description: It is the pnp device's password.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        username:
                            description: It is the pnp device's username.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                userMicNumbers:
                    description: It is the pnp device's userMicNumbers.
                    returned: success,changed,always
                    type: list
                userSudiSerialNos:
                    description: It is the pnp device's userSudiSerialNos.
                    returned: success,changed,always
                    type: list
                addnMacAddrs:
                    description: It is the pnp device's addnMacAddrs.
                    returned: success,changed,always
                    type: list
                preWorkflowCliOuputs:
                    description: It is the pnp device's preWorkflowCliOuputs.
                    returned: success,changed,always
                    type: list
                    contains:
                        cli:
                            description: It is the pnp device's cli.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        cliOutput:
                            description: It is the pnp device's cliOutput.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                tags:
                    description: It is the pnp device's tags.
                    returned: success,changed,always
                    type: dict
                sudiRequired:
                    description: It is the pnp device's sudiRequired.
                    returned: success,changed,always
                    type: bool
                    sample: false
                smartAccountId:
                    description: It is the pnp device's smartAccountId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                virtualAccountId:
                    description: It is the pnp device's virtualAccountId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                populateInventory:
                    description: It is the pnp device's populateInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                siteName:
                    description: It is the pnp device's siteName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        systemResetWorkflow:
            description: System Reset Workflow, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                _id:
                    description: It is the pnp device's _id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastupdateOn:
                    description: It is the pnp device's lastupdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                imageId:
                    description: It is the pnp device's imageId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currTaskIdx:
                    description: It is the pnp device's currTaskIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tasks:
                    description: It is the pnp device's tasks.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp device's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currWorkItemIdx:
                            description: It is the pnp device's currWorkItemIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        taskSeqNo:
                            description: It is the pnp device's taskSeqNo.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        endTime:
                            description: It is the pnp device's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                addToInventory:
                    description: It is the pnp device's addToInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                instanceType:
                    description: It is the pnp device's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the pnp device's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                execTime:
                    description: It is the pnp device's execTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp device's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                useState:
                    description: It is the pnp device's useState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configId:
                    description: It is the pnp device's configId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the pnp device's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp device's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        systemWorkflow:
            description: System Workflow, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                _id:
                    description: It is the pnp device's _id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastupdateOn:
                    description: It is the pnp device's lastupdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                imageId:
                    description: It is the pnp device's imageId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currTaskIdx:
                    description: It is the pnp device's currTaskIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tasks:
                    description: It is the pnp device's tasks.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp device's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currWorkItemIdx:
                            description: It is the pnp device's currWorkItemIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        taskSeqNo:
                            description: It is the pnp device's taskSeqNo.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        endTime:
                            description: It is the pnp device's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                addToInventory:
                    description: It is the pnp device's addToInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                instanceType:
                    description: It is the pnp device's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the pnp device's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                execTime:
                    description: It is the pnp device's execTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp device's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                useState:
                    description: It is the pnp device's useState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configId:
                    description: It is the pnp device's configId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the pnp device's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp device's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        workflow:
            description: Workflow, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                _id:
                    description: It is the pnp device's _id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastupdateOn:
                    description: It is the pnp device's lastupdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                imageId:
                    description: It is the pnp device's imageId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currTaskIdx:
                    description: It is the pnp device's currTaskIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tasks:
                    description: It is the pnp device's tasks.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp device's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currWorkItemIdx:
                            description: It is the pnp device's currWorkItemIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        taskSeqNo:
                            description: It is the pnp device's taskSeqNo.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        endTime:
                            description: It is the pnp device's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                addToInventory:
                    description: It is the pnp device's addToInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                instanceType:
                    description: It is the pnp device's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the pnp device's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                execTime:
                    description: It is the pnp device's execTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp device's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                useState:
                    description: It is the pnp device's useState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configId:
                    description: It is the pnp device's configId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the pnp device's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp device's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        runSummaryList:
            description: Run Summary List, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                details:
                    description: It is the pnp device's details.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                historyTaskInfo:
                    description: It is the pnp device's historyTaskInfo.
                    returned: success,changed,always
                    type: dict
                    contains:
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        addnDetails:
                            description: It is the pnp device's addnDetails.
                            returned: success,changed,always
                            type: list
                            contains:
                                key:
                                    description: It is the pnp device's key.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                value:
                                    description: It is the pnp device's value.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                errorFlag:
                    description: It is the pnp device's errorFlag.
                    returned: success,changed,always
                    type: bool
                    sample: false
                timestamp:
                    description: It is the pnp device's timestamp.
                    returned: success,changed,always
                    type: int
                    sample: 0

        workflowParameters:
            description: Workflow Parameters, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                topOfStackSerialNumber:
                    description: It is the pnp device's topOfStackSerialNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                licenseLevel:
                    description: It is the pnp device's licenseLevel.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                licenseType:
                    description: It is the pnp device's licenseType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configList:
                    description: It is the pnp device's configList.
                    returned: success,changed,always
                    type: list
                    contains:
                        configParameters:
                            description: It is the pnp device's configParameters.
                            returned: success,changed,always
                            type: list
                            contains:
                                key:
                                    description: It is the pnp device's key.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                value:
                                    description: It is the pnp device's value.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        configId:
                            description: It is the pnp device's configId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'


        dayZeroConfig:
            description: Day Zero Config, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                config:
                    description: It is the pnp device's config.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        dayZeroConfigPreview:
            description: Day Zero Config Preview, property of the response body.
            returned: success,changed,always
            type: dict
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        tenantId:
            description: Tenant Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_3:
    description: Deletes specified device from PnP database.
    returned: success,changed,always
    type: dict
    contains:
        _id:
            description: Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        deviceInfo:
            description: Device Info, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                source:
                    description: It is the pnp device's source.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNumber:
                    description: It is the pnp device's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                stack:
                    description: It is the pnp device's stack.
                    returned: success,changed,always
                    type: bool
                    sample: false
                mode:
                    description: It is the pnp device's mode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                location:
                    description: It is the pnp device's location.
                    returned: success,changed,always
                    type: dict
                    contains:
                        siteId:
                            description: It is the pnp device's siteId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        address:
                            description: It is the pnp device's address.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        latitude:
                            description: It is the pnp device's latitude.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        longitude:
                            description: It is the pnp device's longitude.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        altitude:
                            description: It is the pnp device's altitude.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                onbState:
                    description: It is the pnp device's onbState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authenticatedMicNumber:
                    description: It is the pnp device's authenticatedMicNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authenticatedSudiSerialNo:
                    description: It is the pnp device's authenticatedSudiSerialNo.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                capabilitiesSupported:
                    description: It is the pnp device's capabilitiesSupported.
                    returned: success,changed,always
                    type: list
                featuresSupported:
                    description: It is the pnp device's featuresSupported.
                    returned: success,changed,always
                    type: list
                cmState:
                    description: It is the pnp device's cmState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                firstContact:
                    description: It is the pnp device's firstContact.
                    returned: success,changed,always
                    type: int
                    sample: 0
                lastContact:
                    description: It is the pnp device's lastContact.
                    returned: success,changed,always
                    type: int
                    sample: 0
                macAddress:
                    description: It is the pnp device's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                pid:
                    description: It is the pnp device's pid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceSudiSerialNos:
                    description: It is the pnp device's deviceSudiSerialNos.
                    returned: success,changed,always
                    type: list
                lastUpdateOn:
                    description: It is the pnp device's lastUpdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                workflowId:
                    description: It is the pnp device's workflowId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                workflowName:
                    description: It is the pnp device's workflowName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                projectId:
                    description: It is the pnp device's projectId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                projectName:
                    description: It is the pnp device's projectName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceType:
                    description: It is the pnp device's deviceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                agentType:
                    description: It is the pnp device's agentType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                imageVersion:
                    description: It is the pnp device's imageVersion.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                fileSystemList:
                    description: It is the pnp device's fileSystemList.
                    returned: success,changed,always
                    type: list
                    contains:
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        writeable:
                            description: It is the pnp device's writeable.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        freespace:
                            description: It is the pnp device's freespace.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        readable:
                            description: It is the pnp device's readable.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        size:
                            description: It is the pnp device's size.
                            returned: success,changed,always
                            type: int
                            sample: 0

                pnpProfileList:
                    description: It is the pnp device's pnpProfileList.
                    returned: success,changed,always
                    type: list
                    contains:
                        profileName:
                            description: It is the pnp device's profileName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        discoveryCreated:
                            description: It is the pnp device's discoveryCreated.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        createdBy:
                            description: It is the pnp device's createdBy.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        primaryEndpoint:
                            description: It is the pnp device's primaryEndpoint.
                            returned: success,changed,always
                            type: dict
                            contains:
                                port:
                                    description: It is the pnp device's port.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                protocol:
                                    description: It is the pnp device's protocol.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ipv4Address:
                                    description: It is the pnp device's ipv4Address.
                                    returned: success,changed,always
                                    type: dict
                                ipv6Address:
                                    description: It is the pnp device's ipv6Address.
                                    returned: success,changed,always
                                    type: dict
                                fqdn:
                                    description: It is the pnp device's fqdn.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                certificate:
                                    description: It is the pnp device's certificate.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        secondaryEndpoint:
                            description: It is the pnp device's secondaryEndpoint.
                            returned: success,changed,always
                            type: dict
                            contains:
                                port:
                                    description: It is the pnp device's port.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                protocol:
                                    description: It is the pnp device's protocol.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ipv4Address:
                                    description: It is the pnp device's ipv4Address.
                                    returned: success,changed,always
                                    type: dict
                                ipv6Address:
                                    description: It is the pnp device's ipv6Address.
                                    returned: success,changed,always
                                    type: dict
                                fqdn:
                                    description: It is the pnp device's fqdn.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                certificate:
                                    description: It is the pnp device's certificate.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'


                imageFile:
                    description: It is the pnp device's imageFile.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                httpHeaders:
                    description: It is the pnp device's httpHeaders.
                    returned: success,changed,always
                    type: list
                    contains:
                        key:
                            description: It is the pnp device's key.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        value:
                            description: It is the pnp device's value.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                neighborLinks:
                    description: It is the pnp device's neighborLinks.
                    returned: success,changed,always
                    type: list
                    contains:
                        localInterfaceName:
                            description: It is the pnp device's localInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        localShortInterfaceName:
                            description: It is the pnp device's localShortInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        localMacAddress:
                            description: It is the pnp device's localMacAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteInterfaceName:
                            description: It is the pnp device's remoteInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteShortInterfaceName:
                            description: It is the pnp device's remoteShortInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteMacAddress:
                            description: It is the pnp device's remoteMacAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteDeviceName:
                            description: It is the pnp device's remoteDeviceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remotePlatform:
                            description: It is the pnp device's remotePlatform.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteVersion:
                            description: It is the pnp device's remoteVersion.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                lastSyncTime:
                    description: It is the pnp device's lastSyncTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                ipInterfaces:
                    description: It is the pnp device's ipInterfaces.
                    returned: success,changed,always
                    type: list
                    contains:
                        status:
                            description: It is the pnp device's status.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        macAddress:
                            description: It is the pnp device's macAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        ipv4Address:
                            description: It is the pnp device's ipv4Address.
                            returned: success,changed,always
                            type: dict
                        ipv6AddressList:
                            description: It is the pnp device's ipv6AddressList.
                            returned: success,changed,always
                            type: list
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                hostname:
                    description: It is the pnp device's hostname.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authStatus:
                    description: It is the pnp device's authStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                stackInfo:
                    description: It is the pnp device's stackInfo.
                    returned: success,changed,always
                    type: dict
                    contains:
                        supportsStackWorkflows:
                            description: It is the pnp device's supportsStackWorkflows.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        isFullRing:
                            description: It is the pnp device's isFullRing.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        stackMemberList:
                            description: It is the pnp device's stackMemberList.
                            returned: success,changed,always
                            type: list
                            contains:
                                serialNumber:
                                    description: It is the pnp device's serialNumber.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                role:
                                    description: It is the pnp device's role.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                macAddress:
                                    description: It is the pnp device's macAddress.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                pid:
                                    description: It is the pnp device's pid.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                licenseLevel:
                                    description: It is the pnp device's licenseLevel.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                licenseType:
                                    description: It is the pnp device's licenseType.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                sudiSerialNumber:
                                    description: It is the pnp device's sudiSerialNumber.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                hardwareVersion:
                                    description: It is the pnp device's hardwareVersion.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                stackNumber:
                                    description: It is the pnp device's stackNumber.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                softwareVersion:
                                    description: It is the pnp device's softwareVersion.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                priority:
                                    description: It is the pnp device's priority.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        stackRingProtocol:
                            description: It is the pnp device's stackRingProtocol.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        validLicenseLevels:
                            description: It is the pnp device's validLicenseLevels.
                            returned: success,changed,always
                            type: list
                        totalMemberCount:
                            description: It is the pnp device's totalMemberCount.
                            returned: success,changed,always
                            type: int
                            sample: 0

                reloadRequested:
                    description: It is the pnp device's reloadRequested.
                    returned: success,changed,always
                    type: bool
                    sample: false
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                siteId:
                    description: It is the pnp device's siteId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                aaaCredentials:
                    description: It is the pnp device's aaaCredentials.
                    returned: success,changed,always
                    type: dict
                    contains:
                        password:
                            description: It is the pnp device's password.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        username:
                            description: It is the pnp device's username.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                userMicNumbers:
                    description: It is the pnp device's userMicNumbers.
                    returned: success,changed,always
                    type: list
                userSudiSerialNos:
                    description: It is the pnp device's userSudiSerialNos.
                    returned: success,changed,always
                    type: list
                addnMacAddrs:
                    description: It is the pnp device's addnMacAddrs.
                    returned: success,changed,always
                    type: list
                preWorkflowCliOuputs:
                    description: It is the pnp device's preWorkflowCliOuputs.
                    returned: success,changed,always
                    type: list
                    contains:
                        cli:
                            description: It is the pnp device's cli.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        cliOutput:
                            description: It is the pnp device's cliOutput.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                tags:
                    description: It is the pnp device's tags.
                    returned: success,changed,always
                    type: dict
                sudiRequired:
                    description: It is the pnp device's sudiRequired.
                    returned: success,changed,always
                    type: bool
                    sample: false
                smartAccountId:
                    description: It is the pnp device's smartAccountId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                virtualAccountId:
                    description: It is the pnp device's virtualAccountId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                populateInventory:
                    description: It is the pnp device's populateInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                siteName:
                    description: It is the pnp device's siteName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        systemResetWorkflow:
            description: System Reset Workflow, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                _id:
                    description: It is the pnp device's _id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastupdateOn:
                    description: It is the pnp device's lastupdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                imageId:
                    description: It is the pnp device's imageId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currTaskIdx:
                    description: It is the pnp device's currTaskIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tasks:
                    description: It is the pnp device's tasks.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp device's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currWorkItemIdx:
                            description: It is the pnp device's currWorkItemIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        taskSeqNo:
                            description: It is the pnp device's taskSeqNo.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        endTime:
                            description: It is the pnp device's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                addToInventory:
                    description: It is the pnp device's addToInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                instanceType:
                    description: It is the pnp device's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the pnp device's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                execTime:
                    description: It is the pnp device's execTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp device's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                useState:
                    description: It is the pnp device's useState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configId:
                    description: It is the pnp device's configId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the pnp device's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp device's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        systemWorkflow:
            description: System Workflow, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                _id:
                    description: It is the pnp device's _id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastupdateOn:
                    description: It is the pnp device's lastupdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                imageId:
                    description: It is the pnp device's imageId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currTaskIdx:
                    description: It is the pnp device's currTaskIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tasks:
                    description: It is the pnp device's tasks.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp device's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currWorkItemIdx:
                            description: It is the pnp device's currWorkItemIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        taskSeqNo:
                            description: It is the pnp device's taskSeqNo.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        endTime:
                            description: It is the pnp device's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                addToInventory:
                    description: It is the pnp device's addToInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                instanceType:
                    description: It is the pnp device's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the pnp device's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                execTime:
                    description: It is the pnp device's execTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp device's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                useState:
                    description: It is the pnp device's useState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configId:
                    description: It is the pnp device's configId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the pnp device's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp device's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        workflow:
            description: Workflow, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                _id:
                    description: It is the pnp device's _id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastupdateOn:
                    description: It is the pnp device's lastupdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                imageId:
                    description: It is the pnp device's imageId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currTaskIdx:
                    description: It is the pnp device's currTaskIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tasks:
                    description: It is the pnp device's tasks.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp device's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currWorkItemIdx:
                            description: It is the pnp device's currWorkItemIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        taskSeqNo:
                            description: It is the pnp device's taskSeqNo.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        endTime:
                            description: It is the pnp device's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                addToInventory:
                    description: It is the pnp device's addToInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                instanceType:
                    description: It is the pnp device's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the pnp device's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                execTime:
                    description: It is the pnp device's execTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp device's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                useState:
                    description: It is the pnp device's useState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configId:
                    description: It is the pnp device's configId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the pnp device's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp device's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        runSummaryList:
            description: Run Summary List, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                details:
                    description: It is the pnp device's details.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                historyTaskInfo:
                    description: It is the pnp device's historyTaskInfo.
                    returned: success,changed,always
                    type: dict
                    contains:
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        addnDetails:
                            description: It is the pnp device's addnDetails.
                            returned: success,changed,always
                            type: list
                            contains:
                                key:
                                    description: It is the pnp device's key.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                value:
                                    description: It is the pnp device's value.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                errorFlag:
                    description: It is the pnp device's errorFlag.
                    returned: success,changed,always
                    type: bool
                    sample: false
                timestamp:
                    description: It is the pnp device's timestamp.
                    returned: success,changed,always
                    type: int
                    sample: 0

        workflowParameters:
            description: Workflow Parameters, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                topOfStackSerialNumber:
                    description: It is the pnp device's topOfStackSerialNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                licenseLevel:
                    description: It is the pnp device's licenseLevel.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                licenseType:
                    description: It is the pnp device's licenseType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configList:
                    description: It is the pnp device's configList.
                    returned: success,changed,always
                    type: list
                    contains:
                        configParameters:
                            description: It is the pnp device's configParameters.
                            returned: success,changed,always
                            type: list
                            contains:
                                key:
                                    description: It is the pnp device's key.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                value:
                                    description: It is the pnp device's value.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        configId:
                            description: It is the pnp device's configId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'


        dayZeroConfig:
            description: Day Zero Config, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                config:
                    description: It is the pnp device's config.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        dayZeroConfigPreview:
            description: Day Zero Config Preview, property of the response body.
            returned: success,changed,always
            type: dict
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        tenantId:
            description: Tenant Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_4:
    description: Updates device details specified by device id in PnP database.
    returned: success,changed,always
    type: dict
    contains:
        _id:
            description: Device's Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        deviceInfo:
            description: Device's Device Info.
            returned: success,changed,always
            type: dict
            contains:
                source:
                    description: It is the pnp device's source.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNumber:
                    description: It is the pnp device's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                stack:
                    description: It is the pnp device's stack.
                    returned: success,changed,always
                    type: bool
                    sample: false
                mode:
                    description: It is the pnp device's mode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                location:
                    description: It is the pnp device's location.
                    returned: success,changed,always
                    type: dict
                    contains:
                        siteId:
                            description: It is the pnp device's siteId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        address:
                            description: It is the pnp device's address.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        latitude:
                            description: It is the pnp device's latitude.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        longitude:
                            description: It is the pnp device's longitude.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        altitude:
                            description: It is the pnp device's altitude.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                onbState:
                    description: It is the pnp device's onbState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authenticatedMicNumber:
                    description: It is the pnp device's authenticatedMicNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authenticatedSudiSerialNo:
                    description: It is the pnp device's authenticatedSudiSerialNo.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                capabilitiesSupported:
                    description: It is the pnp device's capabilitiesSupported.
                    returned: success,changed,always
                    type: list
                featuresSupported:
                    description: It is the pnp device's featuresSupported.
                    returned: success,changed,always
                    type: list
                cmState:
                    description: It is the pnp device's cmState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                firstContact:
                    description: It is the pnp device's firstContact.
                    returned: success,changed,always
                    type: int
                    sample: 0
                lastContact:
                    description: It is the pnp device's lastContact.
                    returned: success,changed,always
                    type: int
                    sample: 0
                macAddress:
                    description: It is the pnp device's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                pid:
                    description: It is the pnp device's pid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceSudiSerialNos:
                    description: It is the pnp device's deviceSudiSerialNos.
                    returned: success,changed,always
                    type: list
                lastUpdateOn:
                    description: It is the pnp device's lastUpdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                workflowId:
                    description: It is the pnp device's workflowId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                workflowName:
                    description: It is the pnp device's workflowName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                projectId:
                    description: It is the pnp device's projectId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                projectName:
                    description: It is the pnp device's projectName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceType:
                    description: It is the pnp device's deviceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                agentType:
                    description: It is the pnp device's agentType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                imageVersion:
                    description: It is the pnp device's imageVersion.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                fileSystemList:
                    description: It is the pnp device's fileSystemList.
                    returned: success,changed,always
                    type: list
                    contains:
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        writeable:
                            description: It is the pnp device's writeable.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        freespace:
                            description: It is the pnp device's freespace.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        readable:
                            description: It is the pnp device's readable.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        size:
                            description: It is the pnp device's size.
                            returned: success,changed,always
                            type: int
                            sample: 0

                pnpProfileList:
                    description: It is the pnp device's pnpProfileList.
                    returned: success,changed,always
                    type: list
                    contains:
                        profileName:
                            description: It is the pnp device's profileName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        discoveryCreated:
                            description: It is the pnp device's discoveryCreated.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        createdBy:
                            description: It is the pnp device's createdBy.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        primaryEndpoint:
                            description: It is the pnp device's primaryEndpoint.
                            returned: success,changed,always
                            type: dict
                            contains:
                                port:
                                    description: It is the pnp device's port.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                protocol:
                                    description: It is the pnp device's protocol.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ipv4Address:
                                    description: It is the pnp device's ipv4Address.
                                    returned: success,changed,always
                                    type: dict
                                ipv6Address:
                                    description: It is the pnp device's ipv6Address.
                                    returned: success,changed,always
                                    type: dict
                                fqdn:
                                    description: It is the pnp device's fqdn.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                certificate:
                                    description: It is the pnp device's certificate.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        secondaryEndpoint:
                            description: It is the pnp device's secondaryEndpoint.
                            returned: success,changed,always
                            type: dict
                            contains:
                                port:
                                    description: It is the pnp device's port.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                protocol:
                                    description: It is the pnp device's protocol.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ipv4Address:
                                    description: It is the pnp device's ipv4Address.
                                    returned: success,changed,always
                                    type: dict
                                ipv6Address:
                                    description: It is the pnp device's ipv6Address.
                                    returned: success,changed,always
                                    type: dict
                                fqdn:
                                    description: It is the pnp device's fqdn.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                certificate:
                                    description: It is the pnp device's certificate.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'


                imageFile:
                    description: It is the pnp device's imageFile.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                httpHeaders:
                    description: It is the pnp device's httpHeaders.
                    returned: success,changed,always
                    type: list
                    contains:
                        key:
                            description: It is the pnp device's key.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        value:
                            description: It is the pnp device's value.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                neighborLinks:
                    description: It is the pnp device's neighborLinks.
                    returned: success,changed,always
                    type: list
                    contains:
                        localInterfaceName:
                            description: It is the pnp device's localInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        localShortInterfaceName:
                            description: It is the pnp device's localShortInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        localMacAddress:
                            description: It is the pnp device's localMacAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteInterfaceName:
                            description: It is the pnp device's remoteInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteShortInterfaceName:
                            description: It is the pnp device's remoteShortInterfaceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteMacAddress:
                            description: It is the pnp device's remoteMacAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteDeviceName:
                            description: It is the pnp device's remoteDeviceName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remotePlatform:
                            description: It is the pnp device's remotePlatform.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        remoteVersion:
                            description: It is the pnp device's remoteVersion.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                lastSyncTime:
                    description: It is the pnp device's lastSyncTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                ipInterfaces:
                    description: It is the pnp device's ipInterfaces.
                    returned: success,changed,always
                    type: list
                    contains:
                        status:
                            description: It is the pnp device's status.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        macAddress:
                            description: It is the pnp device's macAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        ipv4Address:
                            description: It is the pnp device's ipv4Address.
                            returned: success,changed,always
                            type: dict
                        ipv6AddressList:
                            description: It is the pnp device's ipv6AddressList.
                            returned: success,changed,always
                            type: list
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                hostname:
                    description: It is the pnp device's hostname.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                authStatus:
                    description: It is the pnp device's authStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                stackInfo:
                    description: It is the pnp device's stackInfo.
                    returned: success,changed,always
                    type: dict
                    contains:
                        supportsStackWorkflows:
                            description: It is the pnp device's supportsStackWorkflows.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        isFullRing:
                            description: It is the pnp device's isFullRing.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        stackMemberList:
                            description: It is the pnp device's stackMemberList.
                            returned: success,changed,always
                            type: list
                            contains:
                                serialNumber:
                                    description: It is the pnp device's serialNumber.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                role:
                                    description: It is the pnp device's role.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                macAddress:
                                    description: It is the pnp device's macAddress.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                pid:
                                    description: It is the pnp device's pid.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                licenseLevel:
                                    description: It is the pnp device's licenseLevel.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                licenseType:
                                    description: It is the pnp device's licenseType.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                sudiSerialNumber:
                                    description: It is the pnp device's sudiSerialNumber.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                hardwareVersion:
                                    description: It is the pnp device's hardwareVersion.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                stackNumber:
                                    description: It is the pnp device's stackNumber.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                softwareVersion:
                                    description: It is the pnp device's softwareVersion.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                priority:
                                    description: It is the pnp device's priority.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        stackRingProtocol:
                            description: It is the pnp device's stackRingProtocol.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        validLicenseLevels:
                            description: It is the pnp device's validLicenseLevels.
                            returned: success,changed,always
                            type: list
                        totalMemberCount:
                            description: It is the pnp device's totalMemberCount.
                            returned: success,changed,always
                            type: int
                            sample: 0

                reloadRequested:
                    description: It is the pnp device's reloadRequested.
                    returned: success,changed,always
                    type: bool
                    sample: false
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                siteId:
                    description: It is the pnp device's siteId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                aaaCredentials:
                    description: It is the pnp device's aaaCredentials.
                    returned: success,changed,always
                    type: dict
                    contains:
                        password:
                            description: It is the pnp device's password.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        username:
                            description: It is the pnp device's username.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                userMicNumbers:
                    description: It is the pnp device's userMicNumbers.
                    returned: success,changed,always
                    type: list
                userSudiSerialNos:
                    description: It is the pnp device's userSudiSerialNos.
                    returned: success,changed,always
                    type: list
                addnMacAddrs:
                    description: It is the pnp device's addnMacAddrs.
                    returned: success,changed,always
                    type: list
                preWorkflowCliOuputs:
                    description: It is the pnp device's preWorkflowCliOuputs.
                    returned: success,changed,always
                    type: list
                    contains:
                        cli:
                            description: It is the pnp device's cli.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        cliOutput:
                            description: It is the pnp device's cliOutput.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                tags:
                    description: It is the pnp device's tags.
                    returned: success,changed,always
                    type: dict
                sudiRequired:
                    description: It is the pnp device's sudiRequired.
                    returned: success,changed,always
                    type: bool
                    sample: false
                smartAccountId:
                    description: It is the pnp device's smartAccountId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                virtualAccountId:
                    description: It is the pnp device's virtualAccountId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                populateInventory:
                    description: It is the pnp device's populateInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                siteName:
                    description: It is the pnp device's siteName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        systemResetWorkflow:
            description: Device's System Reset Workflow.
            returned: success,changed,always
            type: dict
            contains:
                _id:
                    description: It is the pnp device's _id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastupdateOn:
                    description: It is the pnp device's lastupdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                imageId:
                    description: It is the pnp device's imageId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currTaskIdx:
                    description: It is the pnp device's currTaskIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tasks:
                    description: It is the pnp device's tasks.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp device's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currWorkItemIdx:
                            description: It is the pnp device's currWorkItemIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        taskSeqNo:
                            description: It is the pnp device's taskSeqNo.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        endTime:
                            description: It is the pnp device's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                addToInventory:
                    description: It is the pnp device's addToInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                instanceType:
                    description: It is the pnp device's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the pnp device's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                execTime:
                    description: It is the pnp device's execTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp device's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                useState:
                    description: It is the pnp device's useState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configId:
                    description: It is the pnp device's configId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the pnp device's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp device's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        systemWorkflow:
            description: Device's System Workflow.
            returned: success,changed,always
            type: dict
            contains:
                _id:
                    description: It is the pnp device's _id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastupdateOn:
                    description: It is the pnp device's lastupdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                imageId:
                    description: It is the pnp device's imageId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currTaskIdx:
                    description: It is the pnp device's currTaskIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tasks:
                    description: It is the pnp device's tasks.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp device's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currWorkItemIdx:
                            description: It is the pnp device's currWorkItemIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        taskSeqNo:
                            description: It is the pnp device's taskSeqNo.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        endTime:
                            description: It is the pnp device's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                addToInventory:
                    description: It is the pnp device's addToInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                instanceType:
                    description: It is the pnp device's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the pnp device's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                execTime:
                    description: It is the pnp device's execTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp device's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                useState:
                    description: It is the pnp device's useState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configId:
                    description: It is the pnp device's configId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the pnp device's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp device's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        workflow:
            description: Device's Workflow.
            returned: success,changed,always
            type: dict
            contains:
                _id:
                    description: It is the pnp device's _id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                state:
                    description: It is the pnp device's state.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the pnp device's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                description:
                    description: It is the pnp device's description.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                lastupdateOn:
                    description: It is the pnp device's lastupdateOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                imageId:
                    description: It is the pnp device's imageId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                currTaskIdx:
                    description: It is the pnp device's currTaskIdx.
                    returned: success,changed,always
                    type: int
                    sample: 0
                addedOn:
                    description: It is the pnp device's addedOn.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tasks:
                    description: It is the pnp device's tasks.
                    returned: success,changed,always
                    type: list
                    contains:
                        state:
                            description: It is the pnp device's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currWorkItemIdx:
                            description: It is the pnp device's currWorkItemIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        taskSeqNo:
                            description: It is the pnp device's taskSeqNo.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        endTime:
                            description: It is the pnp device's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                addToInventory:
                    description: It is the pnp device's addToInventory.
                    returned: success,changed,always
                    type: bool
                    sample: false
                instanceType:
                    description: It is the pnp device's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                endTime:
                    description: It is the pnp device's endTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                execTime:
                    description: It is the pnp device's execTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                startTime:
                    description: It is the pnp device's startTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                useState:
                    description: It is the pnp device's useState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configId:
                    description: It is the pnp device's configId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the pnp device's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the pnp device's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp device's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        runSummaryList:
            description: Device's Run Summary List (list of objects).
            returned: success,changed,always
            type: list
            contains:
                details:
                    description: It is the pnp device's details.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                historyTaskInfo:
                    description: It is the pnp device's historyTaskInfo.
                    returned: success,changed,always
                    type: dict
                    contains:
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        addnDetails:
                            description: It is the pnp device's addnDetails.
                            returned: success,changed,always
                            type: list
                            contains:
                                key:
                                    description: It is the pnp device's key.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                value:
                                    description: It is the pnp device's value.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                errorFlag:
                    description: It is the pnp device's errorFlag.
                    returned: success,changed,always
                    type: bool
                    sample: false
                timestamp:
                    description: It is the pnp device's timestamp.
                    returned: success,changed,always
                    type: int
                    sample: 0

        workflowParameters:
            description: Device's Workflow Parameters.
            returned: success,changed,always
            type: dict
            contains:
                topOfStackSerialNumber:
                    description: It is the pnp device's topOfStackSerialNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                licenseLevel:
                    description: It is the pnp device's licenseLevel.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                licenseType:
                    description: It is the pnp device's licenseType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                configList:
                    description: It is the pnp device's configList.
                    returned: success,changed,always
                    type: list
                    contains:
                        configParameters:
                            description: It is the pnp device's configParameters.
                            returned: success,changed,always
                            type: list
                            contains:
                                key:
                                    description: It is the pnp device's key.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                value:
                                    description: It is the pnp device's value.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        configId:
                            description: It is the pnp device's configId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'


        dayZeroConfig:
            description: Device's Day Zero Config.
            returned: success,changed,always
            type: dict
            contains:
                config:
                    description: It is the pnp device's config.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        dayZeroConfigPreview:
            description: Device's Day Zero Config Preview.
            returned: success,changed,always
            type: dict
        version:
            description: Device's version.
            returned: success,changed,always
            type: int
            sample: 0
        tenantId:
            description: Device's Tenant Id.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_5:
    description: Returns the device count based on filter criteria. This is useful for pagination.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0

data_6:
    description: Returns history for a specific device. Serial number is a required parameter.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                timestamp:
                    description: It is the pnp device's timestamp.
                    returned: success,changed,always
                    type: int
                    sample: 0
                details:
                    description: It is the pnp device's details.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                historyTaskInfo:
                    description: It is the pnp device's historyTaskInfo.
                    returned: success,changed,always
                    type: dict
                    contains:
                        name:
                            description: It is the pnp device's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        timeTaken:
                            description: It is the pnp device's timeTaken.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workItemList:
                            description: It is the pnp device's workItemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                command:
                                    description: It is the pnp device's command.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                startTime:
                                    description: It is the pnp device's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                endTime:
                                    description: It is the pnp device's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                timeTaken:
                                    description: It is the pnp device's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                outputStr:
                                    description: It is the pnp device's outputStr.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        addnDetails:
                            description: It is the pnp device's addnDetails.
                            returned: success,changed,always
                            type: list
                            contains:
                                key:
                                    description: It is the pnp device's key.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                value:
                                    description: It is the pnp device's value.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'


                errorFlag:
                    description: It is the pnp device's errorFlag.
                    returned: success,changed,always
                    type: bool
                    sample: false

        statusCode:
            description: StatusCode, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.pnp_device import module_definition


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    elif state == "delete":
        dnac.exec("delete")

    elif state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    elif state == "update":
        dnac.disable_validation()
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()