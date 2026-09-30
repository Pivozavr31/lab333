import math
result = sum((3.2 ** (2 * n + 1)) / math.factorial(2 * n + 1) * math.log(n/2) for n in range(1,51))
print(result)
