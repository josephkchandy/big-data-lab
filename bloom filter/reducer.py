#!/usr/bin/env python3
import sys

size = 10
bits = [0]*size

for line in sys.stdin:
    key, val = line.strip().split("\t")
    key = int(key)
    bits[key] = 1

print("Bloom Filter:", bits)
