import base64
import socket
from struct import *

BUFFER_SIZE = 1024

# HSM Network Address - EDIT AS NEEDED
TCP_IP = '5.30.221.78'
TCP_PORT = 1500

# header & command to send - EDIT AS NEEDED
HEADER = 'HEAD'

# Create the commands here. Try examples below.
COMMAND = 'NC'

# calculate the message length in byte and add to front of message string.
l = len(HEADER + COMMAND)
SIZE = pack('>h', l)

# Create message
MESSAGE = SIZE + HEADER.encode() + COMMAND.encode()

# Create socket and connect
print("Connecting to HSM ... ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
try:
    s.connect((TCP_IP, TCP_PORT))
except Exception as e:
    print("Can't connect to {TCP_IP}")
    exit(0)

# send MESSAGE
s.send(MESSAGE)

# receive response
data = s.recv(BUFFER_SIZE)
s.close()

print("sent data    : ", MESSAGE)
# print("sent data  (HEX)  : ", MESSAGE.hex())

# Printing received data
print("received data: ", data)
# print("received data (HEX):", data.hex())

input('Press Enter key to exit')  # stop the window from disappearing