#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
line_count = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                      403: 0, 404: 0, 405: 0, 500: 0}


def print_stats():
    """Function to print the file size and status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def process_line(line):
    """Process a single log line and extract file size and status code."""
    global total_size, line_count

    # Split the line to extract status code and file size
    try:
        parts = line.split()
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Check if the status code is one we're tracking
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        # Add to the total file size
        total_size += file_size
        line_count += 1

    except (IndexError, ValueError):
        # Skip lines that don't match the required format
        pass


def signal_handler(sig, frame):
    """Handle CTRL + C signal to print the stats."""
    print_stats()
    sys.exit(0)


# Set up signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Read stdin line by line
try:
    for line in sys.stdin:
        process_line(line)

        # Print stats after every 10 lines
        if line_count % 10 == 0 and line_count > 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
