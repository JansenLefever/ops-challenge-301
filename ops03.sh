#!/bin/bash

# Author: Jansen Lefever
# Class: 301D2 Ops Challenge 2
# Purpose: using chmod to change the permissions on a file

#list directories 
ls -al

#Askes user for input
echo "What Directory's permission would you like to change:"

#Creates variable 
read dir

#More input
echo "What chmod permissions would you like to input:"

#Another Var
read perm

#Excutes
chmod -R -v $perm $dir 

#End