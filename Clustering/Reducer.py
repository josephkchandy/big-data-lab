# reducer.py
#!/usr/bin/env python3
import sys

cluster = None
sumx = 0
sumy = 0
count = 0

for line in sys.stdin:
    key, val = line.strip().split("\t")
    x, y = map(float, val.split(","))

    if key == cluster:
        sumx += x
        sumy += y
        count += 1
    else:
        if cluster is not None:
            print(cluster, sumx/count, sumy/count)

        cluster = key
        sumx = x
        sumy = y
        count = 1

if cluster is not None:
    print(cluster, sumx/count, sumy/count)
