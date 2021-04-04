import math

def reg(x):
    return -0.0612 * x**(2.8586) * math.e**(-0.1590*x) + 42

print(reg(365)) # 42.0

day = [15, 49, 77, 110, 140, 170, 197, 226, 255, 285]
milk = [25.6, 40.2, 42.0, 43.8, 42.0, 43.6, 41.8, 43.8, 42.0, 42.0]

res_sum = 0
for i in range(10):
    res_sum = (reg(day[i]) - milk[i])**4
res_sum = math.sqrt(res_sum)
res_sum = (1/3) * res_sum
print(res_sum) # 6.731613057885967e-29 ~= 0