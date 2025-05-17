import numpy as np
import math

def f(x):
    return 1/(x**2)

last = float('inf')

h = 1 - 0.2
while True:
    sum = 0
    cur = 0.2
    while cur + h <= 1:
        sum += (f(cur) + f(cur + h)) * h / 2
        cur += h
    if abs(cur-1) > 1e-3:
        sum += (f(cur) + f(1)) * (1 - cur) / 2
       
    if abs(sum - last) < 0.02:
        print(f"Approximate value: {sum}, h = {h}, Error between two iterations: {abs(sum - last)}")
        break
    
    last = sum
    h /= 2