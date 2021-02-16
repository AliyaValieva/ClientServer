#server
import socket
from pathlib import Path

def server():
    SERVER_ADDR = '127.0.0.1'
    PORT = 60000
    ADDR = (SERVER_ADDR,PORT)

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(ADDR)
    serverSocket.listen(10)

    while True:
        clientSocket, addr = serverSocket.accept()  # accept has a return value
        store = clientSocket.recv(1024)
        s = store.decode('utf-8')
        p = Path(s)

        if p.exists():
            with open(s,'r') as foo:
                f = foo.read(1024)
                while f: clientSocket.send(f.encode('utf-8')); f = foo.read(1024)
        else: fileNotFound = 'A file is not available on the server, please provide a file'; clientSocket.send (fileNotFound.encode('utf-8'));
        clientSocket.close()
        # user feedback that the conncetion was successful

            # check if that path exists
if __name__ == '__main__':
    server()
#
# print('I am the server')
# import socket
# # create an instance of the socket  obj
# serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # protocol, type
# host = socket.gethostname()
# # print(host)
# # sets my server IP address
# host_address = '000.0.0.0' #
# # sets a port value
# port = 8000
# #binds the host and the port to identify my connection
# serverSocket.bind((host_address, port)) # since it needs 1 argumnet and cannot be 1
#
# #call the listen func to allow connections come in
# serverSocket.listen(10) # 5 is number of cuncurrent connections to allow, cannot be 1
#
# while True:
#     #accept connections when they come in
#     clientSocket,addr = serverSocket.accept() # accept has a return value
#
#     #user feedback that the conncetion was successful
#     print('Got a new connection from: ', addr)
#     serverString = 'I am teh server you are conecting to.'
#     clientSocket.send(serverString.encode('utf-8')) # string unicode
