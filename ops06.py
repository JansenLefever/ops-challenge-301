#!/usr/bin/env python3

# Author: Jansen Lefever
# Class: 301D2 Ops Challenge 6
# Purpose: Using bash commands in python 3

# How to use Linux/Bash commands within Python
# First import the os library
import os



# Then use os.popen to call any kind of bash command
# Declare a variable
who = os.popen("whoami")
ip = os.popen("ip a")
info = os.popen("sudo lshw -short")

# Print to terminal

print("You are " + who.read())

print("Here is your IP address")
print(ip.read())

print("Here is you system info")
print(info.read())


# End
