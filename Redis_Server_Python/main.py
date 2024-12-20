import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    #server_socket.accept() # wait for client
    # client, addr = server_socket.accept()
    # client.send(b"+PONG\r\n")
    # client, addr = server_socket.accept()
    # client.send(b"+PONG\r\n")
    while True:
        client, addr = server_socket.accept()
        with client:
            while client.recv(8000):
                client.send(b"+PONG\r\n")


if __name__ == "__main__":
    main()
