#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
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
    - Required for state query.
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
    - Required for state query.
    type: bool

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
"""

EXAMPLES = r"""
- name: get_device_list
  cisco.dnac.pnp_device:
    state: query  # required
    cm_state: SomeValue  # string
    last_contact: True  # boolean
    limit: 1  #  integer
    name: SomeValue  # string
    offset: 1  #  integer
    onb_state: SomeValue  # string
    pid: SomeValue  # string
    project_id: SomeValue  # string
    project_name: SomeValue  # string
    serial_number: SomeValue  # string
    smart_account_id: SomeValue  # string
    sort: SomeValue  # string
    sort_order: SomeValue  # string
    source: SomeValue  # string
    state: SomeValue  # string
    virtual_account_id: SomeValue  # string
    workflow_id: SomeValue  # string
    workflow_name: SomeValue  # string
  register: query_result
  
- name: add_device
  cisco.dnac.pnp_device:
    state: create  # required
    deviceInfo:  # required
      aaaCredentials:
        password: SomeValue  # string
        username: SomeValue  # string
      addedOn: 1  #  integer
      addnMacAddrs:
      - SomeValue  # string
      agentType: SomeValue  # string
      authStatus: SomeValue  # string
      authenticatedSudiSerialNo: SomeValue  # string
      capabilitiesSupported:
      - SomeValue  # string
      cmState: SomeValue  # string
      description: SomeValue  # string
      deviceSudiSerialNos:
      - SomeValue  # string
      deviceType: SomeValue  # string
      featuresSupported:
      - SomeValue  # string
      fileSystemList:
      - freespace: 1  #  integer
        name: SomeValue  # string
        readable: True  # boolean
        size: 1  #  integer
        type: SomeValue  # string
        writeable: True  # boolean
      firstContact: 1  #  integer
      hostname: SomeValue  # string
      httpHeaders:
      - key: SomeValue  # string
        value: SomeValue  # string
      imageFile: SomeValue  # string
      imageVersion: SomeValue  # string
      ipInterfaces:
      - ipv4Address: None
        ipv6AddressList:
        macAddress: SomeValue  # string
        name: SomeValue  # string
        status: SomeValue  # string
      lastContact: 1  #  integer
      lastSyncTime: 1  #  integer
      lastUpdateOn: 1  #  integer
      location:
        address: SomeValue  # string
        altitude: SomeValue  # string
        latitude: SomeValue  # string
        longitude: SomeValue  # string
        siteId: SomeValue  # string
      macAddress: SomeValue  # string
      mode: SomeValue  # string
      name: SomeValue  # string
      neighborLinks:
      - localInterfaceName: SomeValue  # string
        localMacAddress: SomeValue  # string
        localShortInterfaceName: SomeValue  # string
        remoteDeviceName: SomeValue  # string
        remoteInterfaceName: SomeValue  # string
        remoteMacAddress: SomeValue  # string
        remotePlatform: SomeValue  # string
        remoteShortInterfaceName: SomeValue  # string
        remoteVersion: SomeValue  # string
      onbState: SomeValue  # string
      pid: SomeValue  # string
      pnpProfileList:
      - createdBy: SomeValue  # string
        discoveryCreated: True  # boolean
        primaryEndpoint:
          certificate: SomeValue  # string
          fqdn: SomeValue  # string
          ipv4Address: None
          ipv6Address: None
          port: 1  #  integer
          protocol: SomeValue  # string
        profileName: SomeValue  # string
        secondaryEndpoint:
          certificate: SomeValue  # string
          fqdn: SomeValue  # string
          ipv4Address: None
          ipv6Address: None
          port: 1  #  integer
          protocol: SomeValue  # string
      populateInventory: True  # boolean
      preWorkflowCliOuputs:
      - cli: SomeValue  # string
        cliOutput: SomeValue  # string
      projectId: SomeValue  # string
      projectName: SomeValue  # string
      reloadRequested: True  # boolean
      serialNumber: SomeValue  # string
      smartAccountId: SomeValue  # string
      source: SomeValue  # string
      stack: True  # boolean
      stackInfo:
        isFullRing: True  # boolean
        stackMemberList:
        - hardwareVersion: SomeValue  # string
          licenseLevel: SomeValue  # string
          licenseType: SomeValue  # string
          macAddress: SomeValue  # string
          pid: SomeValue  # string
          priority: 1  #  integer
          role: SomeValue  # string
          serialNumber: SomeValue  # string
          softwareVersion: SomeValue  # string
          stackNumber: 1  #  integer
          state: SomeValue  # string
          sudiSerialNumber: SomeValue  # string
        stackRingProtocol: SomeValue  # string
        supportsStackWorkflows: True  # boolean
        totalMemberCount: 1  #  integer
        validLicenseLevels:
        - SomeValue  # string
      state: SomeValue  # string
      sudiRequired: True  # boolean
      tags: None
      userSudiSerialNos:
      - SomeValue  # string
      virtualAccountId: SomeValue  # string
      workflowId: SomeValue  # string
      workflowName: SomeValue  # string
    _id: SomeValue  # string
    runSummaryList:
    - details: SomeValue  # string
      errorFlag: True  # boolean
      historyTaskInfo:
        addnDetails:
        - key: SomeValue  # string
          value: SomeValue  # string
        name: SomeValue  # string
        timeTaken: 1  #  integer
        type: SomeValue  # string
        workItemList:
        - command: SomeValue  # string
          endTime: 1  #  integer
          outputStr: SomeValue  # string
          startTime: 1  #  integer
          state: SomeValue  # string
          timeTaken: 1  #  integer
      timestamp: 1  #  integer
    systemResetWorkflow:
      _id: SomeValue  # string
      addToInventory: True  # boolean
      addedOn: 1  #  integer
      configId: SomeValue  # string
      currTaskIdx: 1  #  integer
      description: SomeValue  # string
      endTime: 1  #  integer
      execTime: 1  #  integer
      imageId: SomeValue  # string
      instanceType: SomeValue  # string
      lastupdateOn: 1  #  integer
      name: SomeValue  # string
      startTime: 1  #  integer
      state: SomeValue  # string
      tasks:
      - currWorkItemIdx: 1  #  integer
        endTime: 1  #  integer
        name: SomeValue  # string
        startTime: 1  #  integer
        state: SomeValue  # string
        taskSeqNo: 1  #  integer
        timeTaken: 1  #  integer
        type: SomeValue  # string
        workItemList:
        - command: SomeValue  # string
          endTime: 1  #  integer
          outputStr: SomeValue  # string
          startTime: 1  #  integer
          state: SomeValue  # string
          timeTaken: 1  #  integer
      tenantId: SomeValue  # string
      type: SomeValue  # string
      useState: SomeValue  # string
      version: 1  #  integer
    systemWorkflow:
      _id: SomeValue  # string
      addToInventory: True  # boolean
      addedOn: 1  #  integer
      configId: SomeValue  # string
      currTaskIdx: 1  #  integer
      description: SomeValue  # string
      endTime: 1  #  integer
      execTime: 1  #  integer
      imageId: SomeValue  # string
      instanceType: SomeValue  # string
      lastupdateOn: 1  #  integer
      name: SomeValue  # string
      startTime: 1  #  integer
      state: SomeValue  # string
      tasks:
      - currWorkItemIdx: 1  #  integer
        endTime: 1  #  integer
        name: SomeValue  # string
        startTime: 1  #  integer
        state: SomeValue  # string
        taskSeqNo: 1  #  integer
        timeTaken: 1  #  integer
        type: SomeValue  # string
        workItemList:
        - command: SomeValue  # string
          endTime: 1  #  integer
          outputStr: SomeValue  # string
          startTime: 1  #  integer
          state: SomeValue  # string
          timeTaken: 1  #  integer
      tenantId: SomeValue  # string
      type: SomeValue  # string
      useState: SomeValue  # string
      version: 1  #  integer
    tenantId: SomeValue  # string
    version: 1  #  integer
    workflow:
      _id: SomeValue  # string
      addToInventory: True  # boolean
      addedOn: 1  #  integer
      configId: SomeValue  # string
      currTaskIdx: 1  #  integer
      description: SomeValue  # string
      endTime: 1  #  integer
      execTime: 1  #  integer
      imageId: SomeValue  # string
      instanceType: SomeValue  # string
      lastupdateOn: 1  #  integer
      name: SomeValue  # string
      startTime: 1  #  integer
      state: SomeValue  # string
      tasks:
      - currWorkItemIdx: 1  #  integer
        endTime: 1  #  integer
        name: SomeValue  # string
        startTime: 1  #  integer
        state: SomeValue  # string
        taskSeqNo: 1  #  integer
        timeTaken: 1  #  integer
        type: SomeValue  # string
        workItemList:
        - command: SomeValue  # string
          endTime: 1  #  integer
          outputStr: SomeValue  # string
          startTime: 1  #  integer
          state: SomeValue  # string
          timeTaken: 1  #  integer
      tenantId: SomeValue  # string
      type: SomeValue  # string
      useState: SomeValue  # string
      version: 1  #  integer
    workflowParameters:
      configList:
      - configId: SomeValue  # string
        configParameters:
        - key: SomeValue  # string
          value: SomeValue  # string
      licenseLevel: SomeValue  # string
      licenseType: SomeValue  # string
      topOfStackSerialNumber: SomeValue  # string
  
- name: get_device_by_id
  cisco.dnac.pnp_device:
    state: query  # required
    id: SomeValue  # string, required
  register: query_result
  
- name: delete_device_by_id_from_pnp
  cisco.dnac.pnp_device:
    state: delete  # required
    id: SomeValue  # string, required
  
- name: update_device
  cisco.dnac.pnp_device:
    state: update  # required
    id: SomeValue  # string, required
    deviceInfo:  # required
      aaaCredentials:
        password: SomeValue  # string
        username: SomeValue  # string
      addedOn: 1  #  integer
      addnMacAddrs:
      - SomeValue  # string
      agentType: SomeValue  # string
      authStatus: SomeValue  # string
      authenticatedSudiSerialNo: SomeValue  # string
      capabilitiesSupported:
      - SomeValue  # string
      cmState: SomeValue  # string
      description: SomeValue  # string
      deviceSudiSerialNos:
      - SomeValue  # string
      deviceType: SomeValue  # string
      featuresSupported:
      - SomeValue  # string
      fileSystemList:
      - freespace: 1  #  integer
        name: SomeValue  # string
        readable: True  # boolean
        size: 1  #  integer
        type: SomeValue  # string
        writeable: True  # boolean
      firstContact: 1  #  integer
      hostname: SomeValue  # string
      httpHeaders:
      - key: SomeValue  # string
        value: SomeValue  # string
      imageFile: SomeValue  # string
      imageVersion: SomeValue  # string
      ipInterfaces:
      - ipv4Address: None
        ipv6AddressList:
        macAddress: SomeValue  # string
        name: SomeValue  # string
        status: SomeValue  # string
      lastContact: 1  #  integer
      lastSyncTime: 1  #  integer
      lastUpdateOn: 1  #  integer
      location:
        address: SomeValue  # string
        altitude: SomeValue  # string
        latitude: SomeValue  # string
        longitude: SomeValue  # string
        siteId: SomeValue  # string
      macAddress: SomeValue  # string
      mode: SomeValue  # string
      name: SomeValue  # string
      neighborLinks:
      - localInterfaceName: SomeValue  # string
        localMacAddress: SomeValue  # string
        localShortInterfaceName: SomeValue  # string
        remoteDeviceName: SomeValue  # string
        remoteInterfaceName: SomeValue  # string
        remoteMacAddress: SomeValue  # string
        remotePlatform: SomeValue  # string
        remoteShortInterfaceName: SomeValue  # string
        remoteVersion: SomeValue  # string
      onbState: SomeValue  # string
      pid: SomeValue  # string
      pnpProfileList:
      - createdBy: SomeValue  # string
        discoveryCreated: True  # boolean
        primaryEndpoint:
          certificate: SomeValue  # string
          fqdn: SomeValue  # string
          ipv4Address: None
          ipv6Address: None
          port: 1  #  integer
          protocol: SomeValue  # string
        profileName: SomeValue  # string
        secondaryEndpoint:
          certificate: SomeValue  # string
          fqdn: SomeValue  # string
          ipv4Address: None
          ipv6Address: None
          port: 1  #  integer
          protocol: SomeValue  # string
      populateInventory: True  # boolean
      preWorkflowCliOuputs:
      - cli: SomeValue  # string
        cliOutput: SomeValue  # string
      projectId: SomeValue  # string
      projectName: SomeValue  # string
      reloadRequested: True  # boolean
      serialNumber: SomeValue  # string
      smartAccountId: SomeValue  # string
      source: SomeValue  # string
      stack: True  # boolean
      stackInfo:
        isFullRing: True  # boolean
        stackMemberList:
        - hardwareVersion: SomeValue  # string
          licenseLevel: SomeValue  # string
          licenseType: SomeValue  # string
          macAddress: SomeValue  # string
          pid: SomeValue  # string
          priority: 1  #  integer
          role: SomeValue  # string
          serialNumber: SomeValue  # string
          softwareVersion: SomeValue  # string
          stackNumber: 1  #  integer
          state: SomeValue  # string
          sudiSerialNumber: SomeValue  # string
        stackRingProtocol: SomeValue  # string
        supportsStackWorkflows: True  # boolean
        totalMemberCount: 1  #  integer
        validLicenseLevels:
        - SomeValue  # string
      state: SomeValue  # string
      sudiRequired: True  # boolean
      tags: None
      userSudiSerialNos:
      - SomeValue  # string
      virtualAccountId: SomeValue  # string
      workflowId: SomeValue  # string
      workflowName: SomeValue  # string
    _id: SomeValue  # string
    runSummaryList:
    - details: SomeValue  # string
      errorFlag: True  # boolean
      historyTaskInfo:
        addnDetails:
        - key: SomeValue  # string
          value: SomeValue  # string
        name: SomeValue  # string
        timeTaken: 1  #  integer
        type: SomeValue  # string
        workItemList:
        - command: SomeValue  # string
          endTime: 1  #  integer
          outputStr: SomeValue  # string
          startTime: 1  #  integer
          state: SomeValue  # string
          timeTaken: 1  #  integer
      timestamp: 1  #  integer
    systemResetWorkflow:
      _id: SomeValue  # string
      addToInventory: True  # boolean
      addedOn: 1  #  integer
      configId: SomeValue  # string
      currTaskIdx: 1  #  integer
      description: SomeValue  # string
      endTime: 1  #  integer
      execTime: 1  #  integer
      imageId: SomeValue  # string
      instanceType: SomeValue  # string
      lastupdateOn: 1  #  integer
      name: SomeValue  # string
      startTime: 1  #  integer
      state: SomeValue  # string
      tasks:
      - currWorkItemIdx: 1  #  integer
        endTime: 1  #  integer
        name: SomeValue  # string
        startTime: 1  #  integer
        state: SomeValue  # string
        taskSeqNo: 1  #  integer
        timeTaken: 1  #  integer
        type: SomeValue  # string
        workItemList:
        - command: SomeValue  # string
          endTime: 1  #  integer
          outputStr: SomeValue  # string
          startTime: 1  #  integer
          state: SomeValue  # string
          timeTaken: 1  #  integer
      tenantId: SomeValue  # string
      type: SomeValue  # string
      useState: SomeValue  # string
      version: 1  #  integer
    systemWorkflow:
      _id: SomeValue  # string
      addToInventory: True  # boolean
      addedOn: 1  #  integer
      configId: SomeValue  # string
      currTaskIdx: 1  #  integer
      description: SomeValue  # string
      endTime: 1  #  integer
      execTime: 1  #  integer
      imageId: SomeValue  # string
      instanceType: SomeValue  # string
      lastupdateOn: 1  #  integer
      name: SomeValue  # string
      startTime: 1  #  integer
      state: SomeValue  # string
      tasks:
      - currWorkItemIdx: 1  #  integer
        endTime: 1  #  integer
        name: SomeValue  # string
        startTime: 1  #  integer
        state: SomeValue  # string
        taskSeqNo: 1  #  integer
        timeTaken: 1  #  integer
        type: SomeValue  # string
        workItemList:
        - command: SomeValue  # string
          endTime: 1  #  integer
          outputStr: SomeValue  # string
          startTime: 1  #  integer
          state: SomeValue  # string
          timeTaken: 1  #  integer
      tenantId: SomeValue  # string
      type: SomeValue  # string
      useState: SomeValue  # string
      version: 1  #  integer
    tenantId: SomeValue  # string
    version: 1  #  integer
    workflow:
      _id: SomeValue  # string
      addToInventory: True  # boolean
      addedOn: 1  #  integer
      configId: SomeValue  # string
      currTaskIdx: 1  #  integer
      description: SomeValue  # string
      endTime: 1  #  integer
      execTime: 1  #  integer
      imageId: SomeValue  # string
      instanceType: SomeValue  # string
      lastupdateOn: 1  #  integer
      name: SomeValue  # string
      startTime: 1  #  integer
      state: SomeValue  # string
      tasks:
      - currWorkItemIdx: 1  #  integer
        endTime: 1  #  integer
        name: SomeValue  # string
        startTime: 1  #  integer
        state: SomeValue  # string
        taskSeqNo: 1  #  integer
        timeTaken: 1  #  integer
        type: SomeValue  # string
        workItemList:
        - command: SomeValue  # string
          endTime: 1  #  integer
          outputStr: SomeValue  # string
          startTime: 1  #  integer
          state: SomeValue  # string
          timeTaken: 1  #  integer
      tenantId: SomeValue  # string
      type: SomeValue  # string
      useState: SomeValue  # string
      version: 1  #  integer
    workflowParameters:
      configList:
      - configId: SomeValue  # string
        configParameters:
        - key: SomeValue  # string
          value: SomeValue  # string
      licenseLevel: SomeValue  # string
      licenseType: SomeValue  # string
      topOfStackSerialNumber: SomeValue  # string
  
