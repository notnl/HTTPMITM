# Overview
A HTTP MITM barebones web interface tool based off a slight modification of sslstrip using Twisted Web framework for simulation purposes. 

See : https://github.com/moxie0/sslstrip/tree/master/sslstrip

Note that this will only work for intercepting the traffic to host localhost:8080 due to static DNS resolution set in code and also for security reasons. 

A Web interface served using Flask will be run at localhost:9090. 

The target web server is at localhost:8080.

# Details

The flask server uses 2 deque data structure to order requests based on client ip, then all of the captured traffic based on that client ip
will be displayed in order of which the response is received. 


# Building 
Ensure that the bash script is executable and Docker is installed
```
chmod u+x dockerquick.sh
```

To Build and run: 

```
./dockerquick.sh 2 

```

# USAGE 

Navigate to the target web server at localhost:8080 using your
own browser.

Open localhost:9090 to view intercepted traffic after pressing the
the next traffic button

Click the next traffic button to view intercepted traffic 1 by 1
