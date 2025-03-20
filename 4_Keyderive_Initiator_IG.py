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
rece_pubkey = '3059301306072a8648ce3d020106082a8648ce3d030107034200040d416ffa56a45b4e0e8c5d8b11d7972a311cb2a98c9d012b85ee1e32a3fe449177435a45fe7e3ea297b6860ca80e42c9110e34632003207a0ce6cd6976d6e0dd'
init_pvt_key = 'S1016003EX00E00011A0DA748546AD752D2E3BAB3531DEC814EAB77631AEEB314C19AF46B1F0A796F857F6BFEEC2AEDD4564C75D1884CA3D0FB453DC75BAA6608FC4D67A3837E4C5B4407E7CDE20317D8'
# to perform key derivation
shared_info = '004e2e9edca6bb77bb2cf42e98eeba52fb7c22b1e8a275e5a0a70ddb314dbacd220703bccdfdcab38de8f572c12e3f3553cc68f3d3c20115c5a3e4d5d8d96e17'
shared_info_hex = '3030346532653965646361366262373762623263663432653938656562613532666237633232623165386132373565356130613730646462333134646261636432323037303362636364666463616233386465386635373263313265336633353533636336386633643363323031313563356133653464356438643936653137'
# COMMAND = 'IG2103' + rece_pubkey.decode('hex') + init_pvt_key + '10610256' + shared_info_hex + ';0100128D0A1B00S00;:%01'
COMMAND = = 'IG2103' + rece_pubkey.decode('hex') + init_pvt_key + '10610256' + shared_info_hex + ';0100128D0A1B00S00;:%01'


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