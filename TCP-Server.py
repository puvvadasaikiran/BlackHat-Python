import socket
import threading
b_ip="0.0.0.0"
b_port=8888
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((b_ip,b_port))
server.listen(5)
print(" [*] Listening on",(b_ip),":",(b_port))

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(" [*] Received:",(request))
    client_socket.send(("ACK!").encode())
    client_socket.close()


while True:
    client,addr = server.accept()
    print("[*] Accepted Connnection from ",(addr[0],addr[1]))ler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()