#!/bin/bash
# cURL - Display body of only 200 status code reponse
status=$(curl -Is $1 | grep -oP 'HTTP/\d\.\d \K\d+')
if [ $status -eq 200 ]; then
	curl  $1
fi
