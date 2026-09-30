import math
P = 1
for n in range(1,26):
    P = P * ((-1**n)*((n+1)/(math.sin(n**3))**n + n ** n + 6 )*math.sin(n/2))
print(P)
