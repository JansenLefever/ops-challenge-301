#!/bin/bash

# Author: Jansen Lefever
# Class: 301D2 Ops Challenge 2
# Purpose: Clearing system files

#Prints out to the terminal system info

cat  /var/log/syslog 
cat /var/log/wtmp

input=0

#Askes user for input
while [ $input != 4 ] 
    do

    echo
    echo "What would you like to do with the Syslog and wtmp 1) Truncate 2) Shred 3) Print Syslog and wtmp 4) Exit"
    read input

    if [ $input -eq 1 ]; then
    sudo truncate -s 0 /var/log/syslog 
    sudo truncate -s 0 /var/log/wtmp
    fi
#Checks in input is what they want to do
    if [ $input -eq 2 ]; then

    #Shreds logs
    sudo shred -vfvu /var/log/syslog
    sudo shred -vfvu /var/log/wtmp
    fi

    #Shows what is left in the files
    if [ $input -eq 3 ]; then
    cat /var/log/syslog 
    cat /var/log/wtmp
    fi

    echo
    echo "done"
    echo
done

#End