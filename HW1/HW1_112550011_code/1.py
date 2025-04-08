import math

def f(x): #原函數
    return x**2 + math.sin(x) - (math.e**x)/4 -1

def df(x): #函數微分
    return 2*x + math.cos(x) - (math.e**x)/4

def bisection(a, b):
    ### 若b與a的距離小於tol值，就結束
    while abs(b-a) >= 1e-5:      
        m = (b+a)/2
        if(f(a)*f(m) < 0): ##若中間值的函數值與a點函數值異號，更新b點到中間值
            b = m  
        else: ## 否則更新a點到中間值 
            a = m
    return a, b

def secant(x0, x1):
    
    while 1:
        ## 找到x0、x1割線與x軸的交點
        x2 = x1 - f(x1)*(x0-x1)/(f(x0)-f(x1))

        if abs(f(x2)) <= 1e-5:  ##若交點函數值小於容忍值
            return x2

        if f(x2)*f(x0) < 0:   ##若f(x2)與f(x0)異號，把x1縮近來到x2
            x1 = x2
        else:
            x0 = x2
    
def newton(x):
    while 1:
        x = x - f(x)/df(x)    ##每次更新找到在x點的切線與x軸的交點
        if abs(f(x)) < 1e-5:  ##直到新點的函數值小於tol
            return x
        
print('Bisection')
a, b = bisection(0, 2)
print(f"First solution between {a}, {b}")
a, b = bisection(-2, 0)
print(f'Second solution between {a}, {b}')
print('--------------------------------')
print('Secant')
x = secant(0,2)
print(f"First solution near {x}")
x = secant(-2,0)
print(f"Second soltion near {x}")
print('--------------------------------')
print('Newton')
x = newton(2)
print(f'First solution near {x}')
x = newton(-2)
print(f'Second solution near {x}')