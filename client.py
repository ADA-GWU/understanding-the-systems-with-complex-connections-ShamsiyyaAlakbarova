import socket
import sys

s = socket.socket()

if len(sys.argv) != 2:
    print("Please, indicate port number: python client.py <port>")
    sys.exit(1)

try:
    port = int(sys.argv[1])
except ValueError:
    print("Invalid port number")
    sys.exit(1)

print(f'Socket created for port {port}')

server_address = ('127.0.0.1', port)

try:
    s.connect(server_address)
    print(f'Connected to server on port {port}')

    while True:
        number = input("Enter a number (or 'exit' to quit): ")

        if number.lower() == 'exit':
            break

        s.send(number.encode())

        result = s.recv(1024).decode()


except ConnectionRefusedError:
    print("Connection refused. Make sure the server is running.")
finally:
    s.close()
