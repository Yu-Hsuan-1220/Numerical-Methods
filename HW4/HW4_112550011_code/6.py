import numpy as np

# 3-point Gaussian quadrature constants
xi = np.array([-np.sqrt(3/5), 0.0, np.sqrt(3/5)])
wi = np.array([5/9, 8/9, 5/9])

def f_x(x):
    return np.exp(x)

def f_y(y):
    return np.sin(2*y)

def gaussian_quad_x(x):
    mul = 0.1/2 # (b-a)/2
    tmp_sum = 0 
    for i in range(3):
        tmp_sum += wi[i] * f_x(mul * xi[i] + (x + x + 0.1)/2)
    tmp_sum *= mul
    return tmp_sum    

def gaussian_quad_y(y):
    mul = 0.1/2 # (b-a)/2
    tmp_sum = 0
    for i in range(3):
        tmp_sum += wi[i] * f_y(mul * xi[i] + (y + y + 0.1)/2)
    tmp_sum *= mul
    return tmp_sum

# Integration domain and step
x_start, x_end = -0.2, 1.4
y_start, y_end = 0.4, 2.6
h = 0.1

x_total = 0
y_total = 0
x_vals = np.arange(x_start, x_end, h)
y_vals = np.arange(y_start, y_end, h)
for x in x_vals:
    x_total += gaussian_quad_x(x)
for y in y_vals:
    y_total += gaussian_quad_y(y)

print(x_total)
print(y_total)

total = x_total * y_total
print(f"Total integral: {total:.20f}")
