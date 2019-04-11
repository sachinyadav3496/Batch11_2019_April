import socket #server side coding 
host,port = "127.0.0.1",12345 #server address
client = socket.socket()
print(f"Trying to Connect on SERVER {host}:{port}")
client.connect((host,port))
print("Yeah!! Got Connected to SERVER ")
while True :
	smsg = client.recv(1024).decode()
	print(f"Client-->{smsg}".rjust(100))	
	msg = input("server-->")
	client.send(msg.encode())
	if msg.upper().strip() == 'EOF' and smsg.upper().strip() == "EOF" :
		print("Connection Closed by Client")
		client.close()
		break 