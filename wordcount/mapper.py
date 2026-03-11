#!/usr/bin/env python3
import sys

keywords = ["hadoop","mapreduce","data"]

for line in sys.stdin:
    for word in line.lower().split():
        if word in keywords:
            print(word,"\t1")
