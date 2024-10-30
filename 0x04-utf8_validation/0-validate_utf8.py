#!/usr/bin/python3
"""utf-8 encoding module"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding."""
    # Number of bytes remaining to complete the current character
    bytes_remaining = 0

    # Process each byte in the data list
    for byte in data:
        # Mask the byte to get only the 8 least significant bits
        byte = byte & 0xFF

        if bytes_remaining == 0:
            # Determine the number of bytes for the current character
            if (byte >> 7) == 0:  # 1-byte character (0xxxxxxx)
                continue
            elif (byte >> 5) == 0b110:  # 2-byte character (110xxxxx)
                bytes_remaining = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character (1110xxxx)
                bytes_remaining = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character (11110xxx)
                bytes_remaining = 3
            else:
                return False
        else:
            # Check if the byte is a valid continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            bytes_remaining -= 1

    # All characters must be complete (bytes_remaining should be zero)
    return bytes_remaining == 0
