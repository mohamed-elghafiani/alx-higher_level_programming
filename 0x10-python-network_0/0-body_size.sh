#!/usr/bin/env bash
# cURL body size
curl -Is $1 | grep -oP 'Content-Length: \K\d+'
