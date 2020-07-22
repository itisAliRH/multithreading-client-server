import socket
from random import randint

# Server Address
SERVER = "0.0.0.0"

# Server port
PORT = 8080

# Number of messages to send
n = 20

for k in range(n):
  # Init socket
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  # Init connection
  client.connect((SERVER, PORT))

  # Generate 4 digits random number
  rand = randint(1000, 9999)

  # Send message to server
  client.sendall(bytes("This is from Client " + str(rand),'UTF-8'))

  # Close connection
  client.close()
