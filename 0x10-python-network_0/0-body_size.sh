#!/usr/bin/env bash
curl -Is $1 | grep -oP 'Content-Length: \K\d+'
