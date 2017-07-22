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
response = requests.request(request_method,                     #
                            url=url,
                            headers=headers,
                            verify=ssl_verify,
                            data=json.dumps(payload),
                            auth=(username, password))

# If we print the response we'll see an object and if we ask python what the type is it tells us that its
# a request response!
print("Our response object!:")
print(response)
print(type(response))

# Let's see what's inside of it:
print("Attribtues and methods within the object:")
print(dir(response))

# We see a list of attributes that we can access. These attributes are accessible via 'dot notation'
# For example if we want to see the actual content of our post we might do this:
print("The raw content:")
print(response.content)

# It looks kind of funky actually with lots of escape characters. Lets make this look a little cleaner with the json lib

print("Lets use the JSON library and load it up:")
print(json.loads(response.content))

# So what we've done here is load the response string in as a python dictionary.
# We could also do this:
print("Using the response.json() method:")
print(response.json())

# And if we wanted to prettyprint it json.dumps() includes a handy option 'indent' here we're having it indent 4 spaces
# Whenever we get to a new section
print("Pretty Printed JSON:")
print(json.dumps(response.json(), indent=4))

# That's much easier see what's going on.

# One nice thing about JSON is it closely mirrors the structure of a python dictionary
# This means we can access information using keys
# Here's a sample dictionary:

my_sample_dictionary = {"first_key" : "some value",
                        "second_key": "another value",
                        "third_key": "yet another value"}

# We access the value we want by it's key name. For example if I want to access the first key:
print("Printing first_key out of my_sample_dictionary:")
print(my_sample_dictionary["first_key"])

# We tell python which key to retrieve the value for by putting the name of the key we need inside of []'s

# We can get a list with the .keys() method on our dictionary
print("Printing the keys for my_sample_dictionary:")
print(my_sample_dictionary.keys())

# How does this help me deal with REST?
# We can use json.loads() to load JSON data into a python dictionary like so:
my_interfaces = json.loads(response.content)
print("Dictionary type is", type(my_interfaces))
# Now we have a dictionary with our API content in it

print("Printing the dictionary:")
print(my_interfaces)

# This dictionary is a lot more complex than the one we were working with earlier. We actually have fields inside of fields
# And even a list embedded in the dictionary. accessing these fields is pretty straightforward: just keep using the [] notation
print("Lets print the content of the input key so we can see the command we ran:")
print(my_interfaces["ins_api"]["outputs"]["output"]["input"])

# Here we get the contents of the ROW_interface field deep in the dictionary:
print("Here's the interfaces content")
print(my_interfaces["ins_api"]["outputs"]["output"]["body"]["TABLE_interface"]["ROW_interface"])

# So how could we extract just the name of the interface: We can use a for loop to iterate through this part of the dictionary
# we can tell because the content is all enclosed in []'s

for interface in my_interfaces["ins_api"]["outputs"]["output"]["body"]["TABLE_interface"]["ROW_interface"]:
    print(interface["interface"])

# Now we've printed out every interface. We can also use conditionals to look for specific interfaces
# In this example we'll just get interfaces that show as "up"

print("Printing just the interfaces that are up:")
for interface in my_interfaces["ins_api"]["outputs"]["output"]["body"]["TABLE_interface"]["ROW_interface"]:
    if interface["state"] == "up":
        print(interface["interface"])
