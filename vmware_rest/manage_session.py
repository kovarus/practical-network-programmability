#!/usr/bin/env python

"""

   First, we need to import the appropriate libraries and create a login session with the vCenter server

"""

import requests
import json

# Here we are disabling the warning about Insecure Requests as we are using a self-signed certificate so we will be disabling the SSL Verification
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_session():
    # The method we will use through most of the examples here is a GET, however we start with POST as explained later on below
    request_method = "POST"

    # Lets define the URL we need to create our session
    url = "https://10.64.5.21/rest/com/vmware/cis/session"

    # for the session call we need to build out a new set of headers
    headers = {"Content-type": "application/json", "vmware-use-header-authn": None, "vmware-api-session-id": None}

    # Since we're probably using a self signed certificate I'm going to go ahead and disable SSL verification.
    # This will actually be used in our call below
    ssl_verify = False

    # The credentials to log into our device
    username = "administrator@vsphere.local"
    password = "!Passw0rd"

    # The payload is empty in this case as the authentication used is all the session requires
    payload = {} 

    # Now we'll make the request and we'll store the results in a variable called 'request'
    # This is now an object that's going to have a lot of attributes associated with it
    response = requests.request(request_method,                     #
                                url=url,
                                headers=headers,
                                verify=ssl_verify,
                                data=json.dumps(payload),
                                auth=(username, password))

    # retrieve the json response
    json_response = response.json()

    # then we retrieve the token from response
    session_token = json_response["value"]

    # As you can see here, we can print out our response and then store the session identifier for later use
    print("Here is our session token!")
    print(session_token)

    return session_token


#!/usr/bin/env python

"""

   First, we need to import the appropriate libraries and create a login session with the vCenter server

"""

import requests
import json

# Here we are disabling the warning about Insecure Requests as we are using a self-signed certificate so we will be disabling the SSL Verification
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def delete_session(session_token):
    """

        For cleanup, we will delete our session

    """
    # Since we're probably using a self signed certificate I'm going to go ahead and disable SSL verification.
    # This will actually be used in our call below
    ssl_verify = False

    # The credentials to log into our device
    username = "administrator@vsphere.local"
    password = "!Passw0rd"

    # The payload is empty in this case as the authentication used is all the session requires
    payload = {} 

    # We will use the DELETE verb to indicate our intentions here
    request_method = "DELETE"

    # The same url used to create our session
    url = "https://10.64.5.21/rest/com/vmware/cis/session"

    # for the session call we need to build out a new set of headers
    headers = {"Content-type": "application/json", "vmware-use-header-authn": None, "vmware-api-session-id": session_token}

    response = requests.request(request_method,                     #
                                url=url,
                                headers=headers,
                                verify=ssl_verify,
                                data=json.dumps(payload),
                                auth=(username, password))

    if (response.status_code == 200):
        print ('The session was terminated!')
        return True
    else:
        return False