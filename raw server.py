import socket

creating_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket file description created and     CREATING_SOCKET pointing to it 

""" What happens

Python asks the OS to create a socket object in kernel memory.

AF_INET → use IPv4 networking.

SOCK_STREAM → use TCP protocol.

Now inside the kernel something like this exists:

socket structure
protocol: TCP
state: CLOSED

Your program only holds a file descriptor number pointing to that kernel socket."""

creating_socket.bind(("0.0.0.0" ,8000)) # binding socket to 8000 port
creating_socket.listen(5)  # socket starts listening 
print("server is listing")
while True: # keep listing stays alive
    client_socket ,address = creating_socket.accept() # socket accepts request from anywhere on internet
    print("clinet connected with ",address)
    request = client_socket.recv(1024).decode()   # it receives the client request content such as headers body etc
    print("browser send \n",request)
    body = "hello im under the water"
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        f"Content-Length: {len(body)}\r\n"
        "\r\n"
        f"{body}"
    ).encode()
    client_socket.send(response)   # it sends response data to client 
    client_socket.close()

