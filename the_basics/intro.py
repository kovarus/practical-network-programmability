#!/usr/bin/env python
#^^^^^^^^^^
# The line above is called a shebang and it's basically a way of telling your command shell what interpreter to use
# to run this script!
"""

    Some basic stuff about Python! Feel free to use this as notes/a reference as you go through the rest of this stuff
    I'm using Python 3.6 here but most of this should also work with python 2


"""

# Lets start with dynamic types!

my_string = "Some content here!"

# Strings are basically freeform text
# You can do all sorts of things with strings like concatenate them or slice them up or modify them

# Here's some strings below that store a 'text' version of numbers and we're concatenating them together with a +:

x = "1"
y = "1"
z = x + y

# What do you think below would output?
print(z)

# If you guessed 11 then you're right

# What if declare x and y without quotes?

x = 1
y = 1

# Now these are actually 'ints' so when we add them:

z = x + y

# We should get 2!

print(z)

# Python is nice because you can make it human readable so you can figure out what your code is actually doing
# feel free to use descriptive variable names for example:

dmz_router = "10.32.11.19"

# Spacing is also important! It's how we scope code blocks

my_fancy_string = "Fancy!"

def my_fancy_function(my_fancy_string):
    print(my_fancy_string)

# If I don't indent the print statement above then python won't realize that its part of the my_fancy_function() function

# Use spaces not tabs! See Python's PEP8 https://www.python.org/dev/peps/pep-0008/
# This makes your code consistent with the rest of the community
# Your text editor should be able to take tabs and convert them to spaces

# Sometimes we need to have a list of multiple things:

my_routers = ["10.1.0.2", "10.1.0.3", "192.168.1.100", "172.16.35.254"]

# This is called a list! You can tell it's a list because it's contents are surrounded by []'s
# We can do many things with lists, let's count the number of routers in it:

how_many = len(my_routers)
print(f"There are: {how_many} lights! I mean routers")

# What if we wanted to do something to each of those routers?
# We would do a for loop!

for router in my_routers:
    print(router)

# Printing routers doesn't seem so useful right now but you could have a function to backup a configuration for example


# Next we'll get into working with REST APIs