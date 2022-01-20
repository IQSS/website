# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: topic_page.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10topic_page.proto\x12\x0b\x64\x61tacommons\"\xd7\x01\n\x0cPageMetadata\x12\x10\n\x08topic_id\x18\x01 \x01(\t\x12\x12\n\ntopic_name\x18\x02 \x01(\t\x12\x12\n\nplace_dcid\x18\x03 \x03(\t\x12Q\n\x15\x63ontained_place_types\x18\x04 \x03(\x0b\x32\x32.datacommons.PageMetadata.ContainedPlaceTypesEntry\x1a:\n\x18\x43ontainedPlaceTypesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"^\n\x0fStatVarMetadata\x12\x10\n\x08stat_var\x18\x01 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t\x12\x0c\n\x04unit\x18\x03 \x01(\t\x12\x0f\n\x07scaling\x18\x04 \x01(\x01\x12\x0b\n\x03log\x18\x05 \x01(\x08\"\x82\x01\n\x0fRankingMetadata\x12\x14\n\x0cshow_highest\x18\x01 \x01(\x08\x12\x13\n\x0bshow_lowest\x18\x02 \x01(\x08\x12\x15\n\rshow_increase\x18\x03 \x01(\x08\x12\x15\n\rshow_decrease\x18\x04 \x01(\x08\x12\x16\n\x0e\x64iff_base_date\x18\x05 \x01(\t\"(\n\x11HighlightMetadata\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\"\xf0\x02\n\x04Tile\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12(\n\x04type\x18\x03 \x01(\x0e\x32\x1a.datacommons.Tile.TileType\x12\x37\n\x11stat_var_override\x18\x04 \x03(\x0b\x32\x1c.datacommons.StatVarMetadata\x12\x36\n\x10ranking_metadata\x18\x05 \x01(\x0b\x32\x1c.datacommons.RankingMetadata\x12:\n\x12highlight_metadata\x18\x06 \x01(\x0b\x32\x1e.datacommons.HighlightMetadata\"m\n\x08TileType\x12\r\n\tTYPE_NONE\x10\x00\x12\x08\n\x04LINE\x10\x01\x12\x07\n\x03\x42\x41R\x10\x02\x12\x07\n\x03MAP\x10\x03\x12\x0b\n\x07SCATTER\x10\x04\x12\r\n\tBIVARIATE\x10\x05\x12\x0b\n\x07RANKING\x10\x06\x12\r\n\tHIGHLIGHT\x10\x07\"\xb3\x01\n\x05\x42lock\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12%\n\nleft_tiles\x18\x03 \x03(\x0b\x32\x11.datacommons.Tile\x12&\n\x0bright_tiles\x18\x04 \x03(\x0b\x32\x11.datacommons.Tile\x12\x37\n\x11stat_var_metadata\x18\x05 \x03(\x0b\x32\x1c.datacommons.StatVarMetadata\"b\n\x0fTopicPageConfig\x12+\n\x08metadata\x18\x01 \x01(\x0b\x32\x19.datacommons.PageMetadata\x12\"\n\x06\x62locks\x18\x02 \x03(\x0b\x32\x12.datacommons.Blockb\x06proto3')



_PAGEMETADATA = DESCRIPTOR.message_types_by_name['PageMetadata']
_PAGEMETADATA_CONTAINEDPLACETYPESENTRY = _PAGEMETADATA.nested_types_by_name['ContainedPlaceTypesEntry']
_STATVARMETADATA = DESCRIPTOR.message_types_by_name['StatVarMetadata']
_RANKINGMETADATA = DESCRIPTOR.message_types_by_name['RankingMetadata']
_HIGHLIGHTMETADATA = DESCRIPTOR.message_types_by_name['HighlightMetadata']
_TILE = DESCRIPTOR.message_types_by_name['Tile']
_BLOCK = DESCRIPTOR.message_types_by_name['Block']
_TOPICPAGECONFIG = DESCRIPTOR.message_types_by_name['TopicPageConfig']
_TILE_TILETYPE = _TILE.enum_types_by_name['TileType']
PageMetadata = _reflection.GeneratedProtocolMessageType('PageMetadata', (_message.Message,), {

  'ContainedPlaceTypesEntry' : _reflection.GeneratedProtocolMessageType('ContainedPlaceTypesEntry', (_message.Message,), {
    'DESCRIPTOR' : _PAGEMETADATA_CONTAINEDPLACETYPESENTRY,
    '__module__' : 'topic_page_pb2'
    # @@protoc_insertion_point(class_scope:datacommons.PageMetadata.ContainedPlaceTypesEntry)
    })
  ,
  'DESCRIPTOR' : _PAGEMETADATA,
  '__module__' : 'topic_page_pb2'
  # @@protoc_insertion_point(class_scope:datacommons.PageMetadata)
  })
