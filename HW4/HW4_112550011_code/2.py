import numpy as np
import math

def f(x):
    return x + math.sin(x)/3

def f_prime(x):
    return 1 + math.cos(x)/3

def function_difference(x, y):
    n = len(x)
    coef = np.zeros((n, n))
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1])

    return coef

x = [0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
y = [f(i) for i in x]
coeff = function_difference(x, y)
np.set_printoptions(precision=5, suppress=True)
print(f"Divided differences coefficients:")
print(coeff)

target = 0.72
h = 0.2
min_error = float('inf')
best_approx = None
Used_idx = None
for i in range(len(x)-3):
    s = (target - x[i]) / h
    p = coeff[i][0] + coeff[i][1] * s + coeff[i][2] * s * (s - 1) / 2 + coeff[i][3] * s * (s - 1) * (s - 2) / 6
    p_prime = (coeff[i][1] + coeff[i][2] * (s + (s-1))/2 + coeff[i][3] * (s*(s-1) + (s-1)*(s-2) + s*(s-2))/6)/h
    error = abs(p_prime - f_prime(target))
    if error < min_error:
        min_error = error
        best_approx = p_prime
        Used_idx = i
print(f"Used x for approximation: {x[Used_idx]}, {x[Used_idx + 1]}, {x[Used_idx + 2]}")
print(f"Approximate value: {best_approx}, True value: {f_prime(target)}, Error: {abs(best_approx - f_prime(target))}")
print("--------------------------------------------------")

target = 1.33
h = 0.2
min_error = float('inf')
best_approx = None
Used_idx = None
for i in range(len(x)-2):
    s = (target - x[i]) / h
    p = coeff[i][0] + coeff[i][1] * s + coeff[i][2] * s * (s - 1) / 2
    p_prime = (coeff[i][1] + coeff[i][2] * (s + (s-1))/2)/h
    error = abs(p_prime - f_prime(target))
    if error < min_error:
        min_error = error
        best_approx = p_prime
        Used_idx = i

print(f"Used x for approximation: {x[Used_idx]}, {x[Used_idx + 1]}")
print(f"Approximate value: {best_approx}, True value: {f_prime(target)}, Error: {abs(best_approx - f_prime(target))}")
print("--------------------------------------------------")

target = 1.5
h = 0.2
min_error = float('inf')
best_approx = None
Used_idx = None
for i in range(len(x)-4):
    s = (target - x[i]) / h
    p = coeff[i][0] + coeff[i][1] * s + coeff[i][2] * s * (s - 1) / 2 + coeff[i][3] * s * (s - 1) * (s - 2) / 6 + coeff[i][4] * s * (s - 1) * (s - 2) * (s - 3) / 24
    p_prime = (coeff[i][1] + coeff[i][2] * (s + (s-1))/2 + coeff[i][3] * (s*(s-1) + (s-1)*(s-2) + s*(s-2))/6  + coeff[i][4] * (s*(s-1)*(s-2) + (s-1)*(s-2)*(s-3) + s*(s-2)*(s-3) + s*(s-1)*(s-3))/24)/h
    error = abs(p_prime - f_prime(target))
    if error < min_error:
        min_error = error
        best_approx = p_prime
        Used_idx = i

print(f"Used x for approximation: {x[Used_idx]}, {x[Used_idx + 1]}, {x[Used_idx + 2]}, {x[Used_idx + 3]}")
print(f"Approximate value: {best_approx}, True value: {f_prime(target)}, Error: {abs(best_approx - f_prime(target))}")