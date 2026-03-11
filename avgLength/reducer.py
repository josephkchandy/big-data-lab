#!/usr/bin/env python3
import sys

total_length = 0
total_words = 0

for line in sys.stdin:
    key, val = line.strip().split("\t")
    key = int(key)
    val = int(val)

    total_length += key * val
    total_words += val

if total_words:
    print("Average Word Length =", total_length / total_words)
