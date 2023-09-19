#!/usr/bin/python3
import sys
import signal

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Function to handle KeyboardInterrupt (CTRL+C)
def signal_handler(signal, frame):
    print_stats()
    sys.exit(0)

# Function to print statistics
def print_stats():
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_code_counts):
        if status_code_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_code_counts[status_code]))

# Register the signal handler for KeyboardInterrupt
signal.signal(signal.SIGINT, signal_handler)

line_count = 0

# Read input line by line
for line in sys.stdin:
    line_count += 1
    parts = line.split()
    if len(parts) >= 7:
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

    # Check if 10 lines have been processed
    if line_count % 10 == 0:
        print_stats()