- name: get_device_count
  cisco.dnac.pnp_device:
    state: query  # required
    count: True  # boolean, required
    cm_state: SomeValue  # string
    last_contact: True  # boolean
    name: SomeValue  # string
    onb_state: SomeValue  # string
    pid: SomeValue  # string
    project_id: SomeValue  # string
    project_name: SomeValue  # string
    serial_number: SomeValue  # string
    smart_account_id: SomeValue  # string
    source: SomeValue  # string
    state: SomeValue  # string
    virtual_account_id: SomeValue  # string
    workflow_id: SomeValue  # string
    workflow_name: SomeValue  # string
  register: query_result
  
- name: get_device_history
  cisco.dnac.pnp_device:
    state: query  # required
    serial_number: SomeValue  # string, required
    sort: SomeValue  # string
    sort_order: SomeValue  # string
  register: query_result
  
"""

RETURN = """
get_device_list:
    description: Returns list of devices based on filter crieteria. If a limit is not specified, it will default to return 50 devices. Pagination and sorting are also supported by this endpoint.
    returned: always
    type: dict
    contains:
    deviceInfo:
      description: Device Info, property of the response body.
      returned: always
      type: dict
      contains:
        source:
          description: It is the pnp device's source.
          returned: always
          type: str
          sample: '<source>'
        serialNumber:
          description: It is the pnp device's serialNumber.
          returned: always
          type: str
          sample: '<serialnumber>'
        stack:
          description: It is the pnp device's stack.
          returned: always
          type: bool
          sample: false
        mode:
          description: It is the pnp device's mode.
          returned: always
          type: str
          sample: '<mode>'
        state:
          description: It is the pnp device's state.
          returned: always
          type: str
          sample: '<state>'
        location:
          description: It is the pnp device's location.
          returned: always
          type: dict
          contains:
            siteId:
              description: It is the pnp device's siteId.
              returned: always
              type: str
              sample: '<siteid>'
            address:
              description: It is the pnp device's address.
              returned: always
              type: str
              sample: '<address>'
            latitude:
              description: It is the pnp device's latitude.
              returned: always
              type: str
              sample: '<latitude>'
            longitude:
              description: It is the pnp device's longitude.
              returned: always
              type: str
              sample: '<longitude>'
            altitude:
              description: It is the pnp device's altitude.
              returned: always
              type: str
              sample: '<altitude>'

        description:
          description: It is the pnp device's description.
          returned: always
          type: str
          sample: '<description>'
        onbState:
          description: It is the pnp device's onbState.
          returned: always
          type: str
          sample: '<onbstate>'
        authenticatedMicNumber:
          description: It is the pnp device's authenticatedMicNumber.
          returned: always
          type: str
          sample: '<authenticatedmicnumber>'
        authenticatedSudiSerialNo:
          description: It is the pnp device's authenticatedSudiSerialNo.
          returned: always
          type: str
          sample: '<authenticatedsudiserialno>'
        capabilitiesSupported:
          description: It is the pnp device's capabilitiesSupported.
          returned: always
          type: list
        featuresSupported:
          description: It is the pnp device's featuresSupported.
          returned: always
          type: list
        cmState:
          description: It is the pnp device's cmState.
          returned: always
          type: str
          sample: '<cmstate>'
        firstContact:
          description: It is the pnp device's firstContact.
          returned: always
          type: int
          sample: 0
        lastContact:
          description: It is the pnp device's lastContact.
          returned: always
          type: int
          sample: 0
        macAddress:
          description: It is the pnp device's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        pid:
          description: It is the pnp device's pid.
          returned: always
          type: str
          sample: '<pid>'
        deviceSudiSerialNos:
          description: It is the pnp device's deviceSudiSerialNos.
          returned: always
          type: list
        lastUpdateOn:
          description: It is the pnp device's lastUpdateOn.
          returned: always
          type: int
          sample: 0
        workflowId:
          description: It is the pnp device's workflowId.
          returned: always
          type: str
          sample: '<workflowid>'
        workflowName:
          description: It is the pnp device's workflowName.
          returned: always
          type: str
          sample: '<workflowname>'
        projectId:
          description: It is the pnp device's projectId.
          returned: always
          type: str
          sample: '<projectid>'
        projectName:
          description: It is the pnp device's projectName.
          returned: always
          type: str
          sample: '<projectname>'
        deviceType:
          description: It is the pnp device's deviceType.
          returned: always
          type: str
          sample: '<devicetype>'
        agentType:
          description: It is the pnp device's agentType.
          returned: always
          type: str
          sample: '<agenttype>'
        imageVersion:
          description: It is the pnp device's imageVersion.
          returned: always
          type: str
          sample: '<imageversion>'
        fileSystemList:
          description: It is the pnp device's fileSystemList.
          returned: always
          type: list
          contains:
            type:
              description: It is the pnp device's type.
              returned: always
              type: str
              sample: '<type>'
            writeable:
              description: It is the pnp device's writeable.
              returned: always
              type: bool
              sample: false
            freespace:
              description: It is the pnp device's freespace.
              returned: always
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: always
              type: str
              sample: '<name>'
            readable:
              description: It is the pnp device's readable.
              returned: always
              type: bool
              sample: false
            size:
              description: It is the pnp device's size.
              returned: always
              type: int
              sample: 0

        pnpProfileList:
          description: It is the pnp device's pnpProfileList.
          returned: always
          type: list
          contains:
            profileName:
              description: It is the pnp device's profileName.
              returned: always
              type: str
              sample: '<profilename>'
            discoveryCreated:
              description: It is the pnp device's discoveryCreated.
              returned: always
              type: bool
              sample: false
            createdBy:
              description: It is the pnp device's createdBy.
              returned: always
              type: str
              sample: '<createdby>'
            primaryEndpoint:
              description: It is the pnp device's primaryEndpoint.
              returned: always
              type: dict
              contains:
                port:
                  description: It is the pnp device's port.
                  returned: always
                  type: int
                  sample: 0
                protocol:
                  description: It is the pnp device's protocol.
                  returned: always
                  type: str
                  sample: '<protocol>'
                ipv4Address:
                  description: It is the pnp device's ipv4Address.
                  returned: always
                  type: dict
                ipv6Address:
                  description: It is the pnp device's ipv6Address.
                  returned: always
                  type: dict
                fqdn:
                  description: It is the pnp device's fqdn.
                  returned: always
                  type: str
                  sample: '<fqdn>'
                certificate:
                  description: It is the pnp device's certificate.
                  returned: always
                  type: str
                  sample: '<certificate>'

            secondaryEndpoint:
              description: It is the pnp device's secondaryEndpoint.
              returned: always
              type: dict
              contains:
                port:
                  description: It is the pnp device's port.
                  returned: always
                  type: int
                  sample: 0
                protocol:
                  description: It is the pnp device's protocol.
                  returned: always
                  type: str
                  sample: '<protocol>'
                ipv4Address:
                  description: It is the pnp device's ipv4Address.
                  returned: always
                  type: dict
                ipv6Address:
                  description: It is the pnp device's ipv6Address.
                  returned: always
                  type: dict
                fqdn:
                  description: It is the pnp device's fqdn.
                  returned: always
                  type: str
                  sample: '<fqdn>'
                certificate:
                  description: It is the pnp device's certificate.
                  returned: always
                  type: str
                  sample: '<certificate>'


        imageFile:
          description: It is the pnp device's imageFile.
          returned: always
          type: str
          sample: '<imagefile>'
        httpHeaders:
          description: It is the pnp device's httpHeaders.
          returned: always
          type: list
          contains:
            key:
              description: It is the pnp device's key.
              returned: always
              type: str
              sample: '<key>'
            value:
              description: It is the pnp device's value.
              returned: always
              type: str
              sample: '<value>'

        neighborLinks:
          description: It is the pnp device's neighborLinks.
          returned: always
          type: list
          contains:
            localInterfaceName:
              description: It is the pnp device's localInterfaceName.
              returned: always
              type: str
              sample: '<localinterfacename>'
            localShortInterfaceName:
              description: It is the pnp device's localShortInterfaceName.
              returned: always
              type: str
              sample: '<localshortinterfacename>'
            localMacAddress:
              description: It is the pnp device's localMacAddress.
              returned: always
              type: str
              sample: '<localmacaddress>'
            remoteInterfaceName:
              description: It is the pnp device's remoteInterfaceName.
              returned: always
              type: str
              sample: '<remoteinterfacename>'
            remoteShortInterfaceName:
              description: It is the pnp device's remoteShortInterfaceName.
              returned: always
              type: str
              sample: '<remoteshortinterfacename>'
            remoteMacAddress:
              description: It is the pnp device's remoteMacAddress.
              returned: always
              type: str
              sample: '<remotemacaddress>'
            remoteDeviceName:
              description: It is the pnp device's remoteDeviceName.
              returned: always
              type: str
              sample: '<remotedevicename>'
            remotePlatform:
              description: It is the pnp device's remotePlatform.
              returned: always
              type: str
              sample: '<remoteplatform>'
            remoteVersion:
              description: It is the pnp device's remoteVersion.
              returned: always
              type: str
              sample: '<remoteversion>'

        lastSyncTime:
          description: It is the pnp device's lastSyncTime.
          returned: always
          type: int
          sample: 0
        ipInterfaces:
          description: It is the pnp device's ipInterfaces.
          returned: always
          type: list
          contains:
            status:
              description: It is the pnp device's status.
              returned: always
              type: str
              sample: '<status>'
            macAddress:
              description: It is the pnp device's macAddress.
              returned: always
              type: str
              sample: '<macaddress>'
            ipv4Address:
              description: It is the pnp device's ipv4Address.
              returned: always
              type: dict
            ipv6AddressList:
              description: It is the pnp device's ipv6AddressList.
              returned: always
              type: list
            name:
              description: It is the pnp device's name.
              returned: always
              type: str
              sample: '<name>'

        hostname:
          description: It is the pnp device's hostname.
          returned: always
          type: str
          sample: '<hostname>'
        authStatus:
          description: It is the pnp device's authStatus.
          returned: always
          type: str
          sample: '<authstatus>'
        stackInfo:
          description: It is the pnp device's stackInfo.
          returned: always
          type: dict
          contains:
            supportsStackWorkflows:
              description: It is the pnp device's supportsStackWorkflows.
              returned: always
              type: bool
              sample: false
            isFullRing:
              description: It is the pnp device's isFullRing.
              returned: always
              type: bool
              sample: false
            stackMemberList:
              description: It is the pnp device's stackMemberList.
              returned: always
              type: list
              contains:
                serialNumber:
                  description: It is the pnp device's serialNumber.
                  returned: always
                  type: str
                  sample: '<serialnumber>'
                state:
                  description: It is the pnp device's state.
                  returned: always
                  type: str
                  sample: '<state>'
                role:
                  description: It is the pnp device's role.
                  returned: always
                  type: str
                  sample: '<role>'
                macAddress:
                  description: It is the pnp device's macAddress.
                  returned: always
                  type: str
                  sample: '<macaddress>'
                pid:
                  description: It is the pnp device's pid.
                  returned: always
                  type: str
                  sample: '<pid>'
                licenseLevel:
                  description: It is the pnp device's licenseLevel.
                  returned: always
                  type: str
                  sample: '<licenselevel>'
                licenseType:
                  description: It is the pnp device's licenseType.
                  returned: always
                  type: str
                  sample: '<licensetype>'
                sudiSerialNumber:
                  description: It is the pnp device's sudiSerialNumber.
                  returned: always
                  type: str
                  sample: '<sudiserialnumber>'
                hardwareVersion:
                  description: It is the pnp device's hardwareVersion.
                  returned: always
                  type: str
                  sample: '<hardwareversion>'
                stackNumber:
                  description: It is the pnp device's stackNumber.
                  returned: always
                  type: int
                  sample: 0
                softwareVersion:
                  description: It is the pnp device's softwareVersion.
                  returned: always
                  type: str
                  sample: '<softwareversion>'
                priority:
                  description: It is the pnp device's priority.
                  returned: always
                  type: int
                  sample: 0

            stackRingProtocol:
              description: It is the pnp device's stackRingProtocol.
              returned: always
              type: str
              sample: '<stackringprotocol>'
            validLicenseLevels:
              description: It is the pnp device's validLicenseLevels.
              returned: always
              type: list
            totalMemberCount:
              description: It is the pnp device's totalMemberCount.
              returned: always
              type: int
              sample: 0

        reloadRequested:
          description: It is the pnp device's reloadRequested.
          returned: always
          type: bool
          sample: false
        addedOn:
          description: It is the pnp device's addedOn.
          returned: always
          type: int
          sample: 0
        siteId:
          description: It is the pnp device's siteId.
          returned: always
          type: str
          sample: '<siteid>'
        aaaCredentials:
          description: It is the pnp device's aaaCredentials.
          returned: always
          type: dict
          contains:
            password:
              description: It is the pnp device's password.
              returned: always
              type: str
              sample: '*******'
            username:
              description: It is the pnp device's username.
              returned: always
              type: str
              sample: 'devnetuser'

        userMicNumbers:
          description: It is the pnp device's userMicNumbers.
          returned: always
          type: list
        userSudiSerialNos:
          description: It is the pnp device's userSudiSerialNos.
          returned: always
          type: list
        addnMacAddrs:
          description: It is the pnp device's addnMacAddrs.
          returned: always
          type: list
        preWorkflowCliOuputs:
          description: It is the pnp device's preWorkflowCliOuputs.
          returned: always
          type: list
          contains:
            cli:
              description: It is the pnp device's cli.
              returned: always
              type: str
              sample: '<cli>'
            cliOutput:
              description: It is the pnp device's cliOutput.
              returned: always
              type: str
              sample: '<clioutput>'

        tags:
          description: It is the pnp device's tags.
          returned: always
          type: dict
        sudiRequired:
          description: It is the pnp device's sudiRequired.
          returned: always
          type: bool
          sample: false
        smartAccountId:
          description: It is the pnp device's smartAccountId.
          returned: always
          type: str
          sample: '<smartaccountid>'
        virtualAccountId:
          description: It is the pnp device's virtualAccountId.
          returned: always
          type: str
          sample: '<virtualaccountid>'
        populateInventory:
          description: It is the pnp device's populateInventory.
          returned: always
          type: bool
          sample: false
        siteName:
          description: It is the pnp device's siteName.
          returned: always
          type: str
          sample: '<sitename>'
        name:
          description: It is the pnp device's name.
          returned: always
          type: str
          sample: '<name>'

    systemResetWorkflow:
      description: System Reset Workflow, property of the response body.
      returned: always
      type: dict
      contains:
        _id:
          description: It is the pnp device's _id.
          returned: always
          type: str
          sample: '<_id>'
        state:
          description: It is the pnp device's state.
          returned: always
          type: str
          sample: '<state>'
        type:
          description: It is the pnp device's type.
          returned: always
          type: str
          sample: '<type>'
        description:
          description: It is the pnp device's description.
          returned: always
          type: str
          sample: '<description>'
        lastupdateOn:
          description: It is the pnp device's lastupdateOn.
          returned: always
          type: int
          sample: 0
        imageId:
          description: It is the pnp device's imageId.
          returned: always
          type: str
          sample: '<imageid>'
        currTaskIdx:
          description: It is the pnp device's currTaskIdx.
          returned: always
          type: int
          sample: 0
        addedOn:
          description: It is the pnp device's addedOn.
          returned: always
          type: int
          sample: 0
        tasks:
          description: It is the pnp device's tasks.
          returned: always
          type: list
          contains:
            state:
              description: It is the pnp device's state.
              returned: always
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device's type.
              returned: always
              type: str
              sample: '<type>'
            currWorkItemIdx:
              description: It is the pnp device's currWorkItemIdx.
              returned: always
              type: int
              sample: 0
            taskSeqNo:
              description: It is the pnp device's taskSeqNo.
              returned: always
              type: int
              sample: 0
            endTime:
              description: It is the pnp device's endTime.
              returned: always
              type: int
              sample: 0
            startTime:
              description: It is the pnp device's startTime.
              returned: always
              type: int
              sample: 0
            workItemList:
              description: It is the pnp device's workItemList.
              returned: always
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: always
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: always
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: always
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: always
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: always
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: always
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: always
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: always
              type: str
              sample: '<name>'

        addToInventory:
          description: It is the pnp device's addToInventory.
          returned: always
          type: bool
          sample: false
        instanceType:
          description: It is the pnp device's instanceType.
          returned: always
          type: str
          sample: '<instancetype>'
        endTime:
          description: It is the pnp device's endTime.
          returned: always
          type: int
          sample: 0
        execTime:
          description: It is the pnp device's execTime.
          returned: always
          type: int
          sample: 0
        startTime:
          description: It is the pnp device's startTime.
          returned: always
          type: int
          sample: 0
        useState:
          description: It is the pnp device's useState.
          returned: always
          type: str
          sample: '<usestate>'
        configId:
          description: It is the pnp device's configId.
          returned: always
          type: str
          sample: '<configid>'
        name:
          description: It is the pnp device's name.
          returned: always
          type: str
          sample: '<name>'
        version:
          description: It is the pnp device's version.
          returned: always
          type: int
          sample: 0
        tenantId:
          description: It is the pnp device's tenantId.
          returned: always
          type: str
          sample: '<tenantid>'

    systemWorkflow:
      description: System Workflow, property of the response body.
      returned: always
      type: dict
      contains:
        _id:
          description: It is the pnp device's _id.
          returned: always
          type: str
          sample: '<_id>'
        state:
          description: It is the pnp device's state.
          returned: always
          type: str
          sample: '<state>'
        type:
          description: It is the pnp device's type.
          returned: always
          type: str
          sample: '<type>'
        description:
          description: It is the pnp device's description.
          returned: always
          type: str
          sample: '<description>'
        lastupdateOn:
          description: It is the pnp device's lastupdateOn.
          returned: always
          type: int
          sample: 0
        imageId:
          description: It is the pnp device's imageId.
          returned: always
          type: str
          sample: '<imageid>'
        currTaskIdx:
          description: It is the pnp device's currTaskIdx.
          returned: always
          type: int
          sample: 0
        addedOn:
          description: It is the pnp device's addedOn.
          returned: always
          type: int
          sample: 0
        tasks:
          description: It is the pnp device's tasks.
          returned: always
          type: list
          contains:
            state:
              description: It is the pnp device's state.
              returned: always
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device's type.
              returned: always
              type: str
              sample: '<type>'
            currWorkItemIdx:
              description: It is the pnp device's currWorkItemIdx.
              returned: always
              type: int
              sample: 0
            taskSeqNo:
              description: It is the pnp device's taskSeqNo.
              returned: always
              type: int
              sample: 0
            endTime:
              description: It is the pnp device's endTime.
              returned: always
              type: int
              sample: 0
            startTime:
              description: It is the pnp device's startTime.
              returned: always
              type: int
              sample: 0
            workItemList:
              description: It is the pnp device's workItemList.
              returned: always
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: always
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: always
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: always
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: always
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: always
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: always
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: always
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: always
              type: str
              sample: '<name>'

        addToInventory:
          description: It is the pnp device's addToInventory.
          returned: always
          type: bool
          sample: false
        instanceType:
          description: It is the pnp device's instanceType.
          returned: always
          type: str
          sample: '<instancetype>'
        endTime:
          description: It is the pnp device's endTime.
          returned: always
          type: int
          sample: 0
        execTime:
          description: It is the pnp device's execTime.
          returned: always
          type: int
          sample: 0
        startTime:
          description: It is the pnp device's startTime.
          returned: always
          type: int
          sample: 0
        useState:
          description: It is the pnp device's useState.
          returned: always
          type: str
          sample: '<usestate>'
        configId:
          description: It is the pnp device's configId.
          returned: always
          type: str
          sample: '<configid>'
        name:
          description: It is the pnp device's name.
          returned: always
          type: str
          sample: '<name>'
        version:
          description: It is the pnp device's version.
          returned: always
          type: int
          sample: 0
        tenantId:
          description: It is the pnp device's tenantId.
          returned: always
          type: str
          sample: '<tenantid>'

    workflow:
      description: Workflow, property of the response body.
      returned: always
      type: dict
      contains:
        _id:
          description: It is the pnp device's _id.
          returned: always
          type: str
          sample: '<_id>'
        state:
          description: It is the pnp device's state.
          returned: always
          type: str
          sample: '<state>'
        type:
          description: It is the pnp device's type.
          returned: always
          type: str
          sample: '<type>'
        description:
          description: It is the pnp device's description.
          returned: always
          type: str
          sample: '<description>'
        lastupdateOn:
          description: It is the pnp device's lastupdateOn.
          returned: always
          type: int
          sample: 0
        imageId:
          description: It is the pnp device's imageId.
          returned: always
          type: str
          sample: '<imageid>'
        currTaskIdx:
          description: It is the pnp device's currTaskIdx.
          returned: always
          type: int
          sample: 0
        addedOn:
          description: It is the pnp device's addedOn.
          returned: always
          type: int
          sample: 0
        tasks:
          description: It is the pnp device's tasks.
          returned: always
          type: list
          contains:
            state:
              description: It is the pnp device's state.
              returned: always
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device's type.
              returned: always
              type: str
              sample: '<type>'
            currWorkItemIdx:
              description: It is the pnp device's currWorkItemIdx.
              returned: always
              type: int
              sample: 0
            taskSeqNo:
              description: It is the pnp device's taskSeqNo.
              returned: always
              type: int
              sample: 0
            endTime:
              description: It is the pnp device's endTime.
              returned: always
              type: int
              sample: 0
            startTime:
              description: It is the pnp device's startTime.
              returned: always
              type: int
              sample: 0
            workItemList:
              description: It is the pnp device's workItemList.
              returned: always
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: always
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: always
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: always
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: always
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: always
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: always
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: always
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: always
              type: str
              sample: '<name>'

        addToInventory:
          description: It is the pnp device's addToInventory.
          returned: always
          type: bool
          sample: false
        instanceType:
          description: It is the pnp device's instanceType.
          returned: always
          type: str
          sample: '<instancetype>'
        endTime:
          description: It is the pnp device's endTime.
          returned: always
          type: int
          sample: 0
        execTime:
          description: It is the pnp device's execTime.
          returned: always
          type: int
          sample: 0
        startTime:
          description: It is the pnp device's startTime.
          returned: always
          type: int
          sample: 0
        useState:
          description: It is the pnp device's useState.
          returned: always
          type: str
          sample: '<usestate>'
        configId:
          description: It is the pnp device's configId.
          returned: always
          type: str
          sample: '<configid>'
        name:
          description: It is the pnp device's name.
          returned: always
          type: str
          sample: '<name>'
        version:
          description: It is the pnp device's version.
          returned: always
          type: int
          sample: 0
        tenantId:
          description: It is the pnp device's tenantId.
          returned: always
          type: str
          sample: '<tenantid>'

    runSummaryList:
      description: Run Summary List, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        details:
          description: It is the pnp device's details.
          returned: always
          type: str
          sample: '<details>'
        historyTaskInfo:
          description: It is the pnp device's historyTaskInfo.
          returned: always
          type: dict
          contains:
            type:
              description: It is the pnp device's type.
              returned: always
              type: str
              sample: '<type>'
            workItemList:
              description: It is the pnp device's workItemList.
              returned: always
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: always
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: always
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: always
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: always
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: always
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: always
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: always
              type: int
              sample: 0
            addnDetails:
              description: It is the pnp device's addnDetails.
              returned: always
              type: list
              contains:
                key:
                  description: It is the pnp device's key.
                  returned: always
                  type: str
                  sample: '<key>'
                value:
                  description: It is the pnp device's value.
                  returned: always
                  type: str
                  sample: '<value>'

            name:
              description: It is the pnp device's name.
              returned: always
              type: str
              sample: '<name>'

        errorFlag:
          description: It is the pnp device's errorFlag.
          returned: always
          type: bool
          sample: false
        timestamp:
          description: It is the pnp device's timestamp.
          returned: always
          type: int
          sample: 0

    workflowParameters:
      description: Workflow Parameters, property of the response body.
      returned: always
      type: dict
      contains:
        topOfStackSerialNumber:
          description: It is the pnp device's topOfStackSerialNumber.
          returned: always
          type: str
          sample: '<topofstackserialnumber>'
        licenseLevel:
          description: It is the pnp device's licenseLevel.
          returned: always
          type: str
          sample: '<licenselevel>'
        licenseType:
          description: It is the pnp device's licenseType.
          returned: always
          type: str
          sample: '<licensetype>'
        configList:
          description: It is the pnp device's configList.
          returned: always
          type: list
          contains:
            configParameters:
              description: It is the pnp device's configParameters.
              returned: always
              type: list
              contains:
                key:
                  description: It is the pnp device's key.
                  returned: always
                  type: str
                  sample: '<key>'
                value:
                  description: It is the pnp device's value.
                  returned: always
                  type: str
                  sample: '<value>'

            configId:
              description: It is the pnp device's configId.
              returned: always
              type: str
              sample: '<configid>'


    dayZeroConfig:
      description: Day Zero Config, property of the response body.
      returned: always
      type: dict
      contains:
        config:
          description: It is the pnp device's config.
          returned: always
          type: str
          sample: '<config>'

    dayZeroConfigPreview:
      description: Day Zero Config Preview, property of the response body.
      returned: always
      type: dict
    version:
      description: Version, property of the response body.
      returned: always
      type: int
      sample: 0
    tenantId:
      description: Tenant Id, property of the response body.
      returned: always
      type: str
      sample: '<tenantid>'

