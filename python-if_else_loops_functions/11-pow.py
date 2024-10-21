#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        result = 1 / a
        for _ in range(abs(b) - 1):
            result /= a
    else:
        result = 1
        for _ in range(b):
            result *= a
    return result
