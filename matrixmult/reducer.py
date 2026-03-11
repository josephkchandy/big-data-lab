#!/usr/bin/env python3
import sys

current_key = None
A = {}
B = {}

for line in sys.stdin:
    key, val = line.strip().split("\t")
    parts = val.split(",")

    if key != current_key:
        if current_key is not None:
            result = 0
            for k in A:
                if k in B:
                    result += A[k] * B[k]
            print(current_key, result)

        current_key = key
        A = {}
        B = {}

    if parts[0] == "A":
        A[int(parts[1])] = int(parts[2])
    else:
        B[int(parts[1])] = int(parts[2])

if current_key is not None:
    result = 0
    for k in A:
        if k in B:
            result += A[k] * B[k]
    print(current_key, result)
