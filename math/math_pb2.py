# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: math.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nmath.proto\x12\x04math\"7\n\nSumRequest\x12\x13\n\x0b\x66irstNumber\x18\x01 \x01(\x02\x12\x14\n\x0csecondNumber\x18\x02 \x01(\x02\"0\n\x0bSumResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08response\x18\x02 \x01(\x02\x32\x34\n\x04Math\x12,\n\x03Sum\x12\x10.math.SumRequest\x1a\x11.math.SumResponse\"\x00\x62\x06proto3')



_SUMREQUEST = DESCRIPTOR.message_types_by_name['SumRequest']
_SUMRESPONSE = DESCRIPTOR.message_types_by_name['SumResponse']
SumRequest = _reflection.GeneratedProtocolMessageType('SumRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUMREQUEST,
  '__module__' : 'math_pb2'
  # @@protoc_insertion_point(class_scope:math.SumRequest)
  })
_sym_db.RegisterMessage(SumRequest)

SumResponse = _reflection.GeneratedProtocolMessageType('SumResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUMRESPONSE,
  '__module__' : 'math_pb2'
  # @@protoc_insertion_point(class_scope:math.SumResponse)
  })
_sym_db.RegisterMessage(SumResponse)

_MATH = DESCRIPTOR.services_by_name['Math']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SUMREQUEST._serialized_start=20
  _SUMREQUEST._serialized_end=75
  _SUMRESPONSE._serialized_start=77
  _SUMRESPONSE._serialized_end=125
  _MATH._serialized_start=127
  _MATH._serialized_end=179
# @@protoc_insertion_point(module_scope)
