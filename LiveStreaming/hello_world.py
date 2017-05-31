#
# Flask Hello World
#

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<iframe width ="750px" height = "550px" src= https://plot.ly/~sammyjld/21/tick-data-stream/ ><iframe>'

if __name__ == '__main__':
    app.run(port=27017, debug=True)