_sym_db.RegisterMessage(PageMetadata)
_sym_db.RegisterMessage(PageMetadata.ContainedPlaceTypesEntry)

StatVarMetadata = _reflection.GeneratedProtocolMessageType('StatVarMetadata', (_message.Message,), {
  'DESCRIPTOR' : _STATVARMETADATA,
  '__module__' : 'topic_page_pb2'
  # @@protoc_insertion_point(class_scope:datacommons.StatVarMetadata)
  })
_sym_db.RegisterMessage(StatVarMetadata)

RankingMetadata = _reflection.GeneratedProtocolMessageType('RankingMetadata', (_message.Message,), {
  'DESCRIPTOR' : _RANKINGMETADATA,
  '__module__' : 'topic_page_pb2'
  # @@protoc_insertion_point(class_scope:datacommons.RankingMetadata)
  })
_sym_db.RegisterMessage(RankingMetadata)

HighlightMetadata = _reflection.GeneratedProtocolMessageType('HighlightMetadata', (_message.Message,), {
  'DESCRIPTOR' : _HIGHLIGHTMETADATA,
  '__module__' : 'topic_page_pb2'
  # @@protoc_insertion_point(class_scope:datacommons.HighlightMetadata)
  })
_sym_db.RegisterMessage(HighlightMetadata)

Tile = _reflection.GeneratedProtocolMessageType('Tile', (_message.Message,), {
  'DESCRIPTOR' : _TILE,
  '__module__' : 'topic_page_pb2'
  # @@protoc_insertion_point(class_scope:datacommons.Tile)
  })
_sym_db.RegisterMessage(Tile)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'topic_page_pb2'
  # @@protoc_insertion_point(class_scope:datacommons.Block)
  })
_sym_db.RegisterMessage(Block)

TopicPageConfig = _reflection.GeneratedProtocolMessageType('TopicPageConfig', (_message.Message,), {
  'DESCRIPTOR' : _TOPICPAGECONFIG,
  '__module__' : 'topic_page_pb2'
  # @@protoc_insertion_point(class_scope:datacommons.TopicPageConfig)
  })
_sym_db.RegisterMessage(TopicPageConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PAGEMETADATA_CONTAINEDPLACETYPESENTRY._options = None
  _PAGEMETADATA_CONTAINEDPLACETYPESENTRY._serialized_options = b'8\001'
  _PAGEMETADATA._serialized_start=34
  _PAGEMETADATA._serialized_end=249
  _PAGEMETADATA_CONTAINEDPLACETYPESENTRY._serialized_start=191
  _PAGEMETADATA_CONTAINEDPLACETYPESENTRY._serialized_end=249
  _STATVARMETADATA._serialized_start=251
  _STATVARMETADATA._serialized_end=345
  _RANKINGMETADATA._serialized_start=348
  _RANKINGMETADATA._serialized_end=478
  _HIGHLIGHTMETADATA._serialized_start=480
  _HIGHLIGHTMETADATA._serialized_end=520
  _TILE._serialized_start=523
  _TILE._serialized_end=891
  _TILE_TILETYPE._serialized_start=782
  _TILE_TILETYPE._serialized_end=891
  _BLOCK._serialized_start=894
  _BLOCK._serialized_end=1073
  _TOPICPAGECONFIG._serialized_start=1075
  _TOPICPAGECONFIG._serialized_end=1173
# @@protoc_insertion_point(module_scope)
