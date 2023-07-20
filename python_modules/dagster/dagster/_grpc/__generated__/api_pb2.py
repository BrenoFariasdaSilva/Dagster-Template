# @generated

# This file was generated by running `python -m dagster._grpc.compile`
# Do not edit this file directly, and do not attempt to recompile it using
# grpc_tools.protoc directly, as several changes must be made to the raw output

# noqa: SLF001

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\tapi.proto\x12\x03\x61pi"\x07\n\x05\x45mpty"\x1b\n\x0bPingRequest\x12\x0c\n\x04\x65\x63ho\x18\x01'
    b' \x01(\t"\x19\n\tPingReply\x12\x0c\n\x04\x65\x63ho\x18\x01'
    b' \x01(\t"=\n\x14StreamingPingRequest\x12\x17\n\x0fsequence_length\x18\x01'
    b" \x01(\x05\x12\x0c\n\x04\x65\x63ho\x18\x02"
    b' \x01(\t";\n\x12StreamingPingEvent\x12\x17\n\x0fsequence_number\x18\x01'
    b" \x01(\x05\x12\x0c\n\x04\x65\x63ho\x18\x02"
    b' \x01(\t"%\n\x10GetServerIdReply\x12\x11\n\tserver_id\x18\x01'
    b" \x01(\t\"O\n\x1c\x45xecutionPlanSnapshotRequest\x12/\n'serialized_execution_plan_snapshot_args\x18\x01"
    b' \x01(\t"H\n\x1a\x45xecutionPlanSnapshotReply\x12*\n"serialized_execution_plan_snapshot\x18\x01'
    b" \x01(\t\"H\n\x1d\x45xternalPartitionNamesRequest\x12'\n\x1fserialized_partition_names_args\x18\x01"
    b' \x01(\t"p\n\x1b\x45xternalPartitionNamesReply\x12Q\nIserialized_external_partition_names_or_external_partition_execution_error\x18\x01'
    b' \x01(\t"4\n\x1b\x45xternalNotebookDataRequest\x12\x15\n\rnotebook_path\x18\x01'
    b' \x01(\t",\n\x19\x45xternalNotebookDataReply\x12\x0f\n\x07\x63ontent\x18\x01'
    b' \x01(\x0c"C\n\x1e\x45xternalPartitionConfigRequest\x12!\n\x19serialized_partition_args\x18\x01'
    b' \x01(\t"r\n\x1c\x45xternalPartitionConfigReply\x12R\nJserialized_external_partition_config_or_external_partition_execution_error\x18\x01'
    b' \x01(\t"A\n\x1c\x45xternalPartitionTagsRequest\x12!\n\x19serialized_partition_args\x18\x01'
    b' \x01(\t"n\n\x1a\x45xternalPartitionTagsReply\x12P\nHserialized_external_partition_tags_or_external_partition_execution_error\x18\x01'
    b' \x01(\t"c\n*ExternalPartitionSetExecutionParamsRequest\x12\x35\n-serialized_partition_set_execution_param_args\x18\x01'
    b' \x01(\t"\x19\n\x17ListRepositoriesRequest"O\n\x15ListRepositoriesReply\x12\x36\n.serialized_list_repositories_response_or_error\x18\x01'
    b' \x01(\t"Y\n%ExternalPipelineSubsetSnapshotRequest\x12\x30\n(serialized_pipeline_subset_snapshot_args\x18\x01'
    b' \x01(\t"Y\n#ExternalPipelineSubsetSnapshotReply\x12\x32\n*serialized_external_pipeline_subset_result\x18\x01'
    b' \x01(\t"a\n\x19\x45xternalRepositoryRequest\x12+\n#serialized_repository_python_origin\x18\x01'
    b" \x01(\t\x12\x17\n\x0f\x64\x65\x66\x65r_snapshots\x18\x02"
    b' \x01(\x08"F\n\x17\x45xternalRepositoryReply\x12+\n#serialized_external_repository_data\x18\x01'
    b' \x01(\t"i\n StreamingExternalRepositoryEvent\x12\x17\n\x0fsequence_number\x18\x01'
    b' \x01(\x05\x12,\n$serialized_external_repository_chunk\x18\x02 \x01(\t"W\n'
    b" ExternalScheduleExecutionRequest\x12\x33\n+serialized_external_schedule_execution_args\x18\x01"
    b' \x01(\t"S\n\x1e\x45xternalSensorExecutionRequest\x12\x31\n)serialized_external_sensor_execution_args\x18\x01'
    b' \x01(\t"H\n\x13StreamingChunkEvent\x12\x17\n\x0fsequence_number\x18\x01'
    b" \x01(\x05\x12\x18\n\x10serialized_chunk\x18\x02"
    b' \x01(\t"@\n\x13ShutdownServerReply\x12)\n!serialized_shutdown_server_result\x18\x01'
    b' \x01(\t"E\n\x16\x43\x61ncelExecutionRequest\x12+\n#serialized_cancel_execution_request\x18\x01'
    b' \x01(\t"B\n\x14\x43\x61ncelExecutionReply\x12*\n"serialized_cancel_execution_result\x18\x01'
    b" \x01(\t\"L\n\x19\x43\x61nCancelExecutionRequest\x12/\n'serialized_can_cancel_execution_request\x18\x01"
    b' \x01(\t"I\n\x17\x43\x61nCancelExecutionReply\x12.\n&serialized_can_cancel_execution_result\x18\x01'
    b' \x01(\t"6\n\x0fStartRunRequest\x12#\n\x1bserialized_execute_run_args\x18\x01'
    b' \x01(\t"4\n\rStartRunReply\x12#\n\x1bserialized_start_run_result\x18\x01'
    b' \x01(\t"8\n\x14GetCurrentImageReply\x12 \n\x18serialized_current_image\x18\x01'
    b' \x01(\t"6\n\x13GetCurrentRunsReply\x12\x1f\n\x17serialized_current_runs\x18\x01'
    b' \x01(\t"L\n\x12\x45xternalJobRequest\x12$\n\x1cserialized_repository_origin\x18\x01'
    b" \x01(\t\x12\x10\n\x08job_name\x18\x02"
    b' \x01(\t"I\n\x10\x45xternalJobReply\x12\x1b\n\x13serialized_job_data\x18\x01'
    b" \x01(\t\x12\x18\n\x10serialized_error\x18\x02"
    b' \x01(\t2\xd3\x0e\n\nDagsterApi\x12*\n\x04Ping\x12\x10.api.PingRequest\x1a\x0e.api.PingReply"\x00\x12/\n\tHeartbeat\x12\x10.api.PingRequest\x1a\x0e.api.PingReply"\x00\x12G\n\rStreamingPing\x12\x19.api.StreamingPingRequest\x1a\x17.api.StreamingPingEvent"\x00\x30\x01\x12\x32\n\x0bGetServerId\x12\n.api.Empty\x1a\x15.api.GetServerIdReply"\x00\x12]\n\x15\x45xecutionPlanSnapshot\x12!.api.ExecutionPlanSnapshotRequest\x1a\x1f.api.ExecutionPlanSnapshotReply"\x00\x12N\n\x10ListRepositories\x12\x1c.api.ListRepositoriesRequest\x1a\x1a.api.ListRepositoriesReply"\x00\x12`\n\x16\x45xternalPartitionNames\x12".api.ExternalPartitionNamesRequest\x1a'
    b' .api.ExternalPartitionNamesReply"\x00\x12Z\n\x14\x45xternalNotebookData\x12'
    b' .api.ExternalNotebookDataRequest\x1a\x1e.api.ExternalNotebookDataReply"\x00\x12\x63\n\x17\x45xternalPartitionConfig\x12#.api.ExternalPartitionConfigRequest\x1a!.api.ExternalPartitionConfigReply"\x00\x12]\n\x15\x45xternalPartitionTags\x12!.api.ExternalPartitionTagsRequest\x1a\x1f.api.ExternalPartitionTagsReply"\x00\x12t\n#ExternalPartitionSetExecutionParams\x12/.api.ExternalPartitionSetExecutionParamsRequest\x1a\x18.api.StreamingChunkEvent"\x00\x30\x01\x12x\n\x1e\x45xternalPipelineSubsetSnapshot\x12*.api.ExternalPipelineSubsetSnapshotRequest\x1a(.api.ExternalPipelineSubsetSnapshotReply"\x00\x12T\n\x12\x45xternalRepository\x12\x1e.api.ExternalRepositoryRequest\x1a\x1c.api.ExternalRepositoryReply"\x00\x12?\n\x0b\x45xternalJob\x12\x17.api.ExternalJobRequest\x1a\x15.api.ExternalJobReply"\x00\x12h\n\x1bStreamingExternalRepository\x12\x1e.api.ExternalRepositoryRequest\x1a%.api.StreamingExternalRepositoryEvent"\x00\x30\x01\x12`\n\x19\x45xternalScheduleExecution\x12%.api.ExternalScheduleExecutionRequest\x1a\x18.api.StreamingChunkEvent"\x00\x30\x01\x12\\\n\x17\x45xternalSensorExecution\x12#.api.ExternalSensorExecutionRequest\x1a\x18.api.StreamingChunkEvent"\x00\x30\x01\x12\x38\n\x0eShutdownServer\x12\n.api.Empty\x1a\x18.api.ShutdownServerReply"\x00\x12K\n\x0f\x43\x61ncelExecution\x12\x1b.api.CancelExecutionRequest\x1a\x19.api.CancelExecutionReply"\x00\x12T\n\x12\x43\x61nCancelExecution\x12\x1e.api.CanCancelExecutionRequest\x1a\x1c.api.CanCancelExecutionReply"\x00\x12\x36\n\x08StartRun\x12\x14.api.StartRunRequest\x1a\x12.api.StartRunReply"\x00\x12:\n\x0fGetCurrentImage\x12\n.api.Empty\x1a\x19.api.GetCurrentImageReply"\x00\x12\x38\n\x0eGetCurrentRuns\x12\n.api.Empty\x1a\x18.api.GetCurrentRunsReply"\x00\x62\x06proto3'
)


