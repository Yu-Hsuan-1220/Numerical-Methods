import numpy as np


A = np.array([[0.4, 0.7, 1],
     [1.2, 2.1, 1],
     [3.4, 4.0, 1],
     [4.1, 4.9, 1],
     [5.7, 6.3, 1],
     [7.2, 8.1, 1],
     [9.3, 8.9, 1],  
    ])

B = np.array([0.031, 0.933, 3.058, 3.349, 4.870, 5.757, 8.921])

# Find least squares solution

X = np.linalg.solve(A.T @ A, A.T @ B)
print(f"Least squares solution: {X}")
Z_fit = A @ X
Z_residuals = B - Z_fit
Z_residuals_sq = Z_residuals**2
Z_residuals_sq_sum = np.sum(Z_residuals_sq)
print(f"Z residuals squared sum: {Z_residuals_sq_sum}")