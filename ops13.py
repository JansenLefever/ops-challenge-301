#!/usr/local/bin/python3

# Author: Jansen Lefever
# Class: 301D2 Ops Challenge 13
# Purpose: Processes HTTP requests

import requests


site = str(input("Enter a website. Exsample: https://api.github.com:"))
print(site)
    
x = int(input('What HTTP request would you like to preform: 1)Get 2)Post 3)Put 4)Delete 5)Head 6)Patch 7)Options 8)Exit:'))
    
    
if x == 1:
    y = str(input("Are you sure? y/n: "))
    if y == 'y':
        response = requests.get(str(site))
        if response.status_code == 200:
            print('Success')
        elif response.status_code == 404:
            print('Site not found')
        else:
            print(response.status_code)
    else:
        print("exiting")
elif x == 2:
    y = str(input("Are you sure? y/n: "))
    if y == 'y':
        response = requests.post(str(site))
        if response.status_code == 200:
            print('Success')
        elif response.status_code == 404:
            print('Site not found')
        else:
            print(response.status_code)
    else:
        print("exiting")
elif x == 3:
    y = str(input("Are you sure? y/n: "))
    if y == 'y':
        response = requests.put(str(site))
        if response.status_code == 200:
            print('Success')
        elif response.status_code == 404:
            print('Site not found')
        else:
            print(response.status_code)
    else:
        print("exiting")
elif x == 4:
    y = str(input("Are you sure? y/n: "))
    if y == 'y':
        response = requests.delete(str(site))
        if response.status_code == 200:
            print('Success')
        elif response.status_code == 404:
            print('Site not found')
        else:
            print(response.status_code)
    else:
        print("exiting")
elif x == 5:
    y = str(input("Are you sure? y/n: "))
    if y == 'y':
        response = requests.head(str(site))
        if response.status_code == 200:
            print('Success')
        elif response.status_code == 404:
            print('Site not found')
        else:
            print(response.status_code)
    else:
        print("exiting")
elif x == 6:
    y = str(input("Are you sure? y/n: "))
    if y == 'y':
        response = requests.patch(str(site))
        if response.status_code == 200:
            print('Success')
        elif response.status_code == 404:
            print('Site not found')
        else:
            print(response.status_code)
    else:
        print("exiting")
elif x == 7:
    y = str(input("Are you sure? y/n: "))
    if y == 'y':
        response = requests.options(str(site))
        if response.status_code == 200:
            print('Success')
        elif response.status_code == 404:
            print('Site not found')
        else:
            print(response.status_code)
    else:
        print("exiting")
elif x == 8:
    print('Exiting Program')
else:
    print('incorrect input')


# https://www.w3schools.com/python/module_requests.asp