_EMPTY = DESCRIPTOR.message_types_by_name["Empty"]
_PINGREQUEST = DESCRIPTOR.message_types_by_name["PingRequest"]
_PINGREPLY = DESCRIPTOR.message_types_by_name["PingReply"]
_STREAMINGPINGREQUEST = DESCRIPTOR.message_types_by_name["StreamingPingRequest"]
_STREAMINGPINGEVENT = DESCRIPTOR.message_types_by_name["StreamingPingEvent"]
_GETSERVERIDREPLY = DESCRIPTOR.message_types_by_name["GetServerIdReply"]
_EXECUTIONPLANSNAPSHOTREQUEST = DESCRIPTOR.message_types_by_name["ExecutionPlanSnapshotRequest"]
_EXECUTIONPLANSNAPSHOTREPLY = DESCRIPTOR.message_types_by_name["ExecutionPlanSnapshotReply"]
_EXTERNALPARTITIONNAMESREQUEST = DESCRIPTOR.message_types_by_name["ExternalPartitionNamesRequest"]
_EXTERNALPARTITIONNAMESREPLY = DESCRIPTOR.message_types_by_name["ExternalPartitionNamesReply"]
_EXTERNALNOTEBOOKDATAREQUEST = DESCRIPTOR.message_types_by_name["ExternalNotebookDataRequest"]
_EXTERNALNOTEBOOKDATAREPLY = DESCRIPTOR.message_types_by_name["ExternalNotebookDataReply"]
_EXTERNALPARTITIONCONFIGREQUEST = DESCRIPTOR.message_types_by_name["ExternalPartitionConfigRequest"]
_EXTERNALPARTITIONCONFIGREPLY = DESCRIPTOR.message_types_by_name["ExternalPartitionConfigReply"]
_EXTERNALPARTITIONTAGSREQUEST = DESCRIPTOR.message_types_by_name["ExternalPartitionTagsRequest"]
_EXTERNALPARTITIONTAGSREPLY = DESCRIPTOR.message_types_by_name["ExternalPartitionTagsReply"]
_EXTERNALPARTITIONSETEXECUTIONPARAMSREQUEST = DESCRIPTOR.message_types_by_name[
    "ExternalPartitionSetExecutionParamsRequest"
]
_LISTREPOSITORIESREQUEST = DESCRIPTOR.message_types_by_name["ListRepositoriesRequest"]
_LISTREPOSITORIESREPLY = DESCRIPTOR.message_types_by_name["ListRepositoriesReply"]
_EXTERNALPIPELINESUBSETSNAPSHOTREQUEST = DESCRIPTOR.message_types_by_name[
    "ExternalPipelineSubsetSnapshotRequest"
]
_EXTERNALPIPELINESUBSETSNAPSHOTREPLY = DESCRIPTOR.message_types_by_name[
    "ExternalPipelineSubsetSnapshotReply"
]
_EXTERNALREPOSITORYREQUEST = DESCRIPTOR.message_types_by_name["ExternalRepositoryRequest"]
_EXTERNALREPOSITORYREPLY = DESCRIPTOR.message_types_by_name["ExternalRepositoryReply"]
_STREAMINGEXTERNALREPOSITORYEVENT = DESCRIPTOR.message_types_by_name[
    "StreamingExternalRepositoryEvent"
]
_EXTERNALSCHEDULEEXECUTIONREQUEST = DESCRIPTOR.message_types_by_name[
    "ExternalScheduleExecutionRequest"
]
_EXTERNALSENSOREXECUTIONREQUEST = DESCRIPTOR.message_types_by_name["ExternalSensorExecutionRequest"]
_STREAMINGCHUNKEVENT = DESCRIPTOR.message_types_by_name["StreamingChunkEvent"]
_SHUTDOWNSERVERREPLY = DESCRIPTOR.message_types_by_name["ShutdownServerReply"]
_CANCELEXECUTIONREQUEST = DESCRIPTOR.message_types_by_name["CancelExecutionRequest"]
_CANCELEXECUTIONREPLY = DESCRIPTOR.message_types_by_name["CancelExecutionReply"]
_CANCANCELEXECUTIONREQUEST = DESCRIPTOR.message_types_by_name["CanCancelExecutionRequest"]
_CANCANCELEXECUTIONREPLY = DESCRIPTOR.message_types_by_name["CanCancelExecutionReply"]
_STARTRUNREQUEST = DESCRIPTOR.message_types_by_name["StartRunRequest"]
_STARTRUNREPLY = DESCRIPTOR.message_types_by_name["StartRunReply"]
_GETCURRENTIMAGEREPLY = DESCRIPTOR.message_types_by_name["GetCurrentImageReply"]
_GETCURRENTRUNSREPLY = DESCRIPTOR.message_types_by_name["GetCurrentRunsReply"]
_EXTERNALJOBREQUEST = DESCRIPTOR.message_types_by_name["ExternalJobRequest"]
_EXTERNALJOBREPLY = DESCRIPTOR.message_types_by_name["ExternalJobReply"]
Empty = _reflection.GeneratedProtocolMessageType(
    "Empty",
    (_message.Message,),
    {
        "DESCRIPTOR": _EMPTY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.Empty)
    },
)
_sym_db.RegisterMessage(Empty)

