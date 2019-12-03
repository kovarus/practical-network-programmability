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

# https
winrm_session = winrm.Session(vm, auth=(username, password), transport='ssl', server_cert_validation='ignore')

# http
# winrm_session = winrm.Session(vm, auth=(username, password))

"""

    Here we can run a poweshell script on the remote machine as well to pull information on the system

"""

# Simple script to retrieve the install RAM via the Guest OS
ps_script = """
$Info = WmiObject Win32_ComputerSystem

Write-Host ($Info | ConvertTo-Json) 
"""

response = winrm_session.run_ps(ps_script)

# Since we know the output will be in JSON format, we can consume it as such
response_json = json.loads(response.std_out.decode())

# We decode the binary output and print it out here
print ('Here is the output of our powershell script!')
print (json.dumps(response_json, indent=4, sort_keys=True))

# An alternative output would be something like this
CIM_System_Roles = [x['Value'] for x in response_json['Properties'] if x['Name'] == "Roles"]
print (json.dumps(CIM_System_Roles, indent=4, sort_keys=True))

# If we had any errors we can access those via our response object as well as shown here
# print ('Ps Script: Errors')
# print (response.std_err.decode())
