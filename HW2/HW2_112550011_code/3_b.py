import numpy as np


A = np.array([
    [4.63, -1.21, 3.22],
    [-3.07, 5.48, 2.11],
    [1.26, 3.11, 4.57]
])

b = np.array([2.22, -3.17, 5.11])
x = np.array([0.0, 0.0, 0.0])
tol = 1e-7
max_iterations = 1000



for iteration in range(max_iterations):
    ## I compute (L+D)^(-1) using forward subsitution
    x_old = x.copy()

    x[0] = (1 / A[0, 0]) * (b[0] - A[0, 1] * x[1] - A[0, 2] * x[2])
    x[1] = (1 / A[1, 1]) * (b[1] - A[1, 2] * x[2] - A[1, 0] * x[0])  ## x[0] is from k+1 iteration
    x[2] = (1 / A[2, 2]) * (b[2] - A[2, 0] * x[0] - A[2, 1] * x[1])  ## x[0], x[1] is from k+1 iteration
    
    if np.linalg.norm(x - x_old, ord = np.inf) < tol:
        print(f"Converge at {iteration + 1} iterations")
        break

print("Solution:", x)
