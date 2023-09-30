import socket
import sys

def handle_client(client_socket):
    while True:
        number = client_socket.recv(1024).decode()

        if not number:
            break

        # Double the number
        result = str(int(number) * 2)

        print('Result from client:', result)

        client_socket.send(result.encode())

    client_socket.close()

def main():
    if len(sys.argv) != 2:
        print("Please, indicate port number: python server.py <port>")
        sys.exit(1)

    try:
        port = int(sys.argv[1])
    except ValueError:
        print("Invalid port number")
        sys.exit(1)

    print(f'Socket created for port {port}')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port))
    s.listen(3)  # You can adjust the backlog queue size as needed

    print(f'Server is listening on port {port}')

    while True:
        c, addr = s.accept()
        print(f'Got connection from', addr)
        handle_client(c)

if __name__ == "__main__":
    main()
