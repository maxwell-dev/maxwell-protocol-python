import maxwell.protocol.maxwell_protocol_pb2 as maxwell_protocol_pb2


def encode_msg(msg):
    if msg.__class__ == maxwell_protocol_pb2.add_routes_rep_t:
        return (92).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.add_routes_req_t:
        return (91).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.assign_frontend_rep_t:
        return (112).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.assign_frontend_req_t:
        return (111).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.auth_rep_t:
        return (28).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.auth_req_t:
        return (27).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.error2_rep_t:
        return (32).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.error_rep_t:
        return (30).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.get_routes_rep_t:
        return (96).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.get_routes_req_t:
        return (95).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.locate_topic_rep_t:
        return (114).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.locate_topic_req_t:
        return (113).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.ok2_rep_t:
        return (31).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.ok_rep_t:
        return (29).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.ping_rep_t:
        return (2).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.ping_req_t:
        return (1).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.pull_rep_t:
        return (6).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.pull_req_t:
        return (5).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.push_rep_t:
        return (4).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.push_req_t:
        return (3).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.register_backend_rep_t:
        return (68).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.register_backend_req_t:
        return (67).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.register_frontend_rep_t:
        return (66).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.register_frontend_req_t:
        return (65).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.register_server_rep_t:
        return (70).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.register_server_req_t:
        return (69).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.req_rep_t:
        return (8).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.req_req_t:
        return (7).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.resolve_ip_rep_t:
        return (122).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.resolve_ip_req_t:
        return (121).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.route_added_msg_t:
        return (100).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.route_deleted_msg_t:
        return (101).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.route_status_changed_msg_t:
        return (102).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    else:
      raise TypeError(f"Unknown msg type: {msg.__class__}")


def decode_msg(encoded_msg):
    msg_type_uint32 = int.from_bytes(encoded_msg[:1], byteorder='little')
    if msg_type_uint32 == 92:
        msg = maxwell_protocol_pb2.add_routes_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 91:
        msg = maxwell_protocol_pb2.add_routes_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 112:
        msg = maxwell_protocol_pb2.assign_frontend_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 111:
        msg = maxwell_protocol_pb2.assign_frontend_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 28:
        msg = maxwell_protocol_pb2.auth_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 27:
        msg = maxwell_protocol_pb2.auth_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 32:
        msg = maxwell_protocol_pb2.error2_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 30:
        msg = maxwell_protocol_pb2.error_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 96:
        msg = maxwell_protocol_pb2.get_routes_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 95:
        msg = maxwell_protocol_pb2.get_routes_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 114:
        msg = maxwell_protocol_pb2.locate_topic_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 113:
        msg = maxwell_protocol_pb2.locate_topic_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 31:
        msg = maxwell_protocol_pb2.ok2_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 29:
        msg = maxwell_protocol_pb2.ok_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 2:
        msg = maxwell_protocol_pb2.ping_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 1:
        msg = maxwell_protocol_pb2.ping_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 6:
        msg = maxwell_protocol_pb2.pull_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 5:
        msg = maxwell_protocol_pb2.pull_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 4:
        msg = maxwell_protocol_pb2.push_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 3:
        msg = maxwell_protocol_pb2.push_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 68:
        msg = maxwell_protocol_pb2.register_backend_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 67:
        msg = maxwell_protocol_pb2.register_backend_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 66:
        msg = maxwell_protocol_pb2.register_frontend_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 65:
        msg = maxwell_protocol_pb2.register_frontend_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 70:
        msg = maxwell_protocol_pb2.register_server_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 69:
        msg = maxwell_protocol_pb2.register_server_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 8:
        msg = maxwell_protocol_pb2.req_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 7:
        msg = maxwell_protocol_pb2.req_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 122:
        msg = maxwell_protocol_pb2.resolve_ip_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 121:
        msg = maxwell_protocol_pb2.resolve_ip_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 100:
        msg = maxwell_protocol_pb2.route_added_msg_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 101:
        msg = maxwell_protocol_pb2.route_deleted_msg_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 102:
        msg = maxwell_protocol_pb2.route_status_changed_msg_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    else:
      raise TypeError(f"Unknown msg type: {msg_type_uint32}")