PingRequest = _reflection.GeneratedProtocolMessageType(
    "PingRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _PINGREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.PingRequest)
    },
)
_sym_db.RegisterMessage(PingRequest)

PingReply = _reflection.GeneratedProtocolMessageType(
    "PingReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _PINGREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.PingReply)
    },
)
_sym_db.RegisterMessage(PingReply)

StreamingPingRequest = _reflection.GeneratedProtocolMessageType(
    "StreamingPingRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _STREAMINGPINGREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.StreamingPingRequest)
    },
)
_sym_db.RegisterMessage(StreamingPingRequest)

StreamingPingEvent = _reflection.GeneratedProtocolMessageType(
    "StreamingPingEvent",
    (_message.Message,),
    {
        "DESCRIPTOR": _STREAMINGPINGEVENT,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.StreamingPingEvent)
    },
)
_sym_db.RegisterMessage(StreamingPingEvent)

GetServerIdReply = _reflection.GeneratedProtocolMessageType(
    "GetServerIdReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETSERVERIDREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.GetServerIdReply)
    },
)
_sym_db.RegisterMessage(GetServerIdReply)

ExecutionPlanSnapshotRequest = _reflection.GeneratedProtocolMessageType(
    "ExecutionPlanSnapshotRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXECUTIONPLANSNAPSHOTREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExecutionPlanSnapshotRequest)
    },
)
_sym_db.RegisterMessage(ExecutionPlanSnapshotRequest)

