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
module: pnp_device_import
short_description: Manage PnpDeviceImport objects of DeviceOnboardingPnp
description:
- Add devices to PnP in bulk.
version_added: '1.0'
author: first last (@GitHubID)
options:
    payload:
        description:
        - A JSON serializable Python object to send in the body of the Request.
        type: list
        required: True
        elements: dict
        suboptions:
            _id:
                description:
                - It is the pnp device import's _id.
                type: str
            deviceInfo:
                description:
                - It is the pnp device import's deviceInfo.
                type: dict
                required: True
                suboptions:
                    aaaCredentials:
                        description:
                        - It is the pnp device import's aaaCredentials.
                        type: dict
                        suboptions:
                            password:
                                description:
                                - It is the pnp device import's password.
                                type: str
                            username:
                                description:
                                - It is the pnp device import's username.
                                type: str

                    addedOn:
                        description:
                        - It is the pnp device import's addedOn.
                        type: int
                    addnMacAddrs:
                        description:
                        - It is the pnp device import's addnMacAddrs.
                        type: list
                    agentType:
                        description:
                        - It is the pnp device import's agentType.
                        type: str
                    authStatus:
                        description:
                        - It is the pnp device import's authStatus.
                        type: str
                    authenticatedSudiSerialNo:
                        description:
                        - It is the pnp device import's authenticatedSudiSerialNo.
                        type: str
                    capabilitiesSupported:
                        description:
                        - It is the pnp device import's capabilitiesSupported.
                        type: list
                    cmState:
                        description:
                        - It is the pnp device import's cmState.
                        type: str
                    description:
                        description:
                        - It is the pnp device import's description.
                        type: str
                    deviceSudiSerialNos:
                        description:
                        - It is the pnp device import's deviceSudiSerialNos.
                        type: list
                    deviceType:
                        description:
                        - It is the pnp device import's deviceType.
                        type: str
                    featuresSupported:
                        description:
                        - It is the pnp device import's featuresSupported.
                        type: list
                    fileSystemList:
                        description:
                        - It is the pnp device import's fileSystemList.
                        type: list
                        elements: dict
                        suboptions:
                            freespace:
                                description:
                                - It is the pnp device import's freespace.
                                type: int
                            name:
                                description:
                                - It is the pnp device import's name.
                                type: str
                            readable:
                                description:
                                - It is the pnp device import's readable.
                                type: bool
                            size:
                                description:
                                - It is the pnp device import's size.
                                type: int
                            type:
                                description:
                                - It is the pnp device import's type.
                                type: str
                            writeable:
                                description:
                                - It is the pnp device import's writeable.
                                type: bool

                    firstContact:
                        description:
                        - It is the pnp device import's firstContact.
                        type: int
                    hostname:
                        description:
                        - It is the pnp device import's hostname.
                        type: str
                    httpHeaders:
                        description:
                        - It is the pnp device import's httpHeaders.
                        type: list
                        elements: dict
                        suboptions:
                            key:
                                description:
                                - It is the pnp device import's key.
                                type: str
                            value:
                                description:
                                - It is the pnp device import's value.
                                type: str

                    imageFile:
                        description:
                        - It is the pnp device import's imageFile.
                        type: str
                    imageVersion:
                        description:
                        - It is the pnp device import's imageVersion.
                        type: str
                    ipInterfaces:
                        description:
                        - It is the pnp device import's ipInterfaces.
                        type: list
                        elements: dict
                        suboptions:
                            ipv4Address:
                                description:
                                - It is the pnp device import's ipv4Address.
                                type: dict
                            ipv6AddressList:
                                description:
                                - It is the pnp device import's ipv6AddressList.
                                type: list
                            macAddress:
                                description:
                                - It is the pnp device import's macAddress.
                                type: str
                            name:
                                description:
                                - It is the pnp device import's name.
                                type: str
                            status:
                                description:
                                - It is the pnp device import's status.
                                type: str

                    lastContact:
                        description:
                        - It is the pnp device import's lastContact.
                        type: int
                    lastSyncTime:
                        description:
                        - It is the pnp device import's lastSyncTime.
                        type: int
                    lastUpdateOn:
                        description:
                        - It is the pnp device import's lastUpdateOn.
                        type: int
                    location:
                        description:
                        - It is the pnp device import's location.
                        type: dict
                        suboptions:
                            address:
                                description:
                                - It is the pnp device import's address.
                                type: str
                            altitude:
                                description:
                                - It is the pnp device import's altitude.
                                type: str
                            latitude:
                                description:
                                - It is the pnp device import's latitude.
                                type: str
                            longitude:
                                description:
                                - It is the pnp device import's longitude.
                                type: str
                            siteId:
                                description:
                                - It is the pnp device import's siteId.
                                type: str

                    macAddress:
                        description:
                        - It is the pnp device import's macAddress.
                        type: str
                    mode:
                        description:
                        - It is the pnp device import's mode.
                        type: str
                    name:
                        description:
                        - It is the pnp device import's name.
                        type: str
                    neighborLinks:
                        description:
                        - It is the pnp device import's neighborLinks.
                        type: list
                        elements: dict
                        suboptions:
                            localInterfaceName:
                                description:
                                - It is the pnp device import's localInterfaceName.
                                type: str
                            localMacAddress:
                                description:
                                - It is the pnp device import's localMacAddress.
                                type: str
                            localShortInterfaceName:
                                description:
                                - It is the pnp device import's localShortInterfaceName.
                                type: str
                            remoteDeviceName:
                                description:
                                - It is the pnp device import's remoteDeviceName.
                                type: str
                            remoteInterfaceName:
                                description:
                                - It is the pnp device import's remoteInterfaceName.
                                type: str
                            remoteMacAddress:
                                description:
                                - It is the pnp device import's remoteMacAddress.
                                type: str
                            remotePlatform:
                                description:
                                - It is the pnp device import's remotePlatform.
                                type: str
                            remoteShortInterfaceName:
                                description:
                                - It is the pnp device import's remoteShortInterfaceName.
                                type: str
                            remoteVersion:
                                description:
                                - It is the pnp device import's remoteVersion.
                                type: str

                    onbState:
                        description:
                        - It is the pnp device import's onbState.
                        type: str
                    pid:
                        description:
                        - It is the pnp device import's pid.
                        type: str
                    pnpProfileList:
                        description:
                        - It is the pnp device import's pnpProfileList.
                        type: list
                        elements: dict
                        suboptions:
                            createdBy:
                                description:
                                - It is the pnp device import's createdBy.
                                type: str
                            discoveryCreated:
                                description:
                                - It is the pnp device import's discoveryCreated.
                                type: bool
                            primaryEndpoint:
                                description:
                                - It is the pnp device import's primaryEndpoint.
                                type: dict
                                suboptions:
                                    certificate:
                                        description:
                                        - It is the pnp device import's certificate.
                                        type: str
                                    fqdn:
                                        description:
                                        - It is the pnp device import's fqdn.
                                        type: str
                                    ipv4Address:
                                        description:
                                        - It is the pnp device import's ipv4Address.
                                        type: dict
                                    ipv6Address:
                                        description:
                                        - It is the pnp device import's ipv6Address.
                                        type: dict
                                    port:
                                        description:
                                        - It is the pnp device import's port.
                                        type: int
                                    protocol:
                                        description:
                                        - It is the pnp device import's protocol.
                                        type: str

                            profileName:
                                description:
                                - It is the pnp device import's profileName.
                                type: str
                            secondaryEndpoint:
                                description:
                                - It is the pnp device import's secondaryEndpoint.
                                type: dict
                                suboptions:
                                    certificate:
                                        description:
                                        - It is the pnp device import's certificate.
                                        type: str
                                    fqdn:
                                        description:
                                        - It is the pnp device import's fqdn.
                                        type: str
                                    ipv4Address:
                                        description:
                                        - It is the pnp device import's ipv4Address.
                                        type: dict
                                    ipv6Address:
                                        description:
                                        - It is the pnp device import's ipv6Address.
                                        type: dict
                                    port:
                                        description:
                                        - It is the pnp device import's port.
                                        type: int
                                    protocol:
                                        description:
                                        - It is the pnp device import's protocol.
                                        type: str


                    populateInventory:
                        description:
                        - It is the pnp device import's populateInventory.
                        type: bool
                    preWorkflowCliOuputs:
                        description:
                        - It is the pnp device import's preWorkflowCliOuputs.
                        type: list
                        elements: dict
                        suboptions:
                            cli:
                                description:
                                - It is the pnp device import's cli.
                                type: str
                            cliOutput:
                                description:
                                - It is the pnp device import's cliOutput.
                                type: str

                    projectId:
                        description:
                        - It is the pnp device import's projectId.
                        type: str
                    projectName:
                        description:
                        - It is the pnp device import's projectName.
                        type: str
                    reloadRequested:
                        description:
                        - It is the pnp device import's reloadRequested.
                        type: bool
                    serialNumber:
                        description:
                        - It is the pnp device import's serialNumber.
                        type: str
                    smartAccountId:
                        description:
                        - It is the pnp device import's smartAccountId.
                        type: str
                    source:
                        description:
                        - It is the pnp device import's source.
                        type: str
                    stack:
                        description:
                        - It is the pnp device import's stack.
                        type: bool
                    stackInfo:
                        description:
                        - It is the pnp device import's stackInfo.
                        type: dict
                        suboptions:
                            isFullRing:
                                description:
                                - It is the pnp device import's isFullRing.
                                type: bool
                            stackMemberList:
                                description:
                                - It is the pnp device import's stackMemberList.
                                type: list
                                elements: dict
                                suboptions:
                                    hardwareVersion:
                                        description:
                                        - It is the pnp device import's hardwareVersion.
                                        type: str
                                    licenseLevel:
                                        description:
                                        - It is the pnp device import's licenseLevel.
                                        type: str
                                    licenseType:
                                        description:
                                        - It is the pnp device import's licenseType.
                                        type: str
                                    macAddress:
                                        description:
                                        - It is the pnp device import's macAddress.
                                        type: str
                                    pid:
                                        description:
                                        - It is the pnp device import's pid.
                                        type: str
                                    priority:
                                        description:
                                        - It is the pnp device import's priority.
                                        type: int
                                    role:
                                        description:
                                        - It is the pnp device import's role.
                                        type: str
                                    serialNumber:
                                        description:
                                        - It is the pnp device import's serialNumber.
                                        type: str
                                    softwareVersion:
                                        description:
                                        - It is the pnp device import's softwareVersion.
                                        type: str
                                    stackNumber:
                                        description:
                                        - It is the pnp device import's stackNumber.
                                        type: int
                                    state:
                                        description:
                                        - It is the pnp device import's state.
                                        type: str
                                    sudiSerialNumber:
                                        description:
                                        - It is the pnp device import's sudiSerialNumber.
                                        type: str

                            stackRingProtocol:
                                description:
                                - It is the pnp device import's stackRingProtocol.
                                type: str
                            supportsStackWorkflows:
                                description:
                                - It is the pnp device import's supportsStackWorkflows.
                                type: bool
                            totalMemberCount:
                                description:
                                - It is the pnp device import's totalMemberCount.
                                type: int
                            validLicenseLevels:
                                description:
                                - It is the pnp device import's validLicenseLevels.
                                type: list

                    state:
                        description:
                        - It is the pnp device import's state.
                        type: str
                    sudiRequired:
                        description:
                        - It is the pnp device import's sudiRequired.
                        type: bool
                    tags:
                        description:
                        - It is the pnp device import's tags.
                        type: dict
                    userSudiSerialNos:
                        description:
                        - It is the pnp device import's userSudiSerialNos.
                        type: list
                    virtualAccountId:
                        description:
                        - It is the pnp device import's virtualAccountId.
                        type: str
                    workflowId:
                        description:
                        - It is the pnp device import's workflowId.
                        type: str
                    workflowName:
                        description:
                        - It is the pnp device import's workflowName.
                        type: str

            runSummaryList:
                description:
                - It is the pnp device import's runSummaryList.
                type: list
                elements: dict
                suboptions:
                    details:
                        description:
                        - It is the pnp device import's details.
                        type: str
                    errorFlag:
                        description:
                        - It is the pnp device import's errorFlag.
                        type: bool
                    historyTaskInfo:
                        description:
                        - It is the pnp device import's historyTaskInfo.
                        type: dict
                        suboptions:
                            addnDetails:
                                description:
                                - It is the pnp device import's addnDetails.
                                type: list
                                elements: dict
                                suboptions:
                                    key:
                                        description:
                                        - It is the pnp device import's key.
                                        type: str
                                    value:
                                        description:
                                        - It is the pnp device import's value.
                                        type: str

                            name:
                                description:
                                - It is the pnp device import's name.
                                type: str
                            timeTaken:
                                description:
                                - It is the pnp device import's timeTaken.
                                type: int
                            type:
                                description:
                                - It is the pnp device import's type.
                                type: str
                            workItemList:
                                description:
                                - It is the pnp device import's workItemList.
                                type: list
                                elements: dict
                                suboptions:
                                    command:
                                        description:
                                        - It is the pnp device import's command.
                                        type: str
                                    endTime:
                                        description:
                                        - It is the pnp device import's endTime.
                                        type: int
                                    outputStr:
                                        description:
                                        - It is the pnp device import's outputStr.
                                        type: str
                                    startTime:
                                        description:
                                        - It is the pnp device import's startTime.
                                        type: int
                                    state:
                                        description:
                                        - It is the pnp device import's state.
                                        type: str
                                    timeTaken:
                                        description:
                                        - It is the pnp device import's timeTaken.
                                        type: int


                    timestamp:
                        description:
                        - It is the pnp device import's timestamp.
                        type: int

            systemResetWorkflow:
                description:
                - It is the pnp device import's systemResetWorkflow.
                type: dict
                suboptions:
                    _id:
                        description:
                        - It is the pnp device import's _id.
                        type: str
                    addToInventory:
                        description:
                        - It is the pnp device import's addToInventory.
                        type: bool
                    addedOn:
                        description:
                        - It is the pnp device import's addedOn.
                        type: int
                    configId:
                        description:
                        - It is the pnp device import's configId.
                        type: str
                    currTaskIdx:
                        description:
                        - It is the pnp device import's currTaskIdx.
                        type: int
                    description:
                        description:
                        - It is the pnp device import's description.
                        type: str
                    endTime:
                        description:
                        - It is the pnp device import's endTime.
                        type: int
                    execTime:
                        description:
                        - It is the pnp device import's execTime.
                        type: int
                    imageId:
                        description:
                        - It is the pnp device import's imageId.
                        type: str
                    instanceType:
                        description:
                        - It is the pnp device import's instanceType.
                        type: str
                    lastupdateOn:
                        description:
                        - It is the pnp device import's lastupdateOn.
                        type: int
                    name:
                        description:
                        - It is the pnp device import's name.
                        type: str
                    startTime:
                        description:
                        - It is the pnp device import's startTime.
                        type: int
                    state:
                        description:
                        - It is the pnp device import's state.
                        type: str
                    tasks:
                        description:
                        - It is the pnp device import's tasks.
                        type: list
                        elements: dict
                        suboptions:
                            currWorkItemIdx:
                                description:
                                - It is the pnp device import's currWorkItemIdx.
                                type: int
                            endTime:
                                description:
                                - It is the pnp device import's endTime.
                                type: int
                            name:
                                description:
                                - It is the pnp device import's name.
                                type: str
                            startTime:
                                description:
                                - It is the pnp device import's startTime.
                                type: int
                            state:
                                description:
                                - It is the pnp device import's state.
                                type: str
                            taskSeqNo:
                                description:
                                - It is the pnp device import's taskSeqNo.
                                type: int
                            timeTaken:
                                description:
                                - It is the pnp device import's timeTaken.
                                type: int
                            type:
                                description:
                                - It is the pnp device import's type.
                                type: str
                            workItemList:
                                description:
                                - It is the pnp device import's workItemList.
                                type: list
                                elements: dict
                                suboptions:
                                    command:
                                        description:
                                        - It is the pnp device import's command.
                                        type: str
                                    endTime:
                                        description:
                                        - It is the pnp device import's endTime.
                                        type: int
                                    outputStr:
                                        description:
                                        - It is the pnp device import's outputStr.
                                        type: str
                                    startTime:
                                        description:
                                        - It is the pnp device import's startTime.
                                        type: int
                                    state:
                                        description:
                                        - It is the pnp device import's state.
                                        type: str
                                    timeTaken:
                                        description:
                                        - It is the pnp device import's timeTaken.
                                        type: int


                    tenantId:
                        description:
                        - It is the pnp device import's tenantId.
                        type: str
                    type:
                        description:
                        - It is the pnp device import's type.
                        type: str
                    useState:
                        description:
                        - It is the pnp device import's useState.
                        type: str
                    version:
                        description:
                        - It is the pnp device import's version.
                        type: int

            systemWorkflow:
                description:
                - It is the pnp device import's systemWorkflow.
                type: dict
                suboptions:
                    _id:
                        description:
                        - It is the pnp device import's _id.
                        type: str
                    addToInventory:
                        description:
                        - It is the pnp device import's addToInventory.
                        type: bool
                    addedOn:
                        description:
                        - It is the pnp device import's addedOn.
                        type: int
                    configId:
                        description:
                        - It is the pnp device import's configId.
                        type: str
                    currTaskIdx:
                        description:
                        - It is the pnp device import's currTaskIdx.
                        type: int
                    description:
                        description:
                        - It is the pnp device import's description.
                        type: str
                    endTime:
                        description:
                        - It is the pnp device import's endTime.
                        type: int
                    execTime:
                        description:
                        - It is the pnp device import's execTime.
                        type: int
                    imageId:
                        description:
                        - It is the pnp device import's imageId.
                        type: str
                    instanceType:
                        description:
                        - It is the pnp device import's instanceType.
                        type: str
                    lastupdateOn:
                        description:
                        - It is the pnp device import's lastupdateOn.
                        type: int
                    name:
                        description:
                        - It is the pnp device import's name.
                        type: str
                    startTime:
                        description:
                        - It is the pnp device import's startTime.
                        type: int
                    state:
                        description:
                        - It is the pnp device import's state.
                        type: str
                    tasks:
                        description:
                        - It is the pnp device import's tasks.
                        type: list
                        elements: dict
                        suboptions:
                            currWorkItemIdx:
                                description:
                                - It is the pnp device import's currWorkItemIdx.
                                type: int
                            endTime:
                                description:
                                - It is the pnp device import's endTime.
                                type: int
                            name:
                                description:
                                - It is the pnp device import's name.
                                type: str
                            startTime:
                                description:
                                - It is the pnp device import's startTime.
                                type: int
                            state:
                                description:
                                - It is the pnp device import's state.
                                type: str
                            taskSeqNo:
                                description:
                                - It is the pnp device import's taskSeqNo.
                                type: int
                            timeTaken:
                                description:
                                - It is the pnp device import's timeTaken.
                                type: int
                            type:
                                description:
                                - It is the pnp device import's type.
                                type: str
                            workItemList:
                                description:
                                - It is the pnp device import's workItemList.
                                type: list
                                elements: dict
                                suboptions:
                                    command:
                                        description:
                                        - It is the pnp device import's command.
                                        type: str
                                    endTime:
                                        description:
                                        - It is the pnp device import's endTime.
                                        type: int
                                    outputStr:
                                        description:
                                        - It is the pnp device import's outputStr.
                                        type: str
                                    startTime:
                                        description:
                                        - It is the pnp device import's startTime.
                                        type: int
                                    state:
                                        description:
                                        - It is the pnp device import's state.
                                        type: str
                                    timeTaken:
                                        description:
                                        - It is the pnp device import's timeTaken.
                                        type: int


                    tenantId:
                        description:
                        - It is the pnp device import's tenantId.
                        type: str
                    type:
                        description:
                        - It is the pnp device import's type.
                        type: str
                    useState:
                        description:
                        - It is the pnp device import's useState.
                        type: str
                    version:
                        description:
                        - It is the pnp device import's version.
                        type: int

            tenantId:
                description:
                - It is the pnp device import's tenantId.
                type: str
            version:
                description:
                - It is the pnp device import's version.
                type: int
            workflow:
                description:
                - It is the pnp device import's workflow.
                type: dict
                suboptions:
                    _id:
                        description:
                        - It is the pnp device import's _id.
                        type: str
                    addToInventory:
                        description:
                        - It is the pnp device import's addToInventory.
                        type: bool
                    addedOn:
                        description:
                        - It is the pnp device import's addedOn.
                        type: int
                    configId:
                        description:
                        - It is the pnp device import's configId.
                        type: str
                    currTaskIdx:
                        description:
                        - It is the pnp device import's currTaskIdx.
                        type: int
                    description:
                        description:
                        - It is the pnp device import's description.
                        type: str
                    endTime:
                        description:
                        - It is the pnp device import's endTime.
                        type: int
                    execTime:
                        description:
                        - It is the pnp device import's execTime.
                        type: int
                    imageId:
                        description:
                        - It is the pnp device import's imageId.
                        type: str
                    instanceType:
                        description:
                        - It is the pnp device import's instanceType.
                        type: str
                    lastupdateOn:
                        description:
                        - It is the pnp device import's lastupdateOn.
                        type: int
                    name:
                        description:
                        - It is the pnp device import's name.
                        type: str
                    startTime:
                        description:
                        - It is the pnp device import's startTime.
                        type: int
                    state:
                        description:
                        - It is the pnp device import's state.
                        type: str
                    tasks:
                        description:
                        - It is the pnp device import's tasks.
                        type: list
                        elements: dict
                        suboptions:
                            currWorkItemIdx:
                                description:
                                - It is the pnp device import's currWorkItemIdx.
                                type: int
                            endTime:
                                description:
                                - It is the pnp device import's endTime.
                                type: int
                            name:
                                description:
                                - It is the pnp device import's name.
                                type: str
                            startTime:
                                description:
                                - It is the pnp device import's startTime.
                                type: int
                            state:
                                description:
                                - It is the pnp device import's state.
                                type: str
                            taskSeqNo:
                                description:
                                - It is the pnp device import's taskSeqNo.
                                type: int
                            timeTaken:
                                description:
                                - It is the pnp device import's timeTaken.
                                type: int
                            type:
                                description:
                                - It is the pnp device import's type.
                                type: str
                            workItemList:
                                description:
                                - It is the pnp device import's workItemList.
                                type: list
                                elements: dict
                                suboptions:
                                    command:
                                        description:
                                        - It is the pnp device import's command.
                                        type: str
                                    endTime:
                                        description:
                                        - It is the pnp device import's endTime.
                                        type: int
                                    outputStr:
                                        description:
                                        - It is the pnp device import's outputStr.
                                        type: str
                                    startTime:
                                        description:
                                        - It is the pnp device import's startTime.
                                        type: int
                                    state:
                                        description:
                                        - It is the pnp device import's state.
                                        type: str
                                    timeTaken:
                                        description:
                                        - It is the pnp device import's timeTaken.
                                        type: int


                    tenantId:
                        description:
                        - It is the pnp device import's tenantId.
                        type: str
                    type:
                        description:
                        - It is the pnp device import's type.
                        type: str
                    useState:
                        description:
                        - It is the pnp device import's useState.
                        type: str
                    version:
                        description:
                        - It is the pnp device import's version.
                        type: int

            workflowParameters:
                description:
                - It is the pnp device import's workflowParameters.
                type: dict
                suboptions:
                    configList:
                        description:
                        - It is the pnp device import's configList.
                        type: list
                        elements: dict
                        suboptions:
                            configId:
                                description:
                                - It is the pnp device import's configId.
                                type: str
                            configParameters:
                                description:
                                - It is the pnp device import's configParameters.
                                type: list
                                elements: dict
                                suboptions:
                                    key:
                                        description:
                                        - It is the pnp device import's key.
                                        type: str
                                    value:
                                        description:
                                        - It is the pnp device import's value.
                                        type: str


                    licenseLevel:
                        description:
                        - It is the pnp device import's licenseLevel.
                        type: str
                    licenseType:
                        description:
                        - It is the pnp device import's licenseType.
                        type: str
                    topOfStackSerialNumber:
                        description:
                        - It is the pnp device import's topOfStackSerialNumber.
                        type: str



requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.pnp_device_import
# Reference by Internet resource
- name: PnpDeviceImport reference
  description: Complete reference of the PnpDeviceImport object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpDeviceImport reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Add devices to PnP in bulk.
    returned: success,changed,always
    type: dict
    contains:
        successList:
            description: Device's Success List (list of objects).
            returned: success,changed,always
            type: list
            contains:
                _id:
                    description: It is the pnp device import's _id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceInfo:
                    description: It is the pnp device import's deviceInfo.
                    returned: success,changed,always
                    type: dict
                    contains:
                        source:
                            description: It is the pnp device import's source.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        serialNumber:
                            description: It is the pnp device import's serialNumber.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        stack:
                            description: It is the pnp device import's stack.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        mode:
                            description: It is the pnp device import's mode.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        state:
                            description: It is the pnp device import's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        location:
                            description: It is the pnp device import's location.
                            returned: success,changed,always
                            type: dict
                            contains:
                                siteId:
                                    description: It is the pnp device import's siteId.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                address:
                                    description: It is the pnp device import's address.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                latitude:
                                    description: It is the pnp device import's latitude.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                longitude:
                                    description: It is the pnp device import's longitude.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                altitude:
                                    description: It is the pnp device import's altitude.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        description:
                            description: It is the pnp device import's description.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        onbState:
                            description: It is the pnp device import's onbState.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        authenticatedMicNumber:
                            description: It is the pnp device import's authenticatedMicNumber.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        authenticatedSudiSerialNo:
                            description: It is the pnp device import's authenticatedSudiSerialNo.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        capabilitiesSupported:
                            description: It is the pnp device import's capabilitiesSupported.
                            returned: success,changed,always
                            type: list
                        featuresSupported:
                            description: It is the pnp device import's featuresSupported.
                            returned: success,changed,always
                            type: list
                        cmState:
                            description: It is the pnp device import's cmState.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        firstContact:
                            description: It is the pnp device import's firstContact.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        lastContact:
                            description: It is the pnp device import's lastContact.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        macAddress:
                            description: It is the pnp device import's macAddress.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        pid:
                            description: It is the pnp device import's pid.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        deviceSudiSerialNos:
                            description: It is the pnp device import's deviceSudiSerialNos.
                            returned: success,changed,always
                            type: list
                        lastUpdateOn:
                            description: It is the pnp device import's lastUpdateOn.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        workflowId:
                            description: It is the pnp device import's workflowId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        workflowName:
                            description: It is the pnp device import's workflowName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        projectId:
                            description: It is the pnp device import's projectId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        projectName:
                            description: It is the pnp device import's projectName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        deviceType:
                            description: It is the pnp device import's deviceType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        agentType:
                            description: It is the pnp device import's agentType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        imageVersion:
                            description: It is the pnp device import's imageVersion.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        fileSystemList:
                            description: It is the pnp device import's fileSystemList.
                            returned: success,changed,always
                            type: list
                            contains:
                                type:
                                    description: It is the pnp device import's type.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                writeable:
                                    description: It is the pnp device import's writeable.
                                    returned: success,changed,always
                                    type: bool
                                    sample: false
                                freespace:
                                    description: It is the pnp device import's freespace.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                name:
                                    description: It is the pnp device import's name.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                readable:
                                    description: It is the pnp device import's readable.
                                    returned: success,changed,always
                                    type: bool
                                    sample: false
                                size:
                                    description: It is the pnp device import's size.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        pnpProfileList:
                            description: It is the pnp device import's pnpProfileList.
                            returned: success,changed,always
                            type: list
                            contains:
                                profileName:
                                    description: It is the pnp device import's profileName.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                discoveryCreated:
                                    description: It is the pnp device import's discoveryCreated.
                                    returned: success,changed,always
                                    type: bool
                                    sample: false
                                createdBy:
                                    description: It is the pnp device import's createdBy.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                primaryEndpoint:
                                    description: It is the pnp device import's primaryEndpoint.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        port:
                                            description: It is the pnp device import's port.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        protocol:
                                            description: It is the pnp device import's protocol.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        ipv4Address:
                                            description: It is the pnp device import's ipv4Address.
                                            returned: success,changed,always
                                            type: dict
                                        ipv6Address:
                                            description: It is the pnp device import's ipv6Address.
                                            returned: success,changed,always
                                            type: dict
                                        fqdn:
                                            description: It is the pnp device import's fqdn.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        certificate:
                                            description: It is the pnp device import's certificate.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'

                                secondaryEndpoint:
                                    description: It is the pnp device import's secondaryEndpoint.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        port:
                                            description: It is the pnp device import's port.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        protocol:
                                            description: It is the pnp device import's protocol.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        ipv4Address:
                                            description: It is the pnp device import's ipv4Address.
                                            returned: success,changed,always
                                            type: dict
                                        ipv6Address:
                                            description: It is the pnp device import's ipv6Address.
                                            returned: success,changed,always
                                            type: dict
                                        fqdn:
                                            description: It is the pnp device import's fqdn.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        certificate:
                                            description: It is the pnp device import's certificate.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'


                        imageFile:
                            description: It is the pnp device import's imageFile.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        httpHeaders:
                            description: It is the pnp device import's httpHeaders.
                            returned: success,changed,always
                            type: list
                            contains:
                                key:
                                    description: It is the pnp device import's key.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                value:
                                    description: It is the pnp device import's value.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        neighborLinks:
                            description: It is the pnp device import's neighborLinks.
                            returned: success,changed,always
                            type: list
                            contains:
                                localInterfaceName:
                                    description: It is the pnp device import's localInterfaceName.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                localShortInterfaceName:
                                    description: It is the pnp device import's localShortInterfaceName.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                localMacAddress:
                                    description: It is the pnp device import's localMacAddress.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                remoteInterfaceName:
                                    description: It is the pnp device import's remoteInterfaceName.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                remoteShortInterfaceName:
                                    description: It is the pnp device import's remoteShortInterfaceName.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                remoteMacAddress:
                                    description: It is the pnp device import's remoteMacAddress.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                remoteDeviceName:
                                    description: It is the pnp device import's remoteDeviceName.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                remotePlatform:
                                    description: It is the pnp device import's remotePlatform.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                remoteVersion:
                                    description: It is the pnp device import's remoteVersion.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        lastSyncTime:
                            description: It is the pnp device import's lastSyncTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        ipInterfaces:
                            description: It is the pnp device import's ipInterfaces.
                            returned: success,changed,always
                            type: list
                            contains:
                                status:
                                    description: It is the pnp device import's status.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                macAddress:
                                    description: It is the pnp device import's macAddress.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ipv4Address:
                                    description: It is the pnp device import's ipv4Address.
                                    returned: success,changed,always
                                    type: dict
                                ipv6AddressList:
                                    description: It is the pnp device import's ipv6AddressList.
                                    returned: success,changed,always
                                    type: list
                                name:
                                    description: It is the pnp device import's name.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        hostname:
                            description: It is the pnp device import's hostname.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        authStatus:
                            description: It is the pnp device import's authStatus.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        stackInfo:
                            description: It is the pnp device import's stackInfo.
                            returned: success,changed,always
                            type: dict
                            contains:
                                supportsStackWorkflows:
                                    description: It is the pnp device import's supportsStackWorkflows.
                                    returned: success,changed,always
                                    type: bool
                                    sample: false
                                isFullRing:
                                    description: It is the pnp device import's isFullRing.
                                    returned: success,changed,always
                                    type: bool
                                    sample: false
                                stackMemberList:
                                    description: It is the pnp device import's stackMemberList.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        serialNumber:
                                            description: It is the pnp device import's serialNumber.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        state:
                                            description: It is the pnp device import's state.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        role:
                                            description: It is the pnp device import's role.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        macAddress:
                                            description: It is the pnp device import's macAddress.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        pid:
                                            description: It is the pnp device import's pid.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        licenseLevel:
                                            description: It is the pnp device import's licenseLevel.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        licenseType:
                                            description: It is the pnp device import's licenseType.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        sudiSerialNumber:
                                            description: It is the pnp device import's sudiSerialNumber.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        hardwareVersion:
                                            description: It is the pnp device import's hardwareVersion.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        stackNumber:
                                            description: It is the pnp device import's stackNumber.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        softwareVersion:
                                            description: It is the pnp device import's softwareVersion.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        priority:
                                            description: It is the pnp device import's priority.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0

                                stackRingProtocol:
                                    description: It is the pnp device import's stackRingProtocol.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                validLicenseLevels:
                                    description: It is the pnp device import's validLicenseLevels.
                                    returned: success,changed,always
                                    type: list
                                totalMemberCount:
                                    description: It is the pnp device import's totalMemberCount.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0

                        reloadRequested:
                            description: It is the pnp device import's reloadRequested.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        addedOn:
                            description: It is the pnp device import's addedOn.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        siteId:
                            description: It is the pnp device import's siteId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        aaaCredentials:
                            description: It is the pnp device import's aaaCredentials.
                            returned: success,changed,always
                            type: dict
                            contains:
                                password:
                                    description: It is the pnp device import's password.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                username:
                                    description: It is the pnp device import's username.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        userMicNumbers:
                            description: It is the pnp device import's userMicNumbers.
                            returned: success,changed,always
                            type: list
                        userSudiSerialNos:
                            description: It is the pnp device import's userSudiSerialNos.
                            returned: success,changed,always
                            type: list
                        addnMacAddrs:
                            description: It is the pnp device import's addnMacAddrs.
                            returned: success,changed,always
                            type: list
                        preWorkflowCliOuputs:
                            description: It is the pnp device import's preWorkflowCliOuputs.
                            returned: success,changed,always
                            type: list
                            contains:
                                cli:
                                    description: It is the pnp device import's cli.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                cliOutput:
                                    description: It is the pnp device import's cliOutput.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        tags:
                            description: It is the pnp device import's tags.
                            returned: success,changed,always
                            type: dict
                        sudiRequired:
                            description: It is the pnp device import's sudiRequired.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        smartAccountId:
                            description: It is the pnp device import's smartAccountId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        virtualAccountId:
                            description: It is the pnp device import's virtualAccountId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        populateInventory:
                            description: It is the pnp device import's populateInventory.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        siteName:
                            description: It is the pnp device import's siteName.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        name:
                            description: It is the pnp device import's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                systemResetWorkflow:
                    description: It is the pnp device import's systemResetWorkflow.
                    returned: success,changed,always
                    type: dict
                    contains:
                        _id:
                            description: It is the pnp device import's _id.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        state:
                            description: It is the pnp device import's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device import's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        description:
                            description: It is the pnp device import's description.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        lastupdateOn:
                            description: It is the pnp device import's lastupdateOn.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        imageId:
                            description: It is the pnp device import's imageId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currTaskIdx:
                            description: It is the pnp device import's currTaskIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        addedOn:
                            description: It is the pnp device import's addedOn.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        tasks:
                            description: It is the pnp device import's tasks.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device import's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                type:
                                    description: It is the pnp device import's type.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                currWorkItemIdx:
                                    description: It is the pnp device import's currWorkItemIdx.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                taskSeqNo:
                                    description: It is the pnp device import's taskSeqNo.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                endTime:
                                    description: It is the pnp device import's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device import's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                workItemList:
                                    description: It is the pnp device import's workItemList.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        state:
                                            description: It is the pnp device import's state.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        command:
                                            description: It is the pnp device import's command.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        outputStr:
                                            description: It is the pnp device import's outputStr.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        endTime:
                                            description: It is the pnp device import's endTime.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        startTime:
                                            description: It is the pnp device import's startTime.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        timeTaken:
                                            description: It is the pnp device import's timeTaken.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0

                                timeTaken:
                                    description: It is the pnp device import's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                name:
                                    description: It is the pnp device import's name.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        addToInventory:
                            description: It is the pnp device import's addToInventory.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        instanceType:
                            description: It is the pnp device import's instanceType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        endTime:
                            description: It is the pnp device import's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        execTime:
                            description: It is the pnp device import's execTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device import's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        useState:
                            description: It is the pnp device import's useState.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        configId:
                            description: It is the pnp device import's configId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        name:
                            description: It is the pnp device import's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        version:
                            description: It is the pnp device import's version.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        tenantId:
                            description: It is the pnp device import's tenantId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                systemWorkflow:
                    description: It is the pnp device import's systemWorkflow.
                    returned: success,changed,always
                    type: dict
                    contains:
                        _id:
                            description: It is the pnp device import's _id.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        state:
                            description: It is the pnp device import's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device import's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        description:
                            description: It is the pnp device import's description.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        lastupdateOn:
                            description: It is the pnp device import's lastupdateOn.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        imageId:
                            description: It is the pnp device import's imageId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currTaskIdx:
                            description: It is the pnp device import's currTaskIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        addedOn:
                            description: It is the pnp device import's addedOn.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        tasks:
                            description: It is the pnp device import's tasks.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device import's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                type:
                                    description: It is the pnp device import's type.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                currWorkItemIdx:
                                    description: It is the pnp device import's currWorkItemIdx.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                taskSeqNo:
                                    description: It is the pnp device import's taskSeqNo.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                endTime:
                                    description: It is the pnp device import's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device import's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                workItemList:
                                    description: It is the pnp device import's workItemList.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        state:
                                            description: It is the pnp device import's state.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        command:
                                            description: It is the pnp device import's command.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        outputStr:
                                            description: It is the pnp device import's outputStr.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        endTime:
                                            description: It is the pnp device import's endTime.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        startTime:
                                            description: It is the pnp device import's startTime.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        timeTaken:
                                            description: It is the pnp device import's timeTaken.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0

                                timeTaken:
                                    description: It is the pnp device import's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                name:
                                    description: It is the pnp device import's name.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        addToInventory:
                            description: It is the pnp device import's addToInventory.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        instanceType:
                            description: It is the pnp device import's instanceType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        endTime:
                            description: It is the pnp device import's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        execTime:
                            description: It is the pnp device import's execTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device import's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        useState:
                            description: It is the pnp device import's useState.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        configId:
                            description: It is the pnp device import's configId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        name:
                            description: It is the pnp device import's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        version:
                            description: It is the pnp device import's version.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        tenantId:
                            description: It is the pnp device import's tenantId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                workflow:
                    description: It is the pnp device import's workflow.
                    returned: success,changed,always
                    type: dict
                    contains:
                        _id:
                            description: It is the pnp device import's _id.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        state:
                            description: It is the pnp device import's state.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        type:
                            description: It is the pnp device import's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        description:
                            description: It is the pnp device import's description.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        lastupdateOn:
                            description: It is the pnp device import's lastupdateOn.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        imageId:
                            description: It is the pnp device import's imageId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        currTaskIdx:
                            description: It is the pnp device import's currTaskIdx.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        addedOn:
                            description: It is the pnp device import's addedOn.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        tasks:
                            description: It is the pnp device import's tasks.
                            returned: success,changed,always
                            type: list
                            contains:
                                state:
                                    description: It is the pnp device import's state.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                type:
                                    description: It is the pnp device import's type.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                currWorkItemIdx:
                                    description: It is the pnp device import's currWorkItemIdx.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                taskSeqNo:
                                    description: It is the pnp device import's taskSeqNo.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                endTime:
                                    description: It is the pnp device import's endTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                startTime:
                                    description: It is the pnp device import's startTime.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                workItemList:
                                    description: It is the pnp device import's workItemList.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        state:
                                            description: It is the pnp device import's state.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        command:
                                            description: It is the pnp device import's command.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        outputStr:
                                            description: It is the pnp device import's outputStr.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        endTime:
                                            description: It is the pnp device import's endTime.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        startTime:
                                            description: It is the pnp device import's startTime.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        timeTaken:
                                            description: It is the pnp device import's timeTaken.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0

                                timeTaken:
                                    description: It is the pnp device import's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                name:
                                    description: It is the pnp device import's name.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        addToInventory:
                            description: It is the pnp device import's addToInventory.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        instanceType:
                            description: It is the pnp device import's instanceType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        endTime:
                            description: It is the pnp device import's endTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        execTime:
                            description: It is the pnp device import's execTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        startTime:
                            description: It is the pnp device import's startTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        useState:
                            description: It is the pnp device import's useState.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        configId:
                            description: It is the pnp device import's configId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        name:
                            description: It is the pnp device import's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        version:
                            description: It is the pnp device import's version.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        tenantId:
                            description: It is the pnp device import's tenantId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                runSummaryList:
                    description: It is the pnp device import's runSummaryList.
                    returned: success,changed,always
                    type: list
                    contains:
                        details:
                            description: It is the pnp device import's details.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        historyTaskInfo:
                            description: It is the pnp device import's historyTaskInfo.
                            returned: success,changed,always
                            type: dict
                            contains:
                                type:
                                    description: It is the pnp device import's type.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                workItemList:
                                    description: It is the pnp device import's workItemList.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        state:
                                            description: It is the pnp device import's state.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        command:
                                            description: It is the pnp device import's command.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        outputStr:
                                            description: It is the pnp device import's outputStr.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        endTime:
                                            description: It is the pnp device import's endTime.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        startTime:
                                            description: It is the pnp device import's startTime.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        timeTaken:
                                            description: It is the pnp device import's timeTaken.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0

                                timeTaken:
                                    description: It is the pnp device import's timeTaken.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                addnDetails:
                                    description: It is the pnp device import's addnDetails.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        key:
                                            description: It is the pnp device import's key.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        value:
                                            description: It is the pnp device import's value.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'

                                name:
                                    description: It is the pnp device import's name.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        errorFlag:
                            description: It is the pnp device import's errorFlag.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        timestamp:
                            description: It is the pnp device import's timestamp.
                            returned: success,changed,always
                            type: int
                            sample: 0

                workflowParameters:
                    description: It is the pnp device import's workflowParameters.
                    returned: success,changed,always
                    type: dict
                    contains:
                        topOfStackSerialNumber:
                            description: It is the pnp device import's topOfStackSerialNumber.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        licenseLevel:
                            description: It is the pnp device import's licenseLevel.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        licenseType:
                            description: It is the pnp device import's licenseType.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        configList:
                            description: It is the pnp device import's configList.
                            returned: success,changed,always
                            type: list
                            contains:
                                configParameters:
                                    description: It is the pnp device import's configParameters.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        key:
                                            description: It is the pnp device import's key.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        value:
                                            description: It is the pnp device import's value.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'

                                configId:
                                    description: It is the pnp device import's configId.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'


                dayZeroConfig:
                    description: It is the pnp device import's dayZeroConfig.
                    returned: success,changed,always
                    type: dict
                    contains:
                        config:
                            description: It is the pnp device import's config.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                dayZeroConfigPreview:
                    description: It is the pnp device import's dayZeroConfigPreview.
                    returned: success,changed,always
                    type: dict
                version:
                    description: It is the pnp device import's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                tenantId:
                    description: It is the pnp device import's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        failureList:
            description: Device's Failure List (list of objects).
            returned: success,changed,always
            type: list
            contains:
                index:
                    description: It is the pnp device import's index.
                    returned: success,changed,always
                    type: int
                    sample: 0
                serialNum:
                    description: It is the pnp device import's serialNum.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the pnp device import's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                msg:
                    description: It is the pnp device import's msg.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'


'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.pnp_device_import import module_definition


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

    if state == "create":
        dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()