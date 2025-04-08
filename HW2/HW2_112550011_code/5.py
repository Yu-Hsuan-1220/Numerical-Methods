import numpy as np

A = np.array([[1e10, 0], [0, 1e-10]])
B = np.array([[1e10, 0], [0, 1e10]])
C = np.array([[1e-10, 0], [0, 1e-10]])
D = np.array([[1, 2], [2, 4]])

A_cond = np.linalg.cond(A, p=1)
B_cond = np.linalg.cond(B, p=1)
C_cond = np.linalg.cond(C, p=1)
D_cond = np.linalg.cond(D, p=1)

print(f"A Condition number: {A_cond}")
print(f"A Condition number: {B_cond}")
print(f"A Condition number: {C_cond}")
print(f"A Condition number: {D_cond}")
