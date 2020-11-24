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
module: pnp_device_import
short_description: Manage PnpDeviceImport objects of DeviceOnboardingPnp
description:
- Add devices to PnP in bulk.
version_added: '1.0'
author: first last (@GitHubID)
options:
  payload:
    description:
    - An object to send in the Request body.
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
"""

EXAMPLES = r"""
- name: import_devices_in_bulk
  cisco.dnac.pnp_device_import
    dnac_host: dnac
    dnac_username: admin
    dnac_password: SomeSecretPassword
    state: create  # required
    payload:  # required
    - deviceInfo:  # required
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
  delegate_to: localhost
  
"""

RETURN = """
import_devices_in_bulk:
    description: Add devices to PnP in bulk.
    returned: success
    type: dict
    contains:
    successList:
      description: Device's Success List (list of objects).
      returned: success
      type: list
      contains:
        _id:
          description: It is the pnp device import's _id.
          returned: success
          type: str
          sample: '<_id>'
        deviceInfo:
          description: It is the pnp device import's deviceInfo.
          returned: success
          type: dict
          contains:
            source:
              description: It is the pnp device import's source.
              returned: success
              type: str
              sample: '<source>'
            serialNumber:
              description: It is the pnp device import's serialNumber.
              returned: success
              type: str
              sample: '<serialnumber>'
            stack:
              description: It is the pnp device import's stack.
              returned: success
              type: bool
              sample: false
            mode:
              description: It is the pnp device import's mode.
              returned: success
              type: str
              sample: '<mode>'
            state:
              description: It is the pnp device import's state.
              returned: success
              type: str
              sample: '<state>'
            location:
              description: It is the pnp device import's location.
              returned: success
              type: dict
              contains:
                siteId:
                  description: It is the pnp device import's siteId.
                  returned: success
                  type: str
                  sample: '<siteid>'
                address:
                  description: It is the pnp device import's address.
                  returned: success
                  type: str
                  sample: '<address>'
                latitude:
                  description: It is the pnp device import's latitude.
                  returned: success
                  type: str
                  sample: '<latitude>'
                longitude:
                  description: It is the pnp device import's longitude.
                  returned: success
                  type: str
                  sample: '<longitude>'
                altitude:
                  description: It is the pnp device import's altitude.
                  returned: success
                  type: str
                  sample: '<altitude>'

            description:
              description: It is the pnp device import's description.
              returned: success
              type: str
              sample: '<description>'
            onbState:
              description: It is the pnp device import's onbState.
              returned: success
              type: str
              sample: '<onbstate>'
            authenticatedMicNumber:
              description: It is the pnp device import's authenticatedMicNumber.
              returned: success
              type: str
              sample: '<authenticatedmicnumber>'
            authenticatedSudiSerialNo:
              description: It is the pnp device import's authenticatedSudiSerialNo.
              returned: success
              type: str
              sample: '<authenticatedsudiserialno>'
            capabilitiesSupported:
              description: It is the pnp device import's capabilitiesSupported.
              returned: success
              type: list
            featuresSupported:
              description: It is the pnp device import's featuresSupported.
              returned: success
              type: list
            cmState:
              description: It is the pnp device import's cmState.
              returned: success
              type: str
              sample: '<cmstate>'
            firstContact:
              description: It is the pnp device import's firstContact.
              returned: success
              type: int
              sample: 0
            lastContact:
              description: It is the pnp device import's lastContact.
              returned: success
              type: int
              sample: 0
            macAddress:
              description: It is the pnp device import's macAddress.
              returned: success
              type: str
              sample: '<macaddress>'
            pid:
              description: It is the pnp device import's pid.
              returned: success
              type: str
              sample: '<pid>'
            deviceSudiSerialNos:
              description: It is the pnp device import's deviceSudiSerialNos.
              returned: success
              type: list
            lastUpdateOn:
              description: It is the pnp device import's lastUpdateOn.
              returned: success
              type: int
              sample: 0
            workflowId:
              description: It is the pnp device import's workflowId.
              returned: success
              type: str
              sample: '<workflowid>'
            workflowName:
              description: It is the pnp device import's workflowName.
              returned: success
              type: str
              sample: '<workflowname>'
            projectId:
              description: It is the pnp device import's projectId.
              returned: success
              type: str
              sample: '<projectid>'
            projectName:
              description: It is the pnp device import's projectName.
              returned: success
              type: str
              sample: '<projectname>'
            deviceType:
              description: It is the pnp device import's deviceType.
              returned: success
              type: str
              sample: '<devicetype>'
            agentType:
              description: It is the pnp device import's agentType.
              returned: success
              type: str
              sample: '<agenttype>'
            imageVersion:
              description: It is the pnp device import's imageVersion.
              returned: success
              type: str
              sample: '<imageversion>'
            fileSystemList:
              description: It is the pnp device import's fileSystemList.
              returned: success
              type: list
              contains:
                type:
                  description: It is the pnp device import's type.
                  returned: success
                  type: str
                  sample: '<type>'
                writeable:
                  description: It is the pnp device import's writeable.
                  returned: success
                  type: bool
                  sample: false
                freespace:
                  description: It is the pnp device import's freespace.
                  returned: success
                  type: int
                  sample: 0
                name:
                  description: It is the pnp device import's name.
                  returned: success
                  type: str
                  sample: '<name>'
                readable:
                  description: It is the pnp device import's readable.
                  returned: success
                  type: bool
                  sample: false
                size:
                  description: It is the pnp device import's size.
                  returned: success
                  type: int
                  sample: 0

            pnpProfileList:
              description: It is the pnp device import's pnpProfileList.
              returned: success
              type: list
              contains:
                profileName:
                  description: It is the pnp device import's profileName.
                  returned: success
                  type: str
                  sample: '<profilename>'
                discoveryCreated:
                  description: It is the pnp device import's discoveryCreated.
                  returned: success
                  type: bool
                  sample: false
                createdBy:
                  description: It is the pnp device import's createdBy.
                  returned: success
                  type: str
                  sample: '<createdby>'
                primaryEndpoint:
                  description: It is the pnp device import's primaryEndpoint.
                  returned: success
                  type: dict
                  contains:
                    port:
                      description: It is the pnp device import's port.
                      returned: success
                      type: int
                      sample: 0
                    protocol:
                      description: It is the pnp device import's protocol.
                      returned: success
                      type: str
                      sample: '<protocol>'
                    ipv4Address:
                      description: It is the pnp device import's ipv4Address.
                      returned: success
                      type: dict
                    ipv6Address:
                      description: It is the pnp device import's ipv6Address.
                      returned: success
                      type: dict
                    fqdn:
                      description: It is the pnp device import's fqdn.
                      returned: success
                      type: str
                      sample: '<fqdn>'
                    certificate:
                      description: It is the pnp device import's certificate.
                      returned: success
                      type: str
                      sample: '<certificate>'

                secondaryEndpoint:
                  description: It is the pnp device import's secondaryEndpoint.
                  returned: success
                  type: dict
                  contains:
                    port:
                      description: It is the pnp device import's port.
                      returned: success
                      type: int
                      sample: 0
                    protocol:
                      description: It is the pnp device import's protocol.
                      returned: success
                      type: str
                      sample: '<protocol>'
                    ipv4Address:
                      description: It is the pnp device import's ipv4Address.
                      returned: success
                      type: dict
                    ipv6Address:
                      description: It is the pnp device import's ipv6Address.
                      returned: success
                      type: dict
                    fqdn:
                      description: It is the pnp device import's fqdn.
                      returned: success
                      type: str
                      sample: '<fqdn>'
                    certificate:
                      description: It is the pnp device import's certificate.
                      returned: success
                      type: str
                      sample: '<certificate>'


            imageFile:
              description: It is the pnp device import's imageFile.
              returned: success
              type: str
              sample: '<imagefile>'
            httpHeaders:
              description: It is the pnp device import's httpHeaders.
              returned: success
              type: list
              contains:
                key:
                  description: It is the pnp device import's key.
                  returned: success
                  type: str
                  sample: '<key>'
                value:
                  description: It is the pnp device import's value.
                  returned: success
                  type: str
                  sample: '<value>'

            neighborLinks:
              description: It is the pnp device import's neighborLinks.
              returned: success
              type: list
              contains:
                localInterfaceName:
                  description: It is the pnp device import's localInterfaceName.
                  returned: success
                  type: str
                  sample: '<localinterfacename>'
                localShortInterfaceName:
                  description: It is the pnp device import's localShortInterfaceName.
                  returned: success
                  type: str
                  sample: '<localshortinterfacename>'
                localMacAddress:
                  description: It is the pnp device import's localMacAddress.
                  returned: success
                  type: str
                  sample: '<localmacaddress>'
                remoteInterfaceName:
                  description: It is the pnp device import's remoteInterfaceName.
                  returned: success
                  type: str
                  sample: '<remoteinterfacename>'
                remoteShortInterfaceName:
                  description: It is the pnp device import's remoteShortInterfaceName.
                  returned: success
                  type: str
                  sample: '<remoteshortinterfacename>'
                remoteMacAddress:
                  description: It is the pnp device import's remoteMacAddress.
                  returned: success
                  type: str
                  sample: '<remotemacaddress>'
                remoteDeviceName:
                  description: It is the pnp device import's remoteDeviceName.
                  returned: success
                  type: str
                  sample: '<remotedevicename>'
                remotePlatform:
                  description: It is the pnp device import's remotePlatform.
                  returned: success
                  type: str
                  sample: '<remoteplatform>'
                remoteVersion:
                  description: It is the pnp device import's remoteVersion.
                  returned: success
                  type: str
                  sample: '<remoteversion>'

            lastSyncTime:
              description: It is the pnp device import's lastSyncTime.
              returned: success
              type: int
              sample: 0
            ipInterfaces:
              description: It is the pnp device import's ipInterfaces.
              returned: success
              type: list
              contains:
                status:
                  description: It is the pnp device import's status.
                  returned: success
                  type: str
                  sample: '<status>'
                macAddress:
                  description: It is the pnp device import's macAddress.
                  returned: success
                  type: str
                  sample: '<macaddress>'
                ipv4Address:
                  description: It is the pnp device import's ipv4Address.
                  returned: success
                  type: dict
                ipv6AddressList:
                  description: It is the pnp device import's ipv6AddressList.
                  returned: success
                  type: list
                name:
                  description: It is the pnp device import's name.
                  returned: success
                  type: str
                  sample: '<name>'

            hostname:
              description: It is the pnp device import's hostname.
              returned: success
              type: str
              sample: '<hostname>'
            authStatus:
              description: It is the pnp device import's authStatus.
              returned: success
              type: str
              sample: '<authstatus>'
            stackInfo:
              description: It is the pnp device import's stackInfo.
              returned: success
              type: dict
              contains:
                supportsStackWorkflows:
                  description: It is the pnp device import's supportsStackWorkflows.
                  returned: success
                  type: bool
                  sample: false
                isFullRing:
                  description: It is the pnp device import's isFullRing.
                  returned: success
                  type: bool
                  sample: false
                stackMemberList:
                  description: It is the pnp device import's stackMemberList.
                  returned: success
                  type: list
                  contains:
                    serialNumber:
                      description: It is the pnp device import's serialNumber.
                      returned: success
                      type: str
                      sample: '<serialnumber>'
                    state:
                      description: It is the pnp device import's state.
                      returned: success
                      type: str
                      sample: '<state>'
                    role:
                      description: It is the pnp device import's role.
                      returned: success
                      type: str
                      sample: '<role>'
                    macAddress:
                      description: It is the pnp device import's macAddress.
                      returned: success
                      type: str
                      sample: '<macaddress>'
                    pid:
                      description: It is the pnp device import's pid.
                      returned: success
                      type: str
                      sample: '<pid>'
                    licenseLevel:
                      description: It is the pnp device import's licenseLevel.
                      returned: success
                      type: str
                      sample: '<licenselevel>'
                    licenseType:
                      description: It is the pnp device import's licenseType.
                      returned: success
                      type: str
                      sample: '<licensetype>'
                    sudiSerialNumber:
                      description: It is the pnp device import's sudiSerialNumber.
                      returned: success
                      type: str
                      sample: '<sudiserialnumber>'
                    hardwareVersion:
                      description: It is the pnp device import's hardwareVersion.
                      returned: success
                      type: str
                      sample: '<hardwareversion>'
                    stackNumber:
                      description: It is the pnp device import's stackNumber.
                      returned: success
                      type: int
                      sample: 0
                    softwareVersion:
                      description: It is the pnp device import's softwareVersion.
                      returned: success
                      type: str
                      sample: '<softwareversion>'
                    priority:
                      description: It is the pnp device import's priority.
                      returned: success
                      type: int
                      sample: 0

                stackRingProtocol:
                  description: It is the pnp device import's stackRingProtocol.
                  returned: success
                  type: str
                  sample: '<stackringprotocol>'
                validLicenseLevels:
                  description: It is the pnp device import's validLicenseLevels.
                  returned: success
                  type: list
                totalMemberCount:
                  description: It is the pnp device import's totalMemberCount.
                  returned: success
                  type: int
                  sample: 0

            reloadRequested:
              description: It is the pnp device import's reloadRequested.
              returned: success
              type: bool
              sample: false
            addedOn:
              description: It is the pnp device import's addedOn.
              returned: success
              type: int
              sample: 0
            siteId:
              description: It is the pnp device import's siteId.
              returned: success
              type: str
              sample: '<siteid>'
            aaaCredentials:
              description: It is the pnp device import's aaaCredentials.
              returned: success
              type: dict
              contains:
                password:
                  description: It is the pnp device import's password.
                  returned: success
                  type: str
                  sample: '*******'
                username:
                  description: It is the pnp device import's username.
                  returned: success
                  type: str
                  sample: 'devnetuser'

            userMicNumbers:
              description: It is the pnp device import's userMicNumbers.
              returned: success
              type: list
            userSudiSerialNos:
              description: It is the pnp device import's userSudiSerialNos.
              returned: success
              type: list
            addnMacAddrs:
              description: It is the pnp device import's addnMacAddrs.
              returned: success
              type: list
            preWorkflowCliOuputs:
              description: It is the pnp device import's preWorkflowCliOuputs.
              returned: success
              type: list
              contains:
                cli:
                  description: It is the pnp device import's cli.
                  returned: success
                  type: str
                  sample: '<cli>'
                cliOutput:
                  description: It is the pnp device import's cliOutput.
                  returned: success
                  type: str
                  sample: '<clioutput>'

            tags:
              description: It is the pnp device import's tags.
              returned: success
              type: dict
            sudiRequired:
              description: It is the pnp device import's sudiRequired.
              returned: success
              type: bool
              sample: false
            smartAccountId:
              description: It is the pnp device import's smartAccountId.
              returned: success
              type: str
              sample: '<smartaccountid>'
            virtualAccountId:
              description: It is the pnp device import's virtualAccountId.
              returned: success
              type: str
              sample: '<virtualaccountid>'
            populateInventory:
              description: It is the pnp device import's populateInventory.
              returned: success
              type: bool
              sample: false
            siteName:
              description: It is the pnp device import's siteName.
              returned: success
              type: str
              sample: '<sitename>'
            name:
              description: It is the pnp device import's name.
              returned: success
              type: str
              sample: '<name>'

        systemResetWorkflow:
          description: It is the pnp device import's systemResetWorkflow.
          returned: success
          type: dict
          contains:
            _id:
              description: It is the pnp device import's _id.
              returned: success
              type: str
              sample: '<_id>'
            state:
              description: It is the pnp device import's state.
              returned: success
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device import's type.
              returned: success
              type: str
              sample: '<type>'
            description:
              description: It is the pnp device import's description.
              returned: success
              type: str
              sample: '<description>'
            lastupdateOn:
              description: It is the pnp device import's lastupdateOn.
              returned: success
              type: int
              sample: 0
            imageId:
              description: It is the pnp device import's imageId.
              returned: success
              type: str
              sample: '<imageid>'
            currTaskIdx:
              description: It is the pnp device import's currTaskIdx.
              returned: success
              type: int
              sample: 0
            addedOn:
              description: It is the pnp device import's addedOn.
              returned: success
              type: int
              sample: 0
            tasks:
              description: It is the pnp device import's tasks.
              returned: success
              type: list
              contains:
                state:
                  description: It is the pnp device import's state.
                  returned: success
                  type: str
                  sample: '<state>'
                type:
                  description: It is the pnp device import's type.
                  returned: success
                  type: str
                  sample: '<type>'
                currWorkItemIdx:
                  description: It is the pnp device import's currWorkItemIdx.
                  returned: success
                  type: int
                  sample: 0
                taskSeqNo:
                  description: It is the pnp device import's taskSeqNo.
                  returned: success
                  type: int
                  sample: 0
                endTime:
                  description: It is the pnp device import's endTime.
                  returned: success
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device import's startTime.
                  returned: success
                  type: int
                  sample: 0
                workItemList:
                  description: It is the pnp device import's workItemList.
                  returned: success
                  type: list
                  contains:
                    state:
                      description: It is the pnp device import's state.
                      returned: success
                      type: str
                      sample: '<state>'
                    command:
                      description: It is the pnp device import's command.
                      returned: success
                      type: str
                      sample: '<command>'
                    outputStr:
                      description: It is the pnp device import's outputStr.
                      returned: success
                      type: str
                      sample: '<outputstr>'
                    endTime:
                      description: It is the pnp device import's endTime.
                      returned: success
                      type: int
                      sample: 0
                    startTime:
                      description: It is the pnp device import's startTime.
                      returned: success
                      type: int
                      sample: 0
                    timeTaken:
                      description: It is the pnp device import's timeTaken.
                      returned: success
                      type: int
                      sample: 0

                timeTaken:
                  description: It is the pnp device import's timeTaken.
                  returned: success
                  type: int
                  sample: 0
                name:
                  description: It is the pnp device import's name.
                  returned: success
                  type: str
                  sample: '<name>'

            addToInventory:
              description: It is the pnp device import's addToInventory.
              returned: success
              type: bool
              sample: false
            instanceType:
              description: It is the pnp device import's instanceType.
              returned: success
              type: str
              sample: '<instancetype>'
            endTime:
              description: It is the pnp device import's endTime.
              returned: success
              type: int
              sample: 0
            execTime:
              description: It is the pnp device import's execTime.
              returned: success
              type: int
              sample: 0
            startTime:
              description: It is the pnp device import's startTime.
              returned: success
              type: int
              sample: 0
            useState:
              description: It is the pnp device import's useState.
              returned: success
              type: str
              sample: '<usestate>'
            configId:
              description: It is the pnp device import's configId.
              returned: success
              type: str
              sample: '<configid>'
            name:
              description: It is the pnp device import's name.
              returned: success
              type: str
              sample: '<name>'
            version:
              description: It is the pnp device import's version.
              returned: success
              type: int
              sample: 0
            tenantId:
              description: It is the pnp device import's tenantId.
              returned: success
              type: str
              sample: '<tenantid>'

        systemWorkflow:
          description: It is the pnp device import's systemWorkflow.
          returned: success
          type: dict
          contains:
            _id:
              description: It is the pnp device import's _id.
              returned: success
              type: str
              sample: '<_id>'
            state:
              description: It is the pnp device import's state.
              returned: success
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device import's type.
              returned: success
              type: str
              sample: '<type>'
            description:
              description: It is the pnp device import's description.
              returned: success
              type: str
              sample: '<description>'
            lastupdateOn:
              description: It is the pnp device import's lastupdateOn.
              returned: success
              type: int
              sample: 0
            imageId:
              description: It is the pnp device import's imageId.
              returned: success
              type: str
              sample: '<imageid>'
            currTaskIdx:
              description: It is the pnp device import's currTaskIdx.
              returned: success
              type: int
              sample: 0
            addedOn:
              description: It is the pnp device import's addedOn.
              returned: success
              type: int
              sample: 0
            tasks:
              description: It is the pnp device import's tasks.
              returned: success
              type: list
              contains:
                state:
                  description: It is the pnp device import's state.
                  returned: success
                  type: str
                  sample: '<state>'
                type:
                  description: It is the pnp device import's type.
                  returned: success
                  type: str
                  sample: '<type>'
                currWorkItemIdx:
                  description: It is the pnp device import's currWorkItemIdx.
                  returned: success
                  type: int
                  sample: 0
                taskSeqNo:
                  description: It is the pnp device import's taskSeqNo.
                  returned: success
                  type: int
                  sample: 0
                endTime:
                  description: It is the pnp device import's endTime.
                  returned: success
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device import's startTime.
                  returned: success
                  type: int
                  sample: 0
                workItemList:
                  description: It is the pnp device import's workItemList.
                  returned: success
                  type: list
                  contains:
                    state:
                      description: It is the pnp device import's state.
                      returned: success
                      type: str
                      sample: '<state>'
                    command:
                      description: It is the pnp device import's command.
                      returned: success
                      type: str
                      sample: '<command>'
                    outputStr:
                      description: It is the pnp device import's outputStr.
                      returned: success
                      type: str
                      sample: '<outputstr>'
                    endTime:
                      description: It is the pnp device import's endTime.
                      returned: success
                      type: int
                      sample: 0
                    startTime:
                      description: It is the pnp device import's startTime.
                      returned: success
                      type: int
                      sample: 0
                    timeTaken:
                      description: It is the pnp device import's timeTaken.
                      returned: success
                      type: int
                      sample: 0

                timeTaken:
                  description: It is the pnp device import's timeTaken.
                  returned: success
                  type: int
                  sample: 0
                name:
                  description: It is the pnp device import's name.
                  returned: success
                  type: str
                  sample: '<name>'

            addToInventory:
              description: It is the pnp device import's addToInventory.
              returned: success
              type: bool
              sample: false
            instanceType:
              description: It is the pnp device import's instanceType.
              returned: success
              type: str
              sample: '<instancetype>'
            endTime:
              description: It is the pnp device import's endTime.
              returned: success
              type: int
              sample: 0
            execTime:
              description: It is the pnp device import's execTime.
              returned: success
              type: int
              sample: 0
            startTime:
              description: It is the pnp device import's startTime.
              returned: success
              type: int
              sample: 0
            useState:
              description: It is the pnp device import's useState.
              returned: success
              type: str
              sample: '<usestate>'
            configId:
              description: It is the pnp device import's configId.
              returned: success
              type: str
              sample: '<configid>'
            name:
              description: It is the pnp device import's name.
              returned: success
              type: str
              sample: '<name>'
            version:
              description: It is the pnp device import's version.
              returned: success
              type: int
              sample: 0
            tenantId:
              description: It is the pnp device import's tenantId.
              returned: success
              type: str
              sample: '<tenantid>'

        workflow:
          description: It is the pnp device import's workflow.
          returned: success
          type: dict
          contains:
            _id:
              description: It is the pnp device import's _id.
              returned: success
              type: str
              sample: '<_id>'
            state:
              description: It is the pnp device import's state.
              returned: success
              type: str
              sample: '<state>'
            type:
              description: It is the pnp device import's type.
              returned: success
              type: str
              sample: '<type>'
            description:
              description: It is the pnp device import's description.
              returned: success
              type: str
              sample: '<description>'
            lastupdateOn:
              description: It is the pnp device import's lastupdateOn.
              returned: success
              type: int
              sample: 0
            imageId:
              description: It is the pnp device import's imageId.
              returned: success
              type: str
              sample: '<imageid>'
            currTaskIdx:
              description: It is the pnp device import's currTaskIdx.
              returned: success
              type: int
              sample: 0
            addedOn:
              description: It is the pnp device import's addedOn.
              returned: success
              type: int
              sample: 0
            tasks:
              description: It is the pnp device import's tasks.
              returned: success
              type: list
              contains:
                state:
                  description: It is the pnp device import's state.
                  returned: success
                  type: str
                  sample: '<state>'
                type:
                  description: It is the pnp device import's type.
                  returned: success
                  type: str
                  sample: '<type>'
                currWorkItemIdx:
                  description: It is the pnp device import's currWorkItemIdx.
                  returned: success
                  type: int
                  sample: 0
                taskSeqNo:
                  description: It is the pnp device import's taskSeqNo.
                  returned: success
                  type: int
                  sample: 0
                endTime:
                  description: It is the pnp device import's endTime.
                  returned: success
                  type: int
                  sample: 0
                startTime:
                  description: It is the pnp device import's startTime.
                  returned: success
                  type: int
                  sample: 0
                workItemList:
                  description: It is the pnp device import's workItemList.
                  returned: success
                  type: list
                  contains:
                    state:
                      description: It is the pnp device import's state.
                      returned: success
                      type: str
                      sample: '<state>'
                    command:
                      description: It is the pnp device import's command.
                      returned: success
                      type: str
                      sample: '<command>'
                    outputStr:
                      description: It is the pnp device import's outputStr.
                      returned: success
                      type: str
                      sample: '<outputstr>'
                    endTime:
                      description: It is the pnp device import's endTime.
                      returned: success
                      type: int
                      sample: 0
                    startTime:
                      description: It is the pnp device import's startTime.
                      returned: success
                      type: int
                      sample: 0
                    timeTaken:
                      description: It is the pnp device import's timeTaken.
                      returned: success
                      type: int
                      sample: 0

                timeTaken:
                  description: It is the pnp device import's timeTaken.
                  returned: success
                  type: int
                  sample: 0
                name:
                  description: It is the pnp device import's name.
                  returned: success
                  type: str
                  sample: '<name>'

            addToInventory:
              description: It is the pnp device import's addToInventory.
              returned: success
              type: bool
              sample: false
            instanceType:
              description: It is the pnp device import's instanceType.
              returned: success
              type: str
              sample: '<instancetype>'
            endTime:
              description: It is the pnp device import's endTime.
              returned: success
              type: int
              sample: 0
            execTime:
              description: It is the pnp device import's execTime.
              returned: success
              type: int
              sample: 0
            startTime:
              description: It is the pnp device import's startTime.
              returned: success
              type: int
              sample: 0
            useState:
              description: It is the pnp device import's useState.
              returned: success
              type: str
              sample: '<usestate>'
            configId:
              description: It is the pnp device import's configId.
              returned: success
              type: str
              sample: '<configid>'
            name:
              description: It is the pnp device import's name.
              returned: success
              type: str
              sample: '<name>'
            version:
              description: It is the pnp device import's version.
              returned: success
              type: int
              sample: 0
            tenantId:
              description: It is the pnp device import's tenantId.
              returned: success
              type: str
              sample: '<tenantid>'

        runSummaryList:
          description: It is the pnp device import's runSummaryList.
          returned: success
          type: list
          contains:
            details:
              description: It is the pnp device import's details.
              returned: success
              type: str
              sample: '<details>'
            historyTaskInfo:
              description: It is the pnp device import's historyTaskInfo.
              returned: success
              type: dict
              contains:
                type:
                  description: It is the pnp device import's type.
                  returned: success
                  type: str
                  sample: '<type>'
                workItemList:
                  description: It is the pnp device import's workItemList.
                  returned: success
                  type: list
                  contains:
                    state:
                      description: It is the pnp device import's state.
                      returned: success
                      type: str
                      sample: '<state>'
                    command:
                      description: It is the pnp device import's command.
                      returned: success
                      type: str
                      sample: '<command>'
                    outputStr:
                      description: It is the pnp device import's outputStr.
                      returned: success
                      type: str
                      sample: '<outputstr>'
                    endTime:
                      description: It is the pnp device import's endTime.
                      returned: success
                      type: int
                      sample: 0
                    startTime:
                      description: It is the pnp device import's startTime.
                      returned: success
                      type: int
                      sample: 0
                    timeTaken:
                      description: It is the pnp device import's timeTaken.
                      returned: success
                      type: int
                      sample: 0

                timeTaken:
                  description: It is the pnp device import's timeTaken.
                  returned: success
                  type: int
                  sample: 0
                addnDetails:
                  description: It is the pnp device import's addnDetails.
                  returned: success
                  type: list
                  contains:
                    key:
                      description: It is the pnp device import's key.
                      returned: success
                      type: str
                      sample: '<key>'
                    value:
                      description: It is the pnp device import's value.
                      returned: success
                      type: str
                      sample: '<value>'

                name:
                  description: It is the pnp device import's name.
                  returned: success
                  type: str
                  sample: '<name>'

            errorFlag:
              description: It is the pnp device import's errorFlag.
              returned: success
              type: bool
              sample: false
            timestamp:
              description: It is the pnp device import's timestamp.
              returned: success
              type: int
              sample: 0

        workflowParameters:
          description: It is the pnp device import's workflowParameters.
          returned: success
          type: dict
          contains:
            topOfStackSerialNumber:
              description: It is the pnp device import's topOfStackSerialNumber.
              returned: success
              type: str
              sample: '<topofstackserialnumber>'
            licenseLevel:
              description: It is the pnp device import's licenseLevel.
              returned: success
              type: str
              sample: '<licenselevel>'
            licenseType:
              description: It is the pnp device import's licenseType.
              returned: success
              type: str
              sample: '<licensetype>'
            configList:
              description: It is the pnp device import's configList.
              returned: success
              type: list
              contains:
                configParameters:
                  description: It is the pnp device import's configParameters.
                  returned: success
                  type: list
                  contains:
                    key:
                      description: It is the pnp device import's key.
                      returned: success
                      type: str
                      sample: '<key>'
                    value:
                      description: It is the pnp device import's value.
                      returned: success
                      type: str
                      sample: '<value>'

                configId:
                  description: It is the pnp device import's configId.
                  returned: success
                  type: str
                  sample: '<configid>'


        dayZeroConfig:
          description: It is the pnp device import's dayZeroConfig.
          returned: success
          type: dict
          contains:
            config:
              description: It is the pnp device import's config.
              returned: success
              type: str
              sample: '<config>'

        dayZeroConfigPreview:
          description: It is the pnp device import's dayZeroConfigPreview.
          returned: success
          type: dict
        version:
          description: It is the pnp device import's version.
          returned: success
          type: int
          sample: 0
        tenantId:
          description: It is the pnp device import's tenantId.
          returned: success
          type: str
          sample: '<tenantid>'

    failureList:
      description: Device's Failure List (list of objects).
      returned: success
      type: list
      contains:
        index:
          description: It is the pnp device import's index.
          returned: success
          type: int
          sample: 0
        serialNum:
          description: It is the pnp device import's serialNum.
          returned: success
          type: str
          sample: '<serialnum>'
        id:
          description: It is the pnp device import's id.
          returned: success
          type: str
          sample: '478012'
        msg:
          description: It is the pnp device import's msg.
          returned: success
          type: str
          sample: '<msg>'


"""