ExecutionPlanSnapshotReply = _reflection.GeneratedProtocolMessageType(
    "ExecutionPlanSnapshotReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXECUTIONPLANSNAPSHOTREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExecutionPlanSnapshotReply)
    },
)
_sym_db.RegisterMessage(ExecutionPlanSnapshotReply)

ExternalPartitionNamesRequest = _reflection.GeneratedProtocolMessageType(
    "ExternalPartitionNamesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALPARTITIONNAMESREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalPartitionNamesRequest)
    },
)
_sym_db.RegisterMessage(ExternalPartitionNamesRequest)

ExternalPartitionNamesReply = _reflection.GeneratedProtocolMessageType(
    "ExternalPartitionNamesReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALPARTITIONNAMESREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalPartitionNamesReply)
    },
)
_sym_db.RegisterMessage(ExternalPartitionNamesReply)

ExternalNotebookDataRequest = _reflection.GeneratedProtocolMessageType(
    "ExternalNotebookDataRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALNOTEBOOKDATAREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalNotebookDataRequest)
    },
)
_sym_db.RegisterMessage(ExternalNotebookDataRequest)

ExternalNotebookDataReply = _reflection.GeneratedProtocolMessageType(
    "ExternalNotebookDataReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALNOTEBOOKDATAREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalNotebookDataReply)
    },
)
_sym_db.RegisterMessage(ExternalNotebookDataReply)

