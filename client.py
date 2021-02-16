# client
import socket

from pathlib import Path
'''You will create 2 new files with the following details:

--- Client Module ---

The client will prompt the user for a text file ".txt" that it wants to receive and the directory where that file is located 
(the full path including the filename as a single user-input is acceptable)
Using the user input, the client will request a copy of the file from the server
The client will wait for the file transfer from the server
The client will store the file in a folder called "Client Folder", which is to be created in the same directory as the ".py" files

--- Server Module ---
The server will accept incoming connections from a client
The server will take a filename and directory from the client and send the data over to the client requesting the file
Other Considerations:
The server code will stay running so that you can keep re-running the client for another file request
You should handle the case that a file is not available on the server; let the client know and the client will let the user know
Do not assume a minimum sized file (be able to handle large text files)'''

''' client knows where the file is located
 the serevr will read str data from txt and send to client

 keep the server running
 client has to create '''
def client():

    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    fp = Path('client_folder')
    fp.mkdir()

    SERVER_ADDR = '127.0.0.1'
    PORT = 60000
    ADDR = (SERVER_ADDR,PORT)
    fileN = input('Please provide a path to teh file ')


    clientSocket.connect(ADDR)
    clientSocket.send(fileN.encode('utf-8'))
    fp = Path('client_folder')
    if not fp.exists():
        fp.mkdir()
    fileName = 'client_folder/result.txt'
    with open(fileName, 'w+') as f:
        while True:
            dataComing = clientSocket.recv(1024)
            if not dataComing:
                break
            data = dataComing.decode('utf-8')
            f.write(data)
    clientSocket.close()
if __name__ == '__main__':
    client()

    # clientSocket.send('file name:',fileName )
    # you drop the txt file in p and then the SERVER should SEND it to client Folder
#     for f in p:
#         with open(fileName,'r') as f:
#             f.read()
#             clientSocket.send(f,decode('utf-8'))
#
#
#     clientsocket.send(serveString, decode('Utf-8'))
#     print('Successfully get the file')
#     s.close()
#     print('connection closed')
# print(dataComing.decode('utf-8'))

#
# def client_program():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((HOST, PORT))
#         data = s.recv(1024)
#         while True:
#             info = sock.recv(1024)
#             data += info
#             if len(info) == 0:
#                 break
#
#     print("Connection from: " + str(conn))
#     user_input = input("Enter the directory of test csv file")
#     input_path = Path(user_input)
#
#     with open(filename, "wb") as f:
#
#     results_path = input_path / 'result'
#     results_path.mkdir(exist_ok=True)
#     if results_path.exists() == True:
#         Clientpath = results_path / 'Client_Folder.py'
#
#     clientsocket.send(serveString, encode('Utf-8')
#     print('Successfully get the file')
#     s.close()
#     print('connection closed')
#
#
#
# print('I am the client')
# import socket
# clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # protocol, type
#
# # define a server address
# serverAddress = '000.0.0.0' # '000.0.0.0
# # just to see whta info is currently set
# host = socket.gethostname()
# client_ip = socket.gethostbyname(host)
# print(client_ip)
# port = 8000
# #
# clientSocket.connect((serverAddress,port))
# dataComing = clientSocket.recv(1024) # buffer size-the max amount of data
# print(dataComing.decode('utf-8')) # doesnt automatically decode it