add_device:
    description: Adds a device to the PnP database.
    returned: success
    type: dict
    contains:
    _id:
      description: Device's Id.
      returned: success
      type: str
      sample: '<_id>'
    deviceInfo:
      description: Device's Device Info.
      returned: success
      type: dict
      contains:
        source:
          description: It is the pnp device's source.
          returned: success
          type: str
          sample: '<source>'
        serialNumber:
          description: It is the pnp device's serialNumber.
          returned: success
          type: str
          sample: '<serialnumber>'
        stack:
          description: It is the pnp device's stack.
          returned: success
          type: bool
          sample: false
        mode:
          description: It is the pnp device's mode.
          returned: success
          type: str
          sample: '<mode>'
        state:
          description: It is the pnp device's state.
          returned: success
          type: str
          sample: '<state>'
        location:
          description: It is the pnp device's location.
          returned: success
          type: dict
          contains:
            siteId:
              description: It is the pnp device's siteId.
              returned: success
              type: str
              sample: '<siteid>'
            address:
              description: It is the pnp device's address.
              returned: success
              type: str
              sample: '<address>'
            latitude:
              description: It is the pnp device's latitude.
              returned: success
              type: str
              sample: '<latitude>'
            longitude:
              description: It is the pnp device's longitude.
              returned: success
              type: str
              sample: '<longitude>'
            altitude:
              description: It is the pnp device's altitude.
              returned: success
              type: str
              sample: '<altitude>'

        description:
          description: It is the pnp device's description.
          returned: success
          type: str
          sample: '<description>'
        onbState:
          description: It is the pnp device's onbState.
          returned: success
          type: str
          sample: '<onbstate>'
        authenticatedMicNumber:
          description: It is the pnp device's authenticatedMicNumber.
          returned: success
          type: str
          sample: '<authenticatedmicnumber>'
        authenticatedSudiSerialNo:
          description: It is the pnp device's authenticatedSudiSerialNo.
          returned: success
          type: str
          sample: '<authenticatedsudiserialno>'
        capabilitiesSupported:
          description: It is the pnp device's capabilitiesSupported.
          returned: success
          type: list
        featuresSupported:
          description: It is the pnp device's featuresSupported.
          returned: success
          type: list
        cmState:
          description: It is the pnp device's cmState.
          returned: success
          type: str
          sample: '<cmstate>'
        firstContact:
          description: It is the pnp device's firstContact.
          returned: success
          type: int
          sample: 0
        lastContact:
          description: It is the pnp device's lastContact.
          returned: success
          type: int
          sample: 0
        macAddress:
          description: It is the pnp device's macAddress.
          returned: success
          type: str
          sample: '<macaddress>'
        pid:
          description: It is the pnp device's pid.
          returned: success
          type: str
          sample: '<pid>'
        deviceSudiSerialNos:
          description: It is the pnp device's deviceSudiSerialNos.
          returned: success
          type: list
        lastUpdateOn:
          description: It is the pnp device's lastUpdateOn.
          returned: success
          type: int
          sample: 0
        workflowId:
          description: It is the pnp device's workflowId.
          returned: success
          type: str
          sample: '<workflowid>'
        workflowName:
          description: It is the pnp device's workflowName.
          returned: success
          type: str
          sample: '<workflowname>'
        projectId:
          description: It is the pnp device's projectId.
          returned: success
          type: str
          sample: '<projectid>'
        projectName:
          description: It is the pnp device's projectName.
          returned: success
          type: str
          sample: '<projectname>'
        deviceType:
          description: It is the pnp device's deviceType.
          returned: success
          type: str
          sample: '<devicetype>'
        agentType:
          description: It is the pnp device's agentType.
          returned: success
          type: str
          sample: '<agenttype>'
        imageVersion:
          description: It is the pnp device's imageVersion.
          returned: success
          type: str
          sample: '<imageversion>'
        fileSystemList:
          description: It is the pnp device's fileSystemList.
          returned: success
          type: list
          contains:
            type:
              description: It is the pnp device's type.
              returned: success
              type: str
              sample: '<type>'
            writeable:
              description: It is the pnp device's writeable.
              returned: success
              type: bool
              sample: false
            freespace:
              description: It is the pnp device's freespace.
              returned: success
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: success
              type: str
              sample: '<name>'
            readable:
              description: It is the pnp device's readable.
              returned: success
              type: bool
              sample: false
            size:
              description: It is the pnp device's size.
              returned: success
              type: int
              sample: 0

        pnpProfileList:
          description: It is the pnp device's pnpProfileList.
          returned: success
          type: list
          contains:
            profileName:
              description: It is the pnp device's profileName.
              returned: success
              type: str
              sample: '<profilename>'
            discoveryCreated:
              description: It is the pnp device's discoveryCreated.
              returned: success
              type: bool
              sample: false
            createdBy:
              description: It is the pnp device's createdBy.
              returned: success
              type: str
              sample: '<createdby>'
            primaryEndpoint:
              description: It is the pnp device's primaryEndpoint.
              returned: success
              type: dict
              contains:
                port:
                  description: It is the pnp device's port.
                  returned: success
                  type: int
                  sample: 0
                protocol:
                  description: It is the pnp device's protocol.
                  returned: success
                  type: str
                  sample: '<protocol>'
                ipv4Address:
                  description: It is the pnp device's ipv4Address.
                  returned: success
                  type: dict
                ipv6Address:
                  description: It is the pnp device's ipv6Address.
                  returned: success
                  type: dict
                fqdn:
                  description: It is the pnp device's fqdn.
                  returned: success
                  type: str
                  sample: '<fqdn>'
                certificate:
                  description: It is the pnp device's certificate.
                  returned: success
                  type: str
                  sample: '<certificate>'

            secondaryEndpoint:
              description: It is the pnp device's secondaryEndpoint.
              returned: success
              type: dict
              contains:
                port:
                  description: It is the pnp device's port.
                  returned: success
                  type: int
                  sample: 0
                protocol:
                  description: It is the pnp device's protocol.
                  returned: success
                  type: str
                  sample: '<protocol>'
                ipv4Address:
                  description: It is the pnp device's ipv4Address.
                  returned: success
                  type: dict
                ipv6Address:
                  description: It is the pnp device's ipv6Address.
                  returned: success
                  type: dict
                fqdn:
                  description: It is the pnp device's fqdn.
                  returned: success
                  type: str
                  sample: '<fqdn>'
                certificate:
                  description: It is the pnp device's certificate.
                  returned: success
                  type: str
                  sample: '<certificate>'


        imageFile:
          description: It is the pnp device's imageFile.
          returned: success
          type: str
          sample: '<imagefile>'
        httpHeaders:
          description: It is the pnp device's httpHeaders.
          returned: success
          type: list
          contains:
            key:
              description: It is the pnp device's key.
              returned: success
              type: str
              sample: '<key>'
            value:
              description: It is the pnp device's value.
              returned: success
              type: str
              sample: '<value>'

        neighborLinks:
          description: It is the pnp device's neighborLinks.
          returned: success
          type: list
          contains:
            localInterfaceName:
              description: It is the pnp device's localInterfaceName.
              returned: success
              type: str
              sample: '<localinterfacename>'
            localShortInterfaceName:
              description: It is the pnp device's localShortInterfaceName.
              returned: success
              type: str
              sample: '<localshortinterfacename>'
            localMacAddress:
              description: It is the pnp device's localMacAddress.
              returned: success
              type: str
              sample: '<localmacaddress>'
            remoteInterfaceName:
              description: It is the pnp device's remoteInterfaceName.
              returned: success
              type: str
              sample: '<remoteinterfacename>'
            remoteShortInterfaceName:
              description: It is the pnp device's remoteShortInterfaceName.
              returned: success
              type: str
              sample: '<remoteshortinterfacename>'
            remoteMacAddress:
              description: It is the pnp device's remoteMacAddress.
              returned: success
              type: str
              sample: '<remotemacaddress>'
            remoteDeviceName:
              description: It is the pnp device's remoteDeviceName.
              returned: success
              type: str
              sample: '<remotedevicename>'
            remotePlatform:
              description: It is the pnp device's remotePlatform.
              returned: success
              type: str
              sample: '<remoteplatform>'
            remoteVersion:
              description: It is the pnp device's remoteVersion.
              returned: success
              type: str
              sample: '<remoteversion>'

        lastSyncTime:
          description: It is the pnp device's lastSyncTime.
          returned: success
          type: int
          sample: 0
        ipInterfaces:
          description: It is the pnp device's ipInterfaces.
          returned: success
          type: list
          contains:
            status:
              description: It is the pnp device's status.
              returned: success
              type: str
              sample: '<status>'
            macAddress:
              description: It is the pnp device's macAddress.
              returned: success
              type: str
              sample: '<macaddress>'
            ipv4Address:
              description: It is the pnp device's ipv4Address.
              returned: success
              type: dict
            ipv6AddressList:
              description: It is the pnp device's ipv6AddressList.
              returned: success
              type: list
            name:
              description: It is the pnp device's name.
              returned: success
              type: str
              sample: '<name>'

        hostname:
          description: It is the pnp device's hostname.
          returned: success
          type: str
          sample: '<hostname>'
        authStatus:
          description: It is the pnp device's authStatus.
          returned: success
          type: str
          sample: '<authstatus>'
        stackInfo:
          description: It is the pnp device's stackInfo.
          returned: success
          type: dict
          contains:
            supportsStackWorkflows:
              description: It is the pnp device's supportsStackWorkflows.
              returned: success
              type: bool
              sample: false
            isFullRing:
              description: It is the pnp device's isFullRing.
              returned: success
              type: bool
              sample: false
            stackMemberList:
              description: It is the pnp device's stackMemberList.
              returned: success
              type: list
              contains:
                serialNumber:
                  description: It is the pnp device's serialNumber.
                  returned: success
                  type: str
                  sample: '<serialnumber>'
                state:
                  description: It is the pnp device's state.
                  returned: success
                  type: str
                  sample: '<state>'
                role:
                  description: It is the pnp device's role.
                  returned: success
                  type: str
                  sample: '<role>'
                macAddress:
                  description: It is the pnp device's macAddress.
                  returned: success
                  type: str
                  sample: '<macaddress>'
                pid:
                  description: It is the pnp device's pid.
                  returned: success
                  type: str
                  sample: '<pid>'
                licenseLevel:
                  description: It is the pnp device's licenseLevel.
                  returned: success
                  type: str
                  sample: '<licenselevel>'
                licenseType:
                  description: It is the pnp device's licenseType.
                  returned: success
                  type: str
                  sample: '<licensetype>'
                sudiSerialNumber:
                  description: It is the pnp device's sudiSerialNumber.
                  returned: success
                  type: str
                  sample: '<sudiserialnumber>'
                hardwareVersion:
                  description: It is the pnp device's hardwareVersion.
                  returned: success
                  type: str
                  sample: '<hardwareversion>'
                stackNumber:
                  description: It is the pnp device's stackNumber.
                  returned: success
                  type: int
                  sample: 0
                softwareVersion:
                  description: It is the pnp device's softwareVersion.
                  returned: success
                  type: str
                  sample: '<softwareversion>'
                priority:
                  description: It is the pnp device's priority.
                  returned: success
                  type: int
                  sample: 0

            stackRingProtocol:
              description: It is the pnp device's stackRingProtocol.
              returned: success
              type: str
              sample: '<stackringprotocol>'
            validLicenseLevels:
              description: It is the pnp device's validLicenseLevels.
              returned: success
              type: list
            totalMemberCount:
              description: It is the pnp device's totalMemberCount.
              returned: success
              type: int
              sample: 0

        reloadRequested:
          description: It is the pnp device's reloadRequested.
          returned: success
          type: bool
          sample: false
        addedOn:
          description: It is the pnp device's addedOn.
          returned: success
          type: int
          sample: 0
        siteId:
          description: It is the pnp device's siteId.
          returned: success
          type: str
          sample: '<siteid>'
        aaaCredentials:
          description: It is the pnp device's aaaCredentials.
          returned: success
          type: dict
          contains:
            password:
              description: It is the pnp device's password.
              returned: success
              type: str
              sample: '*******'
            username:
              description: It is the pnp device's username.
              returned: success
              type: str
              sample: 'devnetuser'

        userMicNumbers:
          description: It is the pnp device's userMicNumbers.
          returned: success
          type: list
        userSudiSerialNos:
          description: It is the pnp device's userSudiSerialNos.
          returned: success
          type: list
        addnMacAddrs:
          description: It is the pnp device's addnMacAddrs.
          returned: success
          type: list
        preWorkflowCliOuputs:
          description: It is the pnp device's preWorkflowCliOuputs.
          returned: success
          type: list
          contains:
            cli:
              description: It is the pnp device's cli.
              returned: success
              type: str
              sample: '<cli>'
            cliOutput:
              description: It is the pnp device's cliOutput.
              returned: success
              type: str
              sample: '<clioutput>'

        tags:
          description: It is the pnp device's tags.
          returned: success
          type: dict
        sudiRequired:
          description: It is the pnp device's sudiRequired.
          returned: success
          type: bool
          sample: false
        smartAccountId:
          description: It is the pnp device's smartAccountId.
          returned: success
          type: str
          sample: '<smartaccountid>'
        virtualAccountId:
          description: It is the pnp device's virtualAccountId.
          returned: success
          type: str
          sample: '<virtualaccountid>'
        populateInventory:
          description: It is the pnp device's populateInventory.
          returned: success
          type: bool
          sample: false
        siteName:
          description: It is the pnp device's siteName.
          returned: success
          type: str
          sample: '<sitename>'
        name:
          description: It is the pnp device's name.
          returned: success
          type: str
          sample: '<name>'

    systemResetWorkflow:
      description: Device's System Reset Workflow.
      returned: success
      type: dict
      contains:
        _id:
          description: It is the pnp device's _id.
          returned: success
          type: str
          sample: '<_id>'
        state:
          description: It is the pnp device's state.
          returned: success
          type: str
          sample: '<state>'
        type:
          description: It is the pnp device's type.
          returned: success
          type: str
          sample: '<type>'
        description:
          description: It is the pnp device's description.
          returned: success
          type: str
          sample: '<description>'
        lastupdateOn:
          description: It is the pnp device's lastupdateOn.
          returned: success
          type: int
          sample: 0
        imageId:
          description: It is the pnp device's imageId.
          returned: success
          type: str
          sample: '<imageid>'
        currTaskIdx:
          description: It is the pnp device's currTaskIdx.
          returned: success
          type: int
          sample: 0
        addedOn:
          description: It is the pnp device's addedOn.
          returned: success
          type: int
          sample: 0
        tasks:
          description: It is the pnp device's tasks.
          returned: success
          type: list
          contains:
            state:
              description: It is the pnp device's state.
              returned: success
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device's type.
              returned: success
              type: str
              sample: '<type>'
            currWorkItemIdx:
              description: It is the pnp device's currWorkItemIdx.
              returned: success
              type: int
              sample: 0
            taskSeqNo:
              description: It is the pnp device's taskSeqNo.
              returned: success
              type: int
              sample: 0
            endTime:
              description: It is the pnp device's endTime.
              returned: success
              type: int
              sample: 0
            startTime:
              description: It is the pnp device's startTime.
              returned: success
              type: int
              sample: 0
            workItemList:
              description: It is the pnp device's workItemList.
              returned: success
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: success
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: success
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: success
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: success
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: success
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: success
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: success
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: success
              type: str
              sample: '<name>'

        addToInventory:
          description: It is the pnp device's addToInventory.
          returned: success
          type: bool
          sample: false
        instanceType:
          description: It is the pnp device's instanceType.
          returned: success
          type: str
          sample: '<instancetype>'
        endTime:
          description: It is the pnp device's endTime.
          returned: success
          type: int
          sample: 0
        execTime:
          description: It is the pnp device's execTime.
          returned: success
          type: int
          sample: 0
        startTime:
          description: It is the pnp device's startTime.
          returned: success
          type: int
          sample: 0
        useState:
          description: It is the pnp device's useState.
          returned: success
          type: str
          sample: '<usestate>'
        configId:
          description: It is the pnp device's configId.
          returned: success
          type: str
          sample: '<configid>'
        name:
          description: It is the pnp device's name.
          returned: success
          type: str
          sample: '<name>'
        version:
          description: It is the pnp device's version.
          returned: success
          type: int
          sample: 0
        tenantId:
          description: It is the pnp device's tenantId.
          returned: success
          type: str
          sample: '<tenantid>'

    systemWorkflow:
      description: Device's System Workflow.
      returned: success
      type: dict
      contains:
        _id:
          description: It is the pnp device's _id.
          returned: success
          type: str
          sample: '<_id>'
        state:
          description: It is the pnp device's state.
          returned: success
          type: str
          sample: '<state>'
        type:
          description: It is the pnp device's type.
          returned: success
          type: str
          sample: '<type>'
        description:
          description: It is the pnp device's description.
          returned: success
          type: str
          sample: '<description>'
        lastupdateOn:
          description: It is the pnp device's lastupdateOn.
          returned: success
          type: int
          sample: 0
        imageId:
          description: It is the pnp device's imageId.
          returned: success
          type: str
          sample: '<imageid>'
        currTaskIdx:
          description: It is the pnp device's currTaskIdx.
          returned: success
          type: int
          sample: 0
        addedOn:
          description: It is the pnp device's addedOn.
          returned: success
          type: int
          sample: 0
        tasks:
          description: It is the pnp device's tasks.
          returned: success
          type: list
          contains:
            state:
              description: It is the pnp device's state.
              returned: success
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device's type.
              returned: success
              type: str
              sample: '<type>'
            currWorkItemIdx:
              description: It is the pnp device's currWorkItemIdx.
              returned: success
              type: int
              sample: 0
            taskSeqNo:
              description: It is the pnp device's taskSeqNo.
              returned: success
              type: int
              sample: 0
            endTime:
              description: It is the pnp device's endTime.
              returned: success
              type: int
              sample: 0
            startTime:
              description: It is the pnp device's startTime.
              returned: success
              type: int
              sample: 0
            workItemList:
              description: It is the pnp device's workItemList.
              returned: success
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: success
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: success
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: success
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: success
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: success
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: success
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: success
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: success
              type: str
              sample: '<name>'

        addToInventory:
          description: It is the pnp device's addToInventory.
          returned: success
          type: bool
          sample: false
        instanceType:
          description: It is the pnp device's instanceType.
          returned: success
          type: str
          sample: '<instancetype>'
        endTime:
          description: It is the pnp device's endTime.
          returned: success
          type: int
          sample: 0
        execTime:
          description: It is the pnp device's execTime.
          returned: success
          type: int
          sample: 0
        startTime:
          description: It is the pnp device's startTime.
          returned: success
          type: int
          sample: 0
        useState:
          description: It is the pnp device's useState.
          returned: success
          type: str
          sample: '<usestate>'
        configId:
          description: It is the pnp device's configId.
          returned: success
          type: str
          sample: '<configid>'
        name:
          description: It is the pnp device's name.
          returned: success
          type: str
          sample: '<name>'
        version:
          description: It is the pnp device's version.
          returned: success
          type: int
          sample: 0
        tenantId:
          description: It is the pnp device's tenantId.
          returned: success
          type: str
          sample: '<tenantid>'

    workflow:
      description: Device's Workflow.
      returned: success
      type: dict
      contains:
        _id:
          description: It is the pnp device's _id.
          returned: success
          type: str
          sample: '<_id>'
        state:
          description: It is the pnp device's state.
          returned: success
          type: str
          sample: '<state>'
        type:
          description: It is the pnp device's type.
          returned: success
          type: str
          sample: '<type>'
        description:
          description: It is the pnp device's description.
          returned: success
          type: str
          sample: '<description>'
        lastupdateOn:
          description: It is the pnp device's lastupdateOn.
          returned: success
          type: int
          sample: 0
        imageId:
          description: It is the pnp device's imageId.
          returned: success
          type: str
          sample: '<imageid>'
        currTaskIdx:
          description: It is the pnp device's currTaskIdx.
          returned: success
          type: int
          sample: 0
        addedOn:
          description: It is the pnp device's addedOn.
          returned: success
          type: int
          sample: 0
        tasks:
          description: It is the pnp device's tasks.
          returned: success
          type: list
          contains:
            state:
              description: It is the pnp device's state.
              returned: success
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device's type.
              returned: success
              type: str
              sample: '<type>'
            currWorkItemIdx:
              description: It is the pnp device's currWorkItemIdx.
              returned: success
              type: int
              sample: 0
            taskSeqNo:
              description: It is the pnp device's taskSeqNo.
              returned: success
              type: int
              sample: 0
            endTime:
              description: It is the pnp device's endTime.
              returned: success
              type: int
              sample: 0
            startTime:
              description: It is the pnp device's startTime.
              returned: success
              type: int
              sample: 0
            workItemList:
              description: It is the pnp device's workItemList.
              returned: success
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: success
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: success
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: success
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: success
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: success
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: success
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: success
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: success
              type: str
              sample: '<name>'

        addToInventory:
          description: It is the pnp device's addToInventory.
          returned: success
          type: bool
          sample: false
        instanceType:
          description: It is the pnp device's instanceType.
          returned: success
          type: str
          sample: '<instancetype>'
        endTime:
          description: It is the pnp device's endTime.
          returned: success
          type: int
          sample: 0
        execTime:
          description: It is the pnp device's execTime.
          returned: success
          type: int
          sample: 0
        startTime:
          description: It is the pnp device's startTime.
          returned: success
          type: int
          sample: 0
        useState:
          description: It is the pnp device's useState.
          returned: success
          type: str
          sample: '<usestate>'
        configId:
          description: It is the pnp device's configId.
          returned: success
          type: str
          sample: '<configid>'
        name:
          description: It is the pnp device's name.
          returned: success
          type: str
          sample: '<name>'
        version:
          description: It is the pnp device's version.
          returned: success
          type: int
          sample: 0
        tenantId:
          description: It is the pnp device's tenantId.
          returned: success
          type: str
          sample: '<tenantid>'

    runSummaryList:
      description: Device's Run Summary List (list of objects).
      returned: success
      type: list
      contains:
        details:
          description: It is the pnp device's details.
          returned: success
          type: str
          sample: '<details>'
        historyTaskInfo:
          description: It is the pnp device's historyTaskInfo.
          returned: success
          type: dict
          contains:
            type:
              description: It is the pnp device's type.
              returned: success
              type: str
              sample: '<type>'
            workItemList:
              description: It is the pnp device's workItemList.
              returned: success
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: success
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: success
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: success
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: success
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: success
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: success
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: success
              type: int
              sample: 0
            addnDetails:
              description: It is the pnp device's addnDetails.
              returned: success
              type: list
              contains:
                key:
                  description: It is the pnp device's key.
                  returned: success
                  type: str
                  sample: '<key>'
                value:
                  description: It is the pnp device's value.
                  returned: success
                  type: str
                  sample: '<value>'

            name:
              description: It is the pnp device's name.
              returned: success
              type: str
              sample: '<name>'

        errorFlag:
          description: It is the pnp device's errorFlag.
          returned: success
          type: bool
          sample: false
        timestamp:
          description: It is the pnp device's timestamp.
          returned: success
          type: int
          sample: 0

    workflowParameters:
      description: Device's Workflow Parameters.
      returned: success
      type: dict
      contains:
        topOfStackSerialNumber:
          description: It is the pnp device's topOfStackSerialNumber.
          returned: success
          type: str
          sample: '<topofstackserialnumber>'
        licenseLevel:
          description: It is the pnp device's licenseLevel.
          returned: success
          type: str
          sample: '<licenselevel>'
        licenseType:
          description: It is the pnp device's licenseType.
          returned: success
          type: str
          sample: '<licensetype>'
        configList:
          description: It is the pnp device's configList.
          returned: success
          type: list
          contains:
            configParameters:
              description: It is the pnp device's configParameters.
              returned: success
              type: list
              contains:
                key:
                  description: It is the pnp device's key.
                  returned: success
                  type: str
                  sample: '<key>'
                value:
                  description: It is the pnp device's value.
                  returned: success
                  type: str
                  sample: '<value>'

            configId:
              description: It is the pnp device's configId.
              returned: success
              type: str
              sample: '<configid>'


    dayZeroConfig:
      description: Device's Day Zero Config.
      returned: success
      type: dict
      contains:
        config:
          description: It is the pnp device's config.
          returned: success
          type: str
          sample: '<config>'

    dayZeroConfigPreview:
      description: Device's Day Zero Config Preview.
      returned: success
      type: dict
    version:
      description: Device's version.
      returned: success
      type: int
      sample: 0
    tenantId:
      description: Device's Tenant Id.
      returned: success
      type: str
      sample: '<tenantid>'