ExternalPartitionConfigRequest = _reflection.GeneratedProtocolMessageType(
    "ExternalPartitionConfigRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALPARTITIONCONFIGREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalPartitionConfigRequest)
    },
)
_sym_db.RegisterMessage(ExternalPartitionConfigRequest)

ExternalPartitionConfigReply = _reflection.GeneratedProtocolMessageType(
    "ExternalPartitionConfigReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALPARTITIONCONFIGREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalPartitionConfigReply)
    },
)
_sym_db.RegisterMessage(ExternalPartitionConfigReply)

ExternalPartitionTagsRequest = _reflection.GeneratedProtocolMessageType(
    "ExternalPartitionTagsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALPARTITIONTAGSREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalPartitionTagsRequest)
    },
)
_sym_db.RegisterMessage(ExternalPartitionTagsRequest)

ExternalPartitionTagsReply = _reflection.GeneratedProtocolMessageType(
    "ExternalPartitionTagsReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALPARTITIONTAGSREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalPartitionTagsReply)
    },
)
_sym_db.RegisterMessage(ExternalPartitionTagsReply)

ExternalPartitionSetExecutionParamsRequest = _reflection.GeneratedProtocolMessageType(
    "ExternalPartitionSetExecutionParamsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALPARTITIONSETEXECUTIONPARAMSREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalPartitionSetExecutionParamsRequest)
    },
)
_sym_db.RegisterMessage(ExternalPartitionSetExecutionParamsRequest)

