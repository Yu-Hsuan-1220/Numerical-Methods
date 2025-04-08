import numpy as np


A = np.array([
    [4.63, -1.21, 3.22],
    [-3.07, 5.48, 2.11],
    [1.26, 3.11, 4.57]
])

b = np.array([2.22, -3.17, 5.11])
x = np.array([0.0, 0.0, 0.0])
tol = 1e-7
max_iterations = 100

def find_val(factor):
    x = np.array([0.0, 0.0, 0.0]) ## reset x
    for iteration in range(max_iterations):
        
        x_old = x.copy()

        x[0] = (1 / A[0, 0]) * (b[0] - A[0, 1] * x[1] - A[0, 2] * x[2])
        dist = x[0]-x_old[0]
        x[0] = x_old[0] + factor * dist
        x[1] = (1 / A[1, 1]) * (b[1] - A[1, 2] * x[2] - A[1, 0] * x[0])
        dist = x[1]-x_old[1]
        x[1] = x_old[1] + factor * dist  
        x[2] = (1 / A[2, 2]) * (b[2] - A[2, 0] * x[0] - A[2, 1] * x[1])  
        dist = x[2]-x_old[2]
        x[2] = x_old[2] + factor * dist

        # sum = 0
        # for i in range(3):
        #     sum = abs(x_old[i] - x[i])
        # if sum < tol:
        #     return iteration
        if np.linalg.norm(x - x_old, ord = np.inf) < tol:
            return iteration
    return 100
min_iter = 100
base = 1
best_factor = -1
factor = 1
for i in range(100):
    tmp = find_val(factor)
    print(f"Factor:{factor:.2f}   Iterations : {tmp}")
    if tmp < min_iter:
        min_iter = tmp
        best_factor = factor
    factor += 0.01
print('------------------------------------------------')
print(f"Best factor:{best_factor:.2f}, iterations:{min_iter}")