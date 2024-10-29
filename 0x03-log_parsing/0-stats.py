#!/usr/bin/python3

"""
This module processes log entries from a web server.

It reads log lines from standard input, parses them, and calculates
statistics such as total file size and counts of HTTP status codes.
"""


import sys
import re
from signal import signal, SIGINT


def print_msg(dict_sc, total_file_size):
    """
    Prints the statistics.

    Args:
        dict_sc: dict of status codes
        total_file_size: total size of the files
    """
    print("File size: {}".format(total_file_size))
    for key in sorted(dict_sc.keys()):
        if dict_sc[key] > 0:
            print("{}: {}".format(key, dict_sc[key]))


# Initialize counters
total_file_size = 0
counter = 0
dict_sc = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

# Define the pattern for matching log lines
log_pattern = re.compile(
    r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \['
    r'(.*?)\] "GET /projects/260 HTTP/1.1" '
    r'(\d{3}) (\d+)$'
)


# Signal handler for CTRL + C
def handle_interrupt(signal_received, frame):
    print_msg(dict_sc, total_file_size)
    sys.exit(0)


# Register the signal handler
signal(SIGINT, handle_interrupt)


try:
    for line in sys.stdin:
        # Try to match the line with the pattern
        match = log_pattern.match(line.strip())
        if match:
            counter += 1

            # Extract status code and file size
            status_code = match.group(3)
            file_size = int(match.group(4))

            # Update the total file size
            total_file_size += file_size

            # Update the status code count if it's in our list
            if status_code in dict_sc:
                dict_sc[status_code] += 1

            # Print statistics every 10 lines
            if counter == 10:
                print_msg(dict_sc, total_file_size)
                counter = 0

finally:
    # Print any remaining statistics after processing all input
    print_msg(dict_sc, total_file_size)
