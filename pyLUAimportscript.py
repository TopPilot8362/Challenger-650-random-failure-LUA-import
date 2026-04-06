import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "FAIL:HYDRAULIC"
sock.sendto(message.encode(), ("127.0.0.1", 49000))
