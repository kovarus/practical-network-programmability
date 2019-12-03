#!/usr/bin/env python

"""

   First, we need to import the appropriate libraries and create a login session with the vCenter server

"""

import requests
import json

# import local library
import manage_session

# Here we are disabling the warning about Insecure Requests as we are using a self-signed certificate so we will be disabling the SSL Verification
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Call get_session to get our session token 
session_token = manage_session.get_session()


# Since we're probably using a self signed certificate I'm going to go ahead and disable SSL verification.
# This will actually be used in our call below
ssl_verify = False


# The credentials to log into our device
username = "administrator@vsphere.local"
password = "!Passw0rd"

# The payload is empty in this case as the authentication used is all the session requires
payload = {} 

# we will be using GET for most of these calls because we are only retrieving data from our environment
request_method = "GET"

# we need to supply a header that contains the type of response we want back as well as our session id
headers = {"Content-type": "application/json", "vmware-api-session-id": session_token }

"""

    Let us do a guest os reboot now

"""

# this request will need to be a POST
request_method = "POST"

# set the vm to reboot
vm = 'vm-456'

# this is the url to retrieve all VM's
url = "https://10.64.5.21/rest/vcenter/vm/{}/guest/power?action=reboot".format(vm)

response = requests.request(request_method,                     #
                            url=url,
                            headers=headers,
                            verify=ssl_verify,
                            data=json.dumps(payload),
                            auth=(username, password))

# retrieve the json response
if (response.status_code == 200):
    print ('The vm ({}) has initiated a OS Reboot!'.format(vm))

"""

    For cleanup, we will delete our session

"""

# delete our session token
manage_session.delete_session(session_token)