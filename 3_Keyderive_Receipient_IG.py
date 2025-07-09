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
init_pubkey = '3059301306072a8648ce3d020106082a8648ce3d0301070342000404224888f32d3788827bda9808f7ae919d3959fc516408916dc09f1e4de08af84e9a7964c98f914ec4815d356287ef92b929191acba0fc16560848c8287d9b92'
# to perform key derivation
shared_info = '004e2e9edca6bb77bb2cf42e98eeba52fb7c22b1e8a275e5a0a70ddb314dbacd220703bccdfdcab38de8f572c12e3f3553cc68f3d3c20115c5a3e4d5d8d96e17'
shared_info_hex = '3030346532653965646361366262373762623263663432653938656562613532666237633232623165386132373565356130613730646462333134646261636432323037303362636364666463616233386465386635373263313265336633353533636336386633643363323031313563356133653464356438643936653137'
COMMAND = 'IG1103' + init_pubkey.decode('hex') + '03110610256' + shared_info_hex + ';01' + '00128D0A1B00S00;:%01'
# COMMAND = 'IG1103' + init_pubkey.decode('hex') + '03110610000' + ';01' + '00128D0A1B00S00;:%01'


# calculate the message length in byte and add to front of message string.
l = len(HEADER + COMMAND)
SIZE = pack('>h', l)

# Create message
# MESSAGE = SIZE + HEADER.encode() + COMMAND.encode()
MESSAGE = SIZE + HEADER + COMMAND

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
print("sent data  (HEX)  : ", MESSAGE.encode('hex'))

# Printing received data
print("received data: ", data)
print ("received data in HEX: ", data.encode('hex'))

input('Press Enter key to exit')  # stop the window from disappearing