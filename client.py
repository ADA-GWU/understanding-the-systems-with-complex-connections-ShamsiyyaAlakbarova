import socket

s = socket.socket()
port = 9001
s.connect(('127.0.0.1', port))

# Get a number from the user
number = input("Enter a number: ")

# Send the number to the server
s.send(number.encode())

s.close()