get_device_by_id:
    description: Returns device details specified by device id.
    returned: always
    type: dict
    contains:
    _id:
      description: Id, property of the response body.
      returned: always
      type: str
      sample: '<_id>'
    deviceInfo:
      description: Device Info, property of the response body.
      returned: always
      type: dict
      contains:
        source:
          description: It is the pnp device's source.
          returned: always
          type: str
          sample: '<source>'
        serialNumber:
          description: It is the pnp device's serialNumber.
          returned: always
          type: str
          sample: '<serialnumber>'
        stack:
          description: It is the pnp device's stack.
          returned: always
          type: bool
          sample: false
        mode:
          description: It is the pnp device's mode.
          returned: always
          type: str
          sample: '<mode>'
        state:
          description: It is the pnp device's state.
          returned: always
          type: str
          sample: '<state>'
        location:
          description: It is the pnp device's location.
          returned: always
          type: dict
          contains:
            siteId:
              description: It is the pnp device's siteId.
              returned: always
              type: str
              sample: '<siteid>'
            address:
              description: It is the pnp device's address.
              returned: always
              type: str
              sample: '<address>'
            latitude:
              description: It is the pnp device's latitude.
              returned: always
              type: str
              sample: '<latitude>'
            longitude:
              description: It is the pnp device's longitude.
              returned: always
              type: str
              sample: '<longitude>'
            altitude:
              description: It is the pnp device's altitude.
              returned: always
              type: str
              sample: '<altitude>'

        description:
          description: It is the pnp device's description.
          returned: always
          type: str
          sample: '<description>'
        onbState:
          description: It is the pnp device's onbState.
          returned: always
          type: str
          sample: '<onbstate>'
        authenticatedMicNumber:
          description: It is the pnp device's authenticatedMicNumber.
          returned: always
          type: str
          sample: '<authenticatedmicnumber>'
        authenticatedSudiSerialNo:
          description: It is the pnp device's authenticatedSudiSerialNo.
          returned: always
          type: str
          sample: '<authenticatedsudiserialno>'
        capabilitiesSupported:
          description: It is the pnp device's capabilitiesSupported.
          returned: always
          type: list
        featuresSupported:
          description: It is the pnp device's featuresSupported.
          returned: always
          type: list
        cmState:
          description: It is the pnp device's cmState.
          returned: always
          type: str
          sample: '<cmstate>'
        firstContact:
          description: It is the pnp device's firstContact.
          returned: always
          type: int
          sample: 0
        lastContact:
          description: It is the pnp device's lastContact.
          returned: always
          type: int
          sample: 0
        macAddress:
          description: It is the pnp device's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        pid:
          description: It is the pnp device's pid.
          returned: always
          type: str
          sample: '<pid>'
        deviceSudiSerialNos:
          description: It is the pnp device's deviceSudiSerialNos.
          returned: always
          type: list
        lastUpdateOn:
          description: It is the pnp device's lastUpdateOn.
          returned: always
          type: int
          sample: 0
        workflowId:
          description: It is the pnp device's workflowId.
          returned: always
          type: str
          sample: '<workflowid>'
        workflowName:
          description: It is the pnp device's workflowName.
          returned: always
          type: str
          sample: '<workflowname>'
        projectId:
          description: It is the pnp device's projectId.
          returned: always
          type: str
          sample: '<projectid>'
        projectName:
          description: It is the pnp device's projectName.
          returned: always
          type: str
          sample: '<projectname>'
        deviceType:
          description: It is the pnp device's deviceType.
          returned: always
          type: str
          sample: '<devicetype>'
        agentType:
          description: It is the pnp device's agentType.
          returned: always
          type: str
          sample: '<agenttype>'
        imageVersion:
          description: It is the pnp device's imageVersion.
          returned: always
          type: str
          sample: '<imageversion>'
        fileSystemList:
          description: It is the pnp device's fileSystemList.
          returned: always
          type: list
          contains:
            type:
              description: It is the pnp device's type.
              returned: always
              type: str
              sample: '<type>'
            writeable:
              description: It is the pnp device's writeable.
              returned: always
              type: bool
              sample: false
            freespace:
              description: It is the pnp device's freespace.
              returned: always
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: always
              type: str
              sample: '<name>'
            readable:
              description: It is the pnp device's readable.
              returned: always
              type: bool
              sample: false
            size:
              description: It is the pnp device's size.
              returned: always
              type: int
              sample: 0

        pnpProfileList:
          description: It is the pnp device's pnpProfileList.
          returned: always
          type: list
          contains:
            profileName:
              description: It is the pnp device's profileName.
              returned: always
              type: str
              sample: '<profilename>'
            discoveryCreated:
              description: It is the pnp device's discoveryCreated.
              returned: always
              type: bool
              sample: false
            createdBy:
              description: It is the pnp device's createdBy.
              returned: always
              type: str
              sample: '<createdby>'
            primaryEndpoint:
              description: It is the pnp device's primaryEndpoint.
              returned: always
              type: dict
              contains:
                port:
                  description: It is the pnp device's port.
                  returned: always
                  type: int
                  sample: 0
                protocol:
                  description: It is the pnp device's protocol.
                  returned: always
                  type: str
                  sample: '<protocol>'
                ipv4Address:
                  description: It is the pnp device's ipv4Address.
                  returned: always
                  type: dict
                ipv6Address:
                  description: It is the pnp device's ipv6Address.
                  returned: always
                  type: dict
                fqdn:
                  description: It is the pnp device's fqdn.
                  returned: always
                  type: str
                  sample: '<fqdn>'
                certificate:
                  description: It is the pnp device's certificate.
                  returned: always
                  type: str
                  sample: '<certificate>'

            secondaryEndpoint:
              description: It is the pnp device's secondaryEndpoint.
              returned: always
              type: dict
              contains:
                port:
                  description: It is the pnp device's port.
                  returned: always
                  type: int
                  sample: 0
                protocol:
                  description: It is the pnp device's protocol.
                  returned: always
                  type: str
                  sample: '<protocol>'
                ipv4Address:
                  description: It is the pnp device's ipv4Address.
                  returned: always
                  type: dict
                ipv6Address:
                  description: It is the pnp device's ipv6Address.
                  returned: always
                  type: dict
                fqdn:
                  description: It is the pnp device's fqdn.
                  returned: always
                  type: str
                  sample: '<fqdn>'
                certificate:
                  description: It is the pnp device's certificate.
                  returned: always
                  type: str
                  sample: '<certificate>'


        imageFile:
          description: It is the pnp device's imageFile.
          returned: always
          type: str
          sample: '<imagefile>'
        httpHeaders:
          description: It is the pnp device's httpHeaders.
          returned: always
          type: list
          contains:
            key:
              description: It is the pnp device's key.
              returned: always
              type: str
              sample: '<key>'
            value:
              description: It is the pnp device's value.
              returned: always
              type: str
              sample: '<value>'

        neighborLinks:
          description: It is the pnp device's neighborLinks.
          returned: always
          type: list
          contains:
            localInterfaceName:
              description: It is the pnp device's localInterfaceName.
              returned: always
              type: str
              sample: '<localinterfacename>'
            localShortInterfaceName:
              description: It is the pnp device's localShortInterfaceName.
              returned: always
              type: str
              sample: '<localshortinterfacename>'
            localMacAddress:
              description: It is the pnp device's localMacAddress.
              returned: always
              type: str
              sample: '<localmacaddress>'
            remoteInterfaceName:
              description: It is the pnp device's remoteInterfaceName.
              returned: always
              type: str
              sample: '<remoteinterfacename>'
            remoteShortInterfaceName:
              description: It is the pnp device's remoteShortInterfaceName.
              returned: always
              type: str
              sample: '<remoteshortinterfacename>'
            remoteMacAddress:
              description: It is the pnp device's remoteMacAddress.
              returned: always
              type: str
              sample: '<remotemacaddress>'
            remoteDeviceName:
              description: It is the pnp device's remoteDeviceName.
              returned: always
              type: str
              sample: '<remotedevicename>'
            remotePlatform:
              description: It is the pnp device's remotePlatform.
              returned: always
              type: str
              sample: '<remoteplatform>'
            remoteVersion:
              description: It is the pnp device's remoteVersion.
              returned: always
              type: str
              sample: '<remoteversion>'

        lastSyncTime:
          description: It is the pnp device's lastSyncTime.
          returned: always
          type: int
          sample: 0
        ipInterfaces:
          description: It is the pnp device's ipInterfaces.
          returned: always
          type: list
          contains:
            status:
              description: It is the pnp device's status.
              returned: always
              type: str
              sample: '<status>'
            macAddress:
              description: It is the pnp device's macAddress.
              returned: always
              type: str
              sample: '<macaddress>'
            ipv4Address:
              description: It is the pnp device's ipv4Address.
              returned: always
              type: dict
            ipv6AddressList:
              description: It is the pnp device's ipv6AddressList.
              returned: always
              type: list
            name:
              description: It is the pnp device's name.
              returned: always
              type: str
              sample: '<name>'

        hostname:
          description: It is the pnp device's hostname.
          returned: always
          type: str
          sample: '<hostname>'
        authStatus:
          description: It is the pnp device's authStatus.
          returned: always
          type: str
          sample: '<authstatus>'
        stackInfo:
          description: It is the pnp device's stackInfo.
          returned: always
          type: dict
          contains:
            supportsStackWorkflows:
              description: It is the pnp device's supportsStackWorkflows.
              returned: always
              type: bool
              sample: false
            isFullRing:
              description: It is the pnp device's isFullRing.
              returned: always
              type: bool
              sample: false
            stackMemberList:
              description: It is the pnp device's stackMemberList.
              returned: always
              type: list
              contains:
                serialNumber:
                  description: It is the pnp device's serialNumber.
                  returned: always
                  type: str
                  sample: '<serialnumber>'
                state:
                  description: It is the pnp device's state.
                  returned: always
                  type: str
                  sample: '<state>'
                role:
                  description: It is the pnp device's role.
                  returned: always
                  type: str
                  sample: '<role>'
                macAddress:
                  description: It is the pnp device's macAddress.
                  returned: always
                  type: str
                  sample: '<macaddress>'
                pid:
                  description: It is the pnp device's pid.
                  returned: always
                  type: str
                  sample: '<pid>'
                licenseLevel:
                  description: It is the pnp device's licenseLevel.
                  returned: always
                  type: str
                  sample: '<licenselevel>'
                licenseType:
                  description: It is the pnp device's licenseType.
                  returned: always
                  type: str
                  sample: '<licensetype>'
                sudiSerialNumber:
                  description: It is the pnp device's sudiSerialNumber.
                  returned: always
                  type: str
                  sample: '<sudiserialnumber>'
                hardwareVersion:
                  description: It is the pnp device's hardwareVersion.
                  returned: always
                  type: str
                  sample: '<hardwareversion>'
                stackNumber:
                  description: It is the pnp device's stackNumber.
                  returned: always
                  type: int
                  sample: 0
                softwareVersion:
                  description: It is the pnp device's softwareVersion.
                  returned: always
                  type: str
                  sample: '<softwareversion>'
                priority:
                  description: It is the pnp device's priority.
                  returned: always
                  type: int
                  sample: 0

            stackRingProtocol:
              description: It is the pnp device's stackRingProtocol.
              returned: always
              type: str
              sample: '<stackringprotocol>'
            validLicenseLevels:
              description: It is the pnp device's validLicenseLevels.
              returned: always
              type: list
            totalMemberCount:
              description: It is the pnp device's totalMemberCount.
              returned: always
              type: int
              sample: 0

        reloadRequested:
          description: It is the pnp device's reloadRequested.
          returned: always
          type: bool
          sample: false
        addedOn:
          description: It is the pnp device's addedOn.
          returned: always
          type: int
          sample: 0
        siteId:
          description: It is the pnp device's siteId.
          returned: always
          type: str
          sample: '<siteid>'
        aaaCredentials:
          description: It is the pnp device's aaaCredentials.
          returned: always
          type: dict
          contains:
            password:
              description: It is the pnp device's password.
              returned: always
              type: str
              sample: '*******'
            username:
              description: It is the pnp device's username.
              returned: always
              type: str
              sample: 'devnetuser'

        userMicNumbers:
          description: It is the pnp device's userMicNumbers.
          returned: always
          type: list
        userSudiSerialNos:
          description: It is the pnp device's userSudiSerialNos.
          returned: always
          type: list
        addnMacAddrs:
          description: It is the pnp device's addnMacAddrs.
          returned: always
          type: list
        preWorkflowCliOuputs:
          description: It is the pnp device's preWorkflowCliOuputs.
          returned: always
          type: list
          contains:
            cli:
              description: It is the pnp device's cli.
              returned: always
              type: str
              sample: '<cli>'
            cliOutput:
              description: It is the pnp device's cliOutput.
              returned: always
              type: str
              sample: '<clioutput>'

        tags:
          description: It is the pnp device's tags.
          returned: always
          type: dict
        sudiRequired:
          description: It is the pnp device's sudiRequired.
          returned: always
          type: bool
          sample: false
        smartAccountId:
          description: It is the pnp device's smartAccountId.
          returned: always
          type: str
          sample: '<smartaccountid>'
        virtualAccountId:
          description: It is the pnp device's virtualAccountId.
          returned: always
          type: str
          sample: '<virtualaccountid>'
        populateInventory:
          description: It is the pnp device's populateInventory.
          returned: always
          type: bool
          sample: false
        siteName:
          description: It is the pnp device's siteName.
          returned: always
          type: str
          sample: '<sitename>'
        name:
          description: It is the pnp device's name.
          returned: always
          type: str
          sample: '<name>'

    systemResetWorkflow:
      description: System Reset Workflow, property of the response body.
      returned: always
      type: dict
      contains:
        _id:
          description: It is the pnp device's _id.
          returned: always
          type: str
          sample: '<_id>'
        state:
          description: It is the pnp device's state.
          returned: always
          type: str
          sample: '<state>'
        type:
          description: It is the pnp device's type.
          returned: always
          type: str
          sample: '<type>'
        description:
          description: It is the pnp device's description.
          returned: always
          type: str
          sample: '<description>'
        lastupdateOn:
          description: It is the pnp device's lastupdateOn.
          returned: always
          type: int
          sample: 0
        imageId:
          description: It is the pnp device's imageId.
          returned: always
          type: str
          sample: '<imageid>'
        currTaskIdx:
          description: It is the pnp device's currTaskIdx.
          returned: always
          type: int
          sample: 0
        addedOn:
          description: It is the pnp device's addedOn.
          returned: always
          type: int
          sample: 0
        tasks:
          description: It is the pnp device's tasks.
          returned: always
          type: list
          contains:
            state:
              description: It is the pnp device's state.
              returned: always
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device's type.
              returned: always
              type: str
              sample: '<type>'
            currWorkItemIdx:
              description: It is the pnp device's currWorkItemIdx.
              returned: always
              type: int
              sample: 0
            taskSeqNo:
              description: It is the pnp device's taskSeqNo.
              returned: always
              type: int
              sample: 0
            endTime:
              description: It is the pnp device's endTime.
              returned: always
              type: int
              sample: 0
            startTime:
              description: It is the pnp device's startTime.
              returned: always
              type: int
              sample: 0
            workItemList:
              description: It is the pnp device's workItemList.
              returned: always
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: always
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: always
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: always
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: always
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: always
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: always
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: always
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: always
              type: str
              sample: '<name>'

        addToInventory:
          description: It is the pnp device's addToInventory.
          returned: always
          type: bool
          sample: false
        instanceType:
          description: It is the pnp device's instanceType.
          returned: always
          type: str
          sample: '<instancetype>'
        endTime:
          description: It is the pnp device's endTime.
          returned: always
          type: int
          sample: 0
        execTime:
          description: It is the pnp device's execTime.
          returned: always
          type: int
          sample: 0
        startTime:
          description: It is the pnp device's startTime.
          returned: always
          type: int
          sample: 0
        useState:
          description: It is the pnp device's useState.
          returned: always
          type: str
          sample: '<usestate>'
        configId:
          description: It is the pnp device's configId.
          returned: always
          type: str
          sample: '<configid>'
        name:
          description: It is the pnp device's name.
          returned: always
          type: str
          sample: '<name>'
        version:
          description: It is the pnp device's version.
          returned: always
          type: int
          sample: 0
        tenantId:
          description: It is the pnp device's tenantId.
          returned: always
          type: str
          sample: '<tenantid>'

    systemWorkflow:
      description: System Workflow, property of the response body.
      returned: always
      type: dict
      contains:
        _id:
          description: It is the pnp device's _id.
          returned: always
          type: str
          sample: '<_id>'
        state:
          description: It is the pnp device's state.
          returned: always
          type: str
          sample: '<state>'
        type:
          description: It is the pnp device's type.
          returned: always
          type: str
          sample: '<type>'
        description:
          description: It is the pnp device's description.
          returned: always
          type: str
          sample: '<description>'
        lastupdateOn:
          description: It is the pnp device's lastupdateOn.
          returned: always
          type: int
          sample: 0
        imageId:
          description: It is the pnp device's imageId.
          returned: always
          type: str
          sample: '<imageid>'
        currTaskIdx:
          description: It is the pnp device's currTaskIdx.
          returned: always
          type: int
          sample: 0
        addedOn:
          description: It is the pnp device's addedOn.
          returned: always
          type: int
          sample: 0
        tasks:
          description: It is the pnp device's tasks.
          returned: always
          type: list
          contains:
            state:
              description: It is the pnp device's state.
              returned: always
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device's type.
              returned: always
              type: str
              sample: '<type>'
            currWorkItemIdx:
              description: It is the pnp device's currWorkItemIdx.
              returned: always
              type: int
              sample: 0
            taskSeqNo:
              description: It is the pnp device's taskSeqNo.
              returned: always
              type: int
              sample: 0
            endTime:
              description: It is the pnp device's endTime.
              returned: always
              type: int
              sample: 0
            startTime:
              description: It is the pnp device's startTime.
              returned: always
              type: int
              sample: 0
            workItemList:
              description: It is the pnp device's workItemList.
              returned: always
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: always
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: always
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: always
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: always
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: always
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: always
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: always
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: always
              type: str
              sample: '<name>'

        addToInventory:
          description: It is the pnp device's addToInventory.
          returned: always
          type: bool
          sample: false
        instanceType:
          description: It is the pnp device's instanceType.
          returned: always
          type: str
          sample: '<instancetype>'
        endTime:
          description: It is the pnp device's endTime.
          returned: always
          type: int
          sample: 0
        execTime:
          description: It is the pnp device's execTime.
          returned: always
          type: int
          sample: 0
        startTime:
          description: It is the pnp device's startTime.
          returned: always
          type: int
          sample: 0
        useState:
          description: It is the pnp device's useState.
          returned: always
          type: str
          sample: '<usestate>'
        configId:
          description: It is the pnp device's configId.
          returned: always
          type: str
          sample: '<configid>'
        name:
          description: It is the pnp device's name.
          returned: always
          type: str
          sample: '<name>'
        version:
          description: It is the pnp device's version.
          returned: always
          type: int
          sample: 0
        tenantId:
          description: It is the pnp device's tenantId.
          returned: always
          type: str
          sample: '<tenantid>'

    workflow:
      description: Workflow, property of the response body.
      returned: always
      type: dict
      contains:
        _id:
          description: It is the pnp device's _id.
          returned: always
          type: str
          sample: '<_id>'
        state:
          description: It is the pnp device's state.
          returned: always
          type: str
          sample: '<state>'
        type:
          description: It is the pnp device's type.
          returned: always
          type: str
          sample: '<type>'
        description:
          description: It is the pnp device's description.
          returned: always
          type: str
          sample: '<description>'
        lastupdateOn:
          description: It is the pnp device's lastupdateOn.
          returned: always
          type: int
          sample: 0
        imageId:
          description: It is the pnp device's imageId.
          returned: always
          type: str
          sample: '<imageid>'
        currTaskIdx:
          description: It is the pnp device's currTaskIdx.
          returned: always
          type: int
          sample: 0
        addedOn:
          description: It is the pnp device's addedOn.
          returned: always
          type: int
          sample: 0
        tasks:
          description: It is the pnp device's tasks.
          returned: always
          type: list
          contains:
            state:
              description: It is the pnp device's state.
              returned: always
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device's type.
              returned: always
              type: str
              sample: '<type>'
            currWorkItemIdx:
              description: It is the pnp device's currWorkItemIdx.
              returned: always
              type: int
              sample: 0
            taskSeqNo:
              description: It is the pnp device's taskSeqNo.
              returned: always
              type: int
              sample: 0
            endTime:
              description: It is the pnp device's endTime.
              returned: always
              type: int
              sample: 0
            startTime:
              description: It is the pnp device's startTime.
              returned: always
              type: int
              sample: 0
            workItemList:
              description: It is the pnp device's workItemList.
              returned: always
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: always
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: always
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: always
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: always
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: always
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: always
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: always
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: always
              type: str
              sample: '<name>'

        addToInventory:
          description: It is the pnp device's addToInventory.
          returned: always
          type: bool
          sample: false
        instanceType:
          description: It is the pnp device's instanceType.
          returned: always
          type: str
          sample: '<instancetype>'
        endTime:
          description: It is the pnp device's endTime.
          returned: always
          type: int
          sample: 0
        execTime:
          description: It is the pnp device's execTime.
          returned: always
          type: int
          sample: 0
        startTime:
          description: It is the pnp device's startTime.
          returned: always
          type: int
          sample: 0
        useState:
          description: It is the pnp device's useState.
          returned: always
          type: str
          sample: '<usestate>'
        configId:
          description: It is the pnp device's configId.
          returned: always
          type: str
          sample: '<configid>'
        name:
          description: It is the pnp device's name.
          returned: always
          type: str
          sample: '<name>'
        version:
          description: It is the pnp device's version.
          returned: always
          type: int
          sample: 0
        tenantId:
          description: It is the pnp device's tenantId.
          returned: always
          type: str
          sample: '<tenantid>'

    runSummaryList:
      description: Run Summary List, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        details:
          description: It is the pnp device's details.
          returned: always
          type: str
          sample: '<details>'
        historyTaskInfo:
          description: It is the pnp device's historyTaskInfo.
          returned: always
          type: dict
          contains:
            type:
              description: It is the pnp device's type.
              returned: always
              type: str
              sample: '<type>'
            workItemList:
              description: It is the pnp device's workItemList.
              returned: always
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: always
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: always
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: always
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: always
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: always
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: always
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: always
              type: int
              sample: 0
            addnDetails:
              description: It is the pnp device's addnDetails.
              returned: always
              type: list
              contains:
                key:
                  description: It is the pnp device's key.
                  returned: always
                  type: str
                  sample: '<key>'
                value:
                  description: It is the pnp device's value.
                  returned: always
                  type: str
                  sample: '<value>'

            name:
              description: It is the pnp device's name.
              returned: always
              type: str
              sample: '<name>'

        errorFlag:
          description: It is the pnp device's errorFlag.
          returned: always
          type: bool
          sample: false
        timestamp:
          description: It is the pnp device's timestamp.
          returned: always
          type: int
          sample: 0

    workflowParameters:
      description: Workflow Parameters, property of the response body.
      returned: always
      type: dict
      contains:
        topOfStackSerialNumber:
          description: It is the pnp device's topOfStackSerialNumber.
          returned: always
          type: str
          sample: '<topofstackserialnumber>'
        licenseLevel:
          description: It is the pnp device's licenseLevel.
          returned: always
          type: str
          sample: '<licenselevel>'
        licenseType:
          description: It is the pnp device's licenseType.
          returned: always
          type: str
          sample: '<licensetype>'
        configList:
          description: It is the pnp device's configList.
          returned: always
          type: list
          contains:
            configParameters:
              description: It is the pnp device's configParameters.
              returned: always
              type: list
              contains:
                key:
                  description: It is the pnp device's key.
                  returned: always
                  type: str
                  sample: '<key>'
                value:
                  description: It is the pnp device's value.
                  returned: always
                  type: str
                  sample: '<value>'

            configId:
              description: It is the pnp device's configId.
              returned: always
              type: str
              sample: '<configid>'


    dayZeroConfig:
      description: Day Zero Config, property of the response body.
      returned: always
      type: dict
      contains:
        config:
          description: It is the pnp device's config.
          returned: always
          type: str
          sample: '<config>'

    dayZeroConfigPreview:
      description: Day Zero Config Preview, property of the response body.
      returned: always
      type: dict
    version:
      description: Version, property of the response body.
      returned: always
      type: int
      sample: 0
    tenantId:
      description: Tenant Id, property of the response body.
      returned: always
      type: str
      sample: '<tenantid>'

