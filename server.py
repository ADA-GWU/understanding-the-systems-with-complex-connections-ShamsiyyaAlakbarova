import socket

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
    
    # Receive the number from the client
    number = c.recv(1024).decode()
    print('Received number:', number)
    
    # Double the number
    result = str(int(number) * 2)
    
    # Send the result back to the client
    c.send(result.encode())
    
    c.close()
