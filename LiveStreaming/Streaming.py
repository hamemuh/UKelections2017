#
# Tick Data Plot
#

import zmg
import datetime
import plotly.plotly as ply
from plotly.graph_objs import *
import plotly.tools as tls

stream_ids = tls.get_credentials_file()['stream_ids']