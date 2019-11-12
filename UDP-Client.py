import socket
t_host="127.0.0.1"
t_port=80
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(("Hello PSK").encode(),(t_host,t_port))
data, addr =client.recvfrom(4096)
print(data)