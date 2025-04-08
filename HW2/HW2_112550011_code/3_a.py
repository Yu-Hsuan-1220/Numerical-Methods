import numpy as np

A = np.array([
    [4.63, -1.21, 3.22],
    [-3.07, 5.48, 2.11],
    [1.26, 3.11, 4.57]
])

b = np.array([2.22, -3.17, 5.11])

x_old = np.array([0.0, 0.0, 0.0])

tol = 1e-7
max_iterations = 1000

for iteration in range(max_iterations):
    x_new = np.zeros((3))
    
    x_new[0] = (1 / A[0, 0]) * (b[0] - A[0, 1] * x_old[1] - A[0, 2] * x_old[2])
    x_new[1] = (1 / A[1, 1]) * (b[1] - A[1, 0] * x_old[0] - A[1, 2] * x_old[2])
    x_new[2] = (1 / A[2, 2]) * (b[2] - A[2, 0] * x_old[0] - A[2, 1] * x_old[1])
    
    if np.linalg.norm(x_new- x_old, ord = np.inf) < tol:
        print(f"Converge at {iteration} iteration")
        break

    x_old = x_new

print("Solution:", x_new)
