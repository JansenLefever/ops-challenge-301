#!/bin/bash

# Author: Jansen Lefever
# Class: 301D2 Ops Challenge 2
# Purpose: Clearing system files

#Prints out to the terminal system info

cat  /var/log/syslog 
cat /var/log/wtmp

#Askes user for input
echo
echo "Do you want to shred syslong and wtmp: yes or no"
read input

#Checks in input is what they want to do
if [ $input == yes ]; then

#Shreds logs
sudo shred -vfvu /var/log/syslog
sudo shred -vfvu /var/log/wtmp

#Shows what is left in the files
cat /var/log/syslog 
cat /var/log/wtmp

echo
echo "done"
fi

#End



