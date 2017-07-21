#!/usr/bin/env python

"""

    Some notes on working with REST APIs

"""

# First things first lets import our requests library to make it nice and easy
import requests
import json

# If you don't have it installed then just 'pip install requests'

# Now lets define some variables. We can just change these up as we need to
# Everything we do in NXAPI is going to be a POST operation
request_method = "POST"

# Lets define the URL we actually want to send the data to:
url = "http://192.168.49.10/ins"

# We need to set some headers so the API knows what we're sending it and how it should respond to us
headers = {"Content-type": "application/json"}

# Since we're probably using a self signed certificate I'm going to go ahead and disable SSL verification.
# This will actually be used in our call below
ssl_verify = False

# The credentials to log into our device
username = "admin"
password = "!Passw0rd"


# This is the thing we actually POST to make the device do something.
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show interface ",
        "output_format": "json"
    }
}

# Now we'll make the request and we'll store the results in a variable called 'request'
# This is now an object that's going to have a lot of attributes associated with it
response = requests.request(request_method,
                            url=url,
                            headers=headers,
                            verify=ssl_verify,
                            data=json.dumps(payload),
                            auth=(username, password)).json()

print(response)
print("#" * 80)
print(json.dumps(response, indent=4))
