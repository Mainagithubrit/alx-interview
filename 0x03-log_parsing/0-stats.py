#!/usr/bin/python3
import sys
import re


# initializing counters
total_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Prits the current statistics"""
    print("File size: {}".format(total_size))
    for status in sorted(status_count):
        if status_count[status] > 0:
            print("{}: {}".format(status, status_count[status]))


try:
    for line in sys.stdin:
        line_count += 1

        # Regular expression to match the expected log format
        match = re.match(
            r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \['
            r'(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)', line
        )

        if match:
            # Extract status code and file size
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            # update counters
            total_size += file_size
            if status_code in status_count:
                status_count[status_code] += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()


except KeyboardInterrupt:
    print_stats()
