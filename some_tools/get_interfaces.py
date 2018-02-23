#!/usr/bin/env python

"""

    Some notes on working with REST APIs

"""

import requests
import json

request_method = "POST"
url = "http://192.168.49.10/ins"

headers = {"Content-type": "application/json"}
ssl_verify = False

username = "admin"
password = "!Passw0rd"

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

response = requests.request(request_method,                     #
                            url=url,
                            headers=headers,
                            verify=ssl_verify,
                            data=json.dumps(payload),
                            auth=(username, password))


my_interfaces = json.loads(response.content)


# Just the name
for interface in my_interfaces["ins_api"]["outputs"]["output"]["body"]["TABLE_interface"]["ROW_interface"]:
    print(interface["interface"])

# this one will crash if there are SVis
# for interface in my_interfaces["ins_api"]["outputs"]["output"]["body"]["TABLE_interface"]["ROW_interface"]:
#     print(interface["interface"], interface["state"])

# This one will work for both!
# for interface in my_interfaces["ins_api"]["outputs"]["output"]["body"]["TABLE_interface"]["ROW_interface"]:
#     if "state" in interface.keys():
#         print(interface["interface"], interface["state"])
#     if "svi_line_proto" in interface.keys():
#         print(interface["interface"], interface["svi_line_proto"])
#     else:
#         pass

# Lets grab the interfaces and their descriptions
# for interface in my_interfaces["ins_api"]["outputs"]["output"]["body"]["TABLE_interface"]["ROW_interface"]:
#     if "state" in interface.keys():
#         if interface["state"] == "up" and "desc" in interface.keys():
#             print(interface["interface"], interface["desc"])
#         if interface["state"] == "up":
#             print(interface["interface"])



# write some logic to get the MAC table and CDP hint

# Now we've printed out every interface. We can also use conditionals to look for specific interfaces
# In this example we'll just get interfaces that show as "up"

# This is commented out as it won't run if there's an SVI configured on the device
# print("Printing just the interfaces that are up:")
# for interface in my_interfaces["ins_api"]["outputs"]["output"]["body"]["TABLE_interface"]["ROW_interface"]:
#     if interface["state"] == "up":
#         print(interface["interface"])s
#
# # If you've got a VLAN then the above code may throw an exception because SVIs don't have a key called 'state'
# # The fix is simple, lets see if that key exists!
# print("Printing just the interfaces that are up:")
# for interface in my_interfaces["ins_api"]["outputs"]["output"]["body"]["TABLE_interface"]["ROW_interface"]:
#     if "state" in interface.keys():
#         if interface["state"] == "up":
#             print(interface["interface"])
#

#
#
# Now lets do something useful;
# display interfaces that are up but don't include a description
#
# Review conditionals! if X and else!
# We can do multiple conditionals if x and y!
#
# check for presence of the 'desc' key in each interface that happens to be up
# print the list/output and review
#
# Now lets go find out more data about our 'up' interfaces with missing descriptions:
# If we get an interface here lets extract the name and use that to go get the mac table entry for it
# show mac address-table interface eth1/2
# we're interested in disp_mac_addr and disp_vlan
#
# Now lets go get the CDP neighbors for it
# show cdp neighbors interface eth1/2
# here we're interseted in device_id, platform_id and port_id
#
# Tool to do the following:
# display all interfaces and descriptions
# display all interfaces that are up without a description
# display all interfaces that are up without a description with CAM and CDP information


#
# Now lets output to a CSV file so we can send this report to other people
#
# importing the csv library
#
# context managers! Use 'with open' to open a file for writing
# write the csv to disk with following fields
# interface_name, interface_state, interface_description, cdp_neighbor_device_id, cdp_neighbor_port_id
#
# open up a csv in excel and update the description enclosed in quotes
#
# now lets go write a tool to update interface descriptions based on the csv file
#
# Lets learn how to make a change 1 at a time first
# use API browser type expected command to update description
# Analyze code thats output

