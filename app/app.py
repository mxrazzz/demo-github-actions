from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)
@app.route('/') # when we are on the / page, it runs this function
def home():
    hostname = socket.gethostname() # get the hostname of the machine e.g. meraz
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #get current time and date into string
    response =  { # prints the response as json 
        "status": "Application is running v2", 
        "hostname": hostname,
        "timestamp": timestamp
    }
    return jsonify(response)

if __name__ == "__main__": #if u run it as python app.y, it runs this file as main, else if u do import app, u need "__name__"
    app.run(host='0.0.0.0', port=5000, debug=True) # runs the app on all interfaces on port 5000 with debug mode on