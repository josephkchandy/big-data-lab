#!/usr/bin/env python3
import sys

m = 10

for line in sys.stdin:
    for word in line.strip().split():
        h1 = sum(ord(c) for c in word) % m
        h2 = (sum(ord(c) for c in word) * 3) % m

        print(h1, "\t1")
        print(h2, "\t1")
