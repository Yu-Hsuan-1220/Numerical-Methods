import numpy as np
import matplotlib.pyplot as plt


def f(x):
    if -1 <= x < -0.5:
        return 0
    if -0.5 <= x < 0.5:
        return 1 - abs(2*x)
    if 0.5 <= x <= 1:
        return 0



def compute_segment_coeffs(x_nodes, y_nodes, S):
    n = len(x_nodes)
    a, b, c, d = [], [], [], []
    for i in range(n - 1):
        h_i = x_nodes[i+1] - x_nodes[i]
        a.append((S[i+1] - S[i]) / (6 * h_i))
        b.append(S[i] / 2)
        c.append((y_nodes[i+1] - y_nodes[i]) / h_i - (2 * h_i * S[i] + h_i * S[i+1]) / 6)
        d.append(y_nodes[i])
    return a, b, c, d



def plot_spline(x_nodes, y_nodes, a, b, c, d):
    plt.figure(figsize=(8,6))

    for i in range(len(a)):
        xs = np.linspace(x_nodes[i], x_nodes[i+1], 100)
        dx = xs - x_nodes[i] # y = a[i]*dx^3 + b[i]*dx^2 + c[i]*dx + d[i]
        ys = a[i]*dx**3 + b[i]*dx**2 + c[i]*dx + d[i]
        plt.plot(xs, ys, label=f"Spline Segment {i}", linestyle='-')

    x_fine = np.linspace(x_nodes[0], x_nodes[-1], 1000)
    y_fine = [f(x) for x in x_fine]
    plt.plot(x_fine, y_fine, label='Original f(x)', color='black', linewidth=2, linestyle='--')

    plt.plot(x_nodes, y_nodes, 'o', color='black', label='Data Points')

    plt.grid(True)
    plt.title("Cubic Spline and Original Function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()



x_nodes = np.array([-1, -0.5, 0, 0.5, 1])
y_nodes = np.array([f(x) for x in x_nodes])
n = len(x_nodes)

h = np.diff(x_nodes)


A = np.zeros((n, n))
b = np.zeros(n)


A[0,0] = 2*h[0]
A[0,1] = h[0]
b[0] = 6 * ((y_nodes[1] - y_nodes[0]) / h[0] - 0)

A[-1,-2] = h[-1]
A[-1,-1] = 2*h[-1]
b[-1] = 6 * (0 - (y_nodes[-1] - y_nodes[-2]) / h[-1])

for i in range(1, n-1):
    A[i, i-1] = h[i-1]
    A[i, i] = 2*(h[i-1] + h[i])
    A[i, i+1] = h[i]
    b[i] = 6*((y_nodes[i+1] - y_nodes[i]) / h[i] - (y_nodes[i] - y_nodes[i-1]) / h[i-1])

S = np.linalg.solve(A, b)


a_coeff, b_coeff, c_coeff, d_coeff = compute_segment_coeffs(x_nodes, y_nodes, S)
plot_spline(x_nodes, y_nodes, a_coeff, b_coeff, c_coeff, d_coeff)
