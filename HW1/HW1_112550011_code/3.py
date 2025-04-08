import math

oo = 1e9

def g1(x):
    if(x==0):
        return oo
    return (4+2*(x**3))/(x**2) -2*x
def g2(x):
    if(x==0):
        return oo
    return math.sqrt(4/x)
def g3(x):
    if(x==0):
        return oo
    return (16+(x**3))/(5*(x**2))


x = 2
for i in range(100):       ##迴圈100次，讓x收斂
    new_x = g1(x)          ##每次更新新的x = g(舊的x)
    if(abs(new_x - x) < 1e-5):
        print('g1 converge')
        print(f'Solution = {new_x}')
        break
    x = new_x
    if i == 99:
        print('g1 diverge')

x = 2
for i in range(100):
    new_x = g2(x)
    if(abs(new_x - x) < 1e-5):
        print('g2 converge')
        print(f'Solution = {new_x}')
        break
    x = new_x
    if i == 99:
        print('g2 diverge')

    
x = 2
for i in range(100):
    new_x = g3(x)
    if(abs(new_x - x) < 1e-5):
        print('g3 converge')
        break
    x = new_x
    if i == 99:
        print('g3 diverge')