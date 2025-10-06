#!/usr/bin/env python
import os

from collections import defaultdict,deque

from flask import Flask,request, make_response,render_template,jsonify

app = Flask(__name__, static_url_path='/static')

class ReceiveData():
    def __init__(self,forHost,contents):
        self.forHost = forHost
        self.contents = contents


recv_data = defaultdict(deque)
order_queue = deque([])


@app.route('/nexttraffic')
def NextInterceptedHTTP():
    nextTrafficToDisplay =  CallNextTraffic()
    if nextTrafficToDisplay:
        return make_response(nextTrafficToDisplay)
    else:
        return make_response("No traffic captured currently!",418)



def CallNextTraffic():
    if len(order_queue) > 0:
        takeFirst = order_queue[0]
        if takeFirst in recv_data:
            if len(recv_data[takeFirst]) > 0:
                 displayData = recv_data[takeFirst].popleft()
                 if len(recv_data[takeFirst]) == 0:
                    recv_data.pop(takeFirst,None) # remove key from dictionary
                    order_queue.popleft()
                 return displayData

    return None 

@app.route('/')
def homepage():
    return render_template('base.html')
        

@app.route("/stream", methods=['POST'])
def stream():
    global recv_data
    rJson = request.get_json()
    recv_data[rJson['from']].append(rJson['capture'])

    if rJson['from'] not in order_queue:
        order_queue.append(rJson['from']) #Add to end of queue if thats the case


    return make_response("Success",200)

@app.route('/get-cookie/')
def get_cookie():
    username = request.cookies.get('somecookiename')
    retStr ='This is your cookie ' + username
    resp = make_response(retStr) 
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
