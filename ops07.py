#!/usr/local/bin/python3

# Author: Jansen Lefever
# Class: 301D2 Ops Challenge 7
# Purpose: Walking down a file tree


import os

### Read user input here into a variable

file_path = input("Enter a file path: ")

### Declare a function here

def walk(): 
  for (root, dirs, files) in os.walk(file_path, topdown=True):
    ### Add a print command here to print ==root==
    print(root)
    ### Add a print command here to print ==dirs==
    print(dirs)
    ### Add a print command here to print ==files==
    print(files)

walk()



# How to read input (refer to https://www.w3schools.com/python/python_user_input.asp)

# https://www.geeksforgeeks.org/os-walk-python/