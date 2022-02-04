#! /bin/bash
#update os
yum update -y
#install apache server
yum install -y httpd
# get date and time of server
DATE_TIME=`date`
# create a custom index.html file
echo "<html>