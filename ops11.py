#!/usr/local/bin/python3

# Author: Jansen Lefever
# Class: 301D2 Ops Challenge 6
# Purpose:

import os

# Create a new file if it does not exist
f = open("demofile.txt", "a")

f.write("Don't know about you, but Beeg Yoshi is a friend of mine.")
f.write("\nHe is the true messiah. ")
f.write("\nGet down with the thiccness")

f = open("demofile.txt", "r")
print(f.read(57))

os.remove("demofile.txt") 