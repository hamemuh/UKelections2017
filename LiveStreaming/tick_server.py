#
# Tick Data Server
#

import zmq
import time
import random

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://0.0.0.0:1777')

AMZN =100.

while True:
    AMZN += random.gauss(0,1) * 0.5
    msg = 'AMZM %s' % AMZN
    #socket.send(str(msg))
    socket.send_string(msg)
    print(msg)
    time.sleep(random.random() *2)