delete_device_by_id_from_pnp:
    description: Deletes specified device from PnP database.
    returned: success
    type: dict
    contains:
    _id:
      description: Id, property of the response body.
      returned: success
      type: str
      sample: '<_id>'
    deviceInfo:
      description: Device Info, property of the response body.
      returned: success
      type: dict
      contains:
        source:
          description: It is the pnp device's source.
          returned: success
          type: str
          sample: '<source>'
        serialNumber:
          description: It is the pnp device's serialNumber.
          returned: success
          type: str
          sample: '<serialnumber>'
        stack:
          description: It is the pnp device's stack.
          returned: success
          type: bool
          sample: false
        mode:
          description: It is the pnp device's mode.
          returned: success
          type: str
          sample: '<mode>'
        state:
          description: It is the pnp device's state.
          returned: success
          type: str
          sample: '<state>'
        location:
          description: It is the pnp device's location.
          returned: success
          type: dict
          contains:
            siteId:
              description: It is the pnp device's siteId.
              returned: success
              type: str
              sample: '<siteid>'
            address:
              description: It is the pnp device's address.
              returned: success
              type: str
              sample: '<address>'
            latitude:
              description: It is the pnp device's latitude.
              returned: success
              type: str
              sample: '<latitude>'
            longitude:
              description: It is the pnp device's longitude.
              returned: success
              type: str
              sample: '<longitude>'
            altitude:
              description: It is the pnp device's altitude.
              returned: success
              type: str
              sample: '<altitude>'

        description:
          description: It is the pnp device's description.
          returned: success
          type: str
          sample: '<description>'
        onbState:
          description: It is the pnp device's onbState.
          returned: success
          type: str
          sample: '<onbstate>'
        authenticatedMicNumber:
          description: It is the pnp device's authenticatedMicNumber.
          returned: success
          type: str
          sample: '<authenticatedmicnumber>'
        authenticatedSudiSerialNo:
          description: It is the pnp device's authenticatedSudiSerialNo.
          returned: success
          type: str
          sample: '<authenticatedsudiserialno>'
        capabilitiesSupported:
          description: It is the pnp device's capabilitiesSupported.
          returned: success
          type: list
        featuresSupported:
          description: It is the pnp device's featuresSupported.
          returned: success
          type: list
        cmState:
          description: It is the pnp device's cmState.
          returned: success
          type: str
          sample: '<cmstate>'
        firstContact:
          description: It is the pnp device's firstContact.
          returned: success
          type: int
          sample: 0
        lastContact:
          description: It is the pnp device's lastContact.
          returned: success
          type: int
          sample: 0
        macAddress:
          description: It is the pnp device's macAddress.
          returned: success
          type: str
          sample: '<macaddress>'
        pid:
          description: It is the pnp device's pid.
          returned: success
          type: str
          sample: '<pid>'
        deviceSudiSerialNos:
          description: It is the pnp device's deviceSudiSerialNos.
          returned: success
          type: list
        lastUpdateOn:
          description: It is the pnp device's lastUpdateOn.
          returned: success
          type: int
          sample: 0
        workflowId:
          description: It is the pnp device's workflowId.
          returned: success
          type: str
          sample: '<workflowid>'
        workflowName:
          description: It is the pnp device's workflowName.
          returned: success
          type: str
          sample: '<workflowname>'
        projectId:
          description: It is the pnp device's projectId.
          returned: success
          type: str
          sample: '<projectid>'
        projectName:
          description: It is the pnp device's projectName.
          returned: success
          type: str
          sample: '<projectname>'
        deviceType:
          description: It is the pnp device's deviceType.
          returned: success
          type: str
          sample: '<devicetype>'
        agentType:
          description: It is the pnp device's agentType.
          returned: success
          type: str
          sample: '<agenttype>'
        imageVersion:
          description: It is the pnp device's imageVersion.
          returned: success
          type: str
          sample: '<imageversion>'
        fileSystemList:
          description: It is the pnp device's fileSystemList.
          returned: success
          type: list
          contains:
            type:
              description: It is the pnp device's type.
              returned: success
              type: str
              sample: '<type>'
            writeable:
              description: It is the pnp device's writeable.
              returned: success
              type: bool
              sample: false
            freespace:
              description: It is the pnp device's freespace.
              returned: success
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: success
              type: str
              sample: '<name>'
            readable:
              description: It is the pnp device's readable.
              returned: success
              type: bool
              sample: false
            size:
              description: It is the pnp device's size.
              returned: success
              type: int
              sample: 0

        pnpProfileList:
          description: It is the pnp device's pnpProfileList.
          returned: success
          type: list
          contains:
            profileName:
              description: It is the pnp device's profileName.
              returned: success
              type: str
              sample: '<profilename>'
            discoveryCreated:
              description: It is the pnp device's discoveryCreated.
              returned: success
              type: bool
              sample: false
            createdBy:
              description: It is the pnp device's createdBy.
              returned: success
              type: str
              sample: '<createdby>'
            primaryEndpoint:
              description: It is the pnp device's primaryEndpoint.
              returned: success
              type: dict
              contains:
                port:
                  description: It is the pnp device's port.
                  returned: success
                  type: int
                  sample: 0
                protocol:
                  description: It is the pnp device's protocol.
                  returned: success
                  type: str
                  sample: '<protocol>'
                ipv4Address:
                  description: It is the pnp device's ipv4Address.
                  returned: success
                  type: dict
                ipv6Address:
                  description: It is the pnp device's ipv6Address.
                  returned: success
                  type: dict
                fqdn:
                  description: It is the pnp device's fqdn.
                  returned: success
                  type: str
                  sample: '<fqdn>'
                certificate:
                  description: It is the pnp device's certificate.
                  returned: success
                  type: str
                  sample: '<certificate>'

            secondaryEndpoint:
              description: It is the pnp device's secondaryEndpoint.
              returned: success
              type: dict
              contains:
                port:
                  description: It is the pnp device's port.
                  returned: success
                  type: int
                  sample: 0
                protocol:
                  description: It is the pnp device's protocol.
                  returned: success
                  type: str
                  sample: '<protocol>'
                ipv4Address:
                  description: It is the pnp device's ipv4Address.
                  returned: success
                  type: dict
                ipv6Address:
                  description: It is the pnp device's ipv6Address.
                  returned: success
                  type: dict
                fqdn:
                  description: It is the pnp device's fqdn.
                  returned: success
                  type: str
                  sample: '<fqdn>'
                certificate:
                  description: It is the pnp device's certificate.
                  returned: success
                  type: str
                  sample: '<certificate>'


        imageFile:
          description: It is the pnp device's imageFile.
          returned: success
          type: str
          sample: '<imagefile>'
        httpHeaders:
          description: It is the pnp device's httpHeaders.
          returned: success
          type: list
          contains:
            key:
              description: It is the pnp device's key.
              returned: success
              type: str
              sample: '<key>'
            value:
              description: It is the pnp device's value.
              returned: success
              type: str
              sample: '<value>'

        neighborLinks:
          description: It is the pnp device's neighborLinks.
          returned: success
          type: list
          contains:
            localInterfaceName:
              description: It is the pnp device's localInterfaceName.
              returned: success
              type: str
              sample: '<localinterfacename>'
            localShortInterfaceName:
              description: It is the pnp device's localShortInterfaceName.
              returned: success
              type: str
              sample: '<localshortinterfacename>'
            localMacAddress:
              description: It is the pnp device's localMacAddress.
              returned: success
              type: str
              sample: '<localmacaddress>'
            remoteInterfaceName:
              description: It is the pnp device's remoteInterfaceName.
              returned: success
              type: str
              sample: '<remoteinterfacename>'
            remoteShortInterfaceName:
              description: It is the pnp device's remoteShortInterfaceName.
              returned: success
              type: str
              sample: '<remoteshortinterfacename>'
            remoteMacAddress:
              description: It is the pnp device's remoteMacAddress.
              returned: success
              type: str
              sample: '<remotemacaddress>'
            remoteDeviceName:
              description: It is the pnp device's remoteDeviceName.
              returned: success
              type: str
              sample: '<remotedevicename>'
            remotePlatform:
              description: It is the pnp device's remotePlatform.
              returned: success
              type: str
              sample: '<remoteplatform>'
            remoteVersion:
              description: It is the pnp device's remoteVersion.
              returned: success
              type: str
              sample: '<remoteversion>'

        lastSyncTime:
          description: It is the pnp device's lastSyncTime.
          returned: success
          type: int
          sample: 0
        ipInterfaces:
          description: It is the pnp device's ipInterfaces.
          returned: success
          type: list
          contains:
            status:
              description: It is the pnp device's status.
              returned: success
              type: str
              sample: '<status>'
            macAddress:
              description: It is the pnp device's macAddress.
              returned: success
              type: str
              sample: '<macaddress>'
            ipv4Address:
              description: It is the pnp device's ipv4Address.
              returned: success
              type: dict
            ipv6AddressList:
              description: It is the pnp device's ipv6AddressList.
              returned: success
              type: list
            name:
              description: It is the pnp device's name.
              returned: success
              type: str
              sample: '<name>'

        hostname:
          description: It is the pnp device's hostname.
          returned: success
          type: str
          sample: '<hostname>'
        authStatus:
          description: It is the pnp device's authStatus.
          returned: success
          type: str
          sample: '<authstatus>'
        stackInfo:
          description: It is the pnp device's stackInfo.
          returned: success
          type: dict
          contains:
            supportsStackWorkflows:
              description: It is the pnp device's supportsStackWorkflows.
              returned: success
              type: bool
              sample: false
            isFullRing:
              description: It is the pnp device's isFullRing.
              returned: success
              type: bool
              sample: false
            stackMemberList:
              description: It is the pnp device's stackMemberList.
              returned: success
              type: list
              contains:
                serialNumber:
                  description: It is the pnp device's serialNumber.
                  returned: success
                  type: str
                  sample: '<serialnumber>'
                state:
                  description: It is the pnp device's state.
                  returned: success
                  type: str
                  sample: '<state>'
                role:
                  description: It is the pnp device's role.
                  returned: success
                  type: str
                  sample: '<role>'
                macAddress:
                  description: It is the pnp device's macAddress.
                  returned: success
                  type: str
                  sample: '<macaddress>'
                pid:
                  description: It is the pnp device's pid.
                  returned: success
                  type: str
                  sample: '<pid>'
                licenseLevel:
                  description: It is the pnp device's licenseLevel.
                  returned: success
                  type: str
                  sample: '<licenselevel>'
                licenseType:
                  description: It is the pnp device's licenseType.
                  returned: success
                  type: str
                  sample: '<licensetype>'
                sudiSerialNumber:
                  description: It is the pnp device's sudiSerialNumber.
                  returned: success
                  type: str
                  sample: '<sudiserialnumber>'
                hardwareVersion:
                  description: It is the pnp device's hardwareVersion.
                  returned: success
                  type: str
                  sample: '<hardwareversion>'
                stackNumber:
                  description: It is the pnp device's stackNumber.
                  returned: success
                  type: int
                  sample: 0
                softwareVersion:
                  description: It is the pnp device's softwareVersion.
                  returned: success
                  type: str
                  sample: '<softwareversion>'
                priority:
                  description: It is the pnp device's priority.
                  returned: success
                  type: int
                  sample: 0

            stackRingProtocol:
              description: It is the pnp device's stackRingProtocol.
              returned: success
              type: str
              sample: '<stackringprotocol>'
            validLicenseLevels:
              description: It is the pnp device's validLicenseLevels.
              returned: success
              type: list
            totalMemberCount:
              description: It is the pnp device's totalMemberCount.
              returned: success
              type: int
              sample: 0

        reloadRequested:
          description: It is the pnp device's reloadRequested.
          returned: success
          type: bool
          sample: false
        addedOn:
          description: It is the pnp device's addedOn.
          returned: success
          type: int
          sample: 0
        siteId:
          description: It is the pnp device's siteId.
          returned: success
          type: str
          sample: '<siteid>'
        aaaCredentials:
          description: It is the pnp device's aaaCredentials.
          returned: success
          type: dict
          contains:
            password:
              description: It is the pnp device's password.
              returned: success
              type: str
              sample: '*******'
            username:
              description: It is the pnp device's username.
              returned: success
              type: str
              sample: 'devnetuser'

        userMicNumbers:
          description: It is the pnp device's userMicNumbers.
          returned: success
          type: list
        userSudiSerialNos:
          description: It is the pnp device's userSudiSerialNos.
          returned: success
          type: list
        addnMacAddrs:
          description: It is the pnp device's addnMacAddrs.
          returned: success
          type: list
        preWorkflowCliOuputs:
          description: It is the pnp device's preWorkflowCliOuputs.
          returned: success
          type: list
          contains:
            cli:
              description: It is the pnp device's cli.
              returned: success
              type: str
              sample: '<cli>'
            cliOutput:
              description: It is the pnp device's cliOutput.
              returned: success
              type: str
              sample: '<clioutput>'

        tags:
          description: It is the pnp device's tags.
          returned: success
          type: dict
        sudiRequired:
          description: It is the pnp device's sudiRequired.
          returned: success
          type: bool
          sample: false
        smartAccountId:
          description: It is the pnp device's smartAccountId.
          returned: success
          type: str
          sample: '<smartaccountid>'
        virtualAccountId:
          description: It is the pnp device's virtualAccountId.
          returned: success
          type: str
          sample: '<virtualaccountid>'
        populateInventory:
          description: It is the pnp device's populateInventory.
          returned: success
          type: bool
          sample: false
        siteName:
          description: It is the pnp device's siteName.
          returned: success
          type: str
          sample: '<sitename>'
        name:
          description: It is the pnp device's name.
          returned: success
          type: str
          sample: '<name>'

    systemResetWorkflow:
      description: System Reset Workflow, property of the response body.
      returned: success
      type: dict
      contains:
        _id:
          description: It is the pnp device's _id.
          returned: success
          type: str
          sample: '<_id>'
        state:
          description: It is the pnp device's state.
          returned: success
          type: str
          sample: '<state>'
        type:
          description: It is the pnp device's type.
          returned: success
          type: str
          sample: '<type>'
        description:
          description: It is the pnp device's description.
          returned: success
          type: str
          sample: '<description>'
        lastupdateOn:
          description: It is the pnp device's lastupdateOn.
          returned: success
          type: int
          sample: 0
        imageId:
          description: It is the pnp device's imageId.
          returned: success
          type: str
          sample: '<imageid>'
        currTaskIdx:
          description: It is the pnp device's currTaskIdx.
          returned: success
          type: int
          sample: 0
        addedOn:
          description: It is the pnp device's addedOn.
          returned: success
          type: int
          sample: 0
        tasks:
          description: It is the pnp device's tasks.
          returned: success
          type: list
          contains:
            state:
              description: It is the pnp device's state.
              returned: success
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device's type.
              returned: success
              type: str
              sample: '<type>'
            currWorkItemIdx:
              description: It is the pnp device's currWorkItemIdx.
              returned: success
              type: int
              sample: 0
            taskSeqNo:
              description: It is the pnp device's taskSeqNo.
              returned: success
              type: int
              sample: 0
            endTime:
              description: It is the pnp device's endTime.
              returned: success
              type: int
              sample: 0
            startTime:
              description: It is the pnp device's startTime.
              returned: success
              type: int
              sample: 0
            workItemList:
              description: It is the pnp device's workItemList.
              returned: success
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: success
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: success
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: success
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: success
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: success
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: success
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: success
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: success
              type: str
              sample: '<name>'

        addToInventory:
          description: It is the pnp device's addToInventory.
          returned: success
          type: bool
          sample: false
        instanceType:
          description: It is the pnp device's instanceType.
          returned: success
          type: str
          sample: '<instancetype>'
        endTime:
          description: It is the pnp device's endTime.
          returned: success
          type: int
          sample: 0
        execTime:
          description: It is the pnp device's execTime.
          returned: success
          type: int
          sample: 0
        startTime:
          description: It is the pnp device's startTime.
          returned: success
          type: int
          sample: 0
        useState:
          description: It is the pnp device's useState.
          returned: success
          type: str
          sample: '<usestate>'
        configId:
          description: It is the pnp device's configId.
          returned: success
          type: str
          sample: '<configid>'
        name:
          description: It is the pnp device's name.
          returned: success
          type: str
          sample: '<name>'
        version:
          description: It is the pnp device's version.
          returned: success
          type: int
          sample: 0
        tenantId:
          description: It is the pnp device's tenantId.
          returned: success
          type: str
          sample: '<tenantid>'

    systemWorkflow:
      description: System Workflow, property of the response body.
      returned: success
      type: dict
      contains:
        _id:
          description: It is the pnp device's _id.
          returned: success
          type: str
          sample: '<_id>'
        state:
          description: It is the pnp device's state.
          returned: success
          type: str
          sample: '<state>'
        type:
          description: It is the pnp device's type.
          returned: success
          type: str
          sample: '<type>'
        description:
          description: It is the pnp device's description.
          returned: success
          type: str
          sample: '<description>'
        lastupdateOn:
          description: It is the pnp device's lastupdateOn.
          returned: success
          type: int
          sample: 0
        imageId:
          description: It is the pnp device's imageId.
          returned: success
          type: str
          sample: '<imageid>'
        currTaskIdx:
          description: It is the pnp device's currTaskIdx.
          returned: success
          type: int
          sample: 0
        addedOn:
          description: It is the pnp device's addedOn.
          returned: success
          type: int
          sample: 0
        tasks:
          description: It is the pnp device's tasks.
          returned: success
          type: list
          contains:
            state:
              description: It is the pnp device's state.
              returned: success
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device's type.
              returned: success
              type: str
              sample: '<type>'
            currWorkItemIdx:
              description: It is the pnp device's currWorkItemIdx.
              returned: success
              type: int
              sample: 0
            taskSeqNo:
              description: It is the pnp device's taskSeqNo.
              returned: success
              type: int
              sample: 0
            endTime:
              description: It is the pnp device's endTime.
              returned: success
              type: int
              sample: 0
            startTime:
              description: It is the pnp device's startTime.
              returned: success
              type: int
              sample: 0
            workItemList:
              description: It is the pnp device's workItemList.
              returned: success
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: success
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: success
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: success
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: success
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: success
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: success
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: success
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: success
              type: str
              sample: '<name>'

        addToInventory:
          description: It is the pnp device's addToInventory.
          returned: success
          type: bool
          sample: false
        instanceType:
          description: It is the pnp device's instanceType.
          returned: success
          type: str
          sample: '<instancetype>'
        endTime:
          description: It is the pnp device's endTime.
          returned: success
          type: int
          sample: 0
        execTime:
          description: It is the pnp device's execTime.
          returned: success
          type: int
          sample: 0
        startTime:
          description: It is the pnp device's startTime.
          returned: success
          type: int
          sample: 0
        useState:
          description: It is the pnp device's useState.
          returned: success
          type: str
          sample: '<usestate>'
        configId:
          description: It is the pnp device's configId.
          returned: success
          type: str
          sample: '<configid>'
        name:
          description: It is the pnp device's name.
          returned: success
          type: str
          sample: '<name>'
        version:
          description: It is the pnp device's version.
          returned: success
          type: int
          sample: 0
        tenantId:
          description: It is the pnp device's tenantId.
          returned: success
          type: str
          sample: '<tenantid>'

    workflow:
      description: Workflow, property of the response body.
      returned: success
      type: dict
      contains:
        _id:
          description: It is the pnp device's _id.
          returned: success
          type: str
          sample: '<_id>'
        state:
          description: It is the pnp device's state.
          returned: success
          type: str
          sample: '<state>'
        type:
          description: It is the pnp device's type.
          returned: success
          type: str
          sample: '<type>'
        description:
          description: It is the pnp device's description.
          returned: success
          type: str
          sample: '<description>'
        lastupdateOn:
          description: It is the pnp device's lastupdateOn.
          returned: success
          type: int
          sample: 0
        imageId:
          description: It is the pnp device's imageId.
          returned: success
          type: str
          sample: '<imageid>'
        currTaskIdx:
          description: It is the pnp device's currTaskIdx.
          returned: success
          type: int
          sample: 0
        addedOn:
          description: It is the pnp device's addedOn.
          returned: success
          type: int
          sample: 0
        tasks:
          description: It is the pnp device's tasks.
          returned: success
          type: list
          contains:
            state:
              description: It is the pnp device's state.
              returned: success
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device's type.
              returned: success
              type: str
              sample: '<type>'
            currWorkItemIdx:
              description: It is the pnp device's currWorkItemIdx.
              returned: success
              type: int
              sample: 0
            taskSeqNo:
              description: It is the pnp device's taskSeqNo.
              returned: success
              type: int
              sample: 0
            endTime:
              description: It is the pnp device's endTime.
              returned: success
              type: int
              sample: 0
            startTime:
              description: It is the pnp device's startTime.
              returned: success
              type: int
              sample: 0
            workItemList:
              description: It is the pnp device's workItemList.
              returned: success
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: success
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: success
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: success
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: success
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: success
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: success
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: success
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: success
              type: str
              sample: '<name>'

        addToInventory:
          description: It is the pnp device's addToInventory.
          returned: success
          type: bool
          sample: false
        instanceType:
          description: It is the pnp device's instanceType.
          returned: success
          type: str
          sample: '<instancetype>'
        endTime:
          description: It is the pnp device's endTime.
          returned: success
          type: int
          sample: 0
        execTime:
          description: It is the pnp device's execTime.
          returned: success
          type: int
          sample: 0
        startTime:
          description: It is the pnp device's startTime.
          returned: success
          type: int
          sample: 0
        useState:
          description: It is the pnp device's useState.
          returned: success
          type: str
          sample: '<usestate>'
        configId:
          description: It is the pnp device's configId.
          returned: success
          type: str
          sample: '<configid>'
        name:
          description: It is the pnp device's name.
          returned: success
          type: str
          sample: '<name>'
        version:
          description: It is the pnp device's version.
          returned: success
          type: int
          sample: 0
        tenantId:
          description: It is the pnp device's tenantId.
          returned: success
          type: str
          sample: '<tenantid>'

    runSummaryList:
      description: Run Summary List, property of the response body (list of objects).
      returned: success
      type: list
      contains:
        details:
          description: It is the pnp device's details.
          returned: success
          type: str
          sample: '<details>'
        historyTaskInfo:
          description: It is the pnp device's historyTaskInfo.
          returned: success
          type: dict
          contains:
            type:
              description: It is the pnp device's type.
              returned: success
              type: str
              sample: '<type>'
            workItemList:
              description: It is the pnp device's workItemList.
              returned: success
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: success
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: success
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: success
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: success
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: success
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: success
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: success
              type: int
              sample: 0
            addnDetails:
              description: It is the pnp device's addnDetails.
              returned: success
              type: list
              contains:
                key:
                  description: It is the pnp device's key.
                  returned: success
                  type: str
                  sample: '<key>'
                value:
                  description: It is the pnp device's value.
                  returned: success
                  type: str
                  sample: '<value>'

            name:
              description: It is the pnp device's name.
              returned: success
              type: str
              sample: '<name>'

        errorFlag:
          description: It is the pnp device's errorFlag.
          returned: success
          type: bool
          sample: false
        timestamp:
          description: It is the pnp device's timestamp.
          returned: success
          type: int
          sample: 0

    workflowParameters:
      description: Workflow Parameters, property of the response body.
      returned: success
      type: dict
      contains:
        topOfStackSerialNumber:
          description: It is the pnp device's topOfStackSerialNumber.
          returned: success
          type: str
          sample: '<topofstackserialnumber>'
        licenseLevel:
          description: It is the pnp device's licenseLevel.
          returned: success
          type: str
          sample: '<licenselevel>'
        licenseType:
          description: It is the pnp device's licenseType.
          returned: success
          type: str
          sample: '<licensetype>'
        configList:
          description: It is the pnp device's configList.
          returned: success
          type: list
          contains:
            configParameters:
              description: It is the pnp device's configParameters.
              returned: success
              type: list
              contains:
                key:
                  description: It is the pnp device's key.
                  returned: success
                  type: str
                  sample: '<key>'
                value:
                  description: It is the pnp device's value.
                  returned: success
                  type: str
                  sample: '<value>'

            configId:
              description: It is the pnp device's configId.
              returned: success
              type: str
              sample: '<configid>'


    dayZeroConfig:
      description: Day Zero Config, property of the response body.
      returned: success
      type: dict
      contains:
        config:
          description: It is the pnp device's config.
          returned: success
          type: str
          sample: '<config>'

    dayZeroConfigPreview:
      description: Day Zero Config Preview, property of the response body.
      returned: success
      type: dict
    version:
      description: Version, property of the response body.
      returned: success
      type: int
      sample: 0
    tenantId:
      description: Tenant Id, property of the response body.
      returned: success
      type: str
      sample: '<tenantid>'

