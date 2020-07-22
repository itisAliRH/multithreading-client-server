import sys, socket
from threading import Thread
from validateRequests import validateRequest
from DB import maxReceiveRequests, maxProccessReceivedRequests

def handleReceive(clientsocket, receivedMassage, clientAddress):
    global maxReceiveRequests
    response = validateRequest(clientsocket, receivedMassage, clientAddress)
    if response:
        print(f"Message received for handling from {clientAddress[0]} on port {clientAddress[1]}: {receivedMassage.decode()}")
    else:
        print("Limit exceeded!")
    maxReceiveRequests -= 1
    sys.exit(0)

class proccessMassagae(Thread):
    def __init__(self,request, index):
        Thread.__init__(self)
        self.index = index
        self.clientAddress, self.clientsocket = request
    def run(self):
        global maxProccessReceivedRequests
        maxProccessReceivedRequests -= 1
        print(f"Proccess data from request number {self.index} to `{self.clientsocket.decode()}`")
        sys.exit(0)
