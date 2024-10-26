#!/usr/bin/python3
print("".join("{}".format(chr(c) if i % 2 == 0 else chr(c).upper())
for i, c in enumerate(range(ord('z'), ord('a') - 1, -1))), end="")
