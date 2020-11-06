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
module: flow_analysis
short_description: Manage FlowAnalysis objects of PathTrace
description:
- Returns a summary of all flow analyses stored. Results can be filtered by specified parameters.
- Initiates a new flow analysis with periodic refresh and stat collection options. Returns a request id and a task id to get results and follow progress.
- Returns result of a previously requested flow analysis by its Flow Analysis id.
- Deletes a flow analysis request by its id.
version_added: '1.0'
author: first last (@GitHubID)
options:
    dest_ip:
        description:
        - Destination IP address.
        type: str
    dest_port:
        description:
        - Destination port.
        type: str
    gt_create_time:
        description:
        - Analyses requested after this time.
        type: str
    last_update_time:
        description:
        - Last update time.
        type: str
    limit:
        description:
        - Number of resources returned.
        type: str
    lt_create_time:
        description:
        - Analyses requested before this time.
        type: str
    offset:
        description:
        - Start index of resources returned (1-based).
        type: str
    order:
        description:
        - Order by this field.
        type: str
    periodic_refresh:
        description:
        - Is analysis periodically refreshed?.
        type: bool
    protocol:
        description:
        - Protocol query parameter.
        type: str
    sort_by:
        description:
        - Sort by this field.
        type: str
    source_ip:
        description:
        - Source IP address.
        type: str
    source_port:
        description:
        - Source port.
        type: str
    status:
        description:
        - Status query parameter.
        type: str
    task_id:
        description:
        - Task ID.
        type: str
    controlPath:
        description:
        - FlowAnalysisRequest's controlPath.
        type: bool
    destIP:
        description:
        - FlowAnalysisRequest's destIP.
        type: str
        required: True
    destPort:
        description:
        - FlowAnalysisRequest's destPort.
        type: str
    inclusions:
        description:
        - FlowAnalysisRequest's inclusions (list of strings).
        type: list
    periodicRefresh:
        description:
        - FlowAnalysisRequest's periodicRefresh.
        type: bool
    sourceIP:
        description:
        - FlowAnalysisRequest's sourceIP.
        type: str
        required: True
    sourcePort:
        description:
        - FlowAnalysisRequest's sourcePort.
        type: str
    flow_analysis_id:
        description:
        - Flow analysis request id.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.flow_analysis
