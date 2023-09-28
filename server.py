"""import socket

s = socket.socket()
print('Socket created')

port = 9001
s.bind(('', port))
print(f'Socket bound to port {port}')

s.listen(3)
print('Socket is listening')

while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    while True:
        number = c.recv(1024).decode()

        if not number:
            break
        
        # Double the number
        result = str(int(number) * 2)

        print('Result from server:', result)

        c.send(result.encode())

    c.close()"""

import socket

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

# Create sockets and bind them to specific ports
ports = [9001, 9002, 9003]
sockets = []

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port))
    s.listen(5)  # You can adjust the backlog queue size as needed
    sockets.append(s)
    print(f'Socket bound to port {port}')

print('Server is listening on multiple ports')

while True:
    for i, s in enumerate(sockets):
        c, addr = s.accept()
        print(f'Got connection on port {ports[i]} from', addr)
        handle_client(c)



    





