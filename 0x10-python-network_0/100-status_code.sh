#!/bin/bash
# curl - dispaly status code only
curl -sI "$1" | grep -Po 'HTTP/\d\.\d \K\d+'
