import numpy as np
import matplotlib.pyplot as plt


def bezier_curve(ctrl_x, ctrl_y, m1, m2, u_vals):
    M = m1 @ m2
    coeff_x = M @ ctrl_x.T
    coeff_y = M @ ctrl_y.T

    curve_x = np.polyval(coeff_x, u_vals)
    curve_y = np.polyval(coeff_y, u_vals)
    print(f'coeff_x: {coeff_x}, coeff_y: {coeff_y}')
    return curve_x, curve_y


x = np.array([10, 50, 75, 90, 105, 150, 180, 190, 160, 130])
y = np.array([10, 15, 60, 100, 140, 200, 140, 120, 100, 80])

m1 = np.array([
    [2, -2, 1, 1],
    [-3, 3, -2, -1],
    [0, 0, 1, 0],
    [1, 0, 0, 0]
])
m2 = np.array([
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [-3, 3, 0, 0],
    [0, 0, -3, 3]
])


plt.figure(figsize=(10, 6))
u_vals = np.linspace(0, 1, 100) # 100 points for each segment

idx = 0
while idx + 3 < len(x):
    ctrl_x = x[idx:idx+4]
    ctrl_y = y[idx:idx+4]
    
    bx, by = bezier_curve(ctrl_x, ctrl_y, m1, m2, u_vals)
    plt.plot(bx, by, 'black')
    
    idx += 3

plt.plot(x, y, 'ro--', label='Control Points')

plt.title('Connected Bezier Curve from 10 Points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
