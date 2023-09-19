#!/usr/bin/python3
"""Log Parsing Module"""
import sys
import signal


total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def signal_handler(signal, frame):
    """handle KeyboardInterrupt"""
    print_stats()
    sys.exit(0)

def print_stats():
    """print_stats"""
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_code_counts):
        if status_code_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_code_counts[status_code]))

signal.signal(signal.SIGINT, signal_handler)

line_count = 0

for line in sys.stdin:
    line_count += 1
    parts = line.split()
    if len(parts) >= 7:
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

    if line_count % 10 == 0:
        print_stats()

