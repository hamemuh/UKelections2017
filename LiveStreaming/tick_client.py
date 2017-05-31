#
# Tick Data Client
#

import zmq
import datetime


context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://0.0.0.0:1777')



try:
    socket.setsockopt(zmq.SUBSCRIBE, b'') #python 2
except TypeError:
    socket.setsockopt_string(zmq.SUBSCRIBE, b'') # python 3

print'hi3'

while True:
    msg = socket.recv_string() #recieving message
    print '1'
    t=datetime.datetime.now() #time stamping the message
    #print'2'
    #sym, value = msg.split() #splitting the message
    #print'3'
    print str(t) + '|' + msg