update_device:
    description: Updates device details specified by device id in PnP database.
    returned: changed
    type: dict
    contains:
    _id:
      description: Device's Id.
      returned: changed
      type: str
      sample: '<_id>'
    deviceInfo:
      description: Device's Device Info.
      returned: changed
      type: dict
      contains:
        source:
          description: It is the pnp device's source.
          returned: changed
          type: str
          sample: '<source>'
        serialNumber:
          description: It is the pnp device's serialNumber.
          returned: changed
          type: str
          sample: '<serialnumber>'
        stack:
          description: It is the pnp device's stack.
          returned: changed
          type: bool
          sample: false
        mode:
          description: It is the pnp device's mode.
          returned: changed
          type: str
          sample: '<mode>'
        state:
          description: It is the pnp device's state.
          returned: changed
          type: str
          sample: '<state>'
        location:
          description: It is the pnp device's location.
          returned: changed
          type: dict
          contains:
            siteId:
              description: It is the pnp device's siteId.
              returned: changed
              type: str
              sample: '<siteid>'
            address:
              description: It is the pnp device's address.
              returned: changed
              type: str
              sample: '<address>'
            latitude:
              description: It is the pnp device's latitude.
              returned: changed
              type: str
              sample: '<latitude>'
            longitude:
              description: It is the pnp device's longitude.
              returned: changed
              type: str
              sample: '<longitude>'
            altitude:
              description: It is the pnp device's altitude.
              returned: changed
              type: str
              sample: '<altitude>'

        description:
          description: It is the pnp device's description.
          returned: changed
          type: str
          sample: '<description>'
        onbState:
          description: It is the pnp device's onbState.
          returned: changed
          type: str
          sample: '<onbstate>'
        authenticatedMicNumber:
          description: It is the pnp device's authenticatedMicNumber.
          returned: changed
          type: str
          sample: '<authenticatedmicnumber>'
        authenticatedSudiSerialNo:
          description: It is the pnp device's authenticatedSudiSerialNo.
          returned: changed
          type: str
          sample: '<authenticatedsudiserialno>'
        capabilitiesSupported:
          description: It is the pnp device's capabilitiesSupported.
          returned: changed
          type: list
        featuresSupported:
          description: It is the pnp device's featuresSupported.
          returned: changed
          type: list
        cmState:
          description: It is the pnp device's cmState.
          returned: changed
          type: str
          sample: '<cmstate>'
        firstContact:
          description: It is the pnp device's firstContact.
          returned: changed
          type: int
          sample: 0
        lastContact:
          description: It is the pnp device's lastContact.
          returned: changed
          type: int
          sample: 0
        macAddress:
          description: It is the pnp device's macAddress.
          returned: changed
          type: str
          sample: '<macaddress>'
        pid:
          description: It is the pnp device's pid.
          returned: changed
          type: str
          sample: '<pid>'
        deviceSudiSerialNos:
          description: It is the pnp device's deviceSudiSerialNos.
          returned: changed
          type: list
        lastUpdateOn:
          description: It is the pnp device's lastUpdateOn.
          returned: changed
          type: int
          sample: 0
        workflowId:
          description: It is the pnp device's workflowId.
          returned: changed
          type: str
          sample: '<workflowid>'
        workflowName:
          description: It is the pnp device's workflowName.
          returned: changed
          type: str
          sample: '<workflowname>'
        projectId:
          description: It is the pnp device's projectId.
          returned: changed
          type: str
          sample: '<projectid>'
        projectName:
          description: It is the pnp device's projectName.
          returned: changed
          type: str
          sample: '<projectname>'
        deviceType:
          description: It is the pnp device's deviceType.
          returned: changed
          type: str
          sample: '<devicetype>'
        agentType:
          description: It is the pnp device's agentType.
          returned: changed
          type: str
          sample: '<agenttype>'
        imageVersion:
          description: It is the pnp device's imageVersion.
          returned: changed
          type: str
          sample: '<imageversion>'
        fileSystemList:
          description: It is the pnp device's fileSystemList.
          returned: changed
          type: list
          contains:
            type:
              description: It is the pnp device's type.
              returned: changed
              type: str
              sample: '<type>'
            writeable:
              description: It is the pnp device's writeable.
              returned: changed
              type: bool
              sample: false
            freespace:
              description: It is the pnp device's freespace.
              returned: changed
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: changed
              type: str
              sample: '<name>'
            readable:
              description: It is the pnp device's readable.
              returned: changed
              type: bool
              sample: false
            size:
              description: It is the pnp device's size.
              returned: changed
              type: int
              sample: 0

        pnpProfileList:
          description: It is the pnp device's pnpProfileList.
          returned: changed
          type: list
          contains:
            profileName:
              description: It is the pnp device's profileName.
              returned: changed
              type: str
              sample: '<profilename>'
            discoveryCreated:
              description: It is the pnp device's discoveryCreated.
              returned: changed
              type: bool
              sample: false
            createdBy:
              description: It is the pnp device's createdBy.
              returned: changed
              type: str
              sample: '<createdby>'
            primaryEndpoint:
              description: It is the pnp device's primaryEndpoint.
              returned: changed
              type: dict
              contains:
                port:
                  description: It is the pnp device's port.
                  returned: changed
                  type: int
                  sample: 0
                protocol:
                  description: It is the pnp device's protocol.
                  returned: changed
                  type: str
                  sample: '<protocol>'
                ipv4Address:
                  description: It is the pnp device's ipv4Address.
                  returned: changed
                  type: dict
                ipv6Address:
                  description: It is the pnp device's ipv6Address.
                  returned: changed
                  type: dict
                fqdn:
                  description: It is the pnp device's fqdn.
                  returned: changed
                  type: str
                  sample: '<fqdn>'
                certificate:
                  description: It is the pnp device's certificate.
                  returned: changed
                  type: str
                  sample: '<certificate>'

            secondaryEndpoint:
              description: It is the pnp device's secondaryEndpoint.
              returned: changed
              type: dict
              contains:
                port:
                  description: It is the pnp device's port.
                  returned: changed
                  type: int
                  sample: 0
                protocol:
                  description: It is the pnp device's protocol.
                  returned: changed
                  type: str
                  sample: '<protocol>'
                ipv4Address:
                  description: It is the pnp device's ipv4Address.
                  returned: changed
                  type: dict
                ipv6Address:
                  description: It is the pnp device's ipv6Address.
                  returned: changed
                  type: dict
                fqdn:
                  description: It is the pnp device's fqdn.
                  returned: changed
                  type: str
                  sample: '<fqdn>'
                certificate:
                  description: It is the pnp device's certificate.
                  returned: changed
                  type: str
                  sample: '<certificate>'


        imageFile:
          description: It is the pnp device's imageFile.
          returned: changed
          type: str
          sample: '<imagefile>'
        httpHeaders:
          description: It is the pnp device's httpHeaders.
          returned: changed
          type: list
          contains:
            key:
              description: It is the pnp device's key.
              returned: changed
              type: str
              sample: '<key>'
            value:
              description: It is the pnp device's value.
              returned: changed
              type: str
              sample: '<value>'

        neighborLinks:
          description: It is the pnp device's neighborLinks.
          returned: changed
          type: list
          contains:
            localInterfaceName:
              description: It is the pnp device's localInterfaceName.
              returned: changed
              type: str
              sample: '<localinterfacename>'
            localShortInterfaceName:
              description: It is the pnp device's localShortInterfaceName.
              returned: changed
              type: str
              sample: '<localshortinterfacename>'
            localMacAddress:
              description: It is the pnp device's localMacAddress.
              returned: changed
              type: str
              sample: '<localmacaddress>'
            remoteInterfaceName:
              description: It is the pnp device's remoteInterfaceName.
              returned: changed
              type: str
              sample: '<remoteinterfacename>'
            remoteShortInterfaceName:
              description: It is the pnp device's remoteShortInterfaceName.
              returned: changed
              type: str
              sample: '<remoteshortinterfacename>'
            remoteMacAddress:
              description: It is the pnp device's remoteMacAddress.
              returned: changed
              type: str
              sample: '<remotemacaddress>'
            remoteDeviceName:
              description: It is the pnp device's remoteDeviceName.
              returned: changed
              type: str
              sample: '<remotedevicename>'
            remotePlatform:
              description: It is the pnp device's remotePlatform.
              returned: changed
              type: str
              sample: '<remoteplatform>'
            remoteVersion:
              description: It is the pnp device's remoteVersion.
              returned: changed
              type: str
              sample: '<remoteversion>'

        lastSyncTime:
          description: It is the pnp device's lastSyncTime.
          returned: changed
          type: int
          sample: 0
        ipInterfaces:
          description: It is the pnp device's ipInterfaces.
          returned: changed
          type: list
          contains:
            status:
              description: It is the pnp device's status.
              returned: changed
              type: str
              sample: '<status>'
            macAddress:
              description: It is the pnp device's macAddress.
              returned: changed
              type: str
              sample: '<macaddress>'
            ipv4Address:
              description: It is the pnp device's ipv4Address.
              returned: changed
              type: dict
            ipv6AddressList:
              description: It is the pnp device's ipv6AddressList.
              returned: changed
              type: list
            name:
              description: It is the pnp device's name.
              returned: changed
              type: str
              sample: '<name>'

        hostname:
          description: It is the pnp device's hostname.
          returned: changed
          type: str
          sample: '<hostname>'
        authStatus:
          description: It is the pnp device's authStatus.
          returned: changed
          type: str
          sample: '<authstatus>'
        stackInfo:
          description: It is the pnp device's stackInfo.
          returned: changed
          type: dict
          contains:
            supportsStackWorkflows:
              description: It is the pnp device's supportsStackWorkflows.
              returned: changed
              type: bool
              sample: false
            isFullRing:
              description: It is the pnp device's isFullRing.
              returned: changed
              type: bool
              sample: false
            stackMemberList:
              description: It is the pnp device's stackMemberList.
              returned: changed
              type: list
              contains:
                serialNumber:
                  description: It is the pnp device's serialNumber.
                  returned: changed
                  type: str
                  sample: '<serialnumber>'
                state:
                  description: It is the pnp device's state.
                  returned: changed
                  type: str
                  sample: '<state>'
                role:
                  description: It is the pnp device's role.
                  returned: changed
                  type: str
                  sample: '<role>'
                macAddress:
                  description: It is the pnp device's macAddress.
                  returned: changed
                  type: str
                  sample: '<macaddress>'
                pid:
                  description: It is the pnp device's pid.
                  returned: changed
                  type: str
                  sample: '<pid>'
                licenseLevel:
                  description: It is the pnp device's licenseLevel.
                  returned: changed
                  type: str
                  sample: '<licenselevel>'
                licenseType:
                  description: It is the pnp device's licenseType.
                  returned: changed
                  type: str
                  sample: '<licensetype>'
                sudiSerialNumber:
                  description: It is the pnp device's sudiSerialNumber.
                  returned: changed
                  type: str
                  sample: '<sudiserialnumber>'
                hardwareVersion:
                  description: It is the pnp device's hardwareVersion.
                  returned: changed
                  type: str
                  sample: '<hardwareversion>'
                stackNumber:
                  description: It is the pnp device's stackNumber.
                  returned: changed
                  type: int
                  sample: 0
                softwareVersion:
                  description: It is the pnp device's softwareVersion.
                  returned: changed
                  type: str
                  sample: '<softwareversion>'
                priority:
                  description: It is the pnp device's priority.
                  returned: changed
                  type: int
                  sample: 0

            stackRingProtocol:
              description: It is the pnp device's stackRingProtocol.
              returned: changed
              type: str
              sample: '<stackringprotocol>'
            validLicenseLevels:
              description: It is the pnp device's validLicenseLevels.
              returned: changed
              type: list
            totalMemberCount:
              description: It is the pnp device's totalMemberCount.
              returned: changed
              type: int
              sample: 0

        reloadRequested:
          description: It is the pnp device's reloadRequested.
          returned: changed
          type: bool
          sample: false
        addedOn:
          description: It is the pnp device's addedOn.
          returned: changed
          type: int
          sample: 0
        siteId:
          description: It is the pnp device's siteId.
          returned: changed
          type: str
          sample: '<siteid>'
        aaaCredentials:
          description: It is the pnp device's aaaCredentials.
          returned: changed
          type: dict
          contains:
            password:
              description: It is the pnp device's password.
              returned: changed
              type: str
              sample: '*******'
            username:
              description: It is the pnp device's username.
              returned: changed
              type: str
              sample: 'devnetuser'

        userMicNumbers:
          description: It is the pnp device's userMicNumbers.
          returned: changed
          type: list
        userSudiSerialNos:
          description: It is the pnp device's userSudiSerialNos.
          returned: changed
          type: list
        addnMacAddrs:
          description: It is the pnp device's addnMacAddrs.
          returned: changed
          type: list
        preWorkflowCliOuputs:
          description: It is the pnp device's preWorkflowCliOuputs.
          returned: changed
          type: list
          contains:
            cli:
              description: It is the pnp device's cli.
              returned: changed
              type: str
              sample: '<cli>'
            cliOutput:
              description: It is the pnp device's cliOutput.
              returned: changed
              type: str
              sample: '<clioutput>'

        tags:
          description: It is the pnp device's tags.
          returned: changed
          type: dict
        sudiRequired:
          description: It is the pnp device's sudiRequired.
          returned: changed
          type: bool
          sample: false
        smartAccountId:
          description: It is the pnp device's smartAccountId.
          returned: changed
          type: str
          sample: '<smartaccountid>'
        virtualAccountId:
          description: It is the pnp device's virtualAccountId.
          returned: changed
          type: str
          sample: '<virtualaccountid>'
        populateInventory:
          description: It is the pnp device's populateInventory.
          returned: changed
          type: bool
          sample: false
        siteName:
          description: It is the pnp device's siteName.
          returned: changed
          type: str
          sample: '<sitename>'
        name:
          description: It is the pnp device's name.
          returned: changed
          type: str
          sample: '<name>'

    systemResetWorkflow:
      description: Device's System Reset Workflow.
      returned: changed
      type: dict
      contains:
        _id:
          description: It is the pnp device's _id.
          returned: changed
          type: str
          sample: '<_id>'
        state:
          description: It is the pnp device's state.
          returned: changed
          type: str
          sample: '<state>'
        type:
          description: It is the pnp device's type.
          returned: changed
          type: str
          sample: '<type>'
        description:
          description: It is the pnp device's description.
          returned: changed
          type: str
          sample: '<description>'
        lastupdateOn:
          description: It is the pnp device's lastupdateOn.
          returned: changed
          type: int
          sample: 0
        imageId:
          description: It is the pnp device's imageId.
          returned: changed
          type: str
          sample: '<imageid>'
        currTaskIdx:
          description: It is the pnp device's currTaskIdx.
          returned: changed
          type: int
          sample: 0
        addedOn:
          description: It is the pnp device's addedOn.
          returned: changed
          type: int
          sample: 0
        tasks:
          description: It is the pnp device's tasks.
          returned: changed
          type: list
          contains:
            state:
              description: It is the pnp device's state.
              returned: changed
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device's type.
              returned: changed
              type: str
              sample: '<type>'
            currWorkItemIdx:
              description: It is the pnp device's currWorkItemIdx.
              returned: changed
              type: int
              sample: 0
            taskSeqNo:
              description: It is the pnp device's taskSeqNo.
              returned: changed
              type: int
              sample: 0
            endTime:
              description: It is the pnp device's endTime.
              returned: changed
              type: int
              sample: 0
            startTime:
              description: It is the pnp device's startTime.
              returned: changed
              type: int
              sample: 0
            workItemList:
              description: It is the pnp device's workItemList.
              returned: changed
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: changed
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: changed
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: changed
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: changed
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: changed
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: changed
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: changed
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: changed
              type: str
              sample: '<name>'

        addToInventory:
          description: It is the pnp device's addToInventory.
          returned: changed
          type: bool
          sample: false
        instanceType:
          description: It is the pnp device's instanceType.
          returned: changed
          type: str
          sample: '<instancetype>'
        endTime:
          description: It is the pnp device's endTime.
          returned: changed
          type: int
          sample: 0
        execTime:
          description: It is the pnp device's execTime.
          returned: changed
          type: int
          sample: 0
        startTime:
          description: It is the pnp device's startTime.
          returned: changed
          type: int
          sample: 0
        useState:
          description: It is the pnp device's useState.
          returned: changed
          type: str
          sample: '<usestate>'
        configId:
          description: It is the pnp device's configId.
          returned: changed
          type: str
          sample: '<configid>'
        name:
          description: It is the pnp device's name.
          returned: changed
          type: str
          sample: '<name>'
        version:
          description: It is the pnp device's version.
          returned: changed
          type: int
          sample: 0
        tenantId:
          description: It is the pnp device's tenantId.
          returned: changed
          type: str
          sample: '<tenantid>'

    systemWorkflow:
      description: Device's System Workflow.
      returned: changed
      type: dict
      contains:
        _id:
          description: It is the pnp device's _id.
          returned: changed
          type: str
          sample: '<_id>'
        state:
          description: It is the pnp device's state.
          returned: changed
          type: str
          sample: '<state>'
        type:
          description: It is the pnp device's type.
          returned: changed
          type: str
          sample: '<type>'
        description:
          description: It is the pnp device's description.
          returned: changed
          type: str
          sample: '<description>'
        lastupdateOn:
          description: It is the pnp device's lastupdateOn.
          returned: changed
          type: int
          sample: 0
        imageId:
          description: It is the pnp device's imageId.
          returned: changed
          type: str
          sample: '<imageid>'
        currTaskIdx:
          description: It is the pnp device's currTaskIdx.
          returned: changed
          type: int
          sample: 0
        addedOn:
          description: It is the pnp device's addedOn.
          returned: changed
          type: int
          sample: 0
        tasks:
          description: It is the pnp device's tasks.
          returned: changed
          type: list
          contains:
            state:
              description: It is the pnp device's state.
              returned: changed
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device's type.
              returned: changed
              type: str
              sample: '<type>'
            currWorkItemIdx:
              description: It is the pnp device's currWorkItemIdx.
              returned: changed
              type: int
              sample: 0
            taskSeqNo:
              description: It is the pnp device's taskSeqNo.
              returned: changed
              type: int
              sample: 0
            endTime:
              description: It is the pnp device's endTime.
              returned: changed
              type: int
              sample: 0
            startTime:
              description: It is the pnp device's startTime.
              returned: changed
              type: int
              sample: 0
            workItemList:
              description: It is the pnp device's workItemList.
              returned: changed
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: changed
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: changed
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: changed
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: changed
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: changed
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: changed
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: changed
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: changed
              type: str
              sample: '<name>'

        addToInventory:
          description: It is the pnp device's addToInventory.
          returned: changed
          type: bool
          sample: false
        instanceType:
          description: It is the pnp device's instanceType.
          returned: changed
          type: str
          sample: '<instancetype>'
        endTime:
          description: It is the pnp device's endTime.
          returned: changed
          type: int
          sample: 0
        execTime:
          description: It is the pnp device's execTime.
          returned: changed
          type: int
          sample: 0
        startTime:
          description: It is the pnp device's startTime.
          returned: changed
          type: int
          sample: 0
        useState:
          description: It is the pnp device's useState.
          returned: changed
          type: str
          sample: '<usestate>'
        configId:
          description: It is the pnp device's configId.
          returned: changed
          type: str
          sample: '<configid>'
        name:
          description: It is the pnp device's name.
          returned: changed
          type: str
          sample: '<name>'
        version:
          description: It is the pnp device's version.
          returned: changed
          type: int
          sample: 0
        tenantId:
          description: It is the pnp device's tenantId.
          returned: changed
          type: str
          sample: '<tenantid>'

    workflow:
      description: Device's Workflow.
      returned: changed
      type: dict
      contains:
        _id:
          description: It is the pnp device's _id.
          returned: changed
          type: str
          sample: '<_id>'
        state:
          description: It is the pnp device's state.
          returned: changed
          type: str
          sample: '<state>'
        type:
          description: It is the pnp device's type.
          returned: changed
          type: str
          sample: '<type>'
        description:
          description: It is the pnp device's description.
          returned: changed
          type: str
          sample: '<description>'
        lastupdateOn:
          description: It is the pnp device's lastupdateOn.
          returned: changed
          type: int
          sample: 0
        imageId:
          description: It is the pnp device's imageId.
          returned: changed
          type: str
          sample: '<imageid>'
        currTaskIdx:
          description: It is the pnp device's currTaskIdx.
          returned: changed
          type: int
          sample: 0
        addedOn:
          description: It is the pnp device's addedOn.
          returned: changed
          type: int
          sample: 0
        tasks:
          description: It is the pnp device's tasks.
          returned: changed
          type: list
          contains:
            state:
              description: It is the pnp device's state.
              returned: changed
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device's type.
              returned: changed
              type: str
              sample: '<type>'
            currWorkItemIdx:
              description: It is the pnp device's currWorkItemIdx.
              returned: changed
              type: int
              sample: 0
            taskSeqNo:
              description: It is the pnp device's taskSeqNo.
              returned: changed
              type: int
              sample: 0
            endTime:
              description: It is the pnp device's endTime.
              returned: changed
              type: int
              sample: 0
            startTime:
              description: It is the pnp device's startTime.
              returned: changed
              type: int
              sample: 0
            workItemList:
              description: It is the pnp device's workItemList.
              returned: changed
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: changed
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: changed
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: changed
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: changed
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: changed
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: changed
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: changed
              type: int
              sample: 0
            name:
              description: It is the pnp device's name.
              returned: changed
              type: str
              sample: '<name>'

        addToInventory:
          description: It is the pnp device's addToInventory.
          returned: changed
          type: bool
          sample: false
        instanceType:
          description: It is the pnp device's instanceType.
          returned: changed
          type: str
          sample: '<instancetype>'
        endTime:
          description: It is the pnp device's endTime.
          returned: changed
          type: int
          sample: 0
        execTime:
          description: It is the pnp device's execTime.
          returned: changed
          type: int
          sample: 0
        startTime:
          description: It is the pnp device's startTime.
          returned: changed
          type: int
          sample: 0
        useState:
          description: It is the pnp device's useState.
          returned: changed
          type: str
          sample: '<usestate>'
        configId:
          description: It is the pnp device's configId.
          returned: changed
          type: str
          sample: '<configid>'
        name:
          description: It is the pnp device's name.
          returned: changed
          type: str
          sample: '<name>'
        version:
          description: It is the pnp device's version.
          returned: changed
          type: int
          sample: 0
        tenantId:
          description: It is the pnp device's tenantId.
          returned: changed
          type: str
          sample: '<tenantid>'

    runSummaryList:
      description: Device's Run Summary List (list of objects).
      returned: changed
      type: list
      contains:
        details:
          description: It is the pnp device's details.
          returned: changed
          type: str
          sample: '<details>'
        historyTaskInfo:
          description: It is the pnp device's historyTaskInfo.
          returned: changed
          type: dict
          contains:
            type:
              description: It is the pnp device's type.
              returned: changed
              type: str
              sample: '<type>'
            workItemList:
              description: It is the pnp device's workItemList.
              returned: changed
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: changed
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: changed
                  type: str
                  sample: '<command>'
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: changed
                  type: str
                  sample: '<outputstr>'
                endTime:
                  description: It is the pnp device's endTime.
                  returned: changed
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device's startTime.
                  returned: changed
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: changed
                  type: int
                  sample: 0

            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: changed
              type: int
              sample: 0
            addnDetails:
              description: It is the pnp device's addnDetails.
              returned: changed
              type: list
              contains:
                key:
                  description: It is the pnp device's key.
                  returned: changed
                  type: str
                  sample: '<key>'
                value:
                  description: It is the pnp device's value.
                  returned: changed
                  type: str
                  sample: '<value>'

            name:
              description: It is the pnp device's name.
              returned: changed
              type: str
              sample: '<name>'

        errorFlag:
          description: It is the pnp device's errorFlag.
          returned: changed
          type: bool
          sample: false
        timestamp:
          description: It is the pnp device's timestamp.
          returned: changed
          type: int
          sample: 0

    workflowParameters:
      description: Device's Workflow Parameters.
      returned: changed
      type: dict
      contains:
        topOfStackSerialNumber:
          description: It is the pnp device's topOfStackSerialNumber.
          returned: changed
          type: str
          sample: '<topofstackserialnumber>'
        licenseLevel:
          description: It is the pnp device's licenseLevel.
          returned: changed
          type: str
          sample: '<licenselevel>'
        licenseType:
          description: It is the pnp device's licenseType.
          returned: changed
          type: str
          sample: '<licensetype>'
        configList:
          description: It is the pnp device's configList.
          returned: changed
          type: list
          contains:
            configParameters:
              description: It is the pnp device's configParameters.
              returned: changed
              type: list
              contains:
                key:
                  description: It is the pnp device's key.
                  returned: changed
                  type: str
                  sample: '<key>'
                value:
                  description: It is the pnp device's value.
                  returned: changed
                  type: str
                  sample: '<value>'

            configId:
              description: It is the pnp device's configId.
              returned: changed
              type: str
              sample: '<configid>'


    dayZeroConfig:
      description: Device's Day Zero Config.
      returned: changed
      type: dict
      contains:
        config:
          description: It is the pnp device's config.
          returned: changed
          type: str
          sample: '<config>'

    dayZeroConfigPreview:
      description: Device's Day Zero Config Preview.
      returned: changed
      type: dict
    version:
      description: Device's version.
      returned: changed
      type: int
      sample: 0
    tenantId:
      description: Device's Tenant Id.
      returned: changed
      type: str
      sample: '<tenantid>'

