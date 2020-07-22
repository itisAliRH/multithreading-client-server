import socket, threading
from DB import receivedRequestsQueue, maxReceiveRequests
from handleReceive import handleReceive

def ListenServer():
    global maxReceiveRequests
    HOST = "0.0.0.0"
    PORT = 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    print("Server started")
    print("Waiting for client request..")
    while True:
        server.listen()
        clientsocket, clientAddress = server.accept()
        receivedMassage = clientsocket.recv(1024)
        maxReceiveRequests += 1
        if not (maxReceiveRequests < 4):
            print('Received and queued')
            receivedRequestsQueue.append((clientsocket, receivedMassage, clientAddress))
        else:
            print('Received and handled')
            handleRequestThread = threading.Thread(target=handleReceive, args=(clientsocket, receivedMassage, clientAddress))
            handleRequestThread.setDaemon(True)
            handleRequestThread.start()

if __name__ == "__main__":
    ListenServer()