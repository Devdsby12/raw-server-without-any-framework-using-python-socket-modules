import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8000))
server_socket.listen()

requesttt = 0

while True:
    client_socket, address = server_socket.accept()

    request = client_socket.recv(1024)
    decoded = request.decode()

    print("\n------REQUEST------")
    print(decoded)

    first_line = decoded.split("\r\n")[0]
    print("FIRST LINE:", first_line)

    # handle favicon
    if "/favicon.ico" in first_line:
        response = (
            "HTTP/1.1 204 No Content\r\n"
            "Connection: close\r\n"
            "\r\n"
        ).encode()

        client_socket.send(response)
        client_socket.close()
        continue

    # normal request
    body = f"hello im under the water {requesttt}"

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        "Connection: close\r\n"
        f"Content-Length: {len(body)}\r\n"
        "\r\n"
        f"{body}"
    ).encode()

    client_socket.send(response)
    client_socket.close()

    requesttt += 1
