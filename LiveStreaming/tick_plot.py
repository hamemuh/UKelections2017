#
# Tick Data Plot
#

import zmq
import datetime
import plotly.plotly as ply
from plotly.graph_objs import *
import plotly.tools as tls
import time
import numpy as np

tls.set_credentials_file(username='sammyjld', stream_ids=["g62is3r20y", "jzxk52kxy8", "4fpou4hf9l", "3bck8josn6", "diadm30ila", "knvcap2fze", "rilrlq5m3k", "gmj072mooy", "pmkzoy0fw7"], api_key='gVy8g51PwVY4vEsmX3RZ')
stream_ids = tls.get_credentials_file()['stream_ids']

# Socket
context =zmq.Context()
socket =context.socket(zmq.SUB)
socket.connect('tcp://0.0.0.0:1777')
try:
    socket.setsockopt(zmq.SUBSCRIBE, b'') # python 3
except TypeError:
    socket.setsockopt_string(zmq.SUBSCRIBE, b'') # python 2

# Plotly

s= Stream(token=stream_ids[0], maxpoints=100)
t= Scatter(x=[],y=[], name = "Labour", mode='lines+markers',line=dict(color = '#17BECF'),stream=s)
d= Data([t])
l= Layout( title = 'Tick Data Stream')
f= Figure(data = d, layout =l)
ply.iplot(f, filename ='Streaming test', auto_open=True)

st=ply.Stream(stream_ids[0])
st.open()


i= 0
k =5

time.sleep(5)

while True:
    msg = socket.recv_string() #recieving message
    t=datetime.datetime.now()#time stamping the message
    sym, value = msg.split() #splitting the message
    print(str(t) + '|' + msg)

    y = (np.cos(k * i / 50.) * np.cos(i / 50.) + np.random.randn(1))[0]
    st.write(dict(x=t, y=y))

    time.sleep(1)

st.close()

tls.embed('streaming-demos','12')
