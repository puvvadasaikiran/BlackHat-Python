import socket
t_host="127.0.0.1"
t_port=8888
client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((t_host,t_port))
client.send(("GET / HTTP/1.1\r\nHost: vegaauto.com\r\n\r\n").encode())
response=client.recv(4096)
print(response.decode())