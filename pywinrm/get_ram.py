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

    Here we can run a poweshell script on the remote machine as well

"""

# Simple script to retrieve the install RAM via the Guest OS
ps_script = """$strComputer = $Host
$RAM = WmiObject Win32_ComputerSystem
$MB = 1048576

"Installed Memory: " + [int]($RAM.TotalPhysicalMemory /$MB) + " MB" """

response = winrm_session.run_ps(ps_script)

# We decode the binary output and print it out here
print ('Here is the output of our powershell script!')
print (response.std_out.decode())

# If we had any errors we can access those via our response object as well as shown here
# print ('Ps Script: Errors')
# print (response.std_err.decode())
