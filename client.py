"""import socket

s = socket.socket()
print('Socket created')

port = 9001
s.connect(('127.0.0.1', port))

while True:
    # Get a number from the user
    number = input("Enter a number (or 'exit' to quit): ")
    
    if number.lower() == 'exit':
        break

    # Send the number to the server
    s.send(number.encode())

s.close()
"""

import socket
import sys

s = socket.socket()

if len(sys.argv) != 2:
    print("Usage: python client.py <port>")
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
except KeyboardInterrupt:
    print("Client is closing.")
finally:
    s.close()
