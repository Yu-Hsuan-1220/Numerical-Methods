import numpy as np

#Store the tridiagonal matrix in compact form
#n rows and 3 cols

n = 6
A = [[4, -1]] * n
B = [100, 200, 200, 200, 200, 100]
A = np.array(A, dtype=np.float32)
B = np.array(B, dtype=np.float32)

for i in range(1, n):
    tmp = A[i-1][1]/ A[i-1][0]
    A[i][0] = A[i][0] - A[i-1][1] * tmp
    B[i] = B[i] - B[i-1] * tmp

x = [0]*n
x[n-1] = B[n-1] / A[n-1][0]
for i in reversed(range(n-1)):
    x[i] = (B[i] - A[i][1]*x[i+1]) / A[i][0]

print(x)