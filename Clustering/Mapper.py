# mapper.py
#!/usr/bin/env python3
import sys
from math import sqrt

centroids = [(2,2),(8,8)]

for line in sys.stdin:
    x, y = map(float, line.strip().split(","))

    d0 = sqrt((x-centroids[0][0])**2 + (y-centroids[0][1])**2)
    d1 = sqrt((x-centroids[1][0])**2 + (y-centroids[1][1])**2)

    if d0 < d1:
        print(f"0\t{x},{y}")
    else:
        print(f"1\t{x},{y}")
