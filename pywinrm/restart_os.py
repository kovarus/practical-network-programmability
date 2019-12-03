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
winrm_session = winrm.Session(vm, auth=(username, password), transport='ssl', server_cert_validation='ignore')

# http
# winrm_session = winrm.Session(vm, auth=(username, password))

"""

    Reboot the computer via Powershell using PyWinRM

"""

# Simple script to retrieve the install RAM via the Guest OS
ps_script = "Restart-Computer -Force"

response = winrm_session.run_ps(ps_script)

# We decode the binary output and print it out here
print ('The response from our command to reboot the computer!')
print (response.std_out.decode())

# If we had any errors we can access those via our response object as well as shown here
# print ('Ps Script: Errors')
# print (response.std_err.decode())