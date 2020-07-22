import sys, socket
from threading import Thread
from DB import receivedRequestsQueue, maxReceiveRequests
from handleReceive import handleReceive

def handleReceivedQueue():
    global maxReceiveRequests
    while True:
        if (maxReceiveRequests < 4) and len(receivedRequestsQueue):
            queuedRequest = None
            index = len(receivedRequestsQueue)//2*2 - 1
            founded = False
            while index > -1 and (not founded):
                if receivedRequestsQueue[index] != None:
                    queuedRequest = receivedRequestsQueue[index]
                    receivedRequestsQueue[index] = None
                    founded = True
                index -= 2
            if queuedRequest is None:
                if (len(receivedRequestsQueue) % 2) == 0:
                    index = len(receivedRequestsQueue) - 2
                else:
                    index = len(receivedRequestsQueue) - 1
                founded = False
                while index > -1 and (not founded):
                    if receivedRequestsQueue[index] != None:
                        queuedRequest = receivedRequestsQueue[index]
                        receivedRequestsQueue[index] = None
                        founded = True
                    index -= 2
            if queuedRequest:
                print('Restore from queue and handle')
                handleRequestThread = Thread(target=handleReceive, args=(queuedRequest))
                handleRequestThread.start()

if __name__ == "__main__":
    handleReceivedQueue()