# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: messaging.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'messaging.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fmessaging.proto\x12\tmessaging\"E\n\x17\x42roadcastMessageRequest\x12\x11\n\tsender_id\x18\x01 \x01(\t\x12\x17\n\x0fmessage_content\x18\x02 \x01(\t\"?\n\x18\x42roadcastMessageResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\nmessage_id\x18\x02 \x01(\t\"(\n\x15StreamMessagesRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"k\n\x16StreamMessagesResponse\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12\x11\n\tsender_id\x18\x02 \x01(\t\x12\x17\n\x0fmessage_content\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\t2\xc8\x01\n\x10MessagingService\x12[\n\x10\x42roadcastMessage\x12\".messaging.BroadcastMessageRequest\x1a#.messaging.BroadcastMessageResponse\x12W\n\x0eStreamMessages\x12 .messaging.StreamMessagesRequest\x1a!.messaging.StreamMessagesResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messaging_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BROADCASTMESSAGEREQUEST']._serialized_start=30
  _globals['_BROADCASTMESSAGEREQUEST']._serialized_end=99
  _globals['_BROADCASTMESSAGERESPONSE']._serialized_start=101
  _globals['_BROADCASTMESSAGERESPONSE']._serialized_end=164
  _globals['_STREAMMESSAGESREQUEST']._serialized_start=166
  _globals['_STREAMMESSAGESREQUEST']._serialized_end=206
  _globals['_STREAMMESSAGESRESPONSE']._serialized_start=208
  _globals['_STREAMMESSAGESRESPONSE']._serialized_end=315
  _globals['_MESSAGINGSERVICE']._serialized_start=318
  _globals['_MESSAGINGSERVICE']._serialized_end=518
# @@protoc_insertion_point(module_scope)
