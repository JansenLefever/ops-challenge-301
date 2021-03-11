#!/bin/bash

num=0

while [ $num != 4 ]  
    do 

    echo "1) Hello World 2) Ping this computer 3) Ip info 4) Exit"
    read num

    if [ $num -eq 1 ]; then
    echo "Hello World"
    fi

    if [ $num -eq 2 ]; then
    ping -c 4 127.0.0.1
    fi

    if [ $num -eq 3 ]; then
    ip a
    fi
 
    if [ $num -eq 4 ]; then
    echo "Exit"
    fi

    if [ $num -gt 4 ]; then
    echo "incorrect input"
    fi
    
done