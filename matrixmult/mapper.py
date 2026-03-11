#!/usr/bin/env python3
import sys

for line in sys.stdin:
    m, i, j, v = line.strip().split()
    i = int(i)
    j = int(j)
    v = int(v)

    if m == "A":
        for col in range(2):
            print(f"{i},{col}\tA,{j},{v}")
    else:
        for row in range(2):
            print(f"{row},{j}\tB,{i},{v}")
