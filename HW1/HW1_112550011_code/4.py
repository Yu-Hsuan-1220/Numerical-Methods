import math
import numpy as np


def f(x): ##回傳函數的matrix值
    x, y, z = x[0], x[1], x[2]

    return np.array([
        x - 3*y - z**2 + 3,
        2*(x**3) + y - 5*(z**2) +2, 
        4*(x**2) + y + z - 7
    ])

def  J(x):   #回傳Jacobian的matrix值
    x, y, z = x[0], x[1], x[2]

    return np.array([
        [1, -3, -2*z],
        [6*(x**2), 1, -10*z],
        [8*x, 1, 1]
    ])

sol = []      ##找到的解放這裡

x0 = np.array([1,1,1])

for i in range(10):
    fx0 = f(x0) 
    Jx0 = J(x0)                        ##因為要找反函數很浪費時間，所以不要直接算 Xn+1 = Xn - J-1(Xn) * f(Xn)
    s0 = np.linalg.solve(Jx0, -fx0)    ##每次迴圈解 J(Xn)*S0 = -f(Xn)，再更新 Xn+1 = Xn+S0 
    x0 = x0 + s0

    print(f"Iteration {i+1}: x = {x0}")

print(f"Final solution: x = {x0}")
sol.append(x0)

print('--------------------------------')

x0 = np.array([1.3,0.9,-1.2]) # [1.1114, 0.98820, 1.07087]

for i in range(10):
    fx0 = f(x0)
    Jx0 = J(x0)
    s0 = np.linalg.solve(Jx0, -fx0)
    x0 = x0 + s0

    print(f"Iteration {i+1}: x = {x0}")

print(f"Final solution: x = {x0}")
sol.append(x0)

print('--------------------------------')

x0 = np.array([-1.1838, 0.7337, 0.0841])

for i in range(10):
    fx0 = f(x0)
    Jx0 = J(x0)
    s0 = np.linalg.solve(Jx0, -fx0)
    x0 = x0 + s0

    print(f"Iteration {i+1}: x = {x0}")

print(f"Final solution: x = {x0}")
sol.append(x0)

print('--------------------------------')

x0 = np.array([50, 0, 0])

for i in range(20):
    fx0 = f(x0)
    Jx0 = J(x0)
    s0 = np.linalg.solve(Jx0, -fx0)
    x0 = x0 + s0

    print(f"Iteration {i+1}: x = {x0}")

print(f"Final solution: x = {x0}")
sol.append(x0)
print('--------------------------------')

x0 = np.array([-1 + (-1)**(1/2), 0, 0])

for i in range(20):
    fx0 = f(x0)
    Jx0 = J(x0)
    s0 = np.linalg.solve(Jx0, -fx0)
    x0 = x0 + s0

    print(f"Iteration {i+1}: x = {x0}")

print(f"Final solution: x = {x0}")
sol.append(x0)
print('--------------------------------')

x0 = np.array([-1 - (-1)**(1/2), 0, 0])

for i in range(20):
    fx0 = f(x0)
    Jx0 = J(x0)
    s0 = np.linalg.solve(Jx0, -fx0)
    x0 = x0 + s0

    print(f"Iteration {i+1}: x = {x0}")

print(f"Final solution: x = {x0}")
sol.append(x0)

print()
print('Result:')
for i in range(6):
    print(sol[i])