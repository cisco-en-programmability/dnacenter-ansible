#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_device_import
short_description: Manage PnpDeviceImport objects of DeviceOnboardingPnp
description:
- Add devices to PnP in bulk.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
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
  cisco.dnac.pnp_device_import:
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

"""

RETURN = r"""
dnac_response:
  description: A dictionary with the response returned by the DNA Center Python SDK
  returned: always
  type: dict
  sample: {"response": 29, "version": "1.0"}
sdk_function:
  description: The DNA Center SDK function used to execute the task
  returned: always
  type: str
  sample: application_policy.get_application_sets
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""
