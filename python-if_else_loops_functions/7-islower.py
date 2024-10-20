#!/usr/bin/env python3
def islower(c):
    # Get the ASCII value of the character and check if it's between 97 and 122 (inclusive)
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
