# Setting up TCPIP Server

# Importing relevant libraries
import socket
import sys
import time

# Declaring Global Variables
host = '127.0.0.1'
port = 2010 
msg = 1
bit0 = 0b0

print('Building server ....')

# Creating Socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = (host,port)
print('Connecting to ' + str(host) + ' at port ' + str(port) + ' ...')
# Waiting for connection
sock.bind((host, port))
sock.listen(1)

conn, addr = sock.accept()

print('Connection address:', addr)
conn.send(b'connected')
print('Start communication: ')

# st = Timer to trigger communication every 100ms; tt = Timer to toggle bit0 every 500ms
st = time.time()
tt = st

while(1):
    
    if (time.time() - st) * 1000 >= 100:
        
        # Look for the response
        data = conn.recv(4)
        if not data: break
        print('received *' + str(data) + '* ')

        # Attempt to toggle Bit 0 but currently not used
        if (time.time() - tt) * 1000 >= 500:
            bit0 = not bit0
            tt = time.time()

        # Send data
        print('sending *' + str(msg) + '* ...')
        conn.sendall(bytes(msg))

        # Update timer and counter
        st = time.time()

        

print('End of communication')
sock.close()
