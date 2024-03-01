# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: maxwell_protocol.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16maxwell_protocol.proto\x12\x10maxwell.protocol\"\x19\n\nping_req_t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"\x19\n\nping_rep_t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"\x17\n\x08ok_rep_t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"6\n\x0b\x65rror_rep_t\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\x0b\n\x03ref\x18\x0f \x01(\r\">\n\tok2_rep_t\x12\x11\n\tconn0_ref\x18\r \x01(\r\x12\x11\n\tconn1_ref\x18\x0e \x01(\r\x12\x0b\n\x03ref\x18\x0f \x01(\r\"]\n\x0c\x65rror2_rep_t\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\x11\n\tconn0_ref\x18\r \x01(\r\x12\x11\n\tconn1_ref\x18\x0e \x01(\r\x12\x0b\n\x03ref\x18\x0f \x01(\r\"7\n\npush_req_t\x12\r\n\x05topic\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0b\n\x03ref\x18\x0f \x01(\r\"\x19\n\npush_rep_t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"m\n\npull_req_t\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\r\n\x05limit\x18\x03 \x01(\r\x12\x11\n\tconn0_ref\x18\r \x01(\r\x12\x11\n\tconn1_ref\x18\x0e \x01(\r\x12\x0b\n\x03ref\x18\x0f \x01(\r\"f\n\npull_rep_t\x12%\n\x04msgs\x18\x01 \x03(\x0b\x32\x17.maxwell.protocol.msg_t\x12\x11\n\tconn0_ref\x18\r \x01(\r\x12\x11\n\tconn1_ref\x18\x0e \x01(\r\x12\x0b\n\x03ref\x18\x0f \x01(\r\"\x89\x01\n\treq_req_t\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\t\x12*\n\x06header\x18\x0c \x01(\x0b\x32\x1a.maxwell.protocol.header_t\x12\x11\n\tconn0_ref\x18\r \x01(\r\x12\x11\n\tconn1_ref\x18\x0e \x01(\r\x12\x0b\n\x03ref\x18\x0f \x01(\r\"O\n\treq_rep_t\x12\x0f\n\x07payload\x18\x01 \x01(\t\x12\x11\n\tconn0_ref\x18\r \x01(\r\x12\x11\n\tconn1_ref\x18\x0e \x01(\r\x12\x0b\n\x03ref\x18\x0f \x01(\r\"N\n\nauth_req_t\x12\r\n\x05token\x18\x01 \x01(\t\x12\x11\n\tconn0_ref\x18\r \x01(\r\x12\x11\n\tconn1_ref\x18\x0e \x01(\r\x12\x0b\n\x03ref\x18\x0f \x01(\r\"?\n\nauth_rep_t\x12\x11\n\tconn0_ref\x18\r \x01(\r\x12\x11\n\tconn1_ref\x18\x0e \x01(\r\x12\x0b\n\x03ref\x18\x0f \x01(\r\"9\n\x17register_frontend_req_t\x12\x11\n\thttp_port\x18\x01 \x01(\r\x12\x0b\n\x03ref\x18\x0f \x01(\r\"&\n\x17register_frontend_rep_t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"8\n\x16register_backend_req_t\x12\x11\n\thttp_port\x18\x01 \x01(\r\x12\x0b\n\x03ref\x18\x0f \x01(\r\"%\n\x16register_backend_rep_t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"8\n\x16register_service_req_t\x12\x11\n\thttp_port\x18\x01 \x01(\r\x12\x0b\n\x03ref\x18\x0f \x01(\r\"%\n\x16register_service_rep_t\x12\x0b\n\x03ref\x18\x0f \x01(\r\".\n\x10set_routes_req_t\x12\r\n\x05paths\x18\x01 \x03(\t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"\x1f\n\x10set_routes_rep_t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"\x1f\n\x10get_routes_req_t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"V\n\x10get_routes_rep_t\x12\x35\n\x0croute_groups\x18\x01 \x03(\x0b\x32\x1f.maxwell.protocol.route_group_t\x12\x0b\n\x03ref\x18\x0f \x01(\r\",\n\x1dget_topic_dist_checksum_req_t\x12\x0b\n\x03ref\x18\x0f \x01(\r\">\n\x1dget_topic_dist_checksum_rep_t\x12\x10\n\x08\x63hecksum\x18\x01 \x01(\r\x12\x0b\n\x03ref\x18\x0f \x01(\r\",\n\x1dget_route_dist_checksum_req_t\x12\x0b\n\x03ref\x18\x0f \x01(\r\">\n\x1dget_route_dist_checksum_rep_t\x12\x10\n\x08\x63hecksum\x18\x01 \x01(\r\x12\x0b\n\x03ref\x18\x0f \x01(\r\"\"\n\x13pick_frontend_req_t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"4\n\x13pick_frontend_rep_t\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"#\n\x14pick_frontends_req_t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"6\n\x14pick_frontends_rep_t\x12\x11\n\tendpoints\x18\x01 \x03(\t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"0\n\x12locate_topic_req_t\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"3\n\x12locate_topic_rep_t\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"\x1f\n\x10resolve_ip_req_t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"+\n\x10resolve_ip_rep_t\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0b\n\x03ref\x18\x0f \x01(\r\"9\n\x05msg_t\x12\x0e\n\x06offset\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\":\n\x08header_t\x12\r\n\x05\x61gent\x18\x01 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\"U\n\rroute_group_t\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x19\n\x11healthy_endpoints\x18\x02 \x03(\t\x12\x1b\n\x13unhealthy_endpoints\x18\x03 \x03(\t*\xff\x05\n\nmsg_type_t\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08PING_REQ\x10\x01\x12\x0c\n\x08PING_REP\x10\x02\x12\n\n\x06OK_REP\x10\x1d\x12\r\n\tERROR_REP\x10\x1e\x12\x0b\n\x07OK2_REP\x10\x1f\x12\x0e\n\nERROR2_REP\x10 \x12\x0c\n\x08PUSH_REQ\x10!\x12\x0c\n\x08PUSH_REP\x10\"\x12\x0c\n\x08PULL_REQ\x10#\x12\x0c\n\x08PULL_REP\x10$\x12\x0b\n\x07REQ_REQ\x10\'\x12\x0b\n\x07REQ_REP\x10(\x12\x0c\n\x08\x41UTH_REQ\x10)\x12\x0c\n\x08\x41UTH_REP\x10*\x12\x19\n\x15REGISTER_FRONTEND_REQ\x10\x41\x12\x19\n\x15REGISTER_FRONTEND_REP\x10\x42\x12\x18\n\x14REGISTER_BACKEND_REQ\x10\x43\x12\x18\n\x14REGISTER_BACKEND_REP\x10\x44\x12\x18\n\x14REGISTER_SERVICE_REQ\x10\x45\x12\x18\n\x14REGISTER_SERVICE_REP\x10\x46\x12\x12\n\x0eSET_ROUTES_REQ\x10G\x12\x12\n\x0eSET_ROUTES_REP\x10H\x12\x12\n\x0eGET_ROUTES_REQ\x10K\x12\x12\n\x0eGET_ROUTES_REP\x10L\x12\x1f\n\x1bGET_TOPIC_DIST_CHECKSUM_REQ\x10M\x12\x1f\n\x1bGET_TOPIC_DIST_CHECKSUM_REP\x10N\x12\x1f\n\x1bGET_ROUTE_DIST_CHECKSUM_REQ\x10O\x12\x1f\n\x1bGET_ROUTE_DIST_CHECKSUM_REP\x10P\x12\x15\n\x11PICK_FRONTEND_REQ\x10Q\x12\x15\n\x11PICK_FRONTEND_REP\x10R\x12\x16\n\x12PICK_FRONTENDS_REQ\x10S\x12\x16\n\x12PICK_FRONTENDS_REP\x10T\x12\x14\n\x10LOCATE_TOPIC_REQ\x10U\x12\x14\n\x10LOCATE_TOPIC_REP\x10V\x12\x12\n\x0eRESOLVE_IP_REQ\x10y\x12\x12\n\x0eRESOLVE_IP_REP\x10z*\xde\x03\n\x0c\x65rror_code_t\x12\x06\n\x02OK\x10\x00\x12\x0f\n\x0bUNKNOWN_MSG\x10\x01\x12$\n NOT_ALLOWED_TO_REGISTER_FRONTEND\x10\x64\x12#\n\x1fNOT_ALLOWED_TO_REGISTER_BACKEND\x10\x65\x12#\n\x1fNOT_ALLOWED_TO_REGISTER_SERVICE\x10\x66\x12\x18\n\x14\x46\x41ILED_TO_SET_ROUTES\x10g\x12\x1b\n\x17\x46\x41ILED_TO_PICK_FRONTEND\x10h\x12\x1a\n\x16\x46\x41ILED_TO_LOCATE_TOPIC\x10i\x12\x11\n\x0cMASTER_ERROR\x10\xc7\x01\x12\x1e\n\x19\x46\x41ILED_TO_REQUEST_SERVICE\x10\xc8\x01\x12\x1e\n\x19\x46\x41ILED_TO_REQUEST_BACKEND\x10\xc9\x01\x12\x13\n\x0e\x46RONTEND_ERROR\x10\xab\x02\x12\x13\n\x0e\x46\x41ILED_TO_PUSH\x10\xac\x02\x12\x13\n\x0e\x46\x41ILED_TO_PULL\x10\xad\x02\x12\x12\n\rUNKNOWN_TOPIC\x10\xae\x02\x12\x12\n\rBACKEND_ERROR\x10\x8f\x03\x12\x11\n\x0cUNKNOWN_PATH\x10\x90\x03\x12\x12\n\rSERVICE_ERROR\x10\xf3\x03\x12\x11\n\x0c\x43LIENT_ERROR\x10\xd7\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'maxwell_protocol_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MSG_TYPE_T']._serialized_start=2289
  _globals['_MSG_TYPE_T']._serialized_end=3056
  _globals['_ERROR_CODE_T']._serialized_start=3059
  _globals['_ERROR_CODE_T']._serialized_end=3537
  _globals['_PING_REQ_T']._serialized_start=44
  _globals['_PING_REQ_T']._serialized_end=69
  _globals['_PING_REP_T']._serialized_start=71
  _globals['_PING_REP_T']._serialized_end=96
  _globals['_OK_REP_T']._serialized_start=98
  _globals['_OK_REP_T']._serialized_end=121
  _globals['_ERROR_REP_T']._serialized_start=123
  _globals['_ERROR_REP_T']._serialized_end=177
  _globals['_OK2_REP_T']._serialized_start=179
  _globals['_OK2_REP_T']._serialized_end=241
  _globals['_ERROR2_REP_T']._serialized_start=243
  _globals['_ERROR2_REP_T']._serialized_end=336
  _globals['_PUSH_REQ_T']._serialized_start=338
  _globals['_PUSH_REQ_T']._serialized_end=393
  _globals['_PUSH_REP_T']._serialized_start=395
  _globals['_PUSH_REP_T']._serialized_end=420
  _globals['_PULL_REQ_T']._serialized_start=422
  _globals['_PULL_REQ_T']._serialized_end=531
  _globals['_PULL_REP_T']._serialized_start=533
  _globals['_PULL_REP_T']._serialized_end=635
  _globals['_REQ_REQ_T']._serialized_start=638
  _globals['_REQ_REQ_T']._serialized_end=775
  _globals['_REQ_REP_T']._serialized_start=777
  _globals['_REQ_REP_T']._serialized_end=856
  _globals['_AUTH_REQ_T']._serialized_start=858
  _globals['_AUTH_REQ_T']._serialized_end=936
  _globals['_AUTH_REP_T']._serialized_start=938
  _globals['_AUTH_REP_T']._serialized_end=1001
  _globals['_REGISTER_FRONTEND_REQ_T']._serialized_start=1003
  _globals['_REGISTER_FRONTEND_REQ_T']._serialized_end=1060
  _globals['_REGISTER_FRONTEND_REP_T']._serialized_start=1062
  _globals['_REGISTER_FRONTEND_REP_T']._serialized_end=1100
  _globals['_REGISTER_BACKEND_REQ_T']._serialized_start=1102
  _globals['_REGISTER_BACKEND_REQ_T']._serialized_end=1158
  _globals['_REGISTER_BACKEND_REP_T']._serialized_start=1160
  _globals['_REGISTER_BACKEND_REP_T']._serialized_end=1197
  _globals['_REGISTER_SERVICE_REQ_T']._serialized_start=1199
  _globals['_REGISTER_SERVICE_REQ_T']._serialized_end=1255
  _globals['_REGISTER_SERVICE_REP_T']._serialized_start=1257
  _globals['_REGISTER_SERVICE_REP_T']._serialized_end=1294
  _globals['_SET_ROUTES_REQ_T']._serialized_start=1296
  _globals['_SET_ROUTES_REQ_T']._serialized_end=1342
  _globals['_SET_ROUTES_REP_T']._serialized_start=1344
  _globals['_SET_ROUTES_REP_T']._serialized_end=1375
  _globals['_GET_ROUTES_REQ_T']._serialized_start=1377
  _globals['_GET_ROUTES_REQ_T']._serialized_end=1408
  _globals['_GET_ROUTES_REP_T']._serialized_start=1410
  _globals['_GET_ROUTES_REP_T']._serialized_end=1496
  _globals['_GET_TOPIC_DIST_CHECKSUM_REQ_T']._serialized_start=1498
  _globals['_GET_TOPIC_DIST_CHECKSUM_REQ_T']._serialized_end=1542
  _globals['_GET_TOPIC_DIST_CHECKSUM_REP_T']._serialized_start=1544
  _globals['_GET_TOPIC_DIST_CHECKSUM_REP_T']._serialized_end=1606
  _globals['_GET_ROUTE_DIST_CHECKSUM_REQ_T']._serialized_start=1608
  _globals['_GET_ROUTE_DIST_CHECKSUM_REQ_T']._serialized_end=1652
  _globals['_GET_ROUTE_DIST_CHECKSUM_REP_T']._serialized_start=1654
  _globals['_GET_ROUTE_DIST_CHECKSUM_REP_T']._serialized_end=1716
  _globals['_PICK_FRONTEND_REQ_T']._serialized_start=1718
  _globals['_PICK_FRONTEND_REQ_T']._serialized_end=1752
  _globals['_PICK_FRONTEND_REP_T']._serialized_start=1754
  _globals['_PICK_FRONTEND_REP_T']._serialized_end=1806
  _globals['_PICK_FRONTENDS_REQ_T']._serialized_start=1808
  _globals['_PICK_FRONTENDS_REQ_T']._serialized_end=1843
  _globals['_PICK_FRONTENDS_REP_T']._serialized_start=1845
  _globals['_PICK_FRONTENDS_REP_T']._serialized_end=1899
  _globals['_LOCATE_TOPIC_REQ_T']._serialized_start=1901
  _globals['_LOCATE_TOPIC_REQ_T']._serialized_end=1949
  _globals['_LOCATE_TOPIC_REP_T']._serialized_start=1951
  _globals['_LOCATE_TOPIC_REP_T']._serialized_end=2002
  _globals['_RESOLVE_IP_REQ_T']._serialized_start=2004
  _globals['_RESOLVE_IP_REQ_T']._serialized_end=2035
  _globals['_RESOLVE_IP_REP_T']._serialized_start=2037
  _globals['_RESOLVE_IP_REP_T']._serialized_end=2080
  _globals['_MSG_T']._serialized_start=2082
  _globals['_MSG_T']._serialized_end=2139
  _globals['_HEADER_T']._serialized_start=2141
  _globals['_HEADER_T']._serialized_end=2199
  _globals['_ROUTE_GROUP_T']._serialized_start=2201
  _globals['_ROUTE_GROUP_T']._serialized_end=2286
# @@protoc_insertion_point(module_scope)
