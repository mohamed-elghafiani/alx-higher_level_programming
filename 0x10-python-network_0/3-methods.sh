#!/bin/bash
# cURL - methods
curl -sI "$1" | awk '/Allow/ {print $2}'
