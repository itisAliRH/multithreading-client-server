import sys, socket
from DB import allReceivedRequests, maxProccessReceivedRequests
from handleReceive import proccessMassagae

def handleQueuedTasks():
    global maxProccessReceivedRequests
    while True:
        if (maxProccessReceivedRequests < 6) and len(allReceivedRequests):
            request = None
            index = len(allReceivedRequests)//2*2 -1
            founded = False
            while index > -1 and (not founded):
                if allReceivedRequests[index] != None:
                    request = allReceivedRequests[index]
                    allReceivedRequests[index] = None
                    founded = True
                else:
                    index -= 2
            if request is None:
                if (len(allReceivedRequests) % 2) == 0:
                    index = len(allReceivedRequests) - 2
                else:
                    index = len(allReceivedRequests) - 1
                while index > -1 and (not founded):
                    if allReceivedRequests[index] != None:
                        request = allReceivedRequests[index]
                        allReceivedRequests[index] = None
                        founded = True
                    else:
                        index -= 2
            if request:
                maxProccessReceivedRequests -= 1
                newthread = proccessMassagae(request, index)
                newthread.setDaemon(True)
                newthread.start()

if __name__ == "__main__":
    handleQueuedTasks()