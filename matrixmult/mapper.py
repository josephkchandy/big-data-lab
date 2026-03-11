#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.strip().split()

    matrix = parts[0]
    i = int(parts[1])
    j = int(parts[2])
    value = int(parts[3])

    if matrix == "A":
        print((i, j), "\t", ("A", value))
    else:
        print((i, j), "\t", ("B", value))
