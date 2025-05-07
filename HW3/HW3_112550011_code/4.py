import numpy as np
import matplotlib.pyplot as plt

x = np.array([10, 50, 75, 90, 105, 150, 180, 190, 160, 130])
y = np.array([10, 15, 60, 100, 140, 200, 140, 120, 100, 80])

def B_spline(ctrl_x, ctrl_y, m, u_vals):
    coeff_x = (m @ ctrl_x.T) / 6
    coeff_y = (m @ ctrl_y.T) / 6

    curve_x = np.polyval(coeff_x, u_vals)
    curve_y = np.polyval(coeff_y, u_vals)
    print(f'coeff_x: {coeff_x}, coeff_y: {coeff_y}')
    return curve_x, curve_y



m = np.array([
    [-1, 3, -3, 1],
    [3, -6, 3, 0],
    [-3, 0, 3, 0],
    [1, 4, 1, 0]
])

plt.figure(figsize=(10, 6))
u_vals = np.linspace(0, 1, 100) # 100 points for each segment

idx = 1
while idx + 2 < len(x):
    ctrl_x = x[idx-1:idx+3]
    ctrl_y = y[idx-1:idx+3]
    
    bx, by = B_spline(ctrl_x, ctrl_y, m, u_vals)
    plt.plot(bx, by, 'black')
    idx += 1

plt.plot(x, y, 'ro--', label='Control Points')

plt.title('Connected B-spline from 10 Points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()