import maxwell.protocol.maxwell_protocol_pb2 as maxwell_protocol_pb2


def encode_msg(msg):
    if msg.__class__ == maxwell_protocol_pb2.add_route_msg_t:
        return (71).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.add_route_rep_t:
        return (68).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.add_route_req_t:
        return (67).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.auth_rep_t:
        return (28).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.auth_req_t:
        return (27).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.delete_route_msg_t:
        return (72).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.delete_route_rep_t:
        return (70).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.delete_route_req_t:
        return (69).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.delete_topics_rep_t:
        return (84).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.delete_topics_req_t:
        return (83).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.do2_rep_t:
        return (10).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.do2_req_t:
        return (9).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.do_rep_t:
        return (8).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.do_req_t:
        return (7).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.error2_rep_t:
        return (32).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.error_rep_t:
        return (30).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.ok2_rep_t:
        return (31).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.ok_rep_t:
        return (29).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.ping_rep_t:
        return (2).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.ping_req_t:
        return (1).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.pull_rep_t:
        return (4).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.pull_req_t:
        return (3).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.pull_routes_rep_t:
        return (76).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.pull_routes_req_t:
        return (75).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.push_rep_t:
        return (6).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.push_req_t:
        return (5).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.push_routes_rep_t:
        return (74).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.push_routes_req_t:
        return (73).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.register_backend_rep_t:
        return (82).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.register_backend_req_t:
        return (81).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.register_frontend_rep_t:
        return (66).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.register_frontend_req_t:
        return (65).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.resolve_backend_rep_t:
        return (100).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.resolve_backend_req_t:
        return (99).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.resolve_frontend_rep_t:
        return (98).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.resolve_frontend_req_t:
        return (97).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.resolve_ip_rep_t:
        return (122).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.resolve_ip_req_t:
        return (121).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.unwatch_rep_t:
        return (108).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.unwatch_req_t:
        return (107).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.watch_rep_t:
        return (106).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    elif msg.__class__ == maxwell_protocol_pb2.watch_req_t:
        return (105).to_bytes(1, 'little', signed=False) + msg.SerializeToString()
    else:
      raise TypeError(f"Unknown msg type: {msg.__class__}")


def decode_msg(encoded_msg):
    msg_type_uint32 = int.from_bytes(encoded_msg[:1], byteorder='little')
    if msg_type_uint32 == 71:
        msg = maxwell_protocol_pb2.add_route_msg_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 68:
        msg = maxwell_protocol_pb2.add_route_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 67:
        msg = maxwell_protocol_pb2.add_route_req_t()
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
    elif msg_type_uint32 == 72:
        msg = maxwell_protocol_pb2.delete_route_msg_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 70:
        msg = maxwell_protocol_pb2.delete_route_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 69:
        msg = maxwell_protocol_pb2.delete_route_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 84:
        msg = maxwell_protocol_pb2.delete_topics_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 83:
        msg = maxwell_protocol_pb2.delete_topics_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 10:
        msg = maxwell_protocol_pb2.do2_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 9:
        msg = maxwell_protocol_pb2.do2_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 8:
        msg = maxwell_protocol_pb2.do_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 7:
        msg = maxwell_protocol_pb2.do_req_t()
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
    elif msg_type_uint32 == 4:
        msg = maxwell_protocol_pb2.pull_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 3:
        msg = maxwell_protocol_pb2.pull_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 76:
        msg = maxwell_protocol_pb2.pull_routes_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 75:
        msg = maxwell_protocol_pb2.pull_routes_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 6:
        msg = maxwell_protocol_pb2.push_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 5:
        msg = maxwell_protocol_pb2.push_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 74:
        msg = maxwell_protocol_pb2.push_routes_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 73:
        msg = maxwell_protocol_pb2.push_routes_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 82:
        msg = maxwell_protocol_pb2.register_backend_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 81:
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
    elif msg_type_uint32 == 100:
        msg = maxwell_protocol_pb2.resolve_backend_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 99:
        msg = maxwell_protocol_pb2.resolve_backend_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 98:
        msg = maxwell_protocol_pb2.resolve_frontend_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 97:
        msg = maxwell_protocol_pb2.resolve_frontend_req_t()
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
    elif msg_type_uint32 == 108:
        msg = maxwell_protocol_pb2.unwatch_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 107:
        msg = maxwell_protocol_pb2.unwatch_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 106:
        msg = maxwell_protocol_pb2.watch_rep_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    elif msg_type_uint32 == 105:
        msg = maxwell_protocol_pb2.watch_req_t()
        msg.ParseFromString(encoded_msg[1:])
        return msg
    else:
      raise TypeError(f"Unknown msg type: {msg_type_uint32}")
