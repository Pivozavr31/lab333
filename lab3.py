import math 
x=2
x = int(input('введите число')) 
num = (x ** (2*x))+(x**(2/x))
denom = math.exp(2*x)-math.log((x**(2*x))/2)
y = num / denom
print(f"y = {y}")