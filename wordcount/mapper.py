#!/usr/bin/env python3
import sys

# keywords to search
keywords = ["hadoop", "mapreduce", "data"]

for line in sys.stdin:
    words = line.lower().split()

    for word in words:
        if word in keywords:
            print(f"{word}\t1")
