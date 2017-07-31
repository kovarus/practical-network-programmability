#!/usr/bin/env python

"""

    Here we'll go over creating functions and the concept of variable scope!

"""

import requests
import json

url='http://192.168.49.10/ins'
switchuser='admin'
switchpassword='!Passw0rd'




# Lets define a function! We'll take output from the API sandbox and turn it into a re-usable function here
# Defining a function is easy: def function_name(input_arguments):
# The input arguments are any bits of data you might need to execute the function. In this case we want to send
# in our username, password and the URL to access our device
def get_routes(switchuser, switchpassword, url):
    """
    Here's a function that takes in a common set of information, does one thing and then returns the result.

    :param switchuser: A string that contains the username to access the device
    :param switchpassword: A string that contains the password for the given username
    :param url: The URL to reach the NXAPI
    :return: A python dictionary containing the response from the NXAPI

    """

    # These variables are scoped locally to this function only. If you tried to access it outside of the function
    # then you would get an error!
    myheaders = {'content-type': 'application/json'}
    payload = {
      "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show ip route",
        "output_format": "json"
      }
    }

    # Just like before we'll go ahead and make our request. We'll just use the exact output from the API sandbox
    response = requests.post(url,
                             data=json.dumps(payload),
                             headers=myheaders,
                             auth=(switchuser, switchpassword)).json()

    # If we want this function to send out the results for use elsewhere then we have to return it
    return response

# Lets invoke our function and print the output:
print(get_routes(switchuser, switchpassword, url))

# Some notes on variable scope:

first_scope = "first"
second_scope = "second"
if first_scope == "first":
    inside_if_scope = "This is inside the first if statement"
    print(inside_if_scope)

if second_scope == "second":
    inside_if_scope = "This is inside the second if statement"
    print(inside_if_scope)

# If you remove this line:  "inside_if_scope = "This is inside the second if statement" the program will fail to run
# because inside_if_scope isn't declared.