#!/usr/bin/env python3
import sys

stop_words = ["the","is","and","in","to","of","a","for","on","with"]

for line in sys.stdin:
    for word in line.lower().strip().split():
        if word not in stop_words:
            print(word, "\t1")
