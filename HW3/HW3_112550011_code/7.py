import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x*np.exp(-x)
def diff(x):
    return (1-x)*np.exp(-x)

def hermite_interpolation(ctrl_x, ctrl_y, m1, u_vals):
    coeff_x = m1 @ ctrl_x.T
    coeff_y = m1 @ ctrl_y.T

    curve_x = np.polyval(coeff_x, u_vals)
    curve_y = np.polyval(coeff_y, u_vals)
    print(f'coeff_x: {coeff_x}, coeff_y: {coeff_y}')
    return curve_x, curve_y ,coeff_x, coeff_y

m1 = np.array([
    [2, -2, 1, 1],
    [-3, 3, -2, -1],
    [0, 0, 1, 0],
    [1, 0, 0, 0]
])
x = np.array([1, 2, 3])
y = [f(x) for x in x]

plt.figure(figsize=(10, 6))
u_vals = np.linspace(0, 1, 101)


x_input = np.array([1, 2, 1, 1])
y_input = np.array([f(1), f(2), diff(1), diff(2)])
bx, by, cx, cy= hermite_interpolation(x_input, y_input, m1, u_vals)
plt.plot(bx, by, 'black')

print(f"The approximate f(1.5) = {np.polyval(cy, 0.5)}")
print(f"Real value : f(1.5) = {f(1.5)}")

x_input = np.array([2, 3, 1, 1])
y_input = np.array([f(2), f(3), diff(2), diff(3)])
bx, by, cx, cy = hermite_interpolation(x_input, y_input, m1, u_vals)
plt.plot(bx, by, 'black')


plt.plot(x, y, 'ro--', label='Control Points')
plt.title('Hermite Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()