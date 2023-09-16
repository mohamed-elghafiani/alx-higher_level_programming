#!/usr/bin/python3
"""Log Parsing"""
import sys
import re


def parse_log():
    i = 1
    code_n = {}
    size = 0
    for line in sys.stdin:
        filtered = [el.strip() for el in re.findall(" [0-9]+", line)]
        size += int(filtered[-1])

        if code_n.get(filtered[-2], 0):
            code_n[filtered[-2]] += 1
        else:
            code_n[filtered[-2]] = 1

        if i == 10:
            for (k, v) in sorted(code_n.items(), key=lambda item: item[0]):
                sys.stdout.write("{}: {}\n".format(k, v))
            sys.stdout.write("File size: {}\n".format(size))
            code_n = {}
            size = 0
            i = 0
        i += 1


parse_log()
