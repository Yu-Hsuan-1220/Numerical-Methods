import numpy as np

def gaussian_elimination_band(A, b, W):
    N = len(b)
    A = A.astype(float)
    b = b.astype(float)

    for i in range(N):
        pivot = A[i, i]
        if pivot == 0:
            raise ValueError("Zero pivot encountered!")
        for j in range(i+1, min(i + W + 1, N)):
            factor = A[j, i] / pivot
            A[j, i:min(i + W + 1, N)] -= factor * A[i, i:min(i + W + 1, N)]
            b[j] -= factor * b[i]

    x = np.zeros(N)
    for i in reversed(range(N)):
        x[i] = (b[i] - np.dot(A[i, i+1:min(i + W + 1, N)], x[i+1:min(i + W + 1, N)])) / A[i, i]
    
    return x

A = np.array([
    [4, -1, 0, 0, 0, 0],
    [-1, 4, -1, 0, 0, 0],
    [0, -1, 4, -1, 0, 0],
    [0, 0, -1, 4, -1, 0],
    [0, 0, 0, -1, 4, -1],
    [0, 0, 0, 0, -1, 4]
], dtype=float)

b = np.array([100, 200, 200, 200, 200, 100], dtype=float)
W = 1

x = gaussian_elimination_band(A, b, W)
print("Solution x =", x)