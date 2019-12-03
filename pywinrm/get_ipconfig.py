#!/usr/bin/env python

"""

   First, we need to import the appropriate library which in our case is WinRM.
   More informatin about WinRM can be found here: https://pypi.org/project/pywinrm/ 

"""

import winrm
import json

# let us establish a variable for the computer we would like to connect to
vm = "10.64.10.94"

# The credentials to log into our computer
username = "Administrator"
password = "!Passw0rd"

# First we neeed a session

# https
# winrm_session = winrm.Session(vm, auth=(username, password), transport='ssl', server_cert_validation='ignore')

# http
winrm_session = winrm.Session(vm, auth=(username, password))

#winrm_session = winrm.Protocol(
#    endpoint='https://{}:5986/wsman'.format(vm),
#    transport='ntlm',
#    username=r'Administrator',
#    password=password,
#    server_cert_validation='ignore')

"""

    Here we can run a simple command and collect its output

"""

# Then we can simply run any command on that remote machine via the given session
# Our example below is a ipconfig/all command
response = winrm_session.run_cmd('ipconfig', ['/all'])

# We decode the binary output and print it out here
print ('Here is the output of our command!')
print (response.std_out.decode())

# If we had any errors we can access those via our response object as well as shown here
# print ('If any error is found, here is the output as well!')
# print (response.std_err.decode())