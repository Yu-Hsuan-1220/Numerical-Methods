import math

def f(x):
    return ((x-2)**3)*((x-4)**2)

def df(x):
    return 3*((x-2)**2)*((x-4)**2) + ((x-2)**3)*2*(x-4)

def newton(x): ##跟第一題用一樣的方法
    
    while 1:      
        x = x - f(x)/df(x)
        if abs(f(x)) < 1e-5:
            return x
        
print(f"Converge to root {newton(3)}")