get_device_count:
    description: Returns the device count based on filter criteria. This is useful for pagination.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: int
      sample: 0

get_device_history:
    description: Returns history for a specific device. Serial number is a required parameter.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        timestamp:
          description: It is the pnp device's timestamp.
          returned: always
          type: int
          sample: 0
        details:
          description: It is the pnp device's details.
          returned: always
          type: str
          sample: '<details>'
        historyTaskInfo:
          description: It is the pnp device's historyTaskInfo.
          returned: always
          type: dict
          contains:
            name:
              description: It is the pnp device's name.
              returned: always
              type: str
              sample: '<name>'
            type:
              description: It is the pnp device's type.
              returned: always
              type: str
              sample: '<type>'
            timeTaken:
              description: It is the pnp device's timeTaken.
              returned: always
              type: int
              sample: 0
            workItemList:
              description: It is the pnp device's workItemList.
              returned: always
              type: list
              contains:
                state:
                  description: It is the pnp device's state.
                  returned: always
                  type: str
                  sample: '<state>'
                command:
                  description: It is the pnp device's command.
                  returned: always
                  type: str
                  sample: '<command>'
                startTime:
                  description: It is the pnp device's startTime.
                  returned: always
                  type: int
                  sample: 0
                endTime:
                  description: It is the pnp device's endTime.
                  returned: always
                  type: int
                  sample: 0
                timeTaken:
                  description: It is the pnp device's timeTaken.
                  returned: always
                  type: int
                  sample: 0
                outputStr:
                  description: It is the pnp device's outputStr.
                  returned: always
                  type: str
                  sample: '<outputstr>'

            addnDetails:
              description: It is the pnp device's addnDetails.
              returned: always
              type: list
              contains:
                key:
                  description: It is the pnp device's key.
                  returned: always
                  type: str
                  sample: '<key>'
                value:
                  description: It is the pnp device's value.
                  returned: always
                  type: str
                  sample: '<value>'


        errorFlag:
          description: It is the pnp device's errorFlag.
          returned: always
          type: bool
          sample: false

    statusCode:
      description: StatusCode, property of the response body.
      returned: always
      type: int
      sample: 0

"""