# Reference by Internet resource
- name: FlowAnalysis reference
  description: Complete reference of the FlowAnalysis object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: FlowAnalysis reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns a summary of all flow analyses stored. Results can be filtered by specified parameters.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                controlPath:
                    description: It is the flow analysis's controlPath.
                    returned: success,changed,always
                    type: bool
                    sample: false
                createTime:
                    description: It is the flow analysis's createTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                destIP:
                    description: It is the flow analysis's destIP.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                destPort:
                    description: It is the flow analysis's destPort.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                failureReason:
                    description: It is the flow analysis's failureReason.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the flow analysis's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                inclusions:
                    description: It is the flow analysis's inclusions.
                    returned: success,changed,always
                    type: list
                lastUpdateTime:
                    description: It is the flow analysis's lastUpdateTime.
                    returned: success,changed,always
                    type: int
                    sample: 0
                periodicRefresh:
                    description: It is the flow analysis's periodicRefresh.
                    returned: success,changed,always
                    type: bool
                    sample: false
                protocol:
                    description: It is the flow analysis's protocol.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                sourceIP:
                    description: It is the flow analysis's sourceIP.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                sourcePort:
                    description: It is the flow analysis's sourcePort.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                status:
                    description: It is the flow analysis's status.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Initiates a new flow analysis with periodic refresh and stat collection options. Returns a request id and a task id to get results and follow progress.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: FlowAnalysisRequest's response.
            returned: success,changed,always
            type: dict
            contains:
                flowAnalysisId:
                    description: It is the flow analysis's flowAnalysisId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                taskId:
                    description: It is the flow analysis's taskId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                url:
                    description: It is the flow analysis's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: FlowAnalysisRequest's version.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_2:
    description: Returns result of a previously requested flow analysis by its Flow Analysis id.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                detailedStatus:
                    description: It is the flow analysis's detailedStatus.
                    returned: success,changed,always
                    type: dict
                    contains:
                        aclTraceCalculation:
                            description: It is the flow analysis's aclTraceCalculation.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        aclTraceCalculationFailureReason:
                            description: It is the flow analysis's aclTraceCalculationFailureReason.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                lastUpdate:
                    description: It is the flow analysis's lastUpdate.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                networkElements:
                    description: It is the flow analysis's networkElements.
                    returned: success,changed,always
                    type: list
                    contains:
                        accuracyList:
                            description: It is the flow analysis's accuracyList.
                            returned: success,changed,always
                            type: list
                            contains:
                                percent:
                                    description: It is the flow analysis's percent.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                reason:
                                    description: It is the flow analysis's reason.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        detailedStatus:
                            description: It is the flow analysis's detailedStatus.
                            returned: success,changed,always
                            type: dict
                            contains:
                                aclTraceCalculation:
                                    description: It is the flow analysis's aclTraceCalculation.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                aclTraceCalculationFailureReason:
                                    description: It is the flow analysis's aclTraceCalculationFailureReason.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        deviceStatistics:
                            description: It is the flow analysis's deviceStatistics.
                            returned: success,changed,always
                            type: dict
                            contains:
                                cpuStatistics:
                                    description: It is the flow analysis's cpuStatistics.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        fiveMinUsageInPercentage:
                                            description: It is the flow analysis's fiveMinUsageInPercentage.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        fiveSecsUsageInPercentage:
                                            description: It is the flow analysis's fiveSecsUsageInPercentage.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        oneMinUsageInPercentage:
                                            description: It is the flow analysis's oneMinUsageInPercentage.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        refreshedAt:
                                            description: It is the flow analysis's refreshedAt.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0

                                memoryStatistics:
                                    description: It is the flow analysis's memoryStatistics.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        memoryUsage:
                                            description: It is the flow analysis's memoryUsage.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        refreshedAt:
                                            description: It is the flow analysis's refreshedAt.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        totalMemory:
                                            description: It is the flow analysis's totalMemory.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0


                        deviceStatsCollection:
                            description: It is the flow analysis's deviceStatsCollection.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        deviceStatsCollectionFailureReason:
                            description: It is the flow analysis's deviceStatsCollectionFailureReason.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        egressPhysicalInterface:
                            description: It is the flow analysis's egressPhysicalInterface.
                            returned: success,changed,always
                            type: dict
                            contains:
                                aclAnalysis:
                                    description: It is the flow analysis's aclAnalysis.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        aclName:
                                            description: It is the flow analysis's aclName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        matchingAces:
                                            description: It is the flow analysis's matchingAces.
                                            returned: success,changed,always
                                            type: list
                                            contains:
                                                ace:
                                                    description: It is the flow analysis's ace.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                matchingPorts:
                                                    description: It is the flow analysis's matchingPorts.
                                                    returned: success,changed,always
                                                    type: list
                                                    contains:
                                                        ports:
                                                            description: It is the flow analysis's ports.
                                                            returned: success,changed,always
                                                            type: list
                                                            contains:
                                                                destPorts:
                                                                    description: It is the flow analysis's destPorts.
                                                                    returned: success,changed,always
                                                                    type: list
                                                                sourcePorts:
                                                                    description: It is the flow analysis's sourcePorts.
                                                                    returned: success,changed,always
                                                                    type: list

                                                        protocol:
                                                            description: It is the flow analysis's protocol.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'

                                                result:
                                                    description: It is the flow analysis's result.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'

                                        result:
                                            description: It is the flow analysis's result.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'

                                id:
                                    description: It is the flow analysis's id.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                interfaceStatistics:
                                    description: It is the flow analysis's interfaceStatistics.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        adminStatus:
                                            description: It is the flow analysis's adminStatus.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        inputPackets:
                                            description: It is the flow analysis's inputPackets.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputQueueCount:
                                            description: It is the flow analysis's inputQueueCount.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputQueueDrops:
                                            description: It is the flow analysis's inputQueueDrops.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputQueueFlushes:
                                            description: It is the flow analysis's inputQueueFlushes.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputQueueMaxDepth:
                                            description: It is the flow analysis's inputQueueMaxDepth.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputRatebps:
                                            description: It is the flow analysis's inputRatebps.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        operationalStatus:
                                            description: It is the flow analysis's operationalStatus.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        outputDrop:
                                            description: It is the flow analysis's outputDrop.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        outputPackets:
                                            description: It is the flow analysis's outputPackets.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        outputQueueCount:
                                            description: It is the flow analysis's outputQueueCount.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        outputQueueDepth:
                                            description: It is the flow analysis's outputQueueDepth.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        outputRatebps:
                                            description: It is the flow analysis's outputRatebps.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        refreshedAt:
                                            description: It is the flow analysis's refreshedAt.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0

                                interfaceStatsCollection:
                                    description: It is the flow analysis's interfaceStatsCollection.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                interfaceStatsCollectionFailureReason:
                                    description: It is the flow analysis's interfaceStatsCollectionFailureReason.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                name:
                                    description: It is the flow analysis's name.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                pathOverlayInfo:
                                    description: It is the flow analysis's pathOverlayInfo.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        controlPlane:
                                            description: It is the flow analysis's controlPlane.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        dataPacketEncapsulation:
                                            description: It is the flow analysis's dataPacketEncapsulation.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        destIp:
                                            description: It is the flow analysis's destIp.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        destPort:
                                            description: It is the flow analysis's destPort.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        protocol:
                                            description: It is the flow analysis's protocol.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        sourceIp:
                                            description: It is the flow analysis's sourceIp.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        sourcePort:
                                            description: It is the flow analysis's sourcePort.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        vxlanInfo:
                                            description: It is the flow analysis's vxlanInfo.
                                            returned: success,changed,always
                                            type: dict
                                            contains:
                                                dscp:
                                                    description: It is the flow analysis's dscp.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                vnid:
                                                    description: It is the flow analysis's vnid.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'


                                qosStatistics:
                                    description: It is the flow analysis's qosStatistics.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        classMapName:
                                            description: It is the flow analysis's classMapName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        dropRate:
                                            description: It is the flow analysis's dropRate.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        numBytes:
                                            description: It is the flow analysis's numBytes.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        numPackets:
                                            description: It is the flow analysis's numPackets.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        offeredRate:
                                            description: It is the flow analysis's offeredRate.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        queueBandwidthbps:
                                            description: It is the flow analysis's queueBandwidthbps.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        queueDepth:
                                            description: It is the flow analysis's queueDepth.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        queueNoBufferDrops:
                                            description: It is the flow analysis's queueNoBufferDrops.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        queueTotalDrops:
                                            description: It is the flow analysis's queueTotalDrops.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        refreshedAt:
                                            description: It is the flow analysis's refreshedAt.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0

                                qosStatsCollection:
                                    description: It is the flow analysis's qosStatsCollection.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                qosStatsCollectionFailureReason:
                                    description: It is the flow analysis's qosStatsCollectionFailureReason.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                usedVlan:
                                    description: It is the flow analysis's usedVlan.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                vrfName:
                                    description: It is the flow analysis's vrfName.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        egressVirtualInterface:
                            description: It is the flow analysis's egressVirtualInterface.
                            returned: success,changed,always
                            type: dict
                            contains:
                                aclAnalysis:
                                    description: It is the flow analysis's aclAnalysis.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        aclName:
                                            description: It is the flow analysis's aclName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        matchingAces:
                                            description: It is the flow analysis's matchingAces.
                                            returned: success,changed,always
                                            type: list
                                            contains:
                                                ace:
                                                    description: It is the flow analysis's ace.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                matchingPorts:
                                                    description: It is the flow analysis's matchingPorts.
                                                    returned: success,changed,always
                                                    type: list
                                                    contains:
                                                        ports:
                                                            description: It is the flow analysis's ports.
                                                            returned: success,changed,always
                                                            type: list
                                                            contains:
                                                                destPorts:
                                                                    description: It is the flow analysis's destPorts.
                                                                    returned: success,changed,always
                                                                    type: list
                                                                sourcePorts:
                                                                    description: It is the flow analysis's sourcePorts.
                                                                    returned: success,changed,always
                                                                    type: list

                                                        protocol:
                                                            description: It is the flow analysis's protocol.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'

                                                result:
                                                    description: It is the flow analysis's result.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'

                                        result:
                                            description: It is the flow analysis's result.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'

                                id:
                                    description: It is the flow analysis's id.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                interfaceStatistics:
                                    description: It is the flow analysis's interfaceStatistics.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        adminStatus:
                                            description: It is the flow analysis's adminStatus.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        inputPackets:
                                            description: It is the flow analysis's inputPackets.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputQueueCount:
                                            description: It is the flow analysis's inputQueueCount.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputQueueDrops:
                                            description: It is the flow analysis's inputQueueDrops.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputQueueFlushes:
                                            description: It is the flow analysis's inputQueueFlushes.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputQueueMaxDepth:
                                            description: It is the flow analysis's inputQueueMaxDepth.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputRatebps:
                                            description: It is the flow analysis's inputRatebps.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        operationalStatus:
                                            description: It is the flow analysis's operationalStatus.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        outputDrop:
                                            description: It is the flow analysis's outputDrop.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        outputPackets:
                                            description: It is the flow analysis's outputPackets.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        outputQueueCount:
                                            description: It is the flow analysis's outputQueueCount.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        outputQueueDepth:
                                            description: It is the flow analysis's outputQueueDepth.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        outputRatebps:
                                            description: It is the flow analysis's outputRatebps.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        refreshedAt:
                                            description: It is the flow analysis's refreshedAt.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0

                                interfaceStatsCollection:
                                    description: It is the flow analysis's interfaceStatsCollection.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                interfaceStatsCollectionFailureReason:
                                    description: It is the flow analysis's interfaceStatsCollectionFailureReason.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                name:
                                    description: It is the flow analysis's name.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                pathOverlayInfo:
                                    description: It is the flow analysis's pathOverlayInfo.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        controlPlane:
                                            description: It is the flow analysis's controlPlane.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        dataPacketEncapsulation:
                                            description: It is the flow analysis's dataPacketEncapsulation.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        destIp:
                                            description: It is the flow analysis's destIp.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        destPort:
                                            description: It is the flow analysis's destPort.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        protocol:
                                            description: It is the flow analysis's protocol.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        sourceIp:
                                            description: It is the flow analysis's sourceIp.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        sourcePort:
                                            description: It is the flow analysis's sourcePort.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        vxlanInfo:
                                            description: It is the flow analysis's vxlanInfo.
                                            returned: success,changed,always
                                            type: dict
                                            contains:
                                                dscp:
                                                    description: It is the flow analysis's dscp.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                vnid:
                                                    description: It is the flow analysis's vnid.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'


                                qosStatistics:
                                    description: It is the flow analysis's qosStatistics.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        classMapName:
                                            description: It is the flow analysis's classMapName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        dropRate:
                                            description: It is the flow analysis's dropRate.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        numBytes:
                                            description: It is the flow analysis's numBytes.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        numPackets:
                                            description: It is the flow analysis's numPackets.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        offeredRate:
                                            description: It is the flow analysis's offeredRate.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        queueBandwidthbps:
                                            description: It is the flow analysis's queueBandwidthbps.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        queueDepth:
                                            description: It is the flow analysis's queueDepth.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        queueNoBufferDrops:
                                            description: It is the flow analysis's queueNoBufferDrops.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        queueTotalDrops:
                                            description: It is the flow analysis's queueTotalDrops.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        refreshedAt:
                                            description: It is the flow analysis's refreshedAt.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0

                                qosStatsCollection:
                                    description: It is the flow analysis's qosStatsCollection.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                qosStatsCollectionFailureReason:
                                    description: It is the flow analysis's qosStatsCollectionFailureReason.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                usedVlan:
                                    description: It is the flow analysis's usedVlan.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                vrfName:
                                    description: It is the flow analysis's vrfName.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        flexConnect:
                            description: It is the flow analysis's flexConnect.
                            returned: success,changed,always
                            type: dict
                            contains:
                                authentication:
                                    description: It is the flow analysis's authentication.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                dataSwitching:
                                    description: It is the flow analysis's dataSwitching.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                egressAclAnalysis:
                                    description: It is the flow analysis's egressAclAnalysis.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        aclName:
                                            description: It is the flow analysis's aclName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        matchingAces:
                                            description: It is the flow analysis's matchingAces.
                                            returned: success,changed,always
                                            type: list
                                            contains:
                                                ace:
                                                    description: It is the flow analysis's ace.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                matchingPorts:
                                                    description: It is the flow analysis's matchingPorts.
                                                    returned: success,changed,always
                                                    type: list
                                                    contains:
                                                        ports:
                                                            description: It is the flow analysis's ports.
                                                            returned: success,changed,always
                                                            type: list
                                                            contains:
                                                                destPorts:
                                                                    description: It is the flow analysis's destPorts.
                                                                    returned: success,changed,always
                                                                    type: list
                                                                sourcePorts:
                                                                    description: It is the flow analysis's sourcePorts.
                                                                    returned: success,changed,always
                                                                    type: list

                                                        protocol:
                                                            description: It is the flow analysis's protocol.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'

                                                result:
                                                    description: It is the flow analysis's result.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'

                                        result:
                                            description: It is the flow analysis's result.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'

                                ingressAclAnalysis:
                                    description: It is the flow analysis's ingressAclAnalysis.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        aclName:
                                            description: It is the flow analysis's aclName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        matchingAces:
                                            description: It is the flow analysis's matchingAces.
                                            returned: success,changed,always
                                            type: list
                                            contains:
                                                ace:
                                                    description: It is the flow analysis's ace.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                matchingPorts:
                                                    description: It is the flow analysis's matchingPorts.
                                                    returned: success,changed,always
                                                    type: list
                                                    contains:
                                                        ports:
                                                            description: It is the flow analysis's ports.
                                                            returned: success,changed,always
                                                            type: list
                                                            contains:
                                                                destPorts:
                                                                    description: It is the flow analysis's destPorts.
                                                                    returned: success,changed,always
                                                                    type: list
                                                                sourcePorts:
                                                                    description: It is the flow analysis's sourcePorts.
                                                                    returned: success,changed,always
                                                                    type: list

                                                        protocol:
                                                            description: It is the flow analysis's protocol.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'

                                                result:
                                                    description: It is the flow analysis's result.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'

                                        result:
                                            description: It is the flow analysis's result.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'

                                wirelessLanControllerId:
                                    description: It is the flow analysis's wirelessLanControllerId.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                wirelessLanControllerName:
                                    description: It is the flow analysis's wirelessLanControllerName.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        id:
                            description: It is the flow analysis's id.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        ingressPhysicalInterface:
                            description: It is the flow analysis's ingressPhysicalInterface.
                            returned: success,changed,always
                            type: dict
                            contains:
                                aclAnalysis:
                                    description: It is the flow analysis's aclAnalysis.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        aclName:
                                            description: It is the flow analysis's aclName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        matchingAces:
                                            description: It is the flow analysis's matchingAces.
                                            returned: success,changed,always
                                            type: list
                                            contains:
                                                ace:
                                                    description: It is the flow analysis's ace.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                matchingPorts:
                                                    description: It is the flow analysis's matchingPorts.
                                                    returned: success,changed,always
                                                    type: list
                                                    contains:
                                                        ports:
                                                            description: It is the flow analysis's ports.
                                                            returned: success,changed,always
                                                            type: list
                                                            contains:
                                                                destPorts:
                                                                    description: It is the flow analysis's destPorts.
                                                                    returned: success,changed,always
                                                                    type: list
                                                                sourcePorts:
                                                                    description: It is the flow analysis's sourcePorts.
                                                                    returned: success,changed,always
                                                                    type: list

                                                        protocol:
                                                            description: It is the flow analysis's protocol.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'

                                                result:
                                                    description: It is the flow analysis's result.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'

                                        result:
                                            description: It is the flow analysis's result.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'

                                id:
                                    description: It is the flow analysis's id.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                interfaceStatistics:
                                    description: It is the flow analysis's interfaceStatistics.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        adminStatus:
                                            description: It is the flow analysis's adminStatus.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        inputPackets:
                                            description: It is the flow analysis's inputPackets.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputQueueCount:
                                            description: It is the flow analysis's inputQueueCount.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputQueueDrops:
                                            description: It is the flow analysis's inputQueueDrops.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputQueueFlushes:
                                            description: It is the flow analysis's inputQueueFlushes.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputQueueMaxDepth:
                                            description: It is the flow analysis's inputQueueMaxDepth.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputRatebps:
                                            description: It is the flow analysis's inputRatebps.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        operationalStatus:
                                            description: It is the flow analysis's operationalStatus.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        outputDrop:
                                            description: It is the flow analysis's outputDrop.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        outputPackets:
                                            description: It is the flow analysis's outputPackets.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        outputQueueCount:
                                            description: It is the flow analysis's outputQueueCount.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        outputQueueDepth:
                                            description: It is the flow analysis's outputQueueDepth.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        outputRatebps:
                                            description: It is the flow analysis's outputRatebps.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        refreshedAt:
                                            description: It is the flow analysis's refreshedAt.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0

                                interfaceStatsCollection:
                                    description: It is the flow analysis's interfaceStatsCollection.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                interfaceStatsCollectionFailureReason:
                                    description: It is the flow analysis's interfaceStatsCollectionFailureReason.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                name:
                                    description: It is the flow analysis's name.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                pathOverlayInfo:
                                    description: It is the flow analysis's pathOverlayInfo.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        controlPlane:
                                            description: It is the flow analysis's controlPlane.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        dataPacketEncapsulation:
                                            description: It is the flow analysis's dataPacketEncapsulation.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        destIp:
                                            description: It is the flow analysis's destIp.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        destPort:
                                            description: It is the flow analysis's destPort.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        protocol:
                                            description: It is the flow analysis's protocol.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        sourceIp:
                                            description: It is the flow analysis's sourceIp.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        sourcePort:
                                            description: It is the flow analysis's sourcePort.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        vxlanInfo:
                                            description: It is the flow analysis's vxlanInfo.
                                            returned: success,changed,always
                                            type: dict
                                            contains:
                                                dscp:
                                                    description: It is the flow analysis's dscp.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                vnid:
                                                    description: It is the flow analysis's vnid.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'


                                qosStatistics:
                                    description: It is the flow analysis's qosStatistics.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        classMapName:
                                            description: It is the flow analysis's classMapName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        dropRate:
                                            description: It is the flow analysis's dropRate.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        numBytes:
                                            description: It is the flow analysis's numBytes.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        numPackets:
                                            description: It is the flow analysis's numPackets.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        offeredRate:
                                            description: It is the flow analysis's offeredRate.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        queueBandwidthbps:
                                            description: It is the flow analysis's queueBandwidthbps.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        queueDepth:
                                            description: It is the flow analysis's queueDepth.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        queueNoBufferDrops:
                                            description: It is the flow analysis's queueNoBufferDrops.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        queueTotalDrops:
                                            description: It is the flow analysis's queueTotalDrops.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        refreshedAt:
                                            description: It is the flow analysis's refreshedAt.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0

                                qosStatsCollection:
                                    description: It is the flow analysis's qosStatsCollection.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                qosStatsCollectionFailureReason:
                                    description: It is the flow analysis's qosStatsCollectionFailureReason.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                usedVlan:
                                    description: It is the flow analysis's usedVlan.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                vrfName:
                                    description: It is the flow analysis's vrfName.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        ingressVirtualInterface:
                            description: It is the flow analysis's ingressVirtualInterface.
                            returned: success,changed,always
                            type: dict
                            contains:
                                aclAnalysis:
                                    description: It is the flow analysis's aclAnalysis.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        aclName:
                                            description: It is the flow analysis's aclName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        matchingAces:
                                            description: It is the flow analysis's matchingAces.
                                            returned: success,changed,always
                                            type: list
                                            contains:
                                                ace:
                                                    description: It is the flow analysis's ace.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                matchingPorts:
                                                    description: It is the flow analysis's matchingPorts.
                                                    returned: success,changed,always
                                                    type: list
                                                    contains:
                                                        ports:
                                                            description: It is the flow analysis's ports.
                                                            returned: success,changed,always
                                                            type: list
                                                            contains:
                                                                destPorts:
                                                                    description: It is the flow analysis's destPorts.
                                                                    returned: success,changed,always
                                                                    type: list
                                                                sourcePorts:
                                                                    description: It is the flow analysis's sourcePorts.
                                                                    returned: success,changed,always
                                                                    type: list

                                                        protocol:
                                                            description: It is the flow analysis's protocol.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'

                                                result:
                                                    description: It is the flow analysis's result.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'

                                        result:
                                            description: It is the flow analysis's result.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'

                                id:
                                    description: It is the flow analysis's id.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                interfaceStatistics:
                                    description: It is the flow analysis's interfaceStatistics.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        adminStatus:
                                            description: It is the flow analysis's adminStatus.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        inputPackets:
                                            description: It is the flow analysis's inputPackets.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputQueueCount:
                                            description: It is the flow analysis's inputQueueCount.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputQueueDrops:
                                            description: It is the flow analysis's inputQueueDrops.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputQueueFlushes:
                                            description: It is the flow analysis's inputQueueFlushes.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputQueueMaxDepth:
                                            description: It is the flow analysis's inputQueueMaxDepth.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        inputRatebps:
                                            description: It is the flow analysis's inputRatebps.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        operationalStatus:
                                            description: It is the flow analysis's operationalStatus.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        outputDrop:
                                            description: It is the flow analysis's outputDrop.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        outputPackets:
                                            description: It is the flow analysis's outputPackets.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        outputQueueCount:
                                            description: It is the flow analysis's outputQueueCount.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        outputQueueDepth:
                                            description: It is the flow analysis's outputQueueDepth.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        outputRatebps:
                                            description: It is the flow analysis's outputRatebps.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        refreshedAt:
                                            description: It is the flow analysis's refreshedAt.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0

                                interfaceStatsCollection:
                                    description: It is the flow analysis's interfaceStatsCollection.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                interfaceStatsCollectionFailureReason:
                                    description: It is the flow analysis's interfaceStatsCollectionFailureReason.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                name:
                                    description: It is the flow analysis's name.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                pathOverlayInfo:
                                    description: It is the flow analysis's pathOverlayInfo.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        controlPlane:
                                            description: It is the flow analysis's controlPlane.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        dataPacketEncapsulation:
                                            description: It is the flow analysis's dataPacketEncapsulation.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        destIp:
                                            description: It is the flow analysis's destIp.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        destPort:
                                            description: It is the flow analysis's destPort.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        protocol:
                                            description: It is the flow analysis's protocol.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        sourceIp:
                                            description: It is the flow analysis's sourceIp.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        sourcePort:
                                            description: It is the flow analysis's sourcePort.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        vxlanInfo:
                                            description: It is the flow analysis's vxlanInfo.
                                            returned: success,changed,always
                                            type: dict
                                            contains:
                                                dscp:
                                                    description: It is the flow analysis's dscp.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                vnid:
                                                    description: It is the flow analysis's vnid.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'


                                qosStatistics:
                                    description: It is the flow analysis's qosStatistics.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        classMapName:
                                            description: It is the flow analysis's classMapName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        dropRate:
                                            description: It is the flow analysis's dropRate.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        numBytes:
                                            description: It is the flow analysis's numBytes.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        numPackets:
                                            description: It is the flow analysis's numPackets.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        offeredRate:
                                            description: It is the flow analysis's offeredRate.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        queueBandwidthbps:
                                            description: It is the flow analysis's queueBandwidthbps.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        queueDepth:
                                            description: It is the flow analysis's queueDepth.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        queueNoBufferDrops:
                                            description: It is the flow analysis's queueNoBufferDrops.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        queueTotalDrops:
                                            description: It is the flow analysis's queueTotalDrops.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        refreshedAt:
                                            description: It is the flow analysis's refreshedAt.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0

                                qosStatsCollection:
                                    description: It is the flow analysis's qosStatsCollection.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                qosStatsCollectionFailureReason:
                                    description: It is the flow analysis's qosStatsCollectionFailureReason.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                usedVlan:
                                    description: It is the flow analysis's usedVlan.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                vrfName:
                                    description: It is the flow analysis's vrfName.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        ip:
                            description: It is the flow analysis's ip.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        linkInformationSource:
                            description: It is the flow analysis's linkInformationSource.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        name:
                            description: It is the flow analysis's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        perfMonCollection:
                            description: It is the flow analysis's perfMonCollection.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        perfMonCollectionFailureReason:
                            description: It is the flow analysis's perfMonCollectionFailureReason.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        perfMonStatistics:
                            description: It is the flow analysis's perfMonStatistics.
                            returned: success,changed,always
                            type: list
                            contains:
                                byteRate:
                                    description: It is the flow analysis's byteRate.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                destIpAddress:
                                    description: It is the flow analysis's destIpAddress.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                destPort:
                                    description: It is the flow analysis's destPort.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                inputInterface:
                                    description: It is the flow analysis's inputInterface.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ipv4DSCP:
                                    description: It is the flow analysis's ipv4DSCP.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ipv4TTL:
                                    description: It is the flow analysis's ipv4TTL.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                outputInterface:
                                    description: It is the flow analysis's outputInterface.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                packetBytes:
                                    description: It is the flow analysis's packetBytes.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                packetCount:
                                    description: It is the flow analysis's packetCount.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                packetLoss:
                                    description: It is the flow analysis's packetLoss.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                packetLossPercentage:
                                    description: It is the flow analysis's packetLossPercentage.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                protocol:
                                    description: It is the flow analysis's protocol.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                refreshedAt:
                                    description: It is the flow analysis's refreshedAt.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                rtpJitterMax:
                                    description: It is the flow analysis's rtpJitterMax.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                rtpJitterMean:
                                    description: It is the flow analysis's rtpJitterMean.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                rtpJitterMin:
                                    description: It is the flow analysis's rtpJitterMin.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                sourceIpAddress:
                                    description: It is the flow analysis's sourceIpAddress.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                sourcePort:
                                    description: It is the flow analysis's sourcePort.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        role:
                            description: It is the flow analysis's role.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        ssid:
                            description: It is the flow analysis's ssid.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        tunnels:
                            description: It is the flow analysis's tunnels.
                            returned: success,changed,always
                            type: list
                        type:
                            description: It is the flow analysis's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        wlanId:
                            description: It is the flow analysis's wlanId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                networkElementsInfo:
                    description: It is the flow analysis's networkElementsInfo.
                    returned: success,changed,always
                    type: list
                    contains:
                        accuracyList:
                            description: It is the flow analysis's accuracyList.
                            returned: success,changed,always
                            type: list
                            contains:
                                percent:
                                    description: It is the flow analysis's percent.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                reason:
                                    description: It is the flow analysis's reason.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        detailedStatus:
                            description: It is the flow analysis's detailedStatus.
                            returned: success,changed,always
                            type: dict
                            contains:
                                aclTraceCalculation:
                                    description: It is the flow analysis's aclTraceCalculation.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                aclTraceCalculationFailureReason:
                                    description: It is the flow analysis's aclTraceCalculationFailureReason.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        deviceStatistics:
                            description: It is the flow analysis's deviceStatistics.
                            returned: success,changed,always
                            type: dict
                            contains:
                                cpuStatistics:
                                    description: It is the flow analysis's cpuStatistics.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        fiveMinUsageInPercentage:
                                            description: It is the flow analysis's fiveMinUsageInPercentage.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        fiveSecsUsageInPercentage:
                                            description: It is the flow analysis's fiveSecsUsageInPercentage.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        oneMinUsageInPercentage:
                                            description: It is the flow analysis's oneMinUsageInPercentage.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        refreshedAt:
                                            description: It is the flow analysis's refreshedAt.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0

                                memoryStatistics:
                                    description: It is the flow analysis's memoryStatistics.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        memoryUsage:
                                            description: It is the flow analysis's memoryUsage.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        refreshedAt:
                                            description: It is the flow analysis's refreshedAt.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0
                                        totalMemory:
                                            description: It is the flow analysis's totalMemory.
                                            returned: success,changed,always
                                            type: int
                                            sample: 0


                        deviceStatsCollection:
                            description: It is the flow analysis's deviceStatsCollection.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        deviceStatsCollectionFailureReason:
                            description: It is the flow analysis's deviceStatsCollectionFailureReason.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        egressInterface:
                            description: It is the flow analysis's egressInterface.
                            returned: success,changed,always
                            type: dict
                            contains:
                                physicalInterface:
                                    description: It is the flow analysis's physicalInterface.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        aclAnalysis:
                                            description: It is the flow analysis's aclAnalysis.
                                            returned: success,changed,always
                                            type: dict
                                            contains:
                                                aclName:
                                                    description: It is the flow analysis's aclName.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                matchingAces:
                                                    description: It is the flow analysis's matchingAces.
                                                    returned: success,changed,always
                                                    type: list
                                                    contains:
                                                        ace:
                                                            description: It is the flow analysis's ace.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'
                                                        matchingPorts:
                                                            description: It is the flow analysis's matchingPorts.
                                                            returned: success,changed,always
                                                            type: list
                                                            contains:
                                                                ports:
                                                                    description: It is the flow analysis's ports.
                                                                    returned: success,changed,always
                                                                    type: list
                                                                    contains:
                                                                        destPorts:
                                                                            description: It is the flow analysis's destPorts.
                                                                            returned: success,changed,always
                                                                            type: list
                                                                        sourcePorts:
                                                                            description: It is the flow analysis's sourcePorts.
                                                                            returned: success,changed,always
                                                                            type: list

                                                                protocol:
                                                                    description: It is the flow analysis's protocol.
                                                                    returned: success,changed,always
                                                                    type: str
                                                                    sample: 'sample_string'

                                                        result:
                                                            description: It is the flow analysis's result.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'

                                                result:
                                                    description: It is the flow analysis's result.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'

                                        id:
                                            description: It is the flow analysis's id.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        interfaceStatistics:
                                            description: It is the flow analysis's interfaceStatistics.
                                            returned: success,changed,always
                                            type: dict
                                            contains:
                                                adminStatus:
                                                    description: It is the flow analysis's adminStatus.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                inputPackets:
                                                    description: It is the flow analysis's inputPackets.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputQueueCount:
                                                    description: It is the flow analysis's inputQueueCount.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputQueueDrops:
                                                    description: It is the flow analysis's inputQueueDrops.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputQueueFlushes:
                                                    description: It is the flow analysis's inputQueueFlushes.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputQueueMaxDepth:
                                                    description: It is the flow analysis's inputQueueMaxDepth.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputRatebps:
                                                    description: It is the flow analysis's inputRatebps.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                operationalStatus:
                                                    description: It is the flow analysis's operationalStatus.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                outputDrop:
                                                    description: It is the flow analysis's outputDrop.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                outputPackets:
                                                    description: It is the flow analysis's outputPackets.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                outputQueueCount:
                                                    description: It is the flow analysis's outputQueueCount.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                outputQueueDepth:
                                                    description: It is the flow analysis's outputQueueDepth.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                outputRatebps:
                                                    description: It is the flow analysis's outputRatebps.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                refreshedAt:
                                                    description: It is the flow analysis's refreshedAt.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0

                                        interfaceStatsCollection:
                                            description: It is the flow analysis's interfaceStatsCollection.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        interfaceStatsCollectionFailureReason:
                                            description: It is the flow analysis's interfaceStatsCollectionFailureReason.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        name:
                                            description: It is the flow analysis's name.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        pathOverlayInfo:
                                            description: It is the flow analysis's pathOverlayInfo.
                                            returned: success,changed,always
                                            type: list
                                            contains:
                                                controlPlane:
                                                    description: It is the flow analysis's controlPlane.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                dataPacketEncapsulation:
                                                    description: It is the flow analysis's dataPacketEncapsulation.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                destIp:
                                                    description: It is the flow analysis's destIp.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                destPort:
                                                    description: It is the flow analysis's destPort.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                protocol:
                                                    description: It is the flow analysis's protocol.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                sourceIp:
                                                    description: It is the flow analysis's sourceIp.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                sourcePort:
                                                    description: It is the flow analysis's sourcePort.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                vxlanInfo:
                                                    description: It is the flow analysis's vxlanInfo.
                                                    returned: success,changed,always
                                                    type: dict
                                                    contains:
                                                        dscp:
                                                            description: It is the flow analysis's dscp.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'
                                                        vnid:
                                                            description: It is the flow analysis's vnid.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'


                                        qosStatistics:
                                            description: It is the flow analysis's qosStatistics.
                                            returned: success,changed,always
                                            type: list
                                            contains:
                                                classMapName:
                                                    description: It is the flow analysis's classMapName.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                dropRate:
                                                    description: It is the flow analysis's dropRate.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                numBytes:
                                                    description: It is the flow analysis's numBytes.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                numPackets:
                                                    description: It is the flow analysis's numPackets.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                offeredRate:
                                                    description: It is the flow analysis's offeredRate.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                queueBandwidthbps:
                                                    description: It is the flow analysis's queueBandwidthbps.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                queueDepth:
                                                    description: It is the flow analysis's queueDepth.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                queueNoBufferDrops:
                                                    description: It is the flow analysis's queueNoBufferDrops.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                queueTotalDrops:
                                                    description: It is the flow analysis's queueTotalDrops.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                refreshedAt:
                                                    description: It is the flow analysis's refreshedAt.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0

                                        qosStatsCollection:
                                            description: It is the flow analysis's qosStatsCollection.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        qosStatsCollectionFailureReason:
                                            description: It is the flow analysis's qosStatsCollectionFailureReason.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        usedVlan:
                                            description: It is the flow analysis's usedVlan.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        vrfName:
                                            description: It is the flow analysis's vrfName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'

                                virtualInterface:
                                    description: It is the flow analysis's virtualInterface.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        aclAnalysis:
                                            description: It is the flow analysis's aclAnalysis.
                                            returned: success,changed,always
                                            type: dict
                                            contains:
                                                aclName:
                                                    description: It is the flow analysis's aclName.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                matchingAces:
                                                    description: It is the flow analysis's matchingAces.
                                                    returned: success,changed,always
                                                    type: list
                                                    contains:
                                                        ace:
                                                            description: It is the flow analysis's ace.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'
                                                        matchingPorts:
                                                            description: It is the flow analysis's matchingPorts.
                                                            returned: success,changed,always
                                                            type: list
                                                            contains:
                                                                ports:
                                                                    description: It is the flow analysis's ports.
                                                                    returned: success,changed,always
                                                                    type: list
                                                                    contains:
                                                                        destPorts:
                                                                            description: It is the flow analysis's destPorts.
                                                                            returned: success,changed,always
                                                                            type: list
                                                                        sourcePorts:
                                                                            description: It is the flow analysis's sourcePorts.
                                                                            returned: success,changed,always
                                                                            type: list

                                                                protocol:
                                                                    description: It is the flow analysis's protocol.
                                                                    returned: success,changed,always
                                                                    type: str
                                                                    sample: 'sample_string'

                                                        result:
                                                            description: It is the flow analysis's result.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'

                                                result:
                                                    description: It is the flow analysis's result.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'

                                        id:
                                            description: It is the flow analysis's id.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        interfaceStatistics:
                                            description: It is the flow analysis's interfaceStatistics.
                                            returned: success,changed,always
                                            type: dict
                                            contains:
                                                adminStatus:
                                                    description: It is the flow analysis's adminStatus.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                inputPackets:
                                                    description: It is the flow analysis's inputPackets.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputQueueCount:
                                                    description: It is the flow analysis's inputQueueCount.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputQueueDrops:
                                                    description: It is the flow analysis's inputQueueDrops.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputQueueFlushes:
                                                    description: It is the flow analysis's inputQueueFlushes.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputQueueMaxDepth:
                                                    description: It is the flow analysis's inputQueueMaxDepth.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputRatebps:
                                                    description: It is the flow analysis's inputRatebps.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                operationalStatus:
                                                    description: It is the flow analysis's operationalStatus.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                outputDrop:
                                                    description: It is the flow analysis's outputDrop.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                outputPackets:
                                                    description: It is the flow analysis's outputPackets.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                outputQueueCount:
                                                    description: It is the flow analysis's outputQueueCount.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                outputQueueDepth:
                                                    description: It is the flow analysis's outputQueueDepth.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                outputRatebps:
                                                    description: It is the flow analysis's outputRatebps.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                refreshedAt:
                                                    description: It is the flow analysis's refreshedAt.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0

                                        interfaceStatsCollection:
                                            description: It is the flow analysis's interfaceStatsCollection.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        interfaceStatsCollectionFailureReason:
                                            description: It is the flow analysis's interfaceStatsCollectionFailureReason.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        name:
                                            description: It is the flow analysis's name.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        pathOverlayInfo:
                                            description: It is the flow analysis's pathOverlayInfo.
                                            returned: success,changed,always
                                            type: list
                                            contains:
                                                controlPlane:
                                                    description: It is the flow analysis's controlPlane.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                dataPacketEncapsulation:
                                                    description: It is the flow analysis's dataPacketEncapsulation.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                destIp:
                                                    description: It is the flow analysis's destIp.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                destPort:
                                                    description: It is the flow analysis's destPort.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                protocol:
                                                    description: It is the flow analysis's protocol.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                sourceIp:
                                                    description: It is the flow analysis's sourceIp.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                sourcePort:
                                                    description: It is the flow analysis's sourcePort.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                vxlanInfo:
                                                    description: It is the flow analysis's vxlanInfo.
                                                    returned: success,changed,always
                                                    type: dict
                                                    contains:
                                                        dscp:
                                                            description: It is the flow analysis's dscp.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'
                                                        vnid:
                                                            description: It is the flow analysis's vnid.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'


                                        qosStatistics:
                                            description: It is the flow analysis's qosStatistics.
                                            returned: success,changed,always
                                            type: list
                                            contains:
                                                classMapName:
                                                    description: It is the flow analysis's classMapName.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                dropRate:
                                                    description: It is the flow analysis's dropRate.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                numBytes:
                                                    description: It is the flow analysis's numBytes.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                numPackets:
                                                    description: It is the flow analysis's numPackets.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                offeredRate:
                                                    description: It is the flow analysis's offeredRate.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                queueBandwidthbps:
                                                    description: It is the flow analysis's queueBandwidthbps.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                queueDepth:
                                                    description: It is the flow analysis's queueDepth.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                queueNoBufferDrops:
                                                    description: It is the flow analysis's queueNoBufferDrops.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                queueTotalDrops:
                                                    description: It is the flow analysis's queueTotalDrops.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                refreshedAt:
                                                    description: It is the flow analysis's refreshedAt.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0

                                        qosStatsCollection:
                                            description: It is the flow analysis's qosStatsCollection.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        qosStatsCollectionFailureReason:
                                            description: It is the flow analysis's qosStatsCollectionFailureReason.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        usedVlan:
                                            description: It is the flow analysis's usedVlan.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        vrfName:
                                            description: It is the flow analysis's vrfName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'


                        flexConnect:
                            description: It is the flow analysis's flexConnect.
                            returned: success,changed,always
                            type: dict
                            contains:
                                authentication:
                                    description: It is the flow analysis's authentication.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                dataSwitching:
                                    description: It is the flow analysis's dataSwitching.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                egressAclAnalysis:
                                    description: It is the flow analysis's egressAclAnalysis.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        aclName:
                                            description: It is the flow analysis's aclName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        matchingAces:
                                            description: It is the flow analysis's matchingAces.
                                            returned: success,changed,always
                                            type: list
                                            contains:
                                                ace:
                                                    description: It is the flow analysis's ace.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                matchingPorts:
                                                    description: It is the flow analysis's matchingPorts.
                                                    returned: success,changed,always
                                                    type: list
                                                    contains:
                                                        ports:
                                                            description: It is the flow analysis's ports.
                                                            returned: success,changed,always
                                                            type: list
                                                            contains:
                                                                destPorts:
                                                                    description: It is the flow analysis's destPorts.
                                                                    returned: success,changed,always
                                                                    type: list
                                                                sourcePorts:
                                                                    description: It is the flow analysis's sourcePorts.
                                                                    returned: success,changed,always
                                                                    type: list

                                                        protocol:
                                                            description: It is the flow analysis's protocol.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'

                                                result:
                                                    description: It is the flow analysis's result.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'

                                        result:
                                            description: It is the flow analysis's result.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'

                                ingressAclAnalysis:
                                    description: It is the flow analysis's ingressAclAnalysis.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        aclName:
                                            description: It is the flow analysis's aclName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        matchingAces:
                                            description: It is the flow analysis's matchingAces.
                                            returned: success,changed,always
                                            type: list
                                            contains:
                                                ace:
                                                    description: It is the flow analysis's ace.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                matchingPorts:
                                                    description: It is the flow analysis's matchingPorts.
                                                    returned: success,changed,always
                                                    type: list
                                                    contains:
                                                        ports:
                                                            description: It is the flow analysis's ports.
                                                            returned: success,changed,always
                                                            type: list
                                                            contains:
                                                                destPorts:
                                                                    description: It is the flow analysis's destPorts.
                                                                    returned: success,changed,always
                                                                    type: list
                                                                sourcePorts:
                                                                    description: It is the flow analysis's sourcePorts.
                                                                    returned: success,changed,always
                                                                    type: list

                                                        protocol:
                                                            description: It is the flow analysis's protocol.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'

                                                result:
                                                    description: It is the flow analysis's result.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'

                                        result:
                                            description: It is the flow analysis's result.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'

                                wirelessLanControllerId:
                                    description: It is the flow analysis's wirelessLanControllerId.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                wirelessLanControllerName:
                                    description: It is the flow analysis's wirelessLanControllerName.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        id:
                            description: It is the flow analysis's id.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        ingressInterface:
                            description: It is the flow analysis's ingressInterface.
                            returned: success,changed,always
                            type: dict
                            contains:
                                physicalInterface:
                                    description: It is the flow analysis's physicalInterface.
                                    returned: success,changed,always
                                    type: dict
                                    contains:
                                        aclAnalysis:
                                            description: It is the flow analysis's aclAnalysis.
                                            returned: success,changed,always
                                            type: dict
                                            contains:
                                                aclName:
                                                    description: It is the flow analysis's aclName.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                matchingAces:
                                                    description: It is the flow analysis's matchingAces.
                                                    returned: success,changed,always
                                                    type: list
                                                    contains:
                                                        ace:
                                                            description: It is the flow analysis's ace.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'
                                                        matchingPorts:
                                                            description: It is the flow analysis's matchingPorts.
                                                            returned: success,changed,always
                                                            type: list
                                                            contains:
                                                                ports:
                                                                    description: It is the flow analysis's ports.
                                                                    returned: success,changed,always
                                                                    type: list
                                                                    contains:
                                                                        destPorts:
                                                                            description: It is the flow analysis's destPorts.
                                                                            returned: success,changed,always
                                                                            type: list
                                                                        sourcePorts:
                                                                            description: It is the flow analysis's sourcePorts.
                                                                            returned: success,changed,always
                                                                            type: list

                                                                protocol:
                                                                    description: It is the flow analysis's protocol.
                                                                    returned: success,changed,always
                                                                    type: str
                                                                    sample: 'sample_string'

                                                        result:
                                                            description: It is the flow analysis's result.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'

                                                result:
                                                    description: It is the flow analysis's result.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'

                                        id:
                                            description: It is the flow analysis's id.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        interfaceStatistics:
                                            description: It is the flow analysis's interfaceStatistics.
                                            returned: success,changed,always
                                            type: dict
                                            contains:
                                                adminStatus:
                                                    description: It is the flow analysis's adminStatus.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                inputPackets:
                                                    description: It is the flow analysis's inputPackets.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputQueueCount:
                                                    description: It is the flow analysis's inputQueueCount.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputQueueDrops:
                                                    description: It is the flow analysis's inputQueueDrops.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputQueueFlushes:
                                                    description: It is the flow analysis's inputQueueFlushes.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputQueueMaxDepth:
                                                    description: It is the flow analysis's inputQueueMaxDepth.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputRatebps:
                                                    description: It is the flow analysis's inputRatebps.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                operationalStatus:
                                                    description: It is the flow analysis's operationalStatus.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                outputDrop:
                                                    description: It is the flow analysis's outputDrop.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                outputPackets:
                                                    description: It is the flow analysis's outputPackets.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                outputQueueCount:
                                                    description: It is the flow analysis's outputQueueCount.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                outputQueueDepth:
                                                    description: It is the flow analysis's outputQueueDepth.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                outputRatebps:
                                                    description: It is the flow analysis's outputRatebps.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                refreshedAt:
                                                    description: It is the flow analysis's refreshedAt.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0

                                        interfaceStatsCollection:
                                            description: It is the flow analysis's interfaceStatsCollection.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        interfaceStatsCollectionFailureReason:
                                            description: It is the flow analysis's interfaceStatsCollectionFailureReason.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        name:
                                            description: It is the flow analysis's name.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        pathOverlayInfo:
                                            description: It is the flow analysis's pathOverlayInfo.
                                            returned: success,changed,always
                                            type: list
                                            contains:
                                                controlPlane:
                                                    description: It is the flow analysis's controlPlane.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                dataPacketEncapsulation:
                                                    description: It is the flow analysis's dataPacketEncapsulation.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                destIp:
                                                    description: It is the flow analysis's destIp.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                destPort:
                                                    description: It is the flow analysis's destPort.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                protocol:
                                                    description: It is the flow analysis's protocol.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                sourceIp:
                                                    description: It is the flow analysis's sourceIp.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                sourcePort:
                                                    description: It is the flow analysis's sourcePort.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                vxlanInfo:
                                                    description: It is the flow analysis's vxlanInfo.
                                                    returned: success,changed,always
                                                    type: dict
                                                    contains:
                                                        dscp:
                                                            description: It is the flow analysis's dscp.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'
                                                        vnid:
                                                            description: It is the flow analysis's vnid.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'


                                        qosStatistics:
                                            description: It is the flow analysis's qosStatistics.
                                            returned: success,changed,always
                                            type: list
                                            contains:
                                                classMapName:
                                                    description: It is the flow analysis's classMapName.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                dropRate:
                                                    description: It is the flow analysis's dropRate.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                numBytes:
                                                    description: It is the flow analysis's numBytes.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                numPackets:
                                                    description: It is the flow analysis's numPackets.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                offeredRate:
                                                    description: It is the flow analysis's offeredRate.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                queueBandwidthbps:
                                                    description: It is the flow analysis's queueBandwidthbps.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                queueDepth:
                                                    description: It is the flow analysis's queueDepth.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                queueNoBufferDrops:
                                                    description: It is the flow analysis's queueNoBufferDrops.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                queueTotalDrops:
                                                    description: It is the flow analysis's queueTotalDrops.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                refreshedAt:
                                                    description: It is the flow analysis's refreshedAt.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0

                                        qosStatsCollection:
                                            description: It is the flow analysis's qosStatsCollection.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        qosStatsCollectionFailureReason:
                                            description: It is the flow analysis's qosStatsCollectionFailureReason.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        usedVlan:
                                            description: It is the flow analysis's usedVlan.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        vrfName:
                                            description: It is the flow analysis's vrfName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'

                                virtualInterface:
                                    description: It is the flow analysis's virtualInterface.
                                    returned: success,changed,always
                                    type: list
                                    contains:
                                        aclAnalysis:
                                            description: It is the flow analysis's aclAnalysis.
                                            returned: success,changed,always
                                            type: dict
                                            contains:
                                                aclName:
                                                    description: It is the flow analysis's aclName.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                matchingAces:
                                                    description: It is the flow analysis's matchingAces.
                                                    returned: success,changed,always
                                                    type: list
                                                    contains:
                                                        ace:
                                                            description: It is the flow analysis's ace.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'
                                                        matchingPorts:
                                                            description: It is the flow analysis's matchingPorts.
                                                            returned: success,changed,always
                                                            type: list
                                                            contains:
                                                                ports:
                                                                    description: It is the flow analysis's ports.
                                                                    returned: success,changed,always
                                                                    type: list
                                                                    contains:
                                                                        destPorts:
                                                                            description: It is the flow analysis's destPorts.
                                                                            returned: success,changed,always
                                                                            type: list
                                                                        sourcePorts:
                                                                            description: It is the flow analysis's sourcePorts.
                                                                            returned: success,changed,always
                                                                            type: list

                                                                protocol:
                                                                    description: It is the flow analysis's protocol.
                                                                    returned: success,changed,always
                                                                    type: str
                                                                    sample: 'sample_string'

                                                        result:
                                                            description: It is the flow analysis's result.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'

                                                result:
                                                    description: It is the flow analysis's result.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'

                                        id:
                                            description: It is the flow analysis's id.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        interfaceStatistics:
                                            description: It is the flow analysis's interfaceStatistics.
                                            returned: success,changed,always
                                            type: dict
                                            contains:
                                                adminStatus:
                                                    description: It is the flow analysis's adminStatus.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                inputPackets:
                                                    description: It is the flow analysis's inputPackets.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputQueueCount:
                                                    description: It is the flow analysis's inputQueueCount.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputQueueDrops:
                                                    description: It is the flow analysis's inputQueueDrops.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputQueueFlushes:
                                                    description: It is the flow analysis's inputQueueFlushes.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputQueueMaxDepth:
                                                    description: It is the flow analysis's inputQueueMaxDepth.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                inputRatebps:
                                                    description: It is the flow analysis's inputRatebps.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                operationalStatus:
                                                    description: It is the flow analysis's operationalStatus.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                outputDrop:
                                                    description: It is the flow analysis's outputDrop.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                outputPackets:
                                                    description: It is the flow analysis's outputPackets.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                outputQueueCount:
                                                    description: It is the flow analysis's outputQueueCount.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                outputQueueDepth:
                                                    description: It is the flow analysis's outputQueueDepth.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                outputRatebps:
                                                    description: It is the flow analysis's outputRatebps.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                refreshedAt:
                                                    description: It is the flow analysis's refreshedAt.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0

                                        interfaceStatsCollection:
                                            description: It is the flow analysis's interfaceStatsCollection.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        interfaceStatsCollectionFailureReason:
                                            description: It is the flow analysis's interfaceStatsCollectionFailureReason.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        name:
                                            description: It is the flow analysis's name.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        pathOverlayInfo:
                                            description: It is the flow analysis's pathOverlayInfo.
                                            returned: success,changed,always
                                            type: list
                                            contains:
                                                controlPlane:
                                                    description: It is the flow analysis's controlPlane.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                dataPacketEncapsulation:
                                                    description: It is the flow analysis's dataPacketEncapsulation.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                destIp:
                                                    description: It is the flow analysis's destIp.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                destPort:
                                                    description: It is the flow analysis's destPort.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                protocol:
                                                    description: It is the flow analysis's protocol.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                sourceIp:
                                                    description: It is the flow analysis's sourceIp.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                sourcePort:
                                                    description: It is the flow analysis's sourcePort.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                vxlanInfo:
                                                    description: It is the flow analysis's vxlanInfo.
                                                    returned: success,changed,always
                                                    type: dict
                                                    contains:
                                                        dscp:
                                                            description: It is the flow analysis's dscp.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'
                                                        vnid:
                                                            description: It is the flow analysis's vnid.
                                                            returned: success,changed,always
                                                            type: str
                                                            sample: 'sample_string'


                                        qosStatistics:
                                            description: It is the flow analysis's qosStatistics.
                                            returned: success,changed,always
                                            type: list
                                            contains:
                                                classMapName:
                                                    description: It is the flow analysis's classMapName.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                dropRate:
                                                    description: It is the flow analysis's dropRate.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                numBytes:
                                                    description: It is the flow analysis's numBytes.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                numPackets:
                                                    description: It is the flow analysis's numPackets.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                offeredRate:
                                                    description: It is the flow analysis's offeredRate.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                queueBandwidthbps:
                                                    description: It is the flow analysis's queueBandwidthbps.
                                                    returned: success,changed,always
                                                    type: str
                                                    sample: 'sample_string'
                                                queueDepth:
                                                    description: It is the flow analysis's queueDepth.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                queueNoBufferDrops:
                                                    description: It is the flow analysis's queueNoBufferDrops.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                queueTotalDrops:
                                                    description: It is the flow analysis's queueTotalDrops.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0
                                                refreshedAt:
                                                    description: It is the flow analysis's refreshedAt.
                                                    returned: success,changed,always
                                                    type: int
                                                    sample: 0

                                        qosStatsCollection:
                                            description: It is the flow analysis's qosStatsCollection.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        qosStatsCollectionFailureReason:
                                            description: It is the flow analysis's qosStatsCollectionFailureReason.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        usedVlan:
                                            description: It is the flow analysis's usedVlan.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'
                                        vrfName:
                                            description: It is the flow analysis's vrfName.
                                            returned: success,changed,always
                                            type: str
                                            sample: 'sample_string'


                        ip:
                            description: It is the flow analysis's ip.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        linkInformationSource:
                            description: It is the flow analysis's linkInformationSource.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        name:
                            description: It is the flow analysis's name.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        perfMonCollection:
                            description: It is the flow analysis's perfMonCollection.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        perfMonCollectionFailureReason:
                            description: It is the flow analysis's perfMonCollectionFailureReason.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        perfMonitorStatistics:
                            description: It is the flow analysis's perfMonitorStatistics.
                            returned: success,changed,always
                            type: list
                            contains:
                                byteRate:
                                    description: It is the flow analysis's byteRate.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                destIpAddress:
                                    description: It is the flow analysis's destIpAddress.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                destPort:
                                    description: It is the flow analysis's destPort.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                inputInterface:
                                    description: It is the flow analysis's inputInterface.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ipv4DSCP:
                                    description: It is the flow analysis's ipv4DSCP.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                ipv4TTL:
                                    description: It is the flow analysis's ipv4TTL.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                outputInterface:
                                    description: It is the flow analysis's outputInterface.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                packetBytes:
                                    description: It is the flow analysis's packetBytes.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                packetCount:
                                    description: It is the flow analysis's packetCount.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                packetLoss:
                                    description: It is the flow analysis's packetLoss.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                packetLossPercentage:
                                    description: It is the flow analysis's packetLossPercentage.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                protocol:
                                    description: It is the flow analysis's protocol.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                refreshedAt:
                                    description: It is the flow analysis's refreshedAt.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                rtpJitterMax:
                                    description: It is the flow analysis's rtpJitterMax.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                rtpJitterMean:
                                    description: It is the flow analysis's rtpJitterMean.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                rtpJitterMin:
                                    description: It is the flow analysis's rtpJitterMin.
                                    returned: success,changed,always
                                    type: int
                                    sample: 0
                                sourceIpAddress:
                                    description: It is the flow analysis's sourceIpAddress.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'
                                sourcePort:
                                    description: It is the flow analysis's sourcePort.
                                    returned: success,changed,always
                                    type: str
                                    sample: 'sample_string'

                        role:
                            description: It is the flow analysis's role.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        ssid:
                            description: It is the flow analysis's ssid.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        tunnels:
                            description: It is the flow analysis's tunnels.
                            returned: success,changed,always
                            type: list
                        type:
                            description: It is the flow analysis's type.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        wlanId:
                            description: It is the flow analysis's wlanId.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'

                properties:
                    description: It is the flow analysis's properties.
                    returned: success,changed,always
                    type: list
                request:
                    description: It is the flow analysis's request.
                    returned: success,changed,always
                    type: dict
                    contains:
                        controlPath:
                            description: It is the flow analysis's controlPath.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        createTime:
                            description: It is the flow analysis's createTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        destIP:
                            description: It is the flow analysis's destIP.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        destPort:
                            description: It is the flow analysis's destPort.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        failureReason:
                            description: It is the flow analysis's failureReason.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        id:
                            description: It is the flow analysis's id.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        inclusions:
                            description: It is the flow analysis's inclusions.
                            returned: success,changed,always
                            type: list
                        lastUpdateTime:
                            description: It is the flow analysis's lastUpdateTime.
                            returned: success,changed,always
                            type: int
                            sample: 0
                        periodicRefresh:
                            description: It is the flow analysis's periodicRefresh.
                            returned: success,changed,always
                            type: bool
                            sample: false
                        protocol:
                            description: It is the flow analysis's protocol.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        sourceIP:
                            description: It is the flow analysis's sourceIP.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        sourcePort:
                            description: It is the flow analysis's sourcePort.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'
                        status:
                            description: It is the flow analysis's status.
                            returned: success,changed,always
                            type: str
                            sample: 'sample_string'


        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_3:
    description: Deletes a flow analysis request by its id.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the flow analysis's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the flow analysis's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.flow_analysis import module_definition


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

    dnac.exit_json()


if __name__ == "__main__":
    main()