ListRepositoriesRequest = _reflection.GeneratedProtocolMessageType(
    "ListRepositoriesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTREPOSITORIESREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ListRepositoriesRequest)
    },
)
_sym_db.RegisterMessage(ListRepositoriesRequest)

ListRepositoriesReply = _reflection.GeneratedProtocolMessageType(
    "ListRepositoriesReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTREPOSITORIESREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ListRepositoriesReply)
    },
)
_sym_db.RegisterMessage(ListRepositoriesReply)

ExternalPipelineSubsetSnapshotRequest = _reflection.GeneratedProtocolMessageType(
    "ExternalPipelineSubsetSnapshotRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALPIPELINESUBSETSNAPSHOTREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalPipelineSubsetSnapshotRequest)
    },
)
_sym_db.RegisterMessage(ExternalPipelineSubsetSnapshotRequest)

ExternalPipelineSubsetSnapshotReply = _reflection.GeneratedProtocolMessageType(
    "ExternalPipelineSubsetSnapshotReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALPIPELINESUBSETSNAPSHOTREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalPipelineSubsetSnapshotReply)
    },
)
_sym_db.RegisterMessage(ExternalPipelineSubsetSnapshotReply)

ExternalRepositoryRequest = _reflection.GeneratedProtocolMessageType(
    "ExternalRepositoryRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALREPOSITORYREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalRepositoryRequest)
    },
)
_sym_db.RegisterMessage(ExternalRepositoryRequest)

ExternalRepositoryReply = _reflection.GeneratedProtocolMessageType(
    "ExternalRepositoryReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALREPOSITORYREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalRepositoryReply)
    },
)
_sym_db.RegisterMessage(ExternalRepositoryReply)

StreamingExternalRepositoryEvent = _reflection.GeneratedProtocolMessageType(
    "StreamingExternalRepositoryEvent",
    (_message.Message,),
    {
        "DESCRIPTOR": _STREAMINGEXTERNALREPOSITORYEVENT,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.StreamingExternalRepositoryEvent)
    },
)
_sym_db.RegisterMessage(StreamingExternalRepositoryEvent)

ExternalScheduleExecutionRequest = _reflection.GeneratedProtocolMessageType(
    "ExternalScheduleExecutionRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALSCHEDULEEXECUTIONREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalScheduleExecutionRequest)
    },
)
_sym_db.RegisterMessage(ExternalScheduleExecutionRequest)

ExternalSensorExecutionRequest = _reflection.GeneratedProtocolMessageType(
    "ExternalSensorExecutionRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALSENSOREXECUTIONREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalSensorExecutionRequest)
    },
)
_sym_db.RegisterMessage(ExternalSensorExecutionRequest)

StreamingChunkEvent = _reflection.GeneratedProtocolMessageType(
    "StreamingChunkEvent",
    (_message.Message,),
    {
        "DESCRIPTOR": _STREAMINGCHUNKEVENT,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.StreamingChunkEvent)
    },
)
_sym_db.RegisterMessage(StreamingChunkEvent)

ShutdownServerReply = _reflection.GeneratedProtocolMessageType(
    "ShutdownServerReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _SHUTDOWNSERVERREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ShutdownServerReply)
    },
)
_sym_db.RegisterMessage(ShutdownServerReply)

CancelExecutionRequest = _reflection.GeneratedProtocolMessageType(
    "CancelExecutionRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCELEXECUTIONREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.CancelExecutionRequest)
    },
)
_sym_db.RegisterMessage(CancelExecutionRequest)

CancelExecutionReply = _reflection.GeneratedProtocolMessageType(
    "CancelExecutionReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCELEXECUTIONREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.CancelExecutionReply)
    },
)
_sym_db.RegisterMessage(CancelExecutionReply)

