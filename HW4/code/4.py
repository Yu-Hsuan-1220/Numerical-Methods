def simpson_one_third(fx, h):
    
    n = len(fx) - 1
    result = fx[0] + fx[-1]
    for i in range(1, n):
        coeff = 4 if i % 2 == 1 else 2
        result += coeff * fx[i]
    return (h / 3) * result

def simpson_three_eighth(fx, h):
    
    return (3 * h / 8) * (fx[0] + 3 * fx[1] + 3 * fx[2] + fx[3])

# Given values
x_vals = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]
f_vals = [1.543, 1.669, 1.811, 1.971, 2.151, 2.352, 2.577, 2.828, 3.107]
h = 0.1

# 1. True value using all Simpson's 1/3 rule
true_value = simpson_one_third(f_vals, h)
print(f"True value using 1/3 rule over all panels: {true_value:.20f}")

# 2. Try using 1/3 on first 2 panels (0 to 2), 3/8 on next 6 (3 to 8)
val1 = simpson_one_third(f_vals[0:3], h)
val1 += simpson_three_eighth(f_vals[2:6], h)
val1 += simpson_three_eighth(f_vals[5:9], h)
print(f"1/3 on [1.0-1.2], 3/8 on [1.2-1.5] & [1.5-1.8]: {val1:.20f}, Error: {abs(val1 - true_value):.20f}")

# 3. Try using 1/3 on last 2 panels (6 to 8), 3/8 on first 6
val2 = simpson_three_eighth(f_vals[0:4], h)
val2 += simpson_three_eighth(f_vals[3:7], h)
val2 += simpson_one_third(f_vals[6:9], h)
print(f"3/8 on [1.0-1.3] & [1.3-1.6], 1/3 on [1.6-1.8]: {val2:.20f}, Error: {abs(val2 - true_value):.20f}")

# 4. Try using 1/3 in the middle (2 panels in middle)
val3 = simpson_three_eighth(f_vals[0:4], h)
val3 += simpson_one_third(f_vals[3:6], h)
val3 += simpson_three_eighth(f_vals[5:9], h)
print(f"3/8 on [1.0-1.3] & [1.5-1.8], 1/3 on [1.3-1.5]: {val3:.20f}, Error: {abs(val3 - true_value):.20f}")
