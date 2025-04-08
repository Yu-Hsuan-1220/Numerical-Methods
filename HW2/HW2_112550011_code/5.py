import numpy as np

A = np.array([[1e10, 0], [0, 1e-10]])
B = np.array([[1e10, 0], [0, 1e10]])
C = np.array([[1e-10, 0], [0, 1e-10]])
D = np.array([[1, 2], [2, 4]])

A_norm = np.linalg.norm(A, ord=np.inf)
B_norm = np.linalg.norm(B, ord=np.inf)
C_norm = np.linalg.norm(C, ord=np.inf)
#D_norm = np.linalg.norm(D, ord=np.inf)

A_inv = np.linalg.inv(A)
B_inv = np.linalg.inv(B)
C_inv = np.linalg.inv(C)
#D_inv = np.linalg.inv(D)

A_inv_norm = np.linalg.norm(A_inv, ord=np.inf)
B_inv_norm = np.linalg.norm(B_inv, ord=np.inf)
C_inv_norm = np.linalg.norm(C_inv, ord=np.inf)
#D_inv_norm = np.linalg.norm(D, ord=np.inf)

A_cond = A_norm * A_inv_norm
B_cond = B_norm * B_inv_norm
C_cond = C_norm * C_inv_norm
#D_cond = D_norm * D_inv_norm

print(f"A Condition number: {A_cond}")
print(f"B Condition number: {B_cond}")
print(f"C Condition number: {C_cond}")
print(f"D Condition number: {np.inf}")
