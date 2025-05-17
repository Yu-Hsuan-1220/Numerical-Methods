import numpy as np
import math

def f(x):
    return 1 + math.log10(x)

def f_prime(x):
    return 1 / (x * math.log(10))

x_vals = [0.15, 0.21, 0.23, 0.27, 0.32, 0.35]
n = len(x_vals)
y_vals = [f(x) for x in x_vals]

# Calculate the divided differences
def divided_difference(x, y):
    n = len(x)
    coef = np.zeros((n, n))
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    return coef

# value for 𝑓′(0.268) from a quadratic interpolating polynomial
def apporximate_value(idx, x0):
    return coeff[idx][1] + coeff[idx][2] * ((x0 - x_vals[idx]) + (x0 - x_vals[idx + 1]))

coeff = divided_difference(x_vals, y_vals)
print(f"Divided differences coefficients: {coeff}")


Ture_value = f_prime(0.268)
min_error = float('inf')
best_approx = None
Used_idx = None
for i in range(n-2):
    x0 = 0.268
    approx_value = apporximate_value(i, x0)
    error = abs(approx_value - Ture_value)
    if error < min_error:
        min_error = error
        best_approx = approx_value
        Used_idx = i

print(f"Used x for approximation: {x_vals[Used_idx]}, {x_vals[Used_idx + 1]}, {x_vals[Used_idx + 2]}")
print(f"Best approximate value: {best_approx}, True value: {Ture_value}, Error: {min_error}")
