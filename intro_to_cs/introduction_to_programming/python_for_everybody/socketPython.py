import socket

# creating a socket
# socket.AF_INET = through internet socket
# socket.SOCK_STREAM = gettings stream of characters one at a time (not blocks of text)
mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# calling a method socket.
# try to connect to host and the port.
mySocket.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mySocket.send(cmd)

while True:
    data = mySocket.recv(512)
    if len(data) <1:
        break
    print(data.decode())
mySocket.close()