#!/usr/bin/python3

"""
This module processes log entries from a web server.

It reads log lines from standard input, parses them, and calculates
statistics such as total file size and counts of HTTP status codes.
"""

import sys
import re


def print_msg(dict_sc, total_file_size):
    """
    Method to print the statistics.

    Args:
        dict_sc: dict of status codes
        total_file_size: total size of the files
    Returns:
        Nothing
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


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

try:
    for line in sys.stdin:
        # Regex to match the expected log format
        match = re.match(
            r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \['
            r'(.*?)\] "GET /projects/260 HTTP/1.1" '
            r'(\d{3}) (\d+)',
            line
        )

        if match:
            counter += 1

            # Extract status code and file size
            status_code = match.group(3)
            file_size = int(match.group(4))

            # Update total file size
            total_file_size += file_size

            # Update status code count
            if status_code in dict_sc:
                dict_sc[status_code] += 1

            # Print statistics every 10 lines
            if counter == 10:
                print_msg(dict_sc, total_file_size)
                # Reset the counter and statistics for the next batch
                counter = 0

finally:
    # Print any remaining statistics after processing all input
    print_msg(dict_sc, total_file_size)
