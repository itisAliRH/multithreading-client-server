from DB import allReceivedRequests, usersRequests, requestId
from random import randint

def requestIdGenerator():
    global requestId
    requestId += 1

def validateRequest(clientsocket, receivedMassage, clientAddress):
    global allReceivedRequests, usersRequests, requestId
    valid = False
    user = usersRequests.get(clientAddress)
    if user is not None:
        if len(user["requests"]) < 5:
            requestIdGenerator()
            usersRequests[clientAddress]['requests'].append((requestId, receivedMassage))
            allReceivedRequests.append((requestId, receivedMassage))
            valid = True
        else:
            valid = False
            clientsocket.close()
    else:
        requestIdGenerator()
        usersRequests[clientAddress] = {'requests': [(requestId, receivedMassage)]}
        allReceivedRequests.append((requestId, receivedMassage))
        valid = True
    clientsocket.close()
    return valid
