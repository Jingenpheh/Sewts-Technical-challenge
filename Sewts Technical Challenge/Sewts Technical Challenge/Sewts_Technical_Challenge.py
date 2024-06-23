# TCP/IP Client through python

# Importing relevant libraries
import socket
import sys
import time

# Declaring Global Variables
host = '192.168.1.199'
port = 2010
msg = 1     

print('Building Client ....')

# Creating Socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = (host,port)

print('Connecting to ' + str(host) + ' at port ' + str(port) + ' ...')
sock.connect (server_address)
# Get connection confirmation
data = sock.recv(9)
print(data)

# Predefined condition for stopping communication : counter = 100
counter = 0
# Timer to trigger communication every 100ms
st = time.time()

while(counter < 100):
       
    if (time.time() - st) * 1000 >= 100:
        # Send predefined msg
        print('sending *' + str(msg) + '* ...')
        sock.sendall(bytes(msg))

        # Look for the response
        data = sock.recv(100)
        print('received *' + str(data) + '* ')

        # Update timer and counter
        st = time.time()
        counter += 1
        
# End communication
print('End of communication')
sock.close
