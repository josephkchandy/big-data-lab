#!/usr/bin/env python3
import sys

current_key = None
values = []

for line in sys.stdin:
    key, val = line.strip().split("\t")

    if key == current_key:
        values.append(val)
    else:
        if current_key:
            result = 0
            for v in values:
                parts = v.strip("() ").split(",")
                result += int(parts[1])
            print(current_key, result)

        current_key = key
        values = [val]

if current_key:
    result = 0
    for v in values:
        parts = v.strip("() ").split(",")
        result += int(parts[1])
    print(current_key, result)
