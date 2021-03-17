#!/usr/local/bin/python3

# Author: Jansen Lefever
# Class: 301D2 Ops Challenge 12
# Purpose:

import psutil

print(psutil.cpu_times(),file=open("output.txt", "a"))


#https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file

#https://psutil.readthedocs.io/en/latest/#system-related-functions