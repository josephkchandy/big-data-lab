#!/usr/bin/env python3
import sys

word = None
count = 0

for line in sys.stdin:
    key,val = line.strip().split("\t")
    val = int(val)

    if key == word:
        count += val
    else:
        if word:
            print(word,count)
        word = key
        count = val

if word:
    print(word,count)