CanCancelExecutionRequest = _reflection.GeneratedProtocolMessageType(
    "CanCancelExecutionRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCANCELEXECUTIONREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.CanCancelExecutionRequest)
    },
)
_sym_db.RegisterMessage(CanCancelExecutionRequest)

CanCancelExecutionReply = _reflection.GeneratedProtocolMessageType(
    "CanCancelExecutionReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCANCELEXECUTIONREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.CanCancelExecutionReply)
    },
)
_sym_db.RegisterMessage(CanCancelExecutionReply)

StartRunRequest = _reflection.GeneratedProtocolMessageType(
    "StartRunRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _STARTRUNREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.StartRunRequest)
    },
)
_sym_db.RegisterMessage(StartRunRequest)

StartRunReply = _reflection.GeneratedProtocolMessageType(
    "StartRunReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _STARTRUNREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.StartRunReply)
    },
)
_sym_db.RegisterMessage(StartRunReply)

GetCurrentImageReply = _reflection.GeneratedProtocolMessageType(
    "GetCurrentImageReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETCURRENTIMAGEREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.GetCurrentImageReply)
    },
)
_sym_db.RegisterMessage(GetCurrentImageReply)

GetCurrentRunsReply = _reflection.GeneratedProtocolMessageType(
    "GetCurrentRunsReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETCURRENTRUNSREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.GetCurrentRunsReply)
    },
)
_sym_db.RegisterMessage(GetCurrentRunsReply)

ExternalJobRequest = _reflection.GeneratedProtocolMessageType(
    "ExternalJobRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALJOBREQUEST,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalJobRequest)
    },
)
_sym_db.RegisterMessage(ExternalJobRequest)

ExternalJobReply = _reflection.GeneratedProtocolMessageType(
    "ExternalJobReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXTERNALJOBREPLY,
        "__module__": "api_pb2"
        # @@protoc_insertion_point(class_scope:api.ExternalJobReply)
    },
)
_sym_db.RegisterMessage(ExternalJobReply)

