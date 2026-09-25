import math
x= -0.2
while x < 0.5:
    num=2*math.sin(x**2)+2*math.acos(-x)
    denom = 3 * math.asin(x**3)+(3**x)*math.cos(3*x)
    y= num / denom
    print(f"При x = {round(x, 2)}, y={y}")
    x+= 0.9
