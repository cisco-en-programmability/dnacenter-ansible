#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

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
version_added: '1.0.0'
author: Rafael Campos (@racampos)
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
"""