_DAGSTERAPI = DESCRIPTOR.services_by_name["DagsterApi"]
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _EMPTY._serialized_start = 18
    _EMPTY._serialized_end = 25
    _PINGREQUEST._serialized_start = 27
    _PINGREQUEST._serialized_end = 54
    _PINGREPLY._serialized_start = 56
    _PINGREPLY._serialized_end = 81
    _STREAMINGPINGREQUEST._serialized_start = 83
    _STREAMINGPINGREQUEST._serialized_end = 144
    _STREAMINGPINGEVENT._serialized_start = 146
    _STREAMINGPINGEVENT._serialized_end = 205
    _GETSERVERIDREPLY._serialized_start = 207
    _GETSERVERIDREPLY._serialized_end = 244
    _EXECUTIONPLANSNAPSHOTREQUEST._serialized_start = 246
    _EXECUTIONPLANSNAPSHOTREQUEST._serialized_end = 325
    _EXECUTIONPLANSNAPSHOTREPLY._serialized_start = 327
    _EXECUTIONPLANSNAPSHOTREPLY._serialized_end = 399
    _EXTERNALPARTITIONNAMESREQUEST._serialized_start = 401
    _EXTERNALPARTITIONNAMESREQUEST._serialized_end = 473
    _EXTERNALPARTITIONNAMESREPLY._serialized_start = 475
    _EXTERNALPARTITIONNAMESREPLY._serialized_end = 587
    _EXTERNALNOTEBOOKDATAREQUEST._serialized_start = 589
    _EXTERNALNOTEBOOKDATAREQUEST._serialized_end = 641
    _EXTERNALNOTEBOOKDATAREPLY._serialized_start = 643
    _EXTERNALNOTEBOOKDATAREPLY._serialized_end = 687
    _EXTERNALPARTITIONCONFIGREQUEST._serialized_start = 689
    _EXTERNALPARTITIONCONFIGREQUEST._serialized_end = 756
    _EXTERNALPARTITIONCONFIGREPLY._serialized_start = 758
    _EXTERNALPARTITIONCONFIGREPLY._serialized_end = 872
    _EXTERNALPARTITIONTAGSREQUEST._serialized_start = 874
    _EXTERNALPARTITIONTAGSREQUEST._serialized_end = 939
    _EXTERNALPARTITIONTAGSREPLY._serialized_start = 941
    _EXTERNALPARTITIONTAGSREPLY._serialized_end = 1051
    _EXTERNALPARTITIONSETEXECUTIONPARAMSREQUEST._serialized_start = 1053
    _EXTERNALPARTITIONSETEXECUTIONPARAMSREQUEST._serialized_end = 1152
    _LISTREPOSITORIESREQUEST._serialized_start = 1154
    _LISTREPOSITORIESREQUEST._serialized_end = 1179
    _LISTREPOSITORIESREPLY._serialized_start = 1181
    _LISTREPOSITORIESREPLY._serialized_end = 1260
    _EXTERNALPIPELINESUBSETSNAPSHOTREQUEST._serialized_start = 1262
    _EXTERNALPIPELINESUBSETSNAPSHOTREQUEST._serialized_end = 1351
    _EXTERNALPIPELINESUBSETSNAPSHOTREPLY._serialized_start = 1353
    _EXTERNALPIPELINESUBSETSNAPSHOTREPLY._serialized_end = 1442
    _EXTERNALREPOSITORYREQUEST._serialized_start = 1444
    _EXTERNALREPOSITORYREQUEST._serialized_end = 1541
    _EXTERNALREPOSITORYREPLY._serialized_start = 1543
    _EXTERNALREPOSITORYREPLY._serialized_end = 1613
    _STREAMINGEXTERNALREPOSITORYEVENT._serialized_start = 1615
    _STREAMINGEXTERNALREPOSITORYEVENT._serialized_end = 1720
    _EXTERNALSCHEDULEEXECUTIONREQUEST._serialized_start = 1722
    _EXTERNALSCHEDULEEXECUTIONREQUEST._serialized_end = 1809
    _EXTERNALSENSOREXECUTIONREQUEST._serialized_start = 1811
    _EXTERNALSENSOREXECUTIONREQUEST._serialized_end = 1894
    _STREAMINGCHUNKEVENT._serialized_start = 1896
    _STREAMINGCHUNKEVENT._serialized_end = 1968
    _SHUTDOWNSERVERREPLY._serialized_start = 1970
    _SHUTDOWNSERVERREPLY._serialized_end = 2034
    _CANCELEXECUTIONREQUEST._serialized_start = 2036
    _CANCELEXECUTIONREQUEST._serialized_end = 2105
    _CANCELEXECUTIONREPLY._serialized_start = 2107
    _CANCELEXECUTIONREPLY._serialized_end = 2173
    _CANCANCELEXECUTIONREQUEST._serialized_start = 2175
    _CANCANCELEXECUTIONREQUEST._serialized_end = 2251
    _CANCANCELEXECUTIONREPLY._serialized_start = 2253
    _CANCANCELEXECUTIONREPLY._serialized_end = 2326
    _STARTRUNREQUEST._serialized_start = 2328
    _STARTRUNREQUEST._serialized_end = 2382
    _STARTRUNREPLY._serialized_start = 2384
    _STARTRUNREPLY._serialized_end = 2436
    _GETCURRENTIMAGEREPLY._serialized_start = 2438
    _GETCURRENTIMAGEREPLY._serialized_end = 2494
    _GETCURRENTRUNSREPLY._serialized_start = 2496
    _GETCURRENTRUNSREPLY._serialized_end = 2550
    _EXTERNALJOBREQUEST._serialized_start = 2552
    _EXTERNALJOBREQUEST._serialized_end = 2628
    _EXTERNALJOBREPLY._serialized_start = 2630
    _EXTERNALJOBREPLY._serialized_end = 2703
    _DAGSTERAPI._serialized_start = 2706
    _DAGSTERAPI._serialized_end = 4581
# @@protoc_insertion_point(module_scope)