#!/bin/bash

# Author: Jansen Lefever
# Class: 301D2 Ops Challenge 2
# Purpose: Create syslog file with current date.

#Varibles
year=`date +%Y`
month=`date +%m`
day=`date +%d`
hour=`date +%H`
minute=`date +%M`
second=`date +%S`
echo `date`
echo "Current Date: $day-$month-$year"
echo "Current Time: $hour:$minute:$second"

date_time=$day-$month-$year-$hour:$minute:$second

# Append to txt file

cat /var/log/syslog >> $date_time.txt

#End