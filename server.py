from threading import Thread
from listenServer import ListenServer
from queuedTasks import handleQueuedTasks
from queuedReceived import handleReceivedQueue

# Server listen thread
listenThread = Thread(target=ListenServer)
listenThread.setDaemon(True)
listenThread.start()

# Queue added requests
queuedTasksThread = Thread(target=handleQueuedTasks)
queuedTasksThread.setDaemon(True)
queuedTasksThread.start()

# Queue received requests
queuedReceivedThread = Thread(target=handleReceivedQueue)
queuedReceivedThread.setDaemon(True)
queuedReceivedThread.start()

# Join thread for wait until the thread terminates.
listenThread.join()
queuedTasksThread.join()
queuedReceivedThread.join()
