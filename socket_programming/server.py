import socket #server side coding 
host,port = "192.168.1.108",12345 #server address
server = socket.socket()
server.bind((host,port))
server.listen()
print(f"SERVER is Listining on {host}:{port}")
client_socket,client_addr = server.accept()
print("Yeah!! Got Connection From {}:{}".format(*client_addr))
while True : 
	msg = input("server-->")
	client_socket.send(msg.encode())
	cmsg = client_socket.recv(1024).decode()
	print(f"Client-->{cmsg}".rjust(100))
	if msg.upper().strip() == 'EOF' and cmsg.upper().strip() == "EOF" :
		print("Connection Closed by Server")
		client_socket.close()
		server.close()
